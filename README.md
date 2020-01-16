# stanford-dj-vm

Xubuntu virtual machine provisioned for Stanford data journalism
courses. 

The VM is based largely on [CIR/Reveal][]'s incredibly handy [instructions][] on rolling a custom VM. Thanks y'all!

See [bootstrap.sh](bootstrap.sh) for details on installed software, or install the VM and kick the tires.

[CIR/Reveal]: https://github.com/cirlabs
[instructions]: https://github.com/cirlabs/vm/blob/master/HOWTO.md

## Download and install

> These docs assume the use of VirtualBox, although the VM should also work with VMWare and any virtualization software that supports OVF 1.0.

**Download pre-built [stanford-dj-vm](https://www.dropbox.com/s/c5gfwrm3ofmejk5/stanford-dj-vm.ova?dl=0)**.

* Download the OVF appliance
* [Import the appliance](https://www.virtualbox.org/manual/ch01.html#ovf-import-appliance)
* Once the virtual machine is running, perform the steps outlined in the `Setup` section of the [USER_MANUAL.pdf](USER_MANUAL.pdf). A copy of the user manual is available on the Xubuntu desktop.


## Roll your own Xubuntu from scratch

### Create the VM

Generally, follow the steps outlined in CIR's [HOWTO][]
for details on downloading Xubuntu and creating a VM.

### Provision the VM

Once you have a clean VM, execute the below shell commands **inside the Xubuntu guest** to provision the machine:

```
mkdir ~/setup
cd ~/setup

curl -O https://raw.githubusercontent.com/stanfordjournalism/stanford-dj-vm/master/bootstrap.sh
chmod a+x bootstrap.s
. ./bootstrap.sh

# Provision configuration script and User Manual for end users
curl -O https://raw.githubusercontent.com/stanfordjournalism/stanford-dj-vm/master/configure_system.py

cd ~/Desktop && curl -O https://raw.githubusercontent.com/stanfordjournalism/stanford-dj-vm/master/USER_MANUAL.pdf 
```

### Export OVF appliance

> Before exporting the machine, you must power it down. If the machine
> is saved in a running state, you will get a warning during the export process.
> 
[Exporting an Appliance in OVF
Format](https://www.virtualbox.org/manual/ch01.html#ovf-export-appliance)

