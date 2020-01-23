# overture_song.AnalysisApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analysis**](AnalysisApi.md#get_analysis) | **GET** /studies/{studyId}/analysis/{id} | GetAnalysis
[**get_analysis_files**](AnalysisApi.md#get_analysis_files) | **GET** /studies/{studyId}/analysis/{id}/files | GetAnalysisFiles
[**get_analysis_for_study**](AnalysisApi.md#get_analysis_for_study) | **GET** /studies/{studyId}/analysis | GetAnalysesForStudy
[**id_search**](AnalysisApi.md#id_search) | **GET** /studies/{studyId}/analysis/search/id | IdSearch
[**id_search_with_body**](AnalysisApi.md#id_search_with_body) | **POST** /studies/{studyId}/analysis/search/id | IdSearchWithBody
[**publish_analysis**](AnalysisApi.md#publish_analysis) | **PUT** /studies/{studyId}/analysis/publish/{id} | PublishAnalysis
[**suppress_analysis**](AnalysisApi.md#suppress_analysis) | **PUT** /studies/{studyId}/analysis/suppress/{id} | SuppressAnalysis
[**unpublish_analysis**](AnalysisApi.md#unpublish_analysis) | **PUT** /studies/{studyId}/analysis/unpublish/{id} | UnpublishAnalysis
[**update_analysis**](AnalysisApi.md#update_analysis) | **PUT** /studies/{studyId}/analysis/{analysisId} | UpdateAnalysis


# **get_analysis**
> Analysis get_analysis(id, study_id)

GetAnalysis

Retrieve the analysis object for an analysisId

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.AnalysisApi()
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # GetAnalysis
    api_response = api_instance.get_analysis(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

[**Analysis**](Analysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_files**
> list[FileEntity] get_analysis_files(id, study_id)

GetAnalysisFiles

Retrieve the file objects for an analysisId

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.AnalysisApi()
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # GetAnalysisFiles
    api_response = api_instance.get_analysis_files(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_analysis_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

[**list[FileEntity]**](FileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_for_study**
> list[Analysis] get_analysis_for_study(study_id, analysis_states=analysis_states)

GetAnalysesForStudy

Retrieve all analysis objects for a studyId

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.AnalysisApi()
study_id = 'study_id_example' # str | studyId
analysis_states = 'PUBLISHED' # str | Non-empty comma separated list of analysis states to filter by (optional) (default to PUBLISHED)

try:
    # GetAnalysesForStudy
    api_response = api_instance.get_analysis_for_study(study_id, analysis_states=analysis_states)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_analysis_for_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**| studyId | 
 **analysis_states** | **str**| Non-empty comma separated list of analysis states to filter by | [optional] [default to PUBLISHED]

### Return type

[**list[Analysis]**](Analysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_search**
> list[Analysis] id_search(study_id, donor_id=donor_id, file_id=file_id, sample_id=sample_id, specimen_id=specimen_id)

IdSearch

Search for analysis objects by specifying regex patterns for the donorIds, sampleIds, specimenIds, or fileIds request parameters

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.AnalysisApi()
study_id = 'study_id_example' # str | studyId
donor_id = 'donor_id_example' # str | donorId (optional)
file_id = 'file_id_example' # str | fileId (optional)
sample_id = 'sample_id_example' # str | sampleId (optional)
specimen_id = 'specimen_id_example' # str | specimenId (optional)

try:
    # IdSearch
    api_response = api_instance.id_search(study_id, donor_id=donor_id, file_id=file_id, sample_id=sample_id, specimen_id=specimen_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->id_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**| studyId | 
 **donor_id** | **str**| donorId | [optional] 
 **file_id** | **str**| fileId | [optional] 
 **sample_id** | **str**| sampleId | [optional] 
 **specimen_id** | **str**| specimenId | [optional] 

### Return type

[**list[Analysis]**](Analysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **id_search_with_body**
> list[Analysis] id_search_with_body(request, study_id)

IdSearchWithBody

Search for analysis objects by specifying an IdSearchRequest

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.AnalysisApi()
request = overture_song.IdSearchRequest() # IdSearchRequest | request
study_id = 'study_id_example' # str | studyId

try:
    # IdSearchWithBody
    api_response = api_instance.id_search_with_body(request, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->id_search_with_body: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IdSearchRequest**](IdSearchRequest.md)| request | 
 **study_id** | **str**| studyId | 

### Return type

[**list[Analysis]**](Analysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json;charset=UTF-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_analysis**
> str publish_analysis(id, study_id, ignore_undefined_md5=ignore_undefined_md5)

PublishAnalysis

Publish an analysis. This checks to see if the files associated with the input analysisId exist in the storage server

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
api_instance = overture_song.AnalysisApi(overture_song.ApiClient(configuration))
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId
ignore_undefined_md5 = false # bool | Ignores files that have an undefined MD5 checksum when publishing (optional) (default to false)

try:
    # PublishAnalysis
    api_response = api_instance.publish_analysis(id, study_id, ignore_undefined_md5=ignore_undefined_md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->publish_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 
 **ignore_undefined_md5** | **bool**| Ignores files that have an undefined MD5 checksum when publishing | [optional] [default to false]

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_analysis**
> str suppress_analysis(id, study_id)

SuppressAnalysis

Suppress an analysis. Used if a previously published analysis is no longer needed. Instead of removing the analysis, it is marked as \"suppressed\"

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
api_instance = overture_song.AnalysisApi(overture_song.ApiClient(configuration))
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # SuppressAnalysis
    api_response = api_instance.suppress_analysis(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->suppress_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_analysis**
> str unpublish_analysis(id, study_id)

UnpublishAnalysis

Unpublish an analysis. Set the analysis status to unpublished

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
api_instance = overture_song.AnalysisApi(overture_song.ApiClient(configuration))
id = 'id_example' # str | id
study_id = 'study_id_example' # str | studyId

try:
    # UnpublishAnalysis
    api_response = api_instance.unpublish_analysis(id, study_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->unpublish_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **study_id** | **str**| studyId | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis**
> update_analysis(analysis_id, study_id, update_analysis_request)

UpdateAnalysis

Update dynamic-data for for an analysis

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
api_instance = overture_song.AnalysisApi(overture_song.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | analysisId
study_id = 'study_id_example' # str | studyId
update_analysis_request = overture_song.JsonNode() # JsonNode | updateAnalysisRequest

try:
    # UpdateAnalysis
    api_instance.update_analysis(analysis_id, study_id, update_analysis_request)
except ApiException as e:
    print("Exception when calling AnalysisApi->update_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| analysisId | 
 **study_id** | **str**| studyId | 
 **update_analysis_request** | [**JsonNode**](JsonNode.md)| updateAnalysisRequest | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, application/json;charset=UTF-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

