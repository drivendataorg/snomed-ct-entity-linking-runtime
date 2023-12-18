import json
import sys
import warnings
from os import PathLike
from pathlib import Path

import yaml


def main(lockfile_path: PathLike):
    with Path(lockfile_path).open("r") as fp:
        lockfile = yaml.safe_load(fp)

    conda_deps = {
        package["name"]: package["version"]
        for package in lockfile["package"]
        if package.get("manager") == "conda"
    }
    pip_deps = {
        package["name"]: package["version"]
        for package in lockfile["package"]
        if package.get("manager") == "pip"
    }

    duplicated_deps = conda_deps.keys() & pip_deps.keys()
    version_info = {
        dep: {"conda": conda_deps[dep], "pip": pip_deps[dep]} for dep in duplicated_deps
    }

    if len(duplicated_deps):
        version_info = {
            dep: {"conda": conda_deps[dep], "pip": pip_deps[dep]} for dep in duplicated_deps
        }
        warnings.warn(
            f"The lockfile includes conda and pip versions for the following package(s): {', '.join(duplicated_deps)}. "
            "This will result in the conda version being uninstalled in favor of the pip version. "
            f"This can usually be fixed by updating {lockfile_path} to pin the package in the dependencies section to the version that pip requests.\n\n"
            f"""{json.dumps(version_info, indent=2)}"""
        )
    else:
        print(f"Lockfile {lockfile_path} passed.")


if __name__ == "__main__":
    main(sys.argv[1])
