# Create Workspace Project

This project provides a command-line tool to create a workspace for a FastAPI project integrated with HTMX and configured for Docker.

## Installation

From the root directory (`create_workspace_project/`), run:

```bash
pip install .
```
## Usage

After installation, run the tool from your command line:

```bash
create-workspace
```

You will be prompted to enter a base folder name. The tool will then create a workspace with the following structure:

```
<your-base-folder>/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```
## About


---

### File: `create_workspace_project/create_workspace/__init__.py`

This file can be empty or contain package-level variables (such as version information).

```python
__version__ = "0.1.0"
```



