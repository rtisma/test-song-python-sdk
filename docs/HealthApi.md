# overture_song.HealthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**is_alive**](HealthApi.md#is_alive) | **GET** /isAlive | IsAlive


# **is_alive**
> bool is_alive()

IsAlive

Checks if the server is running

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.HealthApi()

try:
    # IsAlive
    api_response = api_instance.is_alive()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->is_alive: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

