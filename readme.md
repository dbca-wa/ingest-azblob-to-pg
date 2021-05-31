# ingest-azblob-to-pg - Python

This function app is intended to be wired up to an eventgrid `blobtrigger` event that picks up blobs from a storage container and processes them into a staging area for further processing.

## Initial setup

- Clone this repository
- Setup venv ```python3 -m venv .venv```, then use vscode to run debug or run pipInstall tasks
- Configure `local.settings.json`
- Upload settings to a function app (easiest to create in portal then deploy from VS Code)
- Deploy project to a function app
