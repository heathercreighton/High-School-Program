import subprocess
import os
from tkinter import *
from tkinter import filedialog
from .git_gui import *
import re
from pathlib import Path


def tcmd(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, timeout=10,
                                         universal_newlines=True)
    except subprocess.CalledProcessError as exc:
        error_msg = "Status : FAIL" + str(exc.returncode) + " " + str(exc.output)
        print(error_msg)
        return error_msg
    else:
        if len(output) > 0:
            return str(command) + " output:\n\t" + str(output)
        else:
            return command


def init_setup(local_path, remote_path):
    os.chdir(local_path)
    files = tcmd("ls -la")
    if ".git" not in files:
        tcmd('echo "GITHUB GUI" >> README.md')
        tcmd("git init")
        add()
        commit("Creating Git Repository")
        tcmd("git remote add origin " + str(remote_path))
        return tcmd("git push -u origin master")
    else:
        tcmd('echo "GITHUB GUI" >> README.md')
        add()
        commit("Adding Github to local repo")
        tcmd("git remote set-url origin " + str(remote_path))
        return tcmd("git push --set-upstream origin master")


def check_branches():
    try:
        output = subprocess.check_output("git branch", stderr=subprocess.STDOUT, shell=True, timeout=10,
                                         universal_newlines=True)
    except subprocess.CalledProcessError as exc:
        return "Status : FAIL" + str(exc.returncode) + " " + str(exc.output)
    else:
        return re.findall(r"[\w']+", output)


def switch_branch(branch_name):
    add()
    commit("Working with " + branch_name + " branch")
    if branch_name in check_branches():
        tcmd("git checkout " + str(branch_name))
        return "Switched to " + branch_name + " branch"
    else:
        tcmd("git checkout -b " + str(branch_name))
        return "Created " + branch_name + " branch"


def pull():
    return tcmd("git pull origin master")


def add():
    return tcmd("git add .")


def commit(commit_msg):
    return tcmd('git commit -m "' + str(commit_msg) + '"')


def push(branch_name):
    return tcmd("git push --set-upstream origin " + str(branch_name))


if __name__ == "__main__":
    local = "/Users/exp0ct5/OrangeMethod/git_gui"
    remote = "https://github.homedepot.com/EXP0CT5/GitHub.git"
    branch = "testing_tkinter"
    os.chdir(local)

    # print(switch_branch('create_gui'))

    '''init_setup(local, remote)
    create_branch(branch)
    pull()
    commit("Adding more info")
    push(branch)'''
