# overture_song.SubmitApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit**](SubmitApi.md#submit) | **POST** /submit/{studyId} | Submit


# **submit**
> SubmitResponse submit(json_payload, study_id)

Submit

Synchronously submit a json payload

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = overture_song.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = overture_song.SubmitApi(overture_song.ApiClient(configuration))
json_payload = 'json_payload_example' # str | json_payload
study_id = 'study_id_example' # str | studyId

try:
    # Submit
    api_response = api_instance.submit(json_payload, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmitApi->submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_payload** | **str**| json_payload | 
 **study_id** | **str**| studyId | 

### Return type

[**SubmitResponse**](SubmitResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, application/json;charset=UTF-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

