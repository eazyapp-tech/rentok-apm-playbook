# Technical and AI Exercise: Booking Action List

**For:** Candidates and assessors

## What this exercise is for

Use the attached `booking-action-list-exercise.csv` file to create a clear action list for the product and operations team.

We are testing whether you can use technical or AI tools to turn imperfect data into useful work. We are not testing whether you know a particular programming language.

All records are fictional.

## Time and tools

- You have 45 minutes.
- Use any tool you find useful, including spreadsheets, SQL, Python or AI tools.
- You may ask questions, but continue with stated assumptions when an answer is not essential.

Assume today is **20 August 2026**.

## The rules

- `approved` means the booking has been approved but the person is not yet an active tenant.
- `active` means the person is already an active tenant.
- `pending` means the booking still needs a decision.
- `cancelled` bookings need no move-in action.
- When `auto_convert` is `ON`, an approved booking should become active on its joining date.
- When `auto_convert` is `OFF`, an approved booking needs a manual move-in on or after its joining date.
- Welcome messages should be sent only after the person becomes active.

## What to return

1. An action list showing which records need attention, why, how urgent they are and what should happen next.
2. A short list of data problems or cases you could not decide safely.
3. The file, query, script or steps you used to produce the result.
4. A short note explaining how another person should use or rerun your work tomorrow.

Do not build a polished application. Finish the useful part first.

Download the [fictional exercise data](../../data/booking-action-list-exercise.csv).

---

[Back to the playbook](../../README.md) · [Previous: Product work sample](product-work-sample.md) · [Next: Starting the role](../working/starting-the-role.md)
