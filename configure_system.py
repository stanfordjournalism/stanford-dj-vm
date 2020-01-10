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
    home_dir = os.path.expanduser('~')
    create_configs(home_dir, name, email)
    generate_ssh_keys(home_dir, email)
    configure_git(home_dir, name, email)

def ask_confirm(question):
    answer = input(question)
    answer_clean = answer.strip()
    confirm = input("Is '{}' correct? [yes/no]: ".format(answer_clean))
    if confirm.lower().strip()  in ['y', 'yes']:
        return answer_clean
    else:
        sys.exit("Exiting. Please try again.")

def create_configs(home, user, email):
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

def generate_ssh_keys(home, email):
    private_key = os.path.join(ssh_dir, '.ssh/id_rsa')
    if os.path.exists(private_key):
        print("SSH keys already generated. Skipping!")
    else:
        subprocess.check_call([
            'ssh–keygen', '–t', 'rsa', '4096',
            '-N', "", "-f", private_key
        ])

def configure_git(home, name, email):
    gitconfig = os.path.join(home, '.gitconfig')
    if os.path.exists(gitconfig):
        print("Git user name/email already seem to be configured. Skipping!")
        return
    subprocess.check_call([
        'git', 'config', '--global',
        'user.name', '"{}"'.format(name)
    ])
    subprocess.check_call([
        'git', 'config', '--global',
        'user.email', '"{}"'.format(email)
    ])

if __name__ == '__main__':
    main()
