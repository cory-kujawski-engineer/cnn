from setuptools import setup, find_packages

setup(
    name='cnn_scraper',
    version='0.1.0',
    description='A web scraper for CNN articles',
    author='Cory Kujawski',
    author_email='cory@cyberhumint.com',
    url='https://github.com/cory-kujawski-engineer/cnn_scraper',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.12.3',
        'certifi==2024.8.30',
        'charset-normalizer==3.4.0',
        'html5lib==1.1',
        'idna==3.10',
        'lxml==5.3.0',
        'requests==2.32.3',
        'six==1.16.0',
        'soupsieve==2.6',
        'urllib3==2.2.3',
        'webencodings==0.5.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'cnn_scraper=cnn_scraper:main',  # Assuming you have a main function to run
        ],
    },
) 