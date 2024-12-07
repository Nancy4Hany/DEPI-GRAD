import json
import configparser
import os

# Load the JSON output from Terraform
with open('../Terraform/terraform-output.json', 'r') as file:
    data = json.load(file)

# Create a ConfigParser object
config = configparser.ConfigParser(allow_no_value=True)

# Set default SSH user, fallback to 'azureuser' if the environment variable is not set
ssh_user = os.environ.get('CI_TF_USERNAME', 'azureuser')

# Retrieve the public IP from the Terraform output
public_ip = data['public_ip']['value']

# Add the public IP to the Ansible inventory under the 'minikube' section with separate key-value pairs
config.add_section('minikube')
config.set('minikube', f"{public_ip} ansible_user={ssh_user} ansible_ssh_private_key_file=./gitlab_rsa")

# Add common SSH arguments for all hosts
config['all:vars'] = {
    "ansible_ssh_common_args": "'-o StrictHostKeyChecking=no'"
}

# Write the configuration data to the INI file
with open('inventory.ini', 'w') as configfile:
    config.write(configfile)

# Notify that the process has been completed 
print(f"Public IP {public_ip} saved to inventory.ini")
