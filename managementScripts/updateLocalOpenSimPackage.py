import sys
import os
import httpx
import tarfile

class updateLocalOpenSimPackage(object):
    def __init__(self,url='',filename=''):
        try:
            if url == '':
                raise Exception("Give at least an url")
            if filename == '':
                filename = url[(url.rfind('/')+1):]
            r = httpx.get(url,timeout=120)
            with open('openSimPackage/' + filename,"b+w") as f:
                f.write(r.content)
            tar = tarfile.open('openSimPackage/' + filename)
            tar.extractall()
            tar.close()
            os.remove('./' + filename)
        except:
            raise