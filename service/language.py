

def normalize(lng):
    """normalizze language string
    pl => pl_PL
    en-us => en_US
    en_GB => en_GB
    """
    lng = lng.replace("-", "_")
    if "_" in lng:
        pre, post = lng.split("_")
        lng = pre.lower() + "_" + post.upper()
    else:
        lng = lng.lower() + "_" + lng.upper()

    return lng
