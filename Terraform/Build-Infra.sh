#!/bin/bash

export TF_VAR_vm_ssh_key=$CI_VM_SSH_PUBLIC_KEY
export TF_USERNAME=$CI_TF_USERNAME
export TF_AZURE_SUB_ID=$CI_ARM_SUBSCRIPTION_ID
echo "Initializing Terraform..."
terraform init
echo "Applying Terraform configuration..."
terraform apply -auto-approve \
    -var="admin_username=$TF_USERNAME" \
    -var="subscription_id=$TF_AZURE_SUB_ID" | tee terraform-output.txt
terraform output -json > terraform-output.json
