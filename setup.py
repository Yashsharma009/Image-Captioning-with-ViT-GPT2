from setuptools import setup

setup(
    name="caption-app",
    version="0.1",
    packages=[""],
    install_requires=[
        "streamlit==1.19.0",
        "torch==1.9.0",
        "torchvision==0.10.0",
        "transformers==4.11.3",
        "pillow==8.4.0",
        "vit-pytorch==0.18.0"
    ],
    entry_points={
        "console_scripts": [
            "caption-app = app:main"
        ]
    },
)
