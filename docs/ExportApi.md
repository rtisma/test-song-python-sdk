# overture_song.ExportApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_analyses**](ExportApi.md#export_analyses) | **GET** /export/analysis/{analysisIds} | ExportAnalyses
[**export_study**](ExportApi.md#export_study) | **GET** /export/studies/{studyId} | ExportStudy


# **export_analyses**
> list[ExportedPayload] export_analyses(analysis_ids)

ExportAnalyses

Exports the payload for a list of analysisIds

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.ExportApi()
analysis_ids = 'analysis_ids_example' # str | Comma separated list of analysisIds

try:
    # ExportAnalyses
    api_response = api_instance.export_analyses(analysis_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->export_analyses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_ids** | **str**| Comma separated list of analysisIds | 

### Return type

[**list[ExportedPayload]**](ExportedPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_study**
> list[ExportedPayload] export_study(study_id)

ExportStudy

Exports all the payloads for a study

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.ExportApi()
study_id = 'study_id_example' # str | studyId

try:
    # ExportStudy
    api_response = api_instance.export_study(study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->export_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**| studyId | 

### Return type

[**list[ExportedPayload]**](ExportedPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

