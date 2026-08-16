# Contributing to the APM playbook

Improve this playbook when real work shows that a rule is unclear, missing, or wrong.

## Before writing

State the problem in one sentence:

> A reader cannot decide or do ___ because the playbook currently ___ .

Then check whether an existing page should change. Prefer improving one source over adding a second version.

For a material role or assessment decision, update the [research and decision log](docs/governance/research-and-decisions.md). Keep source facts, RentOk inferences, and RentOk decisions separate.

## Writing standard

- Write from shared ground. A reader should not need the writer sitting beside them.
- Use plain words and short sentences.
- Keep RentOk or Product terms only when the intended reader understands them. Explain private terms once.
- State what the reader needs to understand, decide, or do.
- Use tables only when the information is genuinely parallel.
- Do not use em dashes.
- Do not add generic management language to make a page sound complete.
- Do not mention the tool, model, session, or writing process in a reader-facing page.

## Privacy check

Do not commit:

- resumes or completed candidate templates
- candidate names or contact details
- interview notes, references, or recordings
- compensation or offer details
- customer data, credentials, or internal secrets

Use fictional or fully anonymous examples. Read [Where information lives](docs/governance/where-information-lives.md) when unsure.

## Review before handoff

Run:

~~~bash
python3 scripts/check_docs.py
~~~

Then review the change twice:

1. **Fact check:** Does every changed claim match its source or an explicit decision?
2. **Fresh-context read:** Can the intended reader understand the page and act without private context?

Update CHANGELOG.md when a role rule, assessment rule, expected action, or source-of-truth boundary changes.

## Pull request note

Include:

- the problem this change solves
- the pages affected
- the source or experience behind the change
- whether the matching Notion page was updated or the sync is still pending
- confirmation that no personal information was added

---

[Back to the playbook](README.md)
