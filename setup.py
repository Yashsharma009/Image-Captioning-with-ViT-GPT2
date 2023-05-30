from setuptools import setup, find_packages

setup(
    name='image_captioning_app',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch==1.9.0',
        'transformers==4.10.2',
        'streamlit==1.2.0',
        'Pillow==8.3.2',
    ],
    entry_points={
        'console_scripts': [
            'image_captioning_app = app:main',
        ],
    },
)
