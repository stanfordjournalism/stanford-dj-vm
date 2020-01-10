# stanford-dj-vm

Xubuntu virtual machine provisioned for Stanford data journalism
courses.

> Based on [CIR/Reveal][]'s incredibly handy [HOWTO][] on rolling a
> custom VM. Thanks y'all!l

See `bootstrap.sh` for installed software.

[CIR/Reveal]: https://github.com/cirlabs
[HOWTO]: https://github.com/cirlabs/vm/blob/master/HOWTO.md


## Building Xubuntu from Scratch

### Create the VM

Generally, follow the steps outlined in CIR's [HOWTO][]
for details on downloading Xubuntu and creating a VM.

### Provision the VM

Once you have a clean VM, execute the below shell commands **inside the Xubuntu guest** to provision the machine:

```
mkdir ~/setup
cd ~/setup

curl -s https://github.com/stanfordjournalism/stanford-dj-vm/blob/master/bootstrap.sh > bootstrap.sh
chmod a+x bootstrap.s
. ./bootstrap.sh

# Provision configuration script and User Manual for end users
curl -s https://raw.githubusercontent.com/stanfordjournalism/stanford-dj-vm/master/configure_system.py > configure_system.py

wget -O ~/Desktop/USER_MANUAL.pdf https://raw.githubusercontent.com/stanfordjournalism/stanford-dj-vm/master/USER_MANUAL.pdf 
```

### Export OVF appliance

[Exporting an Appliance in OVF
Format](https://www.virtualbox.org/manual/ch01.html#ovf-export-appliance)

## End user docs

> These docs assume the use of VirtualBox.

* Download the OVF appliance
* [Import the appliance](https://www.virtualbox.org/manual/ch01.html#ovf-import-appliance)
* Once the virtual machine is running, perform the steps outlined in the `Setup` section of the [USER_MANUAL.pdf](USER_MANUAL.pdf). A copy of the user manual is available on the Xubuntu desktop.