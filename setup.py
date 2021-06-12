from setuptools import setup

APP = ['tip_calculator.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'tip.jpg',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['certifi'],
}

setup(
    app=APP,
    name='Tip Calculator',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)