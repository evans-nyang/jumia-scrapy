import os
from github import Github

# Create a GitHub API client instance
github_token = os.getenv('GITHUB_TOKEN')
g = Github(github_token)

# Get the repository and issue details
repo_owner = os.getenv('GITHUB_REPOSITORY_OWNER')
repo_full_name = os.getenv('GITHUB_REPOSITORY')
repo_name = repo_full_name.split('/')[1] if repo_full_name else None
issue_number = os.getenv('GITHUB_EVENT_ISSUE_NUMBER')

# Ensure all required environment variables are available
if not (repo_owner and repo_name and issue_number):
    raise ValueError("Missing required environment variables.")

# Get the repository and issue objects
repo = g.get_repo(repo_full_name)
issue = repo.get_issue(int(issue_number))

# Get the pull request object associated with the issue
pull_request = issue.as_pull_request()

# Get the developer's username from the pull request
developer_username = pull_request.user.login

# Get the contributors for the repository
contributors = repo.get_contributors()

# Check if the developer has contributed to the repository
is_contributor = any(contributor.login == developer_username for contributor in contributors)

# Print the contributor status
print(f"Is contributor: {is_contributor}")
