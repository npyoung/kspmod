#!/usr/bin/env python


import click
import re
import requests
import json
from tempfile import TemporaryFile
from zipfile import ZipFile


@main.command()
@click.argument('project_path', type=str, required=True)
@click.argument('ksp_path', type=str, required=True)
def install(project_path, ksp_path):
    pattern = re.compile(r"https:\/\/github.com\/(\w+)\/(\w+)")
    match = pattern.match(project_path)
    user, repo = match.groups()
    response = requests.get(f"https://api.github.com/repos/{user:s}/{repo:s}/releases/latest")
    response_json = json.loads(response.content)
    zip_url = response_json["assets"][0]["browser_download_url"]
    zip_response = requests.get(zip_url)
    with TemporaryFile() as tf:
        tf.write(zip_response.content)

        with ZipFile(tf) as zip_file:
            zip_file.extractall(ksp_path)


@click.group()
def main():
    pass


if __name__ == "__main__":
    main()
