import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="tabcbm",
    version="0.1.0",
    author="Mateo Espinosa Zarlenga, Zohreh Shams, Michael Edward Nelson, Been Kim, Mateja Jamnik",
    author_email="me466@cam.ac.uk",
    description="Tabular Concept Bottleneck Models",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/mateoespinosa/tabcbm",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    python_requires='>=3.10',
    install_requires=[
        "anndata>=0.7.8",
        "cachetools>=4.1.1",
        "captum>=0.4.1",
        "cmake>=3.26.3",
        "codemod>=1.0.0",
        "colorama>=0.4.3",
        "commonmark>=0.9.1",
        "configobj>=5.0.6",
        "configparser>=5.2.0",
        "dill>=0.3.4",
        "h5py>=3.6.0",
        "joblib>=1.1.0",
        "keras>=2.7.0",
        "Keras-Preprocessing>=1.1.2",
        "numba>=0.54.1",
        "numexpr>=2.8.1",
        "numpy>=1.20.0",
        "pandas>=1.3.4",
        "pathtools>=0.1.2",
        "Pillow>=9.0.0",
        "pip>=23.1.2",
        "prettytable>=3.0.0",
        "promise>=2.3",
        "pyaml>=21.10.1",
        "pytorch-lightning>=1.5.8",
        "pytorch-tabnet>=4.0",
        "PyYAML>=6.0",
        "scanpy>=1.8.2",
        "scikit-image>=0.19.3",
        "scikit-learn>=1.0.2",
        "scikit-learn-extra>=0.2.0",
        "scipy>=1.10.1",
        "setuptools>=44.0.0",
        "setuptools-scm>=6.3.2",
        "smmap>=5.0.0",
        "sympy>=1.9",
        "tab-transformer-pytorch>=0.2.0",
        "tabnet>=0.1.6",
        "tabulate>=0.9.0",
        "tensorflow>=2.7.0",
        "tensorflow-addons>=0.17.1",
        "tensorflow-datasets>=4.4.0",
        "tensorflow-estimator>=2.7.0",
        "tensorflow-gan>=2.1.0",
        "tensorflow-hub>=0.12.0",
        "tensorflow-io-gcs-filesystem>=0.22.0",
        "tensorflow-metadata>=1.4.0",
        "tensorflow-probability>=0.15.0",
        "torch-vision>=0.1.6.dev0",
        "torchmetrics>=0.11.4",
        "torchvision>=0.12.0",
        "torchviz>=0.0.2",
        "tqdm>=4.62.3",
        "xgboost>=1.6.1",
    ],
)


