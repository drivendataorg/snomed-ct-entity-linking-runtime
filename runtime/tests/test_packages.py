import importlib
import subprocess

import pytest

packages = [
    "faiss",
    "gensim",
    "keras",
    "numpy",
    "pandas",
    "scipy",
    "spacy",
    "sklearn",
    "tensorflow",
    "torch",
    "transformers",
]


def is_gpu_available():
    try:
        return subprocess.check_call(["nvidia-smi"]) == 0

    except FileNotFoundError:
        return False


GPU_AVAILABLE = is_gpu_available()


@pytest.mark.parametrize("package_name", packages, ids=packages)
def test_import(package_name):
    """Test that certain dependencies are importable."""
    importlib.import_module(package_name)


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_allocate_torch():
    import torch

    assert torch.cuda.is_available()

    torch.zeros(1).cuda()


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_allocate_tf():
    import tensorflow as tf

    assert tf.test.is_built_with_cuda()
    assert (devices := tf.config.list_logical_devices("GPU"))

    for device in devices:
        with tf.device(device.name):
            tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_allocate_cupy():
    import cupy as cp

    cp.array([1, 2, 3, 4, 5, 6])


def test_spacy():
    import spacy
    from spacy.tokens import DocBin

    if GPU_AVAILABLE:
        spacy.require_gpu()

    nlp = spacy.blank("en")
    training_data = [
        ("Tokyo Tower is 333m tall.", [(0, 11, "BUILDING")]),
    ]

    # the DocBin will store the example documents
    db = DocBin()
    for text, annotations in training_data:
        doc = nlp(text)
        ents = []
        for start, end, label in annotations:
            span = doc.char_span(start, end, label=label)
            ents.append(span)
        doc.ents = ents
        db.add(doc)


@pytest.mark.skipif(not GPU_AVAILABLE, reason="No GPU available")
def test_faiss_n_gpus():
    import faiss
    assert faiss.get_num_gpus() > 0

