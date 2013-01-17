# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name='s3mysqlbkp',
    version='1.0',
    description='MySQL backups to Amazon S3',
    author='Daniel Yavorovich',
    author_email='yavorovich@denni.org',
    url='https://github.com/daniel-yavorovich/s3mysqlbkp',
    license='GPL',
    platforms = ('Any',),
    packages=['s3mysqlbkp'],
    package_dir={'s3mysqlbkp': 'src/s3mysqlbkp'},
    scripts = ['bin/s3mysqlbkp_run.py'],
    data_files=[
        ('../etc', ['cfg/s3mysqlbkp.conf']),
    ],
    requires=['boto (>=2.7.0)'],
)
