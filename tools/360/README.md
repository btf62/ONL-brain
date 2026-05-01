# 360 Review Tools

Utilities for working with annual 360 review source artifacts.

## Private Archive Builder

`build-review-archive.py` parses local review PDFs and regenerates the private 360 review archive:

```bash
python3 tools/360/build-review-archive.py
```

Outputs are written to:

```text
docs/workspaces/360-reviews/private/archive/
```

That output folder contains confidential HR review content and is ignored by git. The tool code is tracked here because the code itself is not confidential.

The builder currently reads source PDFs from Brad's local archive:

```text
/Users/bradfiles/Archive/Old Mac 2022 Files/Downloads
```

It reads those PDFs, but does not modify them.
