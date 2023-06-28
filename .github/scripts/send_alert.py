import os
from github import Github

repo_owner = os.environ['GITHUB_REPOSITORY_OWNER']
repo_name = os.environ['GITHUB_REPOSITORY']
forker = os.environ['GITHUB_ACTOR']
alert_message = f"A fork has been created for the repository {repo_name} by {forker}."

g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo(f"{repo_owner}/{repo_name}")
repo.create_commit_comment(os.environ['GITHUB_SHA'], alert_message)
