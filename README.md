# nhvss_python

## Table of contents

- [nhvss\_python](#nhvss_python)
  - [Table of contents](#table-of-contents)
  - [What is nhvss ?](#what-is-nhvss-)
  - [How it works ?](#how-it-works-)
  - [Pre-requisites](#pre-requisites)
  - [How to install ?](#how-to-install-)
    - [on Debian based systems](#on-debian-based-systems)
    - [on RedHat based systems](#on-redhat-based-systems)
    - [on Arch based systems](#on-arch-based-systems)
    - [on fedora based systems](#on-fedora-based-systems)
    - [Setup the script](#setup-the-script)
    - [How to use it ?](#how-to-use-it-)
  - [Warning](#warning)

## What is nhvss ?

Nhvss (**N**map **H**ost **V**ulnerability **S**canner **S**cript) is a python tool that allows you to scan a network for vulnerabilities. It uses [Nmap](https://nmap.org/book/man.html#man-description) to scan the network and uses the **vulners** script to scan the discovered hosts for vulnerabilities.

## How it works ?

The script uses Nmap to index any host on the network and then uses the **vulners** script to scan the hosts for vulnerabilities. The hosts Networkadresses are stored in a file that goes by a similar name as **YYYY-MM-DD_HH-MinMin-SS_hosts.txt**. The script will then scan the hosts in the file for vulnerabilities and stores the results of each host in seperate files in the [scan_history](scan_history) folder.

## Pre-requisites

Currently the script only works on Linux systems. The script requires the following packages to be installed:

- Nmap
- Python3

## How to install ?

To install the script you need to have Nmap and Python installed on your system. You can install Nmap by running the following command:

### on Debian based systems

```bash
sudo apt-get install nmap
```

```bash
sudo apt-get install python3
```

### on RedHat based systems

```bash
sudo yum install nmap
```

```bash
sudo yum install python3
```

### on Arch based systems

I currently don't know the command to install Nmap on Arch based systems. If you know the command please let me know.

### on fedora based systems

```bash
sudo dnf install nmap
```

```bash
sudo dnf install python3
```

After you have installed Nmap and Python3 you can install the script by running the following commands:

```bash
git clone https://github.com/Moineau54/nhvss_python.git
cd PatH/TO/nhvss_python
```

### Setup the script

Now, if you're on linux or Mac, first make the script executable by running the following command:

```bash
chmod +x install_linux_mac.sh
```

Then run the script by running the following command:

```bash
./install_linux_mac.sh
```

If you're on Windows, run the **install_win.bat** file.

### How to use it ?

Run the script by running the following command:

```bash
# You have to launch the script from the git repository
python /path/to/nhvss.py
```

The script will then ask you if you want to additionally scan the hosts for vulnerabilities. If you want to scan the hosts for vulnerabilities type **y** and press enter. If you don't want to scan the hosts for vulnerabilities type **n** and press enter.

## Warning

The script is still in development and may not work as intended. If you encounter any bugs or have any suggestions please let me know.

This script is for educational and security purposes only. I am not responsible for any damage caused by the script. Use at your own risk.
More on why I made this script can be found in this article on my [blog](https://moineau54.github.io/Moineau-s-tech-corner/2024/07/13/Nmap-Host-Vulnerabilty-Scanner-Script.html).
