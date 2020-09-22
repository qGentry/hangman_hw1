from setuptools import setup, find_packages


def main():

    console_scripts = [
        "run-hangman = bin.run_hangman:main",
    ]

    setup(
        name="games",
        version="1.1",
        author="Fisin Philipp",
        package_dir={"": "src"},
        packages=find_packages("src"),
        description="Simple console games",
        entry_points={
            "console_scripts": console_scripts
        }
    )


if __name__ == '__main__':
    main()
