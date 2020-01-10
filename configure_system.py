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
    generate_ssh_keys(email)
    configure_git(name, email)

def ask_confirm(question):
    answer = input(question)
    answer_clean = answer.strip()
    confirm = input("Is '{}' correct? [yes/no]: ".format(answer_clean))
    if confirm.lower().strip()  in ['y', 'yes']:
        return answer_clean
    else:
        sys.exit("Exiting. Please try again.")

def create_configs(user, email):
    home = os.path.expanduser('~')
    cc_config = "\n".join([
        "default_context:",
        "    full_name: {}".format(user),
        "    email: {}".format(email)
    ])
    dkit_proj_config = {"default_template": ""}
    dkit_gh_config = {"github_api_key": "GITHUB_API_TOKEN"}
    configs = {
        '.cookiecutterrc': cc_config,
        '.datakit/plugins/datakit-project/config.json': dkit_proj_config,
        '.datakit/plugins/datakit-github/config.json': dkit_gh_config,
    }
    for path, settings in configs.items():
        final_path = os.path.join(home, path)
        if os.path.exists(final_path):
            print("{} already exists. Skipping!".format(final_path))
            continue
        if 'cookiecutterrc' in final_path:
            settings = settings.format(user, email)
            write_file(final_path, settings)
            continue
        create_dir(final_path)
        write_json(final_path, settings)

def create_dir(path):
    pth = os.path.dirname(path)
    os.makedirs(pth, exist_ok=True)

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)
    print("Created {}".format(path))

def write_json(path, content):
    with open(path, 'w') as f:
        json.dump(content, f, indent=4)
    print("Created {}".format(path))

def generate_ssh_keys(email):
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
