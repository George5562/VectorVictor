from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vector_victor",
    version="0.1.0",
    author="George Stephens",
    description="Documentation vectorization system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vector_victor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Markup",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
    install_requires=[
        "openai>=1.0.0",
        "dspy-ai>=2.0.0",
        "numpy>=1.21.0",
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "selenium>=4.0.0",
        "webdriver_manager>=3.8.0",
        "tqdm>=4.65.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "vector-victor=vector_victor.cli:main",
        ],
    },
)
