# overture_song.FileApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_files**](FileApi.md#delete_files) | **DELETE** /studies/{studyId}/files/{ids} | DeleteFiles
[**get_file**](FileApi.md#get_file) | **GET** /studies/{studyId}/files/{id} | GetFile
[**update_file**](FileApi.md#update_file) | **PUT** /studies/{studyId}/files/{id} | UpdateFile


# **delete_files**
> str delete_files(ids, study_id)

DeleteFiles

Deletes file data for fileIds

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
api_instance = overture_song.FileApi(overture_song.ApiClient(configuration))
ids = 'ids_example' # str | Comma separated list of fileIds
study_id = 'study_id_example' # str | studyId

try:
    # DeleteFiles
    api_response = api_instance.delete_files(ids, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->delete_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Comma separated list of fileIds | 
 **study_id** | **str**| studyId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> FileEntity get_file(id, study_id)

GetFile

Retrieves file data for a fileId

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.FileApi()
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # GetFile
    api_response = api_instance.get_file(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

[**FileEntity**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileUpdateResponse update_file(file_update_request, id, study_id)

UpdateFile

Updates file data for a fileId

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
api_instance = overture_song.FileApi(overture_song.ApiClient(configuration))
file_update_request = overture_song.FileUpdateRequest() # FileUpdateRequest | File data to update
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # UpdateFile
    api_response = api_instance.update_file(file_update_request, id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_update_request** | [**FileUpdateRequest**](FileUpdateRequest.md)| File data to update | 
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

[**FileUpdateResponse**](FileUpdateResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

