#!/usr/bin/env bash
set -euo pipefail

APP="${APP:-accounts-service}"
NAMESPACE="${NAMESPACE:-default}"
IMAGE="${IMAGE:-$APP:1.0}"

if command -v docker >/dev/null 2>&1; then
  docker images "$IMAGE" > kube-images
elif command -v podman >/dev/null 2>&1; then
  podman images "$IMAGE" > kube-images
elif command -v oc >/dev/null 2>&1; then
  oc get imagestreamtag -n "$NAMESPACE" > kube-images
else
  echo "docker, podman, or oc is required to capture kube-images" >&2
  exit 1
fi

if command -v kubectl >/dev/null 2>&1; then
  {
    kubectl get deployment,pods,replicasets,service -l "app=$APP" -n "$NAMESPACE" -o wide
    echo
    kubectl describe deployment "$APP" -n "$NAMESPACE"
    echo
    kubectl describe service "$APP" -n "$NAMESPACE"
  } > kube-deploy-accounts
elif command -v oc >/dev/null 2>&1; then
  {
    oc get deployment,pods,replicasets,service -l "app=$APP" -n "$NAMESPACE" -o wide
    echo
    oc describe deployment "$APP" -n "$NAMESPACE"
    echo
    oc describe service "$APP" -n "$NAMESPACE"
  } > kube-deploy-accounts
else
  echo "kubectl or oc is required to capture kube-deploy-accounts" >&2
  exit 1
fi

echo "Wrote kube-images and kube-deploy-accounts"
