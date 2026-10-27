#!/usr/bin/env bash
set -euo pipefail

PIPELINERUN="${1:-oc-pipelines-oc-final}"
NAMESPACE="${NAMESPACE:-ci-cd-final}"

if command -v tkn >/dev/null 2>&1; then
  tkn pipelinerun logs "$PIPELINERUN" -n "$NAMESPACE" > pipelinerun.txt
elif command -v oc >/dev/null 2>&1; then
  oc logs -n "$NAMESPACE" "pipelinerun/$PIPELINERUN" > pipelinerun.txt
else
  echo "tkn or oc is required to capture pipelinerun.txt" >&2
  exit 1
fi

echo "Wrote pipelinerun.txt"
