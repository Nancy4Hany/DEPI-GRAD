#!/bin/bash

chmod 400 gitlab_rsa
python3 ./set-inventory.py
ansible-playbook -i inventory.ini minikube.yml -vvv | tee .minikube-playbook-output.txt


