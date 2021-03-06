import os
import ddosa
import dataanalysis.caches.queue as queue
import dataanalysis.core as da

cache=queue.QueueCache(os.environ['DDA_QUEUE'])
cache.delegate_by_default=True

ddosa.CacheStack[-1].parent=cache
ddosa.CacheStack.append(cache)

class ii_skyimage(ddosa.ii_skyimage):
    read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

ddosa.ghost_bustersImage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
ddosa.ibis_gti.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

ddosa.BinEventsSpectra.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
ddosa.ii_spectra_extract.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

ddosa.mosaic_ii_skyimage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

ddosa.ii_lc_extract.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

try:
    da.byname('ii_light').__class__.ii_light.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
except Exception:
    pass

try:
    da.byname('jemx_image').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    da.byname('jemx_spe').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    da.byname('jemx_lcr').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
except Exception:
    pass

