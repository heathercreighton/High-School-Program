# Git Setup

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

