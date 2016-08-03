# googledownload
Download Google Documents public links without a browser 

Background
----------
When downloading large files from Google Docs, Google will often inform you that the file is too large to be scanned for viruses. 
Google then allows you to download the file, but the link is dependent on a cookie and confirmation code.
The cookie and confirmation code must be used to download the file.

Use
---
Use this tool when you want to download the file through a terminal (i.e. without a browser).

```
python setup.py install
```

```python
import googledownload as gd
gd.get_google_download(<String: url for downloading the google file>, <String: output file>)
```

The tool will present a download progress, showing the size of download so far. There is no feature to show % completion.

Feedback
--------

Please feel free to leave a comment, issue, or request.
