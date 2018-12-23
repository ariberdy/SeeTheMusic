""" Download Major Tom
    Sample Block Comment

    Multi-block block comment."""

import urllib


def download_bowie_wav():
    """All Functions have comments like this"""
    urllib.request.urlretrieve("http://www.wavsource.com/snds_2018-06-03_5106726768923853/music/space_oddity.wav", "bowie.wav")

""" The function must be called for this to work.
    Go to Python's command prompt.
    Import this module (>>> import downlaod_bowie_wav)
    Run the function using dot notation (>>> download_bowie_wav.download_bowie_wav())
"""
