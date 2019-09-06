from setuptools import find_packages, setup

setup(
    name='gm_analytics',
    version='0.1.0',
    maintainer='Daniel Barragan',
    maintainer_email='daniel.barragan@correo.icesi.edu.co',
    description='Github manager analytics service',
    url='',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask==1.0.2',
        'connexion==1.5.2',
        'PyGithub==1.35',
    ],
)
