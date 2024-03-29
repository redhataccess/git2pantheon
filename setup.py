from setuptools import setup, find_packages
entry_points = {
    'console_scripts': [
        'git2pantheon = git2pantheon.wsgi:main'
    ]
}
package_data = ['*.yaml']
setup(
    name='git2pantheon',
    version='0.2',
    packages=find_packages(),
    url='',
    license='',
    author='Red Hat, Inc.',
    author_email='',
    description='REST service that provides API to upload modular documentation to Pantheon2',
    install_requires=[
        'pytz>=2020.4',
        'pyudev>=0.22.0',
        'pyxdg>=0.26',
        'PyYAML>=5.3.1',
        'redis>=3.5.3',
        'requests-file>=1.4.3',
        'requests-ftp>=0.3.1',
        'simpleline>=1.6',
        'six>=1.14.0',
        'tinycss2>=1.0.2',
        'Flask>=2.0.3',
        'urllib3>=1.25.7',
        'webencodings>=0.5.1',
        'xcffib>=0.9.0',
        'gitpython>=3.1.30',
        'Flask-Cors>=3.0.10',
        'flasgger>=0.9.5',
        'Flask-Executor>=1.0.0',
        'giturlparse>=0.10.0',
        'marshmallow>=3.14.1',
        'gunicorn>=20.1.0',
        'edgegrid-python>=1.3.1',
        'decorest>=0.1.0',
        'requests>=2.27.1',
        'requests-toolbelt>=0.10.1',
        'contextvars>=2.3',
        'typing-extensions>=4.4.0',
        'pantheon-uploader@ git+https://github.com/redhataccess/pantheon-uploader.git@master#egg=pantheon-uploader-0.2'
    ],
    dependency_links=['https://github.com/redhataccess/pantheon-uploader/tarball/master#egg=pantheon-uploader'],
    entry_points=entry_points,
    package_data={'': package_data}
)
