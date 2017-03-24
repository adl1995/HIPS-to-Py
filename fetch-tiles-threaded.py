# @Author: Adeel Ahmad
# @Date:   2017-03-23 22:48:42

import threading
import urllib.request
import grequests
import time
import asyncio
import aiohttp

urls = [
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
]

urls = [
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91422.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91423.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91424.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91425.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91426.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91427.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91428.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91429.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91430.jpg',
    'http://alasky.u-strasbg.fr/DSS/DSSColor/Norder7/Dir90000/Npix91431.jpg',
]

@asyncio.coroutine
def fetch_url_aiohttp(url,idx):
    response = yield from aiohttp.request('get', url)
    response.close()

start = time.time()

loop = asyncio.get_event_loop()
tasks = [asyncio.async(fetch_url_aiohttp(z, i)) for i, z in enumerate(urls)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print("Elapsed Time aiohttp (with asyncio): %s" % (time.time() - start))

def fetch_url_urllib(url):
    urlHandler = urllib.request.urlopen(url)

start = time.time()

for url in urls:
	urlHandler = urllib.request.urlopen(url)

print("Elapsed Time URLLib (without concurrency): %s" % (time.time() - start))


start = time.time()

threads = [threading.Thread(target=fetch_url_urllib, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed Time URLLib (with concurrency): %s" % (time.time() - start))

start = time.time()

rs = (grequests.get(u) for u in urls)
grequests.map(rs)

print("Elapsed Time GRequests: %s" % (time.time() - start))

