
from github import Github

def fetch_github_repo(repo_url, token=None):
    g = Github(token) if token else Github()
    repo_name = "/".join(repo_url.split("/")[-2:])
    repo = g.get_repo(repo_name)
    files_data = []

    def process_contents(contents, path=""):
        for content_file in contents:
            if content_file.type == "dir":
                process_contents(repo.get_contents(content_file.path), path + content_file.name + "/")
            else:
                try:
                    file_content = repo.get_contents(content_file.path).decoded_content.decode("utf-8", errors="ignore")
                    files_data.append({"path": path + content_file.name, "content": file_content})
                except:
                    continue

    process_contents(repo.get_contents(""))
    return files_data
