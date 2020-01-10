# stanford-dj-vm

Xubuntu virtual machine provisioned for Stanford data journalism
courses.

> Based on [CIR/Reveal][]'s incredibly handy [HOWTO][] on rolling a
> custom VM. Thanks y'all!l

See `bootstrap.sh` for installed software.

[CIR/Reveal]: https://github.com/cirlabs
[HOWTO]: https://github.com/cirlabs/vm/blob/master/HOWTO.md


## Building Xubuntu from Scratch

Generally, follow the steps outlined in CIR's [HOWTO][]
for details on downloading Xubuntu and creating a VM.

Once you have a clean VM, execute the below shell commands **inside the Xubuntu guest**
to provision the machine:

```
mkdir ~/setup
cd ~/setup

curl -s https://github.com/stanfordjournalism/stanford-dj-vm/blob/master/bootstrap.sh > bootstrap.sh
chmod a+x bootstrap.s
. ./bootstrap.sh

# Below script should only be run by end users
curl -s https://github.com/stanfordjournalism/stanford-dj-vm/blob/master/configure_system.py > configure_system.py
```

## User configuration

Every user should `configure_system.py` to generate ssh keys and
configure git and datakit.

```
python ~/setup/configure_system.py
```
