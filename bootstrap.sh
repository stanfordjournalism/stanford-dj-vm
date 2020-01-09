#!/usr/bin/env bash

# Pretty print messages
print_header() {
    length=${#1}
    line=`printf '%*s' $length | tr ' ' "="`
    echo -e '\n'$line
    echo -e $1
    echo -e "$line\n"
}


print_header "Updating Ubuntu"
# Add repositories for QGIS, R
echo "deb http://qgis.org/debian bionic main" | sudo tee -a /etc/apt/sources.list
echo "deb-src http://qgis.org/debian bionic main" | sudo tee -a /etc/apt/sources.list

# add gpg key for qgis download and install
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45

# allow apt to work with https sources
sudo apt-get install apt-transport-https

# point apt to the ubuntu repository for R
sudo echo "deb http://cran.rstudio.com/bin/linux/ubuntu bionic/" | sudo tee -a /etc/apt/sources.list

# add gpg key for R
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key E084DAB9

# add atom to repository sources
echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" | sudo tee /etc/apt/sources.list.d/atom.list

# add gpg key for atom
wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -

#Update apt-get and upgrade packages
sudo apt-get -qq update
sudo apt-get -qq upgrade

# development
print_header "Installing development tools"
sudo apt-get -qq install build-essential fortune make libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev python-dev

# Git
print_header "Installing Git"
sudo apt-get -qq install git-core

# Vim
print_header "Installing Vim"
sudo apt-get -qq install vim

# Atom
print_header "Installing Atom"
sudo apt-get install atom

# Adding curl
sudo apt-get install curl

# R and R-Studio
print_header "Installing R"
sudo apt-get install r-base r-base-dev

# pyenv
print_header "Installing pyenv"
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PATH="/home/stanford/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

source ~/.bashrc

sudo chown -R stanford:stanford .pyenv

pyenv update

print_header "Installing Python 3"
pyenv install 3.7.6
print_header "Setting 3.7.6 as the default Python version"
pyenv global 3.7.6

# python scientific stack
#print_header "Installing Python scientific stack"
#sudo apt-get -qq install python-numpy python-scipy python-matplotlib python-dev python-pip python-sip pyqt4-dev-tools

# various Python libraries we like
print_header "pip installing packaging tools and datakit"
pip install --quiet --upgrade pip
pip install pipenv
pip install csvkit
pip install datakit-core datakit-project datakit-github

# postgres
print_header "installing latest PostgreSQL and PostGIS"
sudo apt-get install -qq postgresql
sudo apt-get install -qq postgis

echo "  IMPORTANT: Remember to create a Postgres superuser for your user!"

sudo -u postgres createuser -s stanford

# Sqlite3
print_header "Installing SQLite3"
sudo apt-get install sqlite3 libsqlite3-dev

#qgis
print_header "Installing QGIS"

sudo apt-get install -y qgis python-qgis

#pspp
print_header "Installing PSPP"
sudo apt-get install pspp

#install Java
print_header "Installing Java"
sudo apt-get -qq install default-jre

#perform one last upgrade to all software packages
print_header "One last upgrade..."
sudo apt-get upgrade
