#!/usr/bin/env bash
set -euo pipefail

REPO="${REPO:-PrathmeshVishwakarma/accounts-service}"

create_label() {
  local name="$1" color="$2" description="$3"
  gh label create "$name" --repo "$REPO" --color "$color" --description "$description" --force
}

create_issue() {
  local title="$1" label="$2" estimate="$3" sprint="$4" body="$5"
  gh issue create --repo "$REPO" --title "$title" --label "$label" --body "$body

Estimate: $estimate
Sprint: $sprint"
}

create_label "Enhancement" "a2eeef" "New feature or request"
create_label "Technical Debt" "d4c5f9" "Internal work that improves the codebase"
create_label "Ice Box" "ededed" "Deferred to a later release"

create_issue "Setting up the development environment" "Technical Debt" 2 "Sprint 1" \
  "As a developer I need a configured development environment so that I can build and test the service."
create_issue "Create an account in the service" "Enhancement" 3 "Sprint 1" \
  "As a representative I need to create an account so that customer details can be stored."
create_issue "Read an account from the service" "Enhancement" 2 "Sprint 1" \
  "As a representative I need to read an account so that I can view customer details."
create_issue "List all accounts in the service" "Enhancement" 2 "Sprint 1" \
  "As a representative I need to list accounts so that I can browse the customer database."
create_issue "Update an account in the service" "Enhancement" 3 "Sprint 1" \
  "As a representative I need to update an account so that customer details stay accurate."
create_issue "Delete an account from the service" "Enhancement" 2 "Sprint 1" \
  "As a representative I need to delete an account so that obsolete records are removed."
create_issue "Need the ability to automate continuous integration checks" "Technical Debt" 3 "Sprint 2" \
  "As a developer I need automated CI checks so that broken code cannot be merged."
create_issue "Need to add security headers and CORS policies" "Technical Debt" 3 "Sprint 2" \
  "As a security engineer I need security headers and CORS policies so that browser clients can safely use the API."
create_issue "Containerize your microservice using Docker" "Technical Debt" 3 "Sprint 3" \
  "As a DevOps engineer I need a Docker image so that the service runs consistently."
create_issue "Deploy your Docker image to Kubernetes" "Technical Debt" 3 "Sprint 3" \
  "As a DevOps engineer I need to deploy to Kubernetes so that the service is available in the cluster."
create_issue "Create a CD pipeline to automate deployment to Kubernetes" "Technical Debt" 5 "Sprint 3" \
  "As a DevOps engineer I need a CD pipeline so that deployments are automated and repeatable."
create_issue "Add pagination to the account list" "Enhancement" 3 "Ice Box" \
  "As a representative I need pagination so that large account lists load quickly."
create_issue "Add authentication to the API" "Enhancement" 5 "Ice Box" \
  "As a security engineer I need authentication so that only authorized clients can call the API."
create_issue "Send a welcome email when an account is created" "Enhancement" 3 "Ice Box" \
  "As a customer I need a welcome email so that I know my account was created."
