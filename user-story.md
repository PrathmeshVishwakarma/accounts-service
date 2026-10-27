# User Stories

This document defines the user-story template and the stories used on the
project Kanban board.

## User-story template

```markdown
**As a** <type of user>
**I need** <some goal>
**So that** <some reason or benefit>

### Acceptance Criteria

**Given** <some context>
**When** <some action is taken>
**Then** <some observable outcome>
```

## Stories

### 1. Create an account

**As a** customer service representative
**I need** to create a customer account
**So that** the customer can be identified and served

**Acceptance Criteria**

**Given** a valid name and email
**When** I `POST /accounts`
**Then** a new account is created and returned with HTTP 201

**Labels:** `enhancement` | **Estimate:** 3 | **Sprint:** 1

### 2. Read an account

**As a** customer service representative
**I need** to read a customer account by ID
**So that** I can view the customer's current details

**Acceptance Criteria**

**Given** an existing account ID
**When** I `GET /accounts/<id>`
**Then** the account is returned with HTTP 200
**And** a missing account returns HTTP 404

**Labels:** `enhancement` | **Estimate:** 2 | **Sprint:** 1

### 3. List all accounts

**As a** customer service representative
**I need** to list all customer accounts
**So that** I can browse the customer database

**Acceptance Criteria**

**Given** accounts exist in the database
**When** I `GET /accounts`
**Then** every account is returned as a JSON array

**Labels:** `enhancement` | **Estimate:** 2 | **Sprint:** 1

### 4. Update an account

**As a** customer service representative
**I need** to update an account
**So that** customer information stays accurate

**Acceptance Criteria**

**Given** an existing account ID and new values
**When** I `PUT /accounts/<id>`
**Then** the account is updated and returned with HTTP 200
**And** a missing account returns HTTP 404

**Labels:** `enhancement` | **Estimate:** 3 | **Sprint:** 1

### 5. Delete an account

**As a** customer service representative
**I need** to delete an account
**So that** obsolete customer records are removed

**Acceptance Criteria**

**Given** an existing account ID
**When** I `DELETE /accounts/<id>`
**Then** the account is removed and HTTP 204 is returned
**And** a missing account returns HTTP 404

**Labels:** `enhancement` | **Estimate:** 2 | **Sprint:** 1

### 6. Set up the development environment

**As a** developer
**I need** a configured development environment
**So that** I can build and test the service

**Acceptance Criteria**

**Given** a clean checkout
**When** I install the requirements and run the tests
**Then** the application starts and the tests run successfully

**Labels:** `technical debt` | **Estimate:** 2 | **Sprint:** 1

### 7. Automate continuous integration checks

**As a** developer
**I need** CI checks on every push
**So that** broken code cannot be merged

**Acceptance Criteria**

**Given** a push to `main`
**When** GitHub Actions runs
**Then** flake8 and nose run and the workflow passes

**Labels:** `technical debt` | **Estimate:** 3 | **Sprint:** 2

### 8. Add security headers and CORS policies

**As a** security engineer
**I need** security headers and CORS policies
**So that** browser clients can safely use the API

**Acceptance Criteria**

**Given** any API response
**When** a client inspects the headers
**Then** the Talisman security headers are present
**And** the configured CORS origins and headers are allowed

**Labels:** `technical debt` | **Estimate:** 3 | **Sprint:** 2

### 9. Containerize the microservice using Docker

**As a** DevOps engineer
**I need** a Docker image for the service
**So that** the service runs consistently in any environment

**Acceptance Criteria**

**Given** the Dockerfile
**When** I run `docker build`
**Then** an image is produced
**And** the container serves the API on port 8080

**Labels:** `technical debt` | **Estimate:** 3 | **Sprint:** 3

### 10. Deploy the Docker image to Kubernetes

**As a** DevOps engineer
**I need** to deploy the image to Kubernetes
**So that** the service is available in the cluster

**Acceptance Criteria**

**Given** a built image
**When** the deployment and service manifests are applied
**Then** the pod is running and the service is reachable

**Labels:** `technical debt` | **Estimate:** 3 | **Sprint:** 3

### 11. Create a CD pipeline to automate deployment to Kubernetes

**As a** DevOps engineer
**I need** a CD pipeline
**So that** deployments are automated and repeatable

**Acceptance Criteria**

**Given** a new commit on `main`
**When** the Tekton pipeline runs
**Then** the code is cloned, linted, tested, built, and deployed

**Labels:** `technical debt` | **Estimate:** 5 | **Sprint:** 3
