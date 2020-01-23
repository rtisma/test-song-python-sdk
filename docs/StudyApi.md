# overture_song.StudyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_study**](StudyApi.md#create_study) | **POST** /studies/{studyId}/ | CreateStudy
[**get_study**](StudyApi.md#get_study) | **GET** /studies/{studyId} | GetStudy
[**get_study_tree**](StudyApi.md#get_study_tree) | **GET** /studies/{studyId}/all | GetStudyTree
[**list_all_study_ids**](StudyApi.md#list_all_study_ids) | **GET** /studies/all | ListAllStudyIds


# **create_study**
> GenericMessage create_study(study, study_id)

CreateStudy

Creates a new study

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
api_instance = overture_song.StudyApi(overture_song.ApiClient(configuration))
study = overture_song.Study() # Study | study
study_id = 'study_id_example' # str | studyId

try:
    # CreateStudy
    api_response = api_instance.create_study(study, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudyApi->create_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study** | [**Study**](Study.md)| study | 
 **study_id** | **str**| studyId | 

### Return type

[**GenericMessage**](GenericMessage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, application/json;charset=UTF-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study**
> Study get_study(study_id)

GetStudy

Retrieves information for a study

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.StudyApi()
study_id = 'study_id_example' # str | studyId

try:
    # GetStudy
    api_response = api_instance.get_study(study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudyApi->get_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**| studyId | 

### Return type

[**Study**](Study.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_tree**
> StudyWithDonors get_study_tree(study_id)

GetStudyTree

Retrieves all donor, specimen and sample data for a study

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.StudyApi()
study_id = 'study_id_example' # str | studyId

try:
    # GetStudyTree
    api_response = api_instance.get_study_tree(study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudyApi->get_study_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**| studyId | 

### Return type

[**StudyWithDonors**](StudyWithDonors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_study_ids**
> list[str] list_all_study_ids()

ListAllStudyIds

Retrieves all studyIds

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.StudyApi()

try:
    # ListAllStudyIds
    api_response = api_instance.list_all_study_ids()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StudyApi->list_all_study_ids: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

