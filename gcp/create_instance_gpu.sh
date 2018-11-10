#!/usr/bin/env bash

IMAGE_FAMILY="tf-1-11-gpu"
ZONE="europe-west4-a"
INSTANCE_NAME="tp-isae-dev-gpu"

gcloud compute instances create ${INSTANCE_NAME} \
  --zone=${ZONE} \
  --image-family=${IMAGE_FAMILY} \
  --image-project=deeplearning-platform-release \
  --machine-type=n1-standard-8 \
  --maintenance-policy=TERMINATE \
  --preemptible \
  --tags=jupyter \
  --scopes default \
  --scopes storage-rw \
  --accelerator='type=nvidia-tesla-v100,count=1' \
  --metadata='install-nvidia-driver=True'
