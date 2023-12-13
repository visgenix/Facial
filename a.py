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
    print("Data to be written:", data)

try:
    repo.create_file('a.py', 'python file', data, branch='main')
except GithubException as e:
    if e.status == 422:
        existing_file = repo.get_contents('a.py', ref='main')
        repo.update_file('a.py', 'Update python file', data, existing_file.sha, branch='main')
        print("done")
    else:
        raise e

# repo_name = 'your_repository_name'
# file_path = 'gt.py'
# branch_name = 'main'

# repo = g.get_user().get_repo(repo_name)

# with open(file_path, 'r') as file:
#     data = file.read()

# try:
#     # Try to create a new file
#     repo.create_file(file_path, 'python file', data, branch=branch_name)
# except GithubException as e:
#     # Check if the exception is due to the file already existing
#     if e.status == 422:  # 422 status code indicates that the resource already exists
#         # Get the existing file content
#         existing_file = repo.get_contents(file_path, ref=branch_name)
#         existing_data = existing_file.decoded_content.decode('utf-8')

#         # Update the existing file with new data
#         repo.update_file(file_path, 'Update python file', data, existing_file.sha, branch_name)
#     else:
#         # Re-raise the exception if it's not due to the file already existing
#         raise e

# # Print the updated file content
# updated_file = repo.get_contents(file_path, ref=branch_name)
# print(updated_file.decoded_content.decode('utf-8'))
