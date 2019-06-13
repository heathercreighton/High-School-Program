# Git Setup

## Time to git it!

Git is the current industry standard for version control. It was originally developed in 2005 by the creator of the Linux operating system, Linus Torvalds.

The Home Depot uses Git because of advantages offered over alternative VCS offerings. Some of the advantages include:

* Superior performance, flexibility and security   
* The broad adoption of Git across the industry makes it an attractive option, especially when it comes to using and contributing to open-source software. Many third-party software tools integrate really well with Git.
* Git itself is an open source project. This means that we can use the Git software without paying a fee and we can lean on the support and contributions of the developer community, as well as contribute back to the source code. This level of scrutiny serves to raise the quality of the software for everyone.

## Create a GitHub account

Go to https://github.com.

Click on sign up. Enter your email and create a username, and password.

You now have a GitHub account!

## Configuring your credentials in git
    
Before we can work with git you first have to make sure you have git.

In your terminal type `git --version`

If git is installed you should see something like this:

```
git version 2.x.x
```

If git isn't installed then copy and paste the following into your terminal.

```
git clone https://github.com/git/git
```

`git clone` command will be discussed later, just trust us for now.

The following commands will customize your configuration with your user name and your email so that your changes can be traced back to you (and then appropriate kudos or punishments can be administered)

```
git config --global --list

git config --global --unset user.name

git config --global --unset user.email

git config --global user.name "John Doe"

git config --global user.email johndoe@example.com
```

