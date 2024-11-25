import os
from glob import glob
from setuptools import setup

package_name = 'limo_joy_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob(os.path.join('launch','*launch.[pxy][ymal]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='lengagne@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'limo_joy_control = limo_joy_control.joy_control:main',
            'joy_selector = limo_joy_control.joy_selector:main',
            'auto_control = limo_joy_control.auto_control:main',
        ],
    },
        
)
