# Stanford Data Journalism VM

This Xubuntu virtual machine includes software used in data journalism courses at [Stanford](https://journalism.stanford.edu/).

Below is a partial list of software available on this machine:

* [Atom](https://atom.io/) for code editing
* [QGIS](https://www.qgis.org/en/site/) for geospatial analysis
* [Postgres](https://www.postgresql.org/) and [SQLite](https://sqlite.org/index.html) databases
* [git](https://git-scm.com/book/en/v2) for software version control
* Python 3.7 and [pipenv](https://pipenv.readthedocs.io/en/latest/)
* [R](https://www.r-project.org/) and [RStudio](https://rstudio.com/)
* Command-line tools:
  * [csvkit](https://csvkit.readthedocs.io/en/latest/) for wrangling data
  * [datakit](https://datakit.ap.org/) for automating analysis workflows


## Setup 

* Create a [GitHub](https://github.com/) account if you don't already have one.
* Open a bash shell by clicking the `Terminal Emulator` icon on the Desktop.
* Run the following code in the shell:

```
python ~/setup/configure_system.py
```

* [Add your ssh key to GitHub][]
* [Generate a GitHub personal API token][]
* Add the GitHub API token to `~/.datakit/plugins/datakit-github/config.json`

[Add your ssh key to GitHub]: https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account

[Generate a GitHub personal API token]: https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line

## Detailed technical info

Details on how this VM was created are [on GitHub](https://github.com/stanfordjournalism/stanford-dj-vm).  For a full list of software added to this machine, see the [bootstrap](https://github.com/stanfordjournalism/stanford-dj-vm/blob/master/bootstrap.sh) and [configuration](https://github.com/stanfordjournalism/stanford-dj-vm/blob/master/configure_system.py) scripts.