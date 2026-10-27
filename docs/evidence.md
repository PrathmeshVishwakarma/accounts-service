# Submission Evidence Guide

This page lists how to capture the runtime artifacts that are not committed to
the repository.

## Kanban screenshots

The board must use these columns: **New Issues**, **Ice Box**,
**Product Backlog**, **Sprint Backlog**, and **Done**. See
[`docs/kanban.md`](kanban.md) for the story-to-column mapping, labels,
estimates, and sprint assignment.

Required files:

- `planning-userstories-done.png`
- `planning-productbacklog-done.png`
- `planning-labels-done.png`
- `planning-kanban-done.png`
- `rest-techdebt-done.png`
- `read-accounts.png`
- `list-accounts.png`
- `update-accounts.png`
- `delete-accounts.png`
- `sprint2-plan.png`
- `ci-kanban-done.png`
- `security-kanban-done.png`
- `sprint3-plan.png`
- `kube-docker-done.png`
- `kube-kubernetes-done.png`
- `cd-pipeline-done.png`

## REST outputs

Regenerate the `rest-*-done` files while the service is running on port 8080:

```bash
FLASK_APP=service:app flask run --port 8080
```

The commands and responses are stored in:

- `rest-create-done`
- `rest-list-done`
- `rest-read-done`
- `rest-update-done`
- `rest-delete-done`

## CI output

`ci-workflow-done` contains the log of the successful GitHub Actions run:

<https://github.com/PrathmeshVishwakarma/accounts-service/actions>

## Security output

`security-headers-done` contains the nose output after the Talisman and CORS
configuration was added. Regenerate it with:

```bash
nosetests -v tests
```

## Kubernetes and OpenShift outputs

If the image and deployment were created locally:

```bash
./scripts/capture-kube-evidence.sh
```

This writes:

- `kube-images` - image name, tag, image ID, created time, and size.
- `kube-deploy-accounts` - deployment, pods, replica sets, and service.

For the Tekton pipeline log:

```bash
./scripts/capture-pipeline-logs.sh oc-pipelines-oc-final
```

This writes `pipelinerun.txt`.

## Application output

`kube-app-output` contains the JSON returned by the running application at
port 8080:

```bash
curl -s http://localhost:8080/
```
