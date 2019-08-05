from setuptools import setup

package_name = 'subscriber_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/subscriber.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Daniel Jeswin',
    author_email='danieljeswin@gmail.com',
    maintainer='Daniel Jeswin',
    maintainer_email='danieljeswin@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal subscribers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'subscriber = subscriber_pkg.my_subscriber:main',
        ],
    },
)