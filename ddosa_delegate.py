import os


if os.environ.get("DDA_DISABLE_ASYNC", "no") == "yes": 
    print("DDA_DISABLE_ASYNC disables ddosa_delegate module")
else:
    import ddosa
    import dataanalysis.caches.queue as queue
    import dataanalysis.core as da

    cache=queue.QueueCache(
            os.environ.get('ODAHUB',
                           os.environ.get('DDA_QUEUE',
                                    "https://crux.staging-1-3.odahub.io@default",
                               ))
            )

    cache.delegate_by_default=True

    ddosa.CacheStack[-1].parent=cache
    ddosa.CacheStack.append(cache)

    print("CacheStack:", ddosa.CacheStack)

    #class ii_skyimage(ddosa.ii_skyimage):
    #    read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

    ddosa.ISGRIImagePack.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    #ddosa.ii_spectra_extract.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    ddosa.ii_lc_extract.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

    #ddosa.ghost_bustersImage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    #ddosa.ibis_gti.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

    #ddosa.BinEventsSpectra.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

    ddosa.mosaic_ii_skyimage.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

    try:
        da.byname('ISGRISpectrumPack').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    except Exception:
        pass

    try:
        da.byname('ii_light').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    except Exception:
        pass

    try:
        da.byname('jemx_image').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
        da.byname('jemx_spe').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
        da.byname('jemx_lcr').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    except Exception:
        pass

    #try:
    #    da.byname('RebinResponse').__class__.read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)
    #except Exception:
    #    pass

