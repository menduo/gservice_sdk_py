#coding:utf-8

'''
module::device
~~~~~~~~~~~~~~
Device operations
'''


from requests import Request

API_URL = "http://api.gizwits.com/app"


def retrieve_device_histroy_data(did, start_ts=1349032093, end_ts=1349032093, entity=1, attr="temp", limit=20, skip=0):
    request_body = {'start_ts': start_ts,
                    'end_ts': end_ts,
                    'entity': entity,
                    'attr': attr,
                    'limit': limit,
                    'skip': skip
                    }
    url = render_url('/devdata/' + str(did))
    return Request("GET", url, data=request_body)

def retrieve_product_histroy_data(product_key, did=None, start_ts=1349032093, end_ts=1349032093, entity=1, attr="temp", limit=20, skip=0):
    request_body = {'did':did,
                    'start_ts': start_ts,
                    'end_ts': end_ts,
                    'entity': entity,
                    'attr': attr,
                    'limit': limit,
                    'skip': skip
                    }
    url = render_url('/devdata/' + str(product_key))
    return Request("GET", url, data=request_body)

def get_bound_devices(limit=20, skip=0):
    request_body = {
        'limit': limit,
        'skip': skip
        }
    return Request("GET", render_url('/bindings'), data=request_body)

def bind_devices(devices):
    '''
    :param devices: struct = > [('did', 'passcode'), ...]
    :returns: Response
    '''
    data_devices = []
    for did, passcode in devices:
        device = {'did': None, 'passcode': None}
        device['did'] = did
        device['passcode'] = passcode
        data_devices.append(device)
    request_body = {'devices':data_devices}
    return Request("POST", render_url('/bindings'), data=request_body)

def unbind_devices(devices):
    data_devices = []
    for did, passcode in devices:
        device = {'did': None, 'passcode': None}
        device['did'] = did
        device['passcode'] = passcode
        data_devices.append(device)
    request_body = {'devices':data_devices}
    return Request("DELETE", render_url('/bindings'), data=request_body)

#===device detail
def device_detail(did):
    url = render_url('/devices/' + str(did))
    return Request("GET", url)

def query_device(product_key, mac):
    request_body = {
        'product_key': product_key,
        'mac':mac
        }
    return Request("GET", render_url('/bindings'), data=request_body)

def remote_control_device(did, raw):
    '''
    :param did: did
    :type did: String

    :param raw: struct => [<byte>, <byte>, ...]
    :type raw: list
    '''
    request_body = {
        'raw': raw
        }
    url = render_url('/control/' + str(did))
    return Request("POST", url)
