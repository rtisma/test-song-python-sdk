# overture_song.DonorApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_donors**](DonorApi.md#delete_donors) | **DELETE** /studies/{studyId}/donors/{ids} | DeleteDonors
[**get_donor**](DonorApi.md#get_donor) | **GET** /studies/{studyId}/donors/{id} | GetDonor


# **delete_donors**
> str delete_donors(ids, study_id)

DeleteDonors

Deletes donor data and all dependent specimens and samples for donorIds

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
api_instance = overture_song.DonorApi(overture_song.ApiClient(configuration))
ids = 'ids_example' # str | Comma separated list of donorIds
study_id = 'study_id_example' # str | studyId

try:
    # DeleteDonors
    api_response = api_instance.delete_donors(ids, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DonorApi->delete_donors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Comma separated list of donorIds | 
 **study_id** | **str**| studyId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_donor**
> Donor get_donor(id, study_id)

GetDonor

Retrieves donor data for a donorId

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.DonorApi()
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # GetDonor
    api_response = api_instance.get_donor(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DonorApi->get_donor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

[**Donor**](Donor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

