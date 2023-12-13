from github import Github
from github import GithubException
from github import Auth
from token_1 import token

auth = Auth.Token(token)

g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)
    
with open('a.py', 'r') as file:
    data = file.read()
    # print("Data to be written:", data)

try:
    repo.create_file('a.py', 'python file', data, branch='main')

except GithubException as e:
    if e.status == 422:
        existing_file = repo.get_contents('a.py', ref='main')
        repo.update_file('a.py', 'Update python file', data, existing_file.sha, branch='main')
        print("done")