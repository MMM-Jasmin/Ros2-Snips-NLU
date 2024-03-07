from setuptools import setup

package_name = 'snipsnlu_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jonas Bröckling',
    maintainer_email='jbroeckling@techfak.uni-bielefeld.de',
    description='Snipüs NLU Node',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'nlu = snipsnlu_node.subscriber_member_function:main',
        ],
    },
)
