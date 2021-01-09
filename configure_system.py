'''
This script helps configure datakit, git and ssh
on a fresh Xubuntu build. Also designed to work
on Macs.

Usage:
    python configure_system.py

'''
import os
import json
import shlex
import subprocess
import sys


def main():
    name = ask_confirm("Full name? ")
    email = ask_confirm("Email? ")
    home_dir = os.path.expanduser('~')
    create_configs(home_dir, name, email)
    generate_ssh_keys(home_dir, email)
    configure_git(home_dir, name, email)
    next_steps()

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
        if file_exists(final_path) and file_has_content(final_path):
            print("{} already exists. Skipping!".format(final_path))
            continue
        if 'cookiecutterrc' in final_path:
            settings = settings.format(user, email)
            write_file(final_path, settings)
            continue
        create_dir(final_path)
        write_json(final_path, settings)


def file_exists(file_path):
    return os.path.exists(file_path)

def file_has_content(file_path):
    return os.path.getsize(file_path) > 0

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
    private_key = os.path.join(home, '.ssh/id_rsa')
    if os.path.exists(private_key):
        print("SSH keys already generated. Skipping!")
    else:
        binary = get_bin_path('ssh-keygen')
        cmd = "{} -q -t rsa -b 4096 -C {} -N '' -f {}".format(
            binary, email, private_key)
        parsed_cmd = shlex.split(cmd)
        subprocess.call(parsed_cmd)
        print("SSH keys generated in ~/.ssh")

def configure_git(home, name, email):
    gitconfig = os.path.join(home, '.gitconfig')
    if os.path.exists(gitconfig):
        print("Git user name/email already seem to be configured. Skipping!")
        return
    print("Configuring {}".format(gitconfig))
    binary = get_bin_path('git')
    subprocess.check_call([
        binary, 'config', '--global',
        'user.name', '{}'.format(name)
    ])
    subprocess.check_call([
        binary, 'config', '--global',
        'user.email', '{}'.format(email)
    ])
    print("Git user name/email configured")

def get_bin_path(name):
    return subprocess\
            .check_output(['which', name])\
            .decode('utf-8').strip()

def next_steps():
    print('\n\n=== Next Steps ===')

    ssh_key_help = '    https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account'
    print('\n(1) Upload your ssh public key to GitHub by following these steps:')
    print(ssh_key_help + '\n')

    api_token_help = '    https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line'
    print('\n(2) Create a GitHub API token by following steps here:')
    print(api_token_help + '\n')

    config = '    ~/.datakit/plugins/datakit-github/config.json'
    print('\n(3) Add the API token to the below config file:')
    print(config, '\n')

if __name__ == '__main__':
    main()
