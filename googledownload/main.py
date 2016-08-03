#!/usr/bin/env python3

# TODO: change precision on downloader
# TODO: ensure correct size

import sys, getopt
import math

import requests
from bs4 import BeautifulSoup

CHUNK_SIZE = 1024 # how many bytes to write at a time

def get_google_download(url_public, save_file_name):
    """ Downloads a Google Drive file from a public link after confirmation
        screen """

    # get the original public URL
    request_public = requests.get(url_public)
    cookies_public_request = request_public.cookies

    # parse the response and get new download link with confirmation
    parsed_request = BeautifulSoup(request_public.text, 'html.parser')
    download_link = parsed_request.find('a', id="uc-download-link")
    if not download_link:
        pass # TODO: error out
    download_url = download_link.get('href')
    if not download_url:
        pass # TODO: error out

    # request the direct download url using cookies from first request
    # include stream=True to stream the download (for large files)
    direct_download_url = "https://docs.google.com" + download_url
    request_download = requests.get(direct_download_url,
                                    cookies=cookies_public_request,
                                    stream=True)
    
    # download file in chunks to specified file name
    size = 0
    with open(save_file_name,'wb') as f:
        for chunk in request_download.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
                size += CHUNK_SIZE
                print("file written: {:>10}".format(convertSize(size/CHUNK_SIZE)), end="\r")
    
    request_public.close()
    request_download.close()

def convertSize(size):
    if (size == 0):
        return '0B'
    size_name = ("KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size,1024)))
    p = math.pow(1024,i)
    s = round(size/p,2)
    return '{size:.1f} {size_name}'.format(size=s, size_name=size_name[i])

HELP_USE_LINE = 'main.py -i <inputurl> -o <outputfile>' 

def main(argv):
    """ Checks for arguments """
    # adapted from:
    # http://www.tutorialspoint.com/python/python_command_line_arguments.htm

    inputurl = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print(HELP_USE_LINE)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(HELP_USE_LINE)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputurl = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputurl and outputfile:
        get_google_download(inputurl,outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
    #url = "https://docs.google.com/uc?id=0B8S3kx1EXmCXUG42Zk1qdV9HajQ&export=download"
    #file = "1.mov"
    #get_google_download(url,file)

