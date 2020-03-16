from setuptools import setup

setup(
    name='KSP-mod',
    license="MIT",
    author="Noah Young",
    author_email="noahpyoung@gmail.com",
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'ksp-mod=kspmod.kspmod:main'
        ]
    }
)
