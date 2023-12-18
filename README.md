# SNOMED CT Entity Linking Runtime

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue) [![Snomed CT Entity Linking Challenge](https://img.shields.io/badge/DrivenData-SNOMED%20CT%20Entity%20Linking%20Challenge-white?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAABBlpQ0NQa0NHQ29sb3JTcGFjZUdlbmVyaWNSR0IAADiNjVVdaBxVFD67c2cjJM5TbDSFdKg/DSUNk1Y0obS6f93dNm6WSTbaIuhk9u7OmMnOODO7/aFPRVB8MeqbFMS/t4AgKPUP2z60L5UKJdrUICg+tPiDUOiLpuuZOzOZabqx3mXufPOd75577rln7wXouapYlpEUARaari0XMuJzh4+IPSuQhIegFwahV1EdK12pTAI2Twt3tVvfQ8J7X9nV3f6frbdGHRUgcR9is+aoC4iPAfCnVct2AXr6kR8/6loe9mLotzFAxC96uOFj18NzPn6NaWbkLOLTiAVVU2qIlxCPzMX4Rgz7MbDWX6BNauuq6OWiYpt13aCxcO9h/p9twWiF823Dp8+Znz6E72Fc+ys1JefhUcRLqpKfRvwI4mttfbYc4NuWm5ERPwaQ3N6ar6YR70RcrNsHqr6fpK21iiF+54Q28yziLYjPN+fKU8HYq6qTxZzBdsS3NVry8jsEwIm6W5rxx3L7bVOe8ufl6jWay3t5RPz6vHlI9n1ynznt6Xzo84SWLQf8pZeUgxXEg4h/oUZB9ufi/rHcShADGWoa5Ul/LpKjDlsv411tpujPSwwXN9QfSxbr+oFSoP9Es4tygK9ZBqtRjI1P2i256uv5UcXOF3yffIU2q4F/vg2zCQUomDCHvQpNWAMRZChABt8W2Gipgw4GMhStFBmKX6FmFxvnwDzyOrSZzcG+wpT+yMhfg/m4zrQqZIc+ghayGvyOrBbTZfGrhVxjEz9+LDcCPyYZIBLZg89eMkn2kXEyASJ5ijxN9pMcshNk7/rYSmxFXjw31v28jDNSpptF3Tm0u6Bg/zMqTFxT16wsDraGI8sp+wVdvfzGX7Fc6Sw3UbbiGZ26V875X/nr/DL2K/xqpOB/5Ffxt3LHWsy7skzD7GxYc3dVGm0G4xbw0ZnFicUd83Hx5FcPRn6WyZnnr/RdPFlvLg5GrJcF+mr5VhlOjUSs9IP0h7QsvSd9KP3Gvc19yn3Nfc59wV0CkTvLneO+4S5wH3NfxvZq8xpa33sWeRi3Z+mWa6xKISNsFR4WcsI24VFhMvInDAhjQlHYgZat6/sWny+ePR0OYx/mp/tcvi5WAYn7sQL0Tf5VVVTpcJQpHVZvTTi+QROMJENkjJQ2VPe4V/OhIpVP5VJpEFM7UxOpsdRBD4ezpnagbQL7/B3VqW6yUurSY959AlnTOm7rDc0Vd0vSk2IarzYqlprq6IioGIbITI5oU4fabVobBe/e9I/0mzK7DxNbLkec+wzAvj/x7Psu4o60AJYcgIHHI24Yz8oH3gU484TastvBHZFIfAvg1Pfs9r/6Mnh+/dTp3MRzrOctgLU3O52/3+901j5A/6sAZ41/AaCffFUDXAvvAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAABEZVhJZk1NACoAAAAIAAIBEgADAAAAAQABAACHaQAEAAAAAQAAACYAAAAAAAKgAgAEAAAAAQAAABCgAwAEAAAAAQAAABAAAAAA/iXkXAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAGZJREFUOBFj/HdD5j8DBYCJAr1grSzzmDRINiNFbQ8jTBPFLoAZNHA04/O8g2THguQke0aKw4ClX5uw97vS7eGhjq6aYhegG0h/PuOfohCyYoGlbw04XCgOA8bwI7PIcgEssCh2AQDqYhG4FWqALwAAAABJRU5ErkJggg==)](https://www.drivendata.org/competitions/258/competition-snomed-ct/)

Welcome to the data and runtime repository the [Snomed CT Entity Linking Challenge](https://www.drivendata.org/competitions/258/competition-snomed-ct/page/816/) on DrivenData! This repository contains a few things:

1. **Submission template** ([`examples/template/`](./examples/template/main.py)) — a template with the function signatures that you should implement in your submission.
1. **Example submission** ([`examples/submission/`](./examples/submission/main.py/)) — a submission with a simple demonstration solution. It will run successfully in the code execution runtime and outputs a valid submission.
1. **Runtime environment specification** ([`runtime/`](./runtime/)) — the definition of the environment where your code will run.

You can use this repository to:

💡 **Get started**: The example submission provides a demonstration solution that loads notes and uses them to generate valid span classification labels. Since it labels all of the text in the provided notes as `4596009 |Laryngeal structure (body structure)|`, it won't win you the competition, but you can use it as a guide for bringing in your own work and generating a real submission.

🔧 **Test your submission**: Test your submission using a locally running version of the competition runtime to discover errors before submitting to the competition website.

📦 **Request new packages in the official runtime**: Since your submission will not have general access to the internet, all dependencies must be pre-installed. If you want to use a package that is not in the runtime environment, make a pull request to this repository. Make sure to test out adding the new package to both official environments, CPU and GPU.

Changes to the repository are documented in [CHANGELOG.md](./CHANGELOG.md).

---

#### [1. Quickstart](#quickstart)

- [Prerequisites](#prerequisites)
- [Setting up the data directory](#setting-up-the-data-directory)
- [Running `make` commands](#running-make-commands)
- [Evaluating your annotations](#evaluating-your-annotations)

#### [2. Testing a submission locally](#testing-a-submission-locally)
- [Code submission format](#code-submission-format)
- [Running your submission locally](#running-your-submission-locally)
- [Smoke tests](#smoke-tests)
- [Runtime network access](#runtime-network-access)

#### [3. Updating runtime packages](#updating-runtime-packages)

#### [4. Makefile commands](#makefile-commands)

---

## Quickstart

This quickstart guide will show you how to get the provided example solution running end-to-end on data and annotations from the training set. Once you get there, it's off to the races!

### Prerequisites

When you make a submission on the DrivenData competition site, we run your submission inside a Docker container, a virtual operating system that allows for a consistent software environment across machines. **The best way to make sure your submission to the site will run is to first run it successfully in the container on your local machine**. For that, you'll need:

- A clone of this repository
- [Docker](https://docs.docker.com/get-docker/)
- At least 5 GB of free space for the CPU version of the Docker image or at least 13 GB of free space for the GPU version
- [GNU make](https://www.gnu.org/software/make/) (optional, but useful for running the commands in the Makefile)

Additional requirements to run with GPU:

- [NVIDIA drivers](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#package-manager-installation) with CUDA 11
- [NVIDIA container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)


### Setting up the data directory

In the official code execution platform, `code_execution/data` will contain data provided for the test set of clinical notes from MIMIC-IV-Note. The data format is a csv file (`test_notes.csv`) with two columns: "note_id", which contains the ID of the note, and "text", which contains the text of the note. Your code should read this file to obtain the text of each note and run model inference to generate non-overlapping annotated spans.

For local execution, you should simply copy over the set of train notes that you [accessed](https://www.drivendata.org/competitions/258/competition-snomed-ct/page/821/) from the challenge PhysioNet page into the `data/` directory and name them `test_notes.csv`. 

### Running `make` commands

To test out the full execution pipeline, make sure Docker is running and then run the following commands in the terminal:

1. **`make pull`** pulls the latest official Docker image from the container registry ([Azure](https://azure.microsoft.com/en-us/services/container-registry/)). You'll need an internet connection for this.
1. **`make pack-example`** packages a code submission with the `main.py` contained in `examples/submission/` that labels all text in the notes as "Larynx" and saves it as `submission/submission.zip`. 
1. **`make test-submission`** will do a test run of your submission, simulating what happens during actual code execution. This command runs the Docker container with the requisite host directories mounted, and executes `main.py` to produce a `submission.csv` file containing your predicted annotations.

```bash
make pull
make pack-example
make test-submission
```

🎉 **Congratulations!** You've just completed your first test run for the SNOMED CT Entity Linking Challenge. If everything worked as expected, you should see a new file `submission/submission.csv` has been generated.

If you were ready to make a real submission to the competition, you would upload the `submission.zip` file from step 2 above to the competition [Submissions page](https://www.drivendata.org/competitions/258/competition-snomed-ct/submissions/).

### Evaluating your annotations

We also provide a script for you to evaluate your generated annotations. This script takes paths to the predicted annotations file and the corresponding ground truth annotations file and evaluates the [macro-averaged character-level IoU metric](https://www.drivendata.org/competitions/258/competition-snomed-ct/page/817/#performance-metric).

```
python scripts/scoring.py submission/submission.csv data/training_annotations.csv
#> macro-averaged character IoU metric: 0.0000
```

It's probably not going to win the competition, but at least it's only up from here!


## Testing your submission locally

As you develop your own submission, you'll need to know a little bit more about how your submission will be unpacked for running inference. This section contains more complete documentation for developing and testing your own submission.

### Code submission format

Your final submission should be a zip archive named with the extension `.zip` (for example, `submission.zip`). The root level of the `submission.zip` file must contain a `main.py` which generates a file called `submission.csv` that contains your predicted annotations for the notes. Your `submission.csv` file should have the same structure as the submission format.

A template for `main.py` is included at [`examples/template/main.py`](./examples/template/main.py). For more detail, see the "what to submit" section of the [code submission page](https://www.drivendata.org/competitions/258/competition-snomed-ct/page/818/).

### Running your submission locally

This section provides instructions on how to run the your submission in the code execution container from your local machine. To simplify the steps, key processes have been defined in the `Makefile`. Commands from the `Makefile` are then run with `make {command_name}`. The basic steps are:

```sh
make pull
make pack-submission
make test-submission
```

Run `make help` for more information about the available commands as well as information on the official and built images that are available locally.

Here's the process in a bit more detail:

1. First, make sure you have set up the [prerequisites](#prerequisites).
1. Download the official competition Docker image:

    ```sh
    make pull
    ```

> [!NOTE]
> If you have built a local version of the runtime image with `make build`, that image will take precedence over the pulled image when using any make commands that run a container. You can explicitly use the pulled image by setting the `SUBMISSION_IMAGE` shell/environment variable to the pulled image or by deleting all locally built images.

1. Save all of your submission files, including the required `main.py` script, in the `submission_src` folder of the runtime repository. Make sure any needed model weights and other assets are saved in `submission_src` as well.

1. Create a `submission/submission.zip` file containing your code and model assets:

    ```sh
    make pack-submission
    #> mkdir -p submission/
    #> cd submission_src; zip -r ../submission/submission.zip ./*
    #>   adding: main.py (deflated 73%)
    ```

1. Launch an instance of the competition Docker image, and run the same inference process that will take place in the official runtime:

    ```sh
    make test-submission
    ```

This runs the container [entrypoint](./runtime/entrypoint.sh) script. First, it unzips `submission/submission.zip` into `/code_execution/src/` in the container. Then, it runs your submitted `main.py`. In the local testing setting, the final submission is saved out to `submission/submission.csv` on your local machine.

> [!NOTE]
> Remember that `code_execution/data` is just a mounted version of what you have saved locally in `data` so you will just be using the training files for local testing. In the official code execution platform, `code_execution/data` will contain the actual test data.

When you run `make test-submission` the logs will be printed to the terminal and written out to `submission/log.txt`. If you run into errors, use the `log.txt` to determine what changes you need to make for your code to execute successfully.

### Logging and smoke tests

In order to prevent leakage of the IDs of notes in the test set, **all logging is prohibited when running inference on the test set notes**. When submitting on the platform, you will have the ability to submit "smoke tests". Smoke tests run with logging enabled on a reduced version of the training set notes in order to run more quickly. They will not be considered for prize evaluation and are intended to let you test your code for correctness. In this competition, smoke tests will be the only place you can view logs or output from your code and to debug. **You should test your code locally as thorougly as possible before submitting your code for smoke tests or for full evaluation.**

The set of notes in the smoke test environment is a subset of the training set notes. We've made it easy to replicate the smoke test note environment locally - all you have to do is:

1. Copy the set of training notes into `data/train_notes.csv`
1. Copy the set of training annotations into `data/train_annotations.csv`
1. Run `make smoke-test-data`

You'll now have the smoke test notes in `data/test_notes.csv` and the corresponding annotations in `data/smoke_test_annotations.csv`. You can run your submission and then score your generated annotations by running

```sh
python scripts/scoring.py submission/submission.csv data/smoke_test_annotations.csv
```

If you've followed the above instructions, this score should match the one you receive from the smoke test environment on the platform.

## Updating runtime packages

If you want to use a package that is not in the environment, you are welcome to make a pull request to this repository. If you're new to the GitHub contribution workflow, check out [this guide by GitHub](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

The runtime manages dependencies using [conda](https://docs.conda.io/en/latest/) environments and [conda-lock](https://github.com/conda/conda-lock). [Here is a good general guide](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533) to conda environments. The official runtime uses **Python 3.10.13** environments.

To submit a pull request for a new package:

1. Fork this repository.

2. Install conda-lock. See [here](https://github.com/conda/conda-lock#installation) for installation options.

3. Edit the [conda](https://docs.conda.io/en/latest/) environment YAML files, `runtime/environment-cpu.yml` and `runtime/environment-gpu.yml`. There are two ways to add a requirement:

    - Conda package manager **(preferred)**: Add an entry to the `dependencies` section. This installs from the [conda-forge](https://anaconda.org/conda-forge/) channel using `conda install`. Conda performs robust dependency resolution with other packages in the `dependencies` section, so we can avoid package version conflicts.
    - Pip package manager: Add an entry to the `pip` section. This installs from PyPI using `pip`, and is an option for packages that are not available in a conda channel.

4. Run `make update-lockfiles`. This will read `environment-cpu.yml` and `environment-gpu.yml`, resolve exact package versions, and save the pinned environments to `conda-lock-cpu.yml` and `conda-lock-gpu.yml`.

5. Locally test that the Docker image builds successfully for CPU and GPU images:

    ```sh
    CPU_OR_GPU=cpu make build
    CPU_OR_GPU=gpu make build
    ```

6. Commit the changes to your forked repository. Ensure that your branch includes updated versions of _all_ of the following:

    - `runtime/conda-lock-cpu.yml`
    - `runtime/conda-lock-gpu.yml`
    - `runtime/environment-cpu.yml`
    - `runtime/environment-gpu.yml`

7. Open a pull request from your branch to the `main` branch of this repository. Navigate to the [Pull requests](https://github.com/drivendataorg/water-supply-forecast-rodeo-runtime/pulls) tab in this repository, and click the "New pull request" button. For more detailed instructions, check out [GitHub's help page](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork).

8. Once you open the pull request, we will use Github Actions to build the Docker images with your changes and run the tests in `runtime/tests`. For security reasons, administrators may need to approve the workflow run before it happens. Once it starts, the process can take up to 30 minutes, and may take longer if your build is queued behind others. You will see a section on the pull request page that shows the status of the tests and links to the logs.

9. You may be asked to submit revisions to your pull request if the tests fail or if a DrivenData staff member has feedback. Pull requests won't be merged until all tests pass and the team has reviewed and approved the changes.

## Make commands

A Makefile with several helpful shell recipes is included in the repository. The runtime documentation above uses it extensively. Running `make` by itself in your shell will list relevant Docker images and provide you the following list of available commands:

```
Available commands:

build               Builds the container locally
clean               Delete temporary Python cache and bytecode files
interact-container  Open an interactive bash shell within the running container (with network access)
pack-example        Creates a submission/submission.zip file from the source code in examples_src
pack-submission     Creates a submission/submission.zip file from the source code in submission_src
pull                Pulls the official container from Azure Container Registry
test-container      Ensures that your locally built image can import all the Python packages successfully when it runs
test-submission     Runs container using code from `submission/submission.zip` and data from WSFR_DATA_ROOT (default `data/`)
update-lockfiles    Updates runtime environment lockfiles
```
