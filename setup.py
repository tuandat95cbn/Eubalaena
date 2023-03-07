from setuptools import find_packages,find_namespace_packages, setup
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='euba',
    packages=find_namespace_packages(where ='src'),
    package_dir={"": "src"},
    version='0.1.2',
    description='a libary suport building ocean sound velocity dataset',
    author='tuandat95cbn@gmail.com',
    license='MIT',
    include_package_data=True,
    install_requires=required,
)
