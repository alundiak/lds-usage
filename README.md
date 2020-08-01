lds_usage
===

# Setup on MacOS

By default MacOS contains Python 2.7, so it's enough to try next command:

```
pip install lds-org
python -m lds_org
```

But if you need/want Python 3, then

```
brew install python3
```

And then:
```
pip3 install lds-org
python3 -m lds_org
```

In case if it was wrongly installed, or u have some errors with `$PATH`, try these:
```
brew link python3
brew link python3 --overwrite --dry-run python3
brew link python3 --overwrite python3
```



## Resources:

- https://github.com/jidn/LDS-org
- https://pypi.python.org/pypi/LDS-org