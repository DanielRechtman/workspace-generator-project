import os

class WorkspaceCreator:
    def __init__(self, base_folder: str):
        self.base = base_folder.strip()
        if not self.base:
            self.base = input("Enter the base folder name: ")
            # raise ValueError("Base folder name cannot be empty!")
        # Ensure the base folder exists
        os.makedirs(self.base, exist_ok=True)

    def create_directories(self):
        print("Creating directories...")
        os.makedirs(os.path.join(self.base, "app", "templates"), exist_ok=True)
        os.makedirs(os.path.join(self.base, "app", "static"), exist_ok=True)

    def create_files(self):
        print("Creating empty project files...")
        files = [
            os.path.join(self.base, "app", "__init__.py"),
            os.path.join(self.base, "app", "main.py"),
            os.path.join(self.base, "app", "templates", "index.html"),
            os.path.join(self.base, "app", "static", "style.css"),
            os.path.join(self.base, "requirements.txt")
        ]
        for file in files:
            with open(file, "w", encoding="utf-8") as f:
                pass  # Creates an empty file

    def write_dockerfile(self):
        print("Writing Dockerfile...")
        dockerfile_content = """# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \\
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 80

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
"""
        with open(os.path.join(self.base, "Dockerfile"), "w", encoding="utf-8") as f:
            f.write(dockerfile_content)

    def write_docker_compose(self):
        print("Writing docker-compose.yml...")
        docker_compose_content = """version: "3.8"

services:
  web:
    build: .
    ports:
      - "8000:80"
"""
        with open(os.path.join(self.base, "docker-compose.yml"), "w", encoding="utf-8") as f:
            f.write(docker_compose_content)

    def write_readme(self):
        print("Writing README.md...")

        project_structure = (
    "```\n"
    f"{self.base}/\n"
    "├── app/\n"
    "│   ├── __init__.py\n"
    "│   ├── main.py\n"
    "│   ├── templates/\n"
    "│   │   └── index.html\n"
    "│   └── static/\n"
    "│       └── style.css\n"
    "├── requirements.txt\n"
    "├── Dockerfile\n"
    "├── docker-compose.yml\n"
    "└── README.md\n"
    "```\n"
)
        readme_content = f"""# FastAPI HTMX Project

This is a starter workspace for a FastAPI project integrated with HTMX and containerized using Docker.

## Project Structure

{project_structure}


## Getting Started

### Using Docker

1. Build and run the container:
   docker-compose up --build

2. Access the application:
   Open your browser and navigate to http://localhost:8000

### Without Docker

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   uvicorn app.main:app --reload

3. Access the application:
   Open your browser and navigate to http://localhost:8000

## About

This project is a minimal starter template that integrates FastAPI with HTMX for dynamic web interactions and is set up for Docker deployment. Customize and expand upon this template as needed.
"""
        with open(os.path.join(self.base, "README.md"), "w", encoding="utf-8") as f:
            f.write(readme_content)

    def create_workspace(self):
        self.create_directories()
        self.create_files()
        self.write_dockerfile()
        self.write_docker_compose()
        self.write_readme()
        print(f"Workspace '{self.base}' has been created with the required structure, starter files, Docker configuration, and README documentation.")

    
   
def main():
        base_folder = input("Enter the base folder name: ")
        try:
            creator = WorkspaceCreator(base_folder)
            creator.create_workspace()
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main();
    # base_folder = input("Enter the base folder name: ")
    # try:
    #     creator = WorkspaceCreator(base_folder)
    #     creator.create_workspace()
    # except ValueError as e:
    #     print(e)
