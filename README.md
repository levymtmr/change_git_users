# Change Git Local User
One way to automate the change of git user for each project


# How does it work

- A simple script to get a txt file inside the each folder project.
- The script get user name and email and set git current user.

# Setup

- Just download the file.

- Create alias inside the .vimrc or .zshrc to access the script with command lines.  

- Change the string path in **projects_path** for your project folders.

- Inside the each project create a **git_user.txt** file 
with just username and email 

- File example:
```
user test, usertest@test.com
```

Thanks!