variable "admin_username" {
  description = "The admin username for the virtual machine"
  type        = string
}

variable "vm_ssh_key" {
  description = "The public SSH key to access the virtual machine"
  type        = string
}

variable "subscription_id" {
  description = "The Azure subscription ID"
  type        = string
}
