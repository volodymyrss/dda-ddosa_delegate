import os
import ddosa
import dataanalysis.caches.queue as queue

cache=queue.QueueCache(os.environ['HOME']+"/ddosa-queue")

ddosa.CacheStack[-1].parent=cache
ddosa.CacheStack.append(cache)

#ddosa.BinEventsImage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
#ddosa.ibis_gti.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

ddosa.ii_spectra_extract.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

