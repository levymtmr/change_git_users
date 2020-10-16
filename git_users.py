import sys
import os


projects_path = os.chdir('change for project path folders')
current_path = os.getcwd()


def change_git_user(user_name, user_email):
    cmd = "git config --global user.name '{}'".format(user_name)
    os.system(cmd)
    cmd = "git config --global user.email '{}'".format(user_email)
    os.system(cmd)
    user = 'git config user.name'
    email = 'git config user.email'
    os.system(user)
    os.system(email)

def change_current_path():
    project_name = sys.argv[1]
    project_path = current_path + '/' + project_name + '/'
    os.chdir(project_path)
    new_current_path_location = os.getcwd()

try:
    change_current_path()

    credentials = open('git_user.txt', 'r')
    user = credentials.read().split(',')
    user_name, user_email = user[0], user[1]

    change_git_user(user_name, user_email)

    print('Success!!!')
except:
    print('Something wrong!!!')