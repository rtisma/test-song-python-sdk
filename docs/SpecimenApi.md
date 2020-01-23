# overture_song.SpecimenApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_specimens**](SpecimenApi.md#delete_specimens) | **DELETE** /studies/{studyId}/specimens/{ids} | DeleteSpecimens
[**get_specimen**](SpecimenApi.md#get_specimen) | **GET** /studies/{studyId}/specimens/{id} | GetSpecimen


# **delete_specimens**
> str delete_specimens(ids, study_id)

DeleteSpecimens

Deletes specimen data and all dependent samples for specimenIds

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
api_instance = overture_song.SpecimenApi(overture_song.ApiClient(configuration))
ids = 'ids_example' # str | Comma separated list of specimenIds
study_id = 'study_id_example' # str | studyId

try:
    # DeleteSpecimens
    api_response = api_instance.delete_specimens(ids, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->delete_specimens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Comma separated list of specimenIds | 
 **study_id** | **str**| studyId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specimen**
> Specimen get_specimen(id, study_id)

GetSpecimen

Retrieves specimen data for a specimenId

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.SpecimenApi()
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # GetSpecimen
    api_response = api_instance.get_specimen(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_specimen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

[**Specimen**](Specimen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

