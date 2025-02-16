from setuptools import setup, find_packages

setup(
    name="create_workspace",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create-workspace = create_workspace.workspace_creator:main',
        ],
    },
    install_requires=[],
)
