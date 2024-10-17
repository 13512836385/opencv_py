from cx_Freeze import setup, Executable

setup(
    name='opencv-py',
    version='1.0',
    executables=[Executable('test.py')]
)