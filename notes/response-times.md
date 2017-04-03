### Response time using urllib, grequests, aiohttp, and asyncio ###

###### For fetching 10 tiles, it took the following mentioned time (in seconds):

* Elapsed time URLLib (without concurrency): 3.5430831909179688
* Elapsed time URLLib (with concurrency): 0.388397216796875
* Elapsed time URLLib (with aiohttp): 0.3900480270385742
* Elapsed time GRequests: 1.6238431930541992

###### For fetching 100 tiles, it took:

* Elapsed time URLLib (without concurrency): 37.7027428150177
* Elapsed time URLLib (with concurrency): 5.575664043426514
* Elapsed time URLLib (with aiohttp): 2.4697625637054443
* Elapsed time GRequests: 4.273705244064331