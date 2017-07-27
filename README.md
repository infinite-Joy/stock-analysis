# stock-analysis
This is a simple stock analysis software for Indian stocks inspired by guidelines from the guidelines of the father of security analysis and value investing, Benjamin Graham.

stock-analysis now is python3 and runs on python3.5

## to start working
First clone the repo
```git clone git@github.com:infinite-Joy/stock-analysis.git```

To install requirements:

fire up virtual env
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To run tests:
```
nosetests
```

To run this file simply type
```bash
python get_stock_data.py
```

This will simply give you a list of the company names that you should invest in the current month

I would recommend this to run once a month.

If you want to run it in a server and access this as a webpage you can look into my [basic barebones webproject](https://github.com/infinite-Joy/stock-analysis-webapp).

[A kivi project](https://github.com/infinite-Joy/stock-analysis-kivy) is also under development for this to run it in as a mobile app. Please check it out.

## Contributing

If you find problems with this software, [log them on GitHub](https://github.com/infinite-Joy/stock-analysis/issues). If you want to contribute, please fork the code and submit a pull request.

Before submitting a pull request, please make sure your forked branch is up to date with the original branch. To do this:

* set your upstream remote:

    $ git remote add upstream git@github.com:infinite-Joy/stock-analysis.git

* make sure you have the latest changes from upstream:

    $ git fetch upstream

* rebase your master branch to upstream before pushing to git and submitting a pull request:

    $ git rebase upstream/master


If you need a windows executable mail me at joydeepubuntu[at]gmail[dot]com
