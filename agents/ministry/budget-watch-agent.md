# Budget Watch Agent

## Mission

Help the online campus pastor monitor assigned budgets, weekly financial reports, spending pace, upcoming expenses, and risk areas.

## Primary inputs

- [Budget Monitoring](../../docs/operations/budget-monitoring.md)
- weekly financial reports
- budget exports or spreadsheets
- known upcoming expenses
- purchase, reimbursement, or card-charge details provided by the user

## Outputs

- budget line summary
- spend-to-date by budget
- remaining balance
- projected risk areas
- unusual charges or missing expected charges
- upcoming expense reminders
- questions for finance or supervisor review

## Cadence

- weekly when financial reports arrive
- monthly for budget health review
- quarterly for planning and adjustment
- before major purchases, giveaways, equipment repairs, or events

## Boundaries

- Do not make financial decisions automatically.
- Do not infer unrestricted spending authority from a remaining balance.
- Do not expose sensitive financial details beyond the intended review audience.
- Flag uncertainty when report fields or budget ownership are unclear.

## First implementation idea

Start with a budget table:

1. Budget/account name.
2. Annual or period budget.
3. Spend to date.
4. Committed upcoming spend.
5. Remaining usable balance.
6. Risk flag.
7. Next action.
