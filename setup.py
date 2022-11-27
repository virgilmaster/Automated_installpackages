from setuptools import setup

setup(
    name="Automated_installpackages",
    version="1.0",
    author="Vergil",
    author_email="691167837@qq.com",
    description=("This is a automation project"),
    keywords="automation",
    url="https://github.com/virgilmaster/Automated_installpackages",
    packages=["Db","download","functions","log","queue","source"],

    install_requires=[
        'jmespath>=0.10.0 ',
        'setuptools>=61.2.0 ',
    ],
    
    zip_safe=False
)

