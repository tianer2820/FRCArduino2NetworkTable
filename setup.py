from setuptools import setup

setup(
    name='FRCArduino2NetworkTable',
    version='0.1',
    modules=[arduino2nt],
    url='https://github.com/tianer2820/FRCArduino2NetworkTable',
    license='MIT',
    author='Toby',
    author_email='tianer2820@163.com',
    description='Access your arudino through network table!',
    requires=['wxPython', 'pyserial']
)
