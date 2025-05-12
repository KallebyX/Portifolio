from setuptools import setup, find_packages

setup(
    name='portifolio-kalleby',
    version='1.0.0',
    description='Portfólio pessoal de Kalleby Evangelho Mota utilizando Flask.',
    author='Kalleby Evangelho Mota',
    author_email='kallebyevangelho03@gmail.com',
    url='https://github.com/KallebyX/Portifolio',
    packages=find_packages(where='backend'),
    package_dir={'': 'backend'},  # Diz que o código está em backend/
    include_package_data=True,
    install_requires=[
        'Flask>=2.0',
        'gunicorn',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
    ],
    python_requires='>=3.8',
)