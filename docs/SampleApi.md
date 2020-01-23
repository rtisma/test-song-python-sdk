# overture_song.SampleApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_samples**](SampleApi.md#delete_samples) | **DELETE** /studies/{studyId}/samples/{ids} | DeleteSamples
[**get_sample**](SampleApi.md#get_sample) | **GET** /studies/{studyId}/samples/{id} | GetSample


# **delete_samples**
> str delete_samples(ids, study_id)

DeleteSamples

Deletes sample data for sampleIds

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
api_instance = overture_song.SampleApi(overture_song.ApiClient(configuration))
ids = 'ids_example' # str | Comma separated list of sampleIds
study_id = 'study_id_example' # str | studyId

try:
    # DeleteSamples
    api_response = api_instance.delete_samples(ids, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->delete_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Comma separated list of sampleIds | 
 **study_id** | **str**| studyId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample**
> Sample get_sample(id, study_id)

GetSample

Retrieves sample data for a sampleId

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.SampleApi()
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # GetSample
    api_response = api_instance.get_sample(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SampleApi->get_sample: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

[**Sample**](Sample.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

