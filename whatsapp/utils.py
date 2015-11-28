import urllib3, certifi

def getMediaFromHttps(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request('GET',url)
    return r.data

