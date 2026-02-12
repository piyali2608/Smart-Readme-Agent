import os

def extract_project_text(folder_path: str) -> str:
    project_text = ""

    for root, dirs, files in os.walk(folder_path):
        for f in files:
            if f.endswith((".py", ".js", ".ts", ".html", ".css", ".md", ".txt")):
                try:
                    with open(os.path.join(root, f), "r", errors="ignore") as file:
                        project_text += f"\n\nFILE: {f}\n"
                        project_text += file.read()
                except:
                    pass

    return project_text



