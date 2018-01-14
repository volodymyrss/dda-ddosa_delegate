import os
import ddosa
import dataanalysis.caches.queue as queue

cache=queue.QueueCache(os.environ['HOME']+"/ddosa-queue")

ddosa.CacheStack[-1].parent=cache
ddosa.CacheStack.append(cache)

#ddosa.BinEventsImage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
#ddosa.ibis_gti.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

ddosa.ii_skyimage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
ddosa.ghost_bustersImage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
ddosa.ibis_gti.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
ddosa.CatExtract.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

