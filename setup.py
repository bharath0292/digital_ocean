from setuptools import setup,find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements_list(requirement_file_name = REQUIREMENT_FILE_NAME) -> list:
    
    requirement_list = None
    try:
        with open(requirement_file_name) as requirement_file:
            requirement_list = [requirement.replace("\n","") for requirement in requirement_file.readlines()]
            requirement_list.remove(REMOVE_PACKAGE)
    except Exception as e:
        raise e

    return requirement_list

setup(
    name = "lstm-text-classiication",
    version = "0.0.1",
    description = "LSTM bbased text classification project and Deployed into DigitalOcean",
    author = "Bharath",
    packages = find_packages(),
    install_requires = get_requirements_list()
)
