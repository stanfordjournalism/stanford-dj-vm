'''
This script helps configure datakit, git and ssh
on a fresh Xubuntu build.

Usage:
    python configure_system.py

'''
import os
import json
import subprocess
import sys


def main():
    name = ask_confirm("Full name? ")
    email = ask_confirm("Email? ")
    create_configs(name, email)
    generate_ssh_keys()
    configure_git()

def ask_confirm(question):
    answer = input(question)
    answer_clean = answer.strip()
    confirm = input("Is '{}' correct? [yes/no]: ".format(answer_clean))
    if confirm.lower().strip()  in ['y', 'yes']:
        return answer_clean
    else:
        sys.exit("Exiting. Please try again.")

def create_configs(user, email):
    cc_config = "default_context:\n    full_name: {}\n    email: {}"
    dkit_proj_config = {"default_template": ""}
    dkit_gh_config = {"github_api_key": "GITHUB_API_TOKEN"}
    configs = {
        '~/.cookiecutterrc': cc_config,
        '~/.datakit/plugins/datakit-project/config.json': dkit_proj_config,
        '~/.datakit/plugins/datakit-github/config.json': dkit_gh_config,
    }
    for path, settings in configs.items():
        if os.path.exists(path):
            print("{} already exists. Skipping!")
            continue
        if 'cookiecutterrc' in path:
            settings = settings.format(user, email)
        create_dir(path)
        write_json(path, settings)

def create_dir(path):
    pth = os.path.dirname(path)
    os.makedirs(pth, exist_ok=True)

def write_file(path, content):
    with open(path) as f:
        f.write(content)
    print("Created {}".format(path))

def write_json(path, content):
    with open(path) as f:
        json.dump(content, f, indent=4)
    print("Created {}".format(path))

def generate_ssh_keys():
    if os.path.exists("~/.ssh/id_rsa"):
        print("SSH keys already generated. Skipping!")
        return
    #TODO: subprocess call

def configure_git(name, email):
    if os.path.exists("~/.gitconfig"):
        print("Git user name/email already seem to be configured. Skipping!")
        return
    #TODO: subprocess call

if __name__ == '__main__':
    main()
