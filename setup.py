from setuptools import setup, find_packages

setup(
    name='kakaomail',
    version='0.1.1',
    description='send simple text using kakao mail',
    license='MIT',
    author='Kyunghonn',
    author_email='aloecandy@gmail.com',
    url='https://github.com/aloecandy/kakaomail',
    keywords=['kakao', 'mail','korean'],
    install_requires=[
        'email'
    ],
    packages=find_packages(exclude=['tests'])
)