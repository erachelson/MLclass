#!/usr/bin/env bash

IMAGE_FAMILY="tf-latest-cpu"
ZONE="europe-west4-a"
INSTANCE_NAME="tp-isae-dev-cpu"

gcloud compute instances create ${INSTANCE_NAME} \
  --zone=${ZONE} \
  --image-family=${IMAGE_FAMILY} \
  --image-project=deeplearning-platform-release \
  --machine-type=n1-standard-8 \
  --maintenance-policy=TERMINATE \
  --preemptible \
  --tags=jupyter \
  --scopes default \
  --scopes storage-rw

#gcloud beta compute --project=deeplearningsps instances create instance-1 \
# --zone=us-central1-c \
# --machine-type=n1-standard-1 \
# --subnet=default \
# --network-tier=PREMIUM \
# --maintenance-policy=MIGRATE \
# --service-account=231775026498-compute@developer.gserviceaccount.com \
# --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --image=debian-9-stretch-v20181011 \
# --image-project=debian-cloud \
# --boot-disk-size=10GB \
# --boot-disk-type=pd-standard \
# --boot-disk-device-name=instance-1
