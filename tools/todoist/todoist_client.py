import json
import os
from typing import Any, Optional
from urllib import error, parse, request


API_BASE_URL = "https://api.todoist.com/api/v1"


class TodoistError(RuntimeError):
    pass


class TodoistClient:
    def __init__(self, api_token: Optional[str] = None) -> None:
        token = api_token or os.environ.get("TODOIST_API_TOKEN")
        if not token:
            raise TodoistError(
                "Missing Todoist API token. Set TODOIST_API_TOKEN in your environment."
            )
        self.api_token = token

    def _request(
        self,
        method: str,
        path: str,
        *,
        payload: Optional[dict[str, Any]] = None,
        query: Optional[dict[str, Any]] = None,
        expected_statuses: tuple[int, ...] = (200,),
    ) -> Any:
        url = f"{API_BASE_URL}{path}"
        if query:
            query_string = parse.urlencode(
                {key: value for key, value in query.items() if value is not None}
            )
            url = f"{url}?{query_string}"

        data = None
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")

        req = request.Request(url=url, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.api_token}")
        req.add_header("Accept", "application/json")
        if payload is not None:
            req.add_header("Content-Type", "application/json")

        try:
            with request.urlopen(req) as response:
                status = response.getcode()
                body = response.read().decode("utf-8")
        except error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            raise TodoistError(
                f"Todoist API request failed with {exc.code} {exc.reason}: {error_body}"
            ) from exc
        except error.URLError as exc:
            raise TodoistError(f"Unable to reach Todoist API: {exc.reason}") from exc

        if status not in expected_statuses:
            raise TodoistError(
                f"Unexpected Todoist response status {status} for {method} {path}"
            )

        if not body:
            return None
        return json.loads(body)

    def _request_all(
        self,
        path: str,
        *,
        query: Optional[dict[str, Any]] = None,
    ) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        cursor: Optional[str] = None

        while True:
            page_query = dict(query or {})
            page_query["limit"] = 200
            if cursor:
                page_query["cursor"] = cursor

            response = self._request("GET", path, query=page_query)
            if isinstance(response, list):
                return records + response

            if not isinstance(response, dict) or "results" not in response:
                raise TodoistError(f"Unexpected Todoist paginated response for {path}")

            results = response.get("results") or []
            if not isinstance(results, list):
                raise TodoistError(f"Unexpected Todoist results response for {path}")
            records.extend(results)

            cursor = response.get("next_cursor")
            if not cursor:
                return records

    def get_tasks(self) -> list[dict[str, Any]]:
        return self._request_all("/tasks")

    def get_projects(self) -> list[dict[str, Any]]:
        return self._request_all("/projects")

    def get_sections(self) -> list[dict[str, Any]]:
        return self._request_all("/sections")

    def get_task(self, task_id: str) -> dict[str, Any]:
        return self._request("GET", f"/tasks/{task_id}")

    def create_task(
        self,
        *,
        content: str,
        description: Optional[str] = None,
        project_id: Optional[str] = None,
        section_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        priority: Optional[int] = None,
        due_date: Optional[str] = None,
        due_string: Optional[str] = None,
        labels: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        payload = {
            "content": content,
            "description": description,
            "project_id": project_id,
            "section_id": section_id,
            "parent_id": parent_id,
            "priority": priority,
            "due_date": due_date,
            "due_string": due_string,
            "labels": labels,
        }
        clean_payload = {key: value for key, value in payload.items() if value is not None}
        return self._request("POST", "/tasks", payload=clean_payload, expected_statuses=(200,))

    def update_task_priority(self, task_id: str, priority: int) -> None:
        self._request(
            "POST",
            f"/tasks/{task_id}",
            payload={"priority": priority},
            expected_statuses=(204,),
        )
