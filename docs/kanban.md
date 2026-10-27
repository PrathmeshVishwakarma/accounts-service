# Kanban Board Plan

The project board uses five columns:

| Column | Purpose |
| --- | --- |
| **New Issues** | All stories before grooming |
| **Ice Box** | Stories deferred to a later release |
| **Product Backlog** | Groomed stories with labels |
| **Sprint Backlog** | Stories committed to the current sprint |
| **Done** | Completed stories |

## Stories and board metadata

| # | Story | Label | Estimate | Sprint | Final column |
| --- | --- | --- | --- | --- | --- |
| 1 | Setting up the development environment | Technical Debt | 2 | 1 | Done |
| 2 | Create an account in the service | Enhancement | 3 | 1 | Done |
| 3 | Read an account from the service | Enhancement | 2 | 1 | Done |
| 4 | List all accounts in the service | Enhancement | 2 | 1 | Done |
| 5 | Update an account in the service | Enhancement | 3 | 1 | Done |
| 6 | Delete an account from the service | Enhancement | 2 | 1 | Done |
| 7 | Need the ability to automate continuous integration checks | Technical Debt | 3 | 2 | Done |
| 8 | Need to add security headers and CORS policies | Technical Debt | 3 | 2 | Done |
| 9 | Containerize your microservice using Docker | Technical Debt | 3 | 3 | Done |
| 10 | Deploy your Docker image to Kubernetes | Technical Debt | 3 | 3 | Done |
| 11 | Create a CD pipeline to automate deployment to Kubernetes | Technical Debt | 5 | 3 | Done |
| 12 | Add pagination to the account list | Enhancement | 3 | Ice Box | Ice Box |
| 13 | Add authentication to the API | Enhancement | 5 | Ice Box | Ice Box |
| 14 | Send a welcome email when an account is created | Enhancement | 3 | Ice Box | Ice Box |

## Creating the issues

Install and authenticate the GitHub CLI, then run:

```bash
gh auth refresh -s project
./scripts/create-issues.sh
```

Create a project named **Accounts Service Kanban** with the five columns above,
add the issues, then set the `Estimate` and `Sprint` fields. The estimates from
the table above are the values to enter.

## Screenshot checklist

Capture each screenshot after moving the cards as described.

| File | What must be visible |
| --- | --- |
| `planning-userstories-done.png` | **New Issues** column with all stories |
| `planning-productbacklog-done.png` | **Ice Box** column with stories 12-14 |
| `planning-labels-done.png` | **Product Backlog** column showing **Technical Debt** and **Enhancement** labels |
| `planning-kanban-done.png` | **Sprint Backlog** column with estimates and **Sprint 1** |
| `rest-techdebt-done.png` | Story 1 in **Done** |
| `read-accounts.png` | Story 3 in **Done** |
| `list-accounts.png` | Story 4 in **Done** |
| `update-accounts.png` | Story 5 in **Done** |
| `delete-accounts.png` | Story 6 in **Done** |
| `sprint2-plan.png` | Stories 7 and 8 in **Sprint Backlog** for Sprint 2 |
| `ci-kanban-done.png` | Story 7 in **Done** |
| `security-kanban-done.png` | Story 8 in **Done** |
| `sprint3-plan.png` | Stories 9, 10, and 11 in **Sprint Backlog** for Sprint 3 |
| `kube-docker-done.png` | Story 9 in **Done** |
| `kube-kubernetes-done.png` | Story 10 in **Done** |
| `cd-pipeline-done.png` | Story 11 in **Done** |
