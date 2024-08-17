import requests
import json

__author__ = "Diariatou Sylla"
__license__ = "BSD 3 Simplified"
__version__ = "0.1.0"
__email__ = "diarrasylla15@gmail.com"

repo = "exam-git"
owner = "Diariatou-s"
secret_key = "${SECRET_KEY}"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {secret_key}",
    "X-GitHub-Api-Version": "2022-11-28",
}


def create_repo(repo_name, headers):
    """Create a GitHub repository.
    This function creates a new GitHub repository with the provided name.
    Args:
        repo_name (str): The name of the repository to create.
        owner (str): The GitHub username of the repository owner.
        headers (dict): HTTP headers used for authentication.

    Returns:
        dict: JSON response from the GitHub API if successful.
        None: If the repository creation fails.
    """
    create_repo_body = {
        "name": repo_name,
        "description": "Repository for the exam.",
        "private": False,
        "has_issues": True,
        "has_wiki": True,
        "auto_init": True,
    }

    create_repo_url = "https://api.github.com/user/repos"
    create_repo_response = requests.post(
        create_repo_url, headers=headers, data=json.dumps(create_repo_body)
    )

    if create_repo_response.status_code == 201:
        print("Dépôt créé avec succès!")
        repo_data = create_repo_response.json()
        print(f"URL du dépôt : {repo_data['html_url']}")
        return repo_data
    else:
        print(f"Échec de la création du dépôt : {create_repo_response.status_code}")
        print(create_repo_response.json())
        return None


def create_issue(repo_name, owner, issue_number, headers):
    """Create an issue in a GitHub repository.
    This function adds a new issue to the specified GitHub repository.
    Args:
        repo_name (str): The name of the repository.
        owner (str): The GitHub username of the repository owner.
        issue_number (int): The number of the issue to create.
        headers (dict): HTTP headers used for authentication.
    Returns:
        dict: JSON response from the GitHub API if successful.
        None: If the issue creation fails.
    """
    create_issue_body = {
        "title": f"Issue {issue_number}",
        "body": f"This is the issue number {issue_number}",
        "labels": ["test"],
    }

    create_issue_url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"
    create_issue_response = requests.post(
        create_issue_url, headers=headers, data=json.dumps(create_issue_body)
    )

    if create_issue_response.status_code == 201:
        print("Ticket créé avec succès!")
        issue_data = create_issue_response.json()
        print(f"URL du ticket : {issue_data['html_url']}")
        return issue_data
    else:
        print(f"Échec de la création du ticket : {create_issue_response.status_code}")
        print(create_issue_response.json())
        return None


def main():
    repo_data = create_repo(repo, headers)

    if repo_data:
        for i in range(1, 3):
            create_issue(repo, owner, i, headers)


if __name__ == "__main__":
    main()
