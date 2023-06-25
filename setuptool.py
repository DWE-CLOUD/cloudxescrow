from setuptools import setup

setup(
    name='python-telegram-bot',
    version='13.7',
    description='Python Telegram Bot Library',
    long_description='Library for creating Telegram bots using Python',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/python-telegram-bot/python-telegram-bot',
    packages=['telegram'],
    install_requires=[
        'python-telegram-bot==13.7',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)