from setuptools import setup, find_packages

setup(
    name='ClustIPy',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/shuichiro-makigaki/ClustIPy',
    license='MIT',
    author='Shuichiro MAKIGAKI',
    author_email='shuichiro.makigaki@gmail.com',
    description='Clustering IPs',
    entry_points='''
        [console_scripts]
        clustipy=clustipy.cmd.clustipy:main
    ''',
)
