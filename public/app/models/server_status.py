import requests
import certifi
import json

def status (url, ref):
    result = None

    try:
        path = certifi.where()
        endpoint = url + "/api/v1/status/peer/"

        # Get actual node information
        r = requests.get(endpoint, verify=path)
        result = json.loads(r.text)
        result['url'] = url
    except:
        return {
            'status' : 'offline : Endpoint unreachable',
            'consensus' : 'Unknown',
            'block_height' : 'Unknown',
            'total_tx' : 'Unknown',
            'state' : 'Unknown',
            'ref_block_height' : 'Unknown',
            'unconfirmed_tx' : 'Unknown',
            'url' : url,
        }
    
    try:
        path = certifi.where()
        # Get reference block height
        ref_endpoint = ref + "/api/v1/status/peer/"
        r = requests.get (ref_endpoint, verify=path)
        ref_result = json.loads (r.text)
        result["ref_block_height"] = ref_result["block_height"]
    except:
        result["ref_block_height"] = 'Unknown'

    # Get reference endpoint information
    return result
