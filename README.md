# RentOk APM Playbook

This is how RentOk hires, supports, and reviews an Associate Product Manager.

It gives candidates, interviewers, managers, and new joiners one shared standard from the first conversation through the first 90 days.

**This is a private working playbook. Do not add resumes, candidate notes, interview recordings, or personal information to this repository.**

[Start here](#start-here) · [Role](#understand-the-role) · [Hiring](#hire-and-assess) · [Working at RentOk](#join-and-do-the-job) · [Templates](#use-the-templates) · [Decisions](docs/governance/research-and-decisions.md) · [Notion](#what-lives-in-notion) · [Contributing](CONTRIBUTING.md)

## What this playbook helps us do

The playbook connects five decisions that are easy to separate by mistake:

1. What job are we hiring for?
2. What evidence should we collect before hiring someone?
3. Should the person join through an internship or a direct full-time offer?
4. What should the person own after joining?
5. How will we know whether the person is growing into an independent Product Manager?

A candidate should not hear one version of the job while the new joiner is judged against another. The role, assessment, onboarding plan, and success review should agree with each other.

## See it in practice

A customer says approved bookings are not becoming tenants.

The APM does not only create a ticket. They find the affected cases, separate product problems from data or operating problems, and state what is known and unknown.

They recommend what to fix first, help Design and Engineering make the work ready, test the result, follow the release, and check what changed for users.

The useful output is not a busy Jira board. It is a clear decision, owned next steps, a checked release, and evidence about the user result.

## Who this is for

| You are | Start here |
|---|---|
| Hiring manager or recruiter | [Internal hiring brief](docs/role/message-to-srijan.md), then [job description](docs/role/job-description.md) and [assessment process](docs/hiring/assessment-process.md) |
| Interviewer | [Candidate scorecard](docs/hiring/candidate-scorecard.md), then the relevant exercise |
| Candidate | [Job description](docs/role/job-description.md), then the exercise shared with you |
| New APM | [Starting the role](docs/working/starting-the-role.md), then [first 90 days](docs/working/first-90-days.md) |
| Product Lead | [Success review](docs/working/success-review.md), [working rhythm](docs/working/weekly-and-sprint-rhythm.md), and [decision rights](docs/working/decision-rights.md) |

## Start here

Read the page that matches the decision in front of you. Follow its links rather than opening every file.

### Understand the role

- [Internal hiring brief: Message to Srijan](docs/role/message-to-srijan.md)
- [Associate Product Manager job description](docs/role/job-description.md)
- [Starting the role](docs/working/starting-the-role.md)
- [KRAs and success review](docs/working/success-review.md)

### Hire and assess

- [Candidate assessment process](docs/hiring/assessment-process.md)
- [Candidate scorecard](docs/hiring/candidate-scorecard.md)
- [Product work sample: Booking to Tenant](docs/hiring/product-work-sample.md)
- [Optional technical exercise: Booking Action List](docs/hiring/technical-exercise.md)
- [Exercise data](data/booking-action-list-exercise.csv)

### Join and do the job

- [Starting the role](docs/working/starting-the-role.md)
- [First 90 days](docs/working/first-90-days.md)
- [Weekly and sprint rhythm](docs/working/weekly-and-sprint-rhythm.md)
- [Decision rights and escalation](docs/working/decision-rights.md)
- [KRAs and success review](docs/working/success-review.md)

### Use the templates

- [Candidate evidence file](templates/candidate-evidence-file.md)
- [Candidate decision note](templates/candidate-decision-note.md)
- [Weekly review](templates/weekly-review.md)

## One role, two ways to join

We are hiring for one job. The entry route depends on the evidence the candidate already has.

An early-career candidate may join through a paid internship intended to convert to full-time. Conversion depends on observed work. It is not promised only because the internship was completed.

A candidate who already shows repeated evidence of doing the job can receive a direct full-time offer. This normally includes RentOk's probation terms. Any exception should follow company policy and have a clear reason.

Probation does not replace a proper assessment. An internship should not be used to underlevel an experienced candidate.

AI experience does not decide the entry route. A candidate with strong Product evidence can receive a direct full-time offer while still learning how to use AI in everyday Product work.

## How AI fits this role

We expect the APM to learn how to use available AI tools to make everyday Product work easier, better checked, and more systematic.

Current experience is useful, but it is not an automatic hiring gate. We care about curiosity, thoughtful use, safe handling of information, and useful progress through real work.

AI may help do the work. It does not own the work. The person who submits, shares, recommends, or acts on an output remains responsible for checking it and for what happens next.

Technical ability is recorded separately. Coding is not required.

## What lives in Notion

The [APM Hiring and Onboarding Hub](https://app.notion.com/p/3bd456d1076a81ef883eeec5bc487c22?pvs=204) is the working wiki for live hiring.

Notion holds:

- the recruiter message and current hiring coordination
- the candidate index and current stage
- resumes and candidate evidence files
- interview notes and hiring decisions
- archived page history

This repository holds the reusable standard, templates, change history, and [research and decision log](docs/governance/research-and-decisions.md). Read [Where information lives](docs/governance/where-information-lives.md) before adding a new kind of page.

## How this playbook should grow

Add a page when it answers a repeated decision or prevents a repeated mistake. Do not add a page only to make the repository look complete.

A useful addition should say:

- who needs it
- what decision or action it supports
- what evidence or experience it is based on
- which existing page it changes or connects to

See [Contributing](CONTRIBUTING.md) for the writing and review rules.

## FAQ

<details>
<summary>Is this only a hiring repository?</summary>

No. Hiring is the first part because the role, assessment, onboarding, and performance standard must agree. The playbook can grow into the practical guide for how an APM works and grows at RentOk.
</details>

<details>
<summary>Which copy is the source of truth?</summary>

Use this repository for reusable playbook pages and version history. Use the Notion hub for live hiring operations and candidate records.

A repository draft may be reviewed before the matching Notion pages are updated. Record the pending sync in the changelog. The change is fully rolled out only after both places match.
</details>

<details>
<summary>Can a candidate see this repository?</summary>

The repository is private. Share only the candidate-facing page needed for that stage. Do not share scorecards, assessor guidance, candidate records, or internal decision notes.
</details>

<details>
<summary>Can we change the assessment for one candidate?</summary>

Use the same core process and scorecard for everyone. Add a question only when it tests a specific claim, gap, or risk. Record why the question was added.
</details>

<details>
<summary>Where do candidate evidence files go?</summary>

Use the blank template in this repository, then create the real file inside the candidate's private Notion record. Never commit the completed file here.
</details>

<details>
<summary>How do I suggest a change?</summary>

Open a pull request that names the decision or repeated problem the change improves. Check the links, privacy boundary, facts, and readability before asking another person to review it.
</details>

## Repository structure

<details>
<summary>Show the folders</summary>

~~~text
docs/
  governance/   Information boundaries, research, and decisions
  hiring/       Assessment process, scorecard, and exercises
  role/         The internal hiring brief and candidate-facing role definition
  working/      Onboarding, operating rhythm, decisions, and success
templates/      Blank working templates. Never completed candidate files
data/           Fictional exercise data
scripts/        Repository checks
~~~
</details>

## Current direction

The first version connects hiring, assessment, onboarding, and the first 90 days. The next additions should come from real use: interview lessons, onboarding gaps, repeated operating decisions, and examples of good APM work.
