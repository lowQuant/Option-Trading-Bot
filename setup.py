from setuptools import setup, find_packages

setup(
    name='option-trading-bot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'pandas_market_calendars',
        'pytz',
        'tabulate',
        'yfinance',
        'numpy',
        'python-dateutil'
    ],
)
