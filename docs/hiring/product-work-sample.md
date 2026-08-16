# Product work sample: Booking to Tenant

**For:** Candidates and assessors

## What this exercise is for

This exercise is about how you understand an unclear product situation, make a decision, and help the work move.

You do not need prior knowledge of RentOk or property management. The information below is enough to begin. Ask questions when the answer could change your recommendation. Make and state a reasonable assumption when it would not.

## Time and format

- You have 90 minutes.
- You may use the internet, notes, and AI tools. Use AI if it helps, but you do not have to. We will judge the work and your reasoning, not whether you used AI.
- Keep your response to two pages or less.
- We will discuss your answer for 20 minutes afterwards.

We care more about a clear decision and a workable next step than presentation quality.

### Working-method note

After your response, add a short note of no more than five bullets. This note does not count toward the two-page limit.

1. What tools and sources did you use?
2. Where, if anywhere, did you use AI?
3. What did you check independently?
4. What did you change or reject?
5. What would you improve with more time?

The note is not scored separately. It helps us understand how you worked and ask better questions.

## The situation

RentOk helps people manage bookings and tenants across PGs, hostels, and rental properties.

Today, an approved booking automatically becomes an active tenant on its joining date. The tenant then receives the normal welcome and check-in messages.

This saves work for many properties. It also causes trouble for properties where the joining date does not mean the person is ready to move in.

All names and numbers in this exercise are fictional. The situation is based on real product patterns.

## What customers are saying

### Sunrise Student Home

> We have 800 beds. A student should become active only after the remaining deposit is paid and the warden confirms arrival. Last week two students became active automatically. Their parents received welcome messages before payment was complete. The front desk then had to explain why the room was not ready.

### Maple Stay

> We have 120 beds. The joining dates are usually correct. Automatic conversion saves us from doing the same work every day. Please do not make every move-in manual.

### CityNest Living

> We run six properties. The back office approves bookings, but wardens handle arrival. Some properties need manual confirmation and some do not. One rule for the entire company will not work.

## What the team knows

### Customer Success

- Eighteen support cases in the last 30 days involved a tenant becoming active too early.
- Four large student hostels accounted for fourteen of those cases.
- Wrong welcome messages create confusion and are difficult to explain after they have been sent.
- Customer Success wants a quick fix.

### Product data

- 420 approved bookings reached their joining date in the last 30 days.
- 402 converted automatically without a reported problem.
- In a small manual trial, nine bookings remained pending for more than one day after their joining date.
- Three of those nine were noticed only when the tenant contacted the property.

These figures are exercise data, not RentOk production data.

### Engineering

- Turning automatic conversion off for everyone would be the quickest technical change.
- The current Add as Tenant process can be reused when a move-in needs a person to confirm it.
- The product can support one small difference in behaviour between properties within the next release.
- Changing a joining date to today or an earlier date can activate a tenant through a separate path.
- The team has capacity for one focused change in the next three weeks. A large system covering payment, KYC, and every readiness rule is not realistic now.

### Design

- The current journey does not give a manager a clear waiting state when an approved booking does not become an active tenant.
- It does not show who should act when the joining date has passed.
- There is no agreed design for old bookings when behaviour changes.

### QA

- Approved bookings remain visible in the Bookings list.
- There is no home-screen reminder for a manual move-in that has been missed.
- QA is concerned that preventing early activation could create another problem where real move-ins are forgotten.

## Your task

Prepare a short note with these sections.

### 1. What I understood

What is the real problem? Who is affected? Where do the needs differ?

### 2. What I recommend

What should RentOk do in the next release? Explain why.

### 3. What I would not do now

What would you deliberately leave out of this release?

### 4. What needs to be decided or checked

List only the questions that could materially change your recommendation. State your current assumption beside each one.

### 5. What happens next

Show the order of work. Include the people who need to be involved, what must be ready before development, how the change should be tested, and what should be checked after release.

### 6. Team update

Write a short update for the Product Lead and Engineering Manager. State the recommendation, main risk, decision needed, and next action.

## What we will discuss afterwards

Be ready to explain:

- the evidence behind your recommendation
- the trade-offs you accepted
- the part you are least confident about
- what you would do if new information challenged your answer

---

[Back to the playbook](../../README.md) · [Previous: Candidate scorecard](candidate-scorecard.md) · [Next: Optional technical exercise](technical-exercise.md)
