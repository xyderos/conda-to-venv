# a simple script to migrate .yml environment packages
# from conda to python virtual environment

import ruamel.yaml

yaml = ruamel.yaml.YAML()

data = yaml.load(open('build.yml'))

requirements = []

for dependency in data['dependencies']:
    if isinstance(dependency, str):
        package, package_version, python_version = depedency.split('=')

        if python_version is '0':
            continue
        requirements.append(package + '==' + package_version)
    elif isinstance(dep, dict):
        for preq in dependency.get('pip', []):
            requirements.append(preq)

with open('build.txt', 'w') as fp:
    for requirement in requirements:
        print(requirement, file=fp)

print("build.txt has been generated, please run pip install -r build.txt to install the dependencies")
