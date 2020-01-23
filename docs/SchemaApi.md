# overture_song.SchemaApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analysis_type_version**](SchemaApi.md#get_analysis_type_version) | **GET** /schemas/{name} | GetAnalysisTypeVersion
[**get_registration_schema**](SchemaApi.md#get_registration_schema) | **GET** /schemas/registration | GetRegistrationSchema
[**list_analysis_types**](SchemaApi.md#list_analysis_types) | **GET** /schemas | ListAnalysisTypes
[**register_analysis_type**](SchemaApi.md#register_analysis_type) | **POST** /schemas | RegisterAnalysisType


# **get_analysis_type_version**
> AnalysisType get_analysis_type_version(name, unrendered_only=unrendered_only, version=version)

GetAnalysisTypeVersion

Retrieves the latest version of a schema for an analysisType

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.SchemaApi()
name = 'name_example' # str | The name of an analysisType
unrendered_only = false # bool | Only retrieve the unrendered schema that was initially registered (optional) (default to false)
version = 56 # int | Optionally, retrieve a specific version of the analysisType (optional)

try:
    # GetAnalysisTypeVersion
    api_response = api_instance.get_analysis_type_version(name, unrendered_only=unrendered_only, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->get_analysis_type_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of an analysisType | 
 **unrendered_only** | **bool**| Only retrieve the unrendered schema that was initially registered | [optional] [default to false]
 **version** | **int**| Optionally, retrieve a specific version of the analysisType | [optional] 

### Return type

[**AnalysisType**](AnalysisType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_schema**
> str get_registration_schema()

GetRegistrationSchema

Retrieves the meta-schema used to validate AnalysisType schemas during registration

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.SchemaApi()

try:
    # GetRegistrationSchema
    api_response = api_instance.get_registration_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->get_registration_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_analysis_types**
> PageDTOAnalysisType list_analysis_types(hide_schema=hide_schema, limit=limit, names=names, offset=offset, page_number=page_number, page_size=page_size, paged=paged, sort=sort, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_order=sort_order, unpaged=unpaged, unrendered_only=unrendered_only, versions=versions)

ListAnalysisTypes

Retrieves a list of registered analysisTypes

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.SchemaApi()
hide_schema = false # bool | Hide the schema field from the response (optional) (default to false)
limit = overture_song.Object() # Object | Number of results to retrieve (optional) (default to 20)
names = ['names_example'] # list[str] | Comma separated list of names (optional)
offset = overture_song.Object() # Object | Index of first result to retrieve (optional) (default to 0)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
paged = true # bool |  (optional)
sort = 'sort_example' # str | Comma separated fields to sort on (optional)
sort_sorted = true # bool |  (optional)
sort_unsorted = true # bool |  (optional)
sort_order = 'sort_order_example' # str | Sorting order: ASC|DESC. Default order: DESC (optional)
unpaged = true # bool |  (optional)
unrendered_only = false # bool | Only retrieve the unrendered schema that was initially registered (optional) (default to false)
versions = [56] # list[int] | Comma separated list of versions (optional)

try:
    # ListAnalysisTypes
    api_response = api_instance.list_analysis_types(hide_schema=hide_schema, limit=limit, names=names, offset=offset, page_number=page_number, page_size=page_size, paged=paged, sort=sort, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, sort_order=sort_order, unpaged=unpaged, unrendered_only=unrendered_only, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->list_analysis_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hide_schema** | **bool**| Hide the schema field from the response | [optional] [default to false]
 **limit** | [**Object**](.md)| Number of results to retrieve | [optional] [default to 20]
 **names** | [**list[str]**](str.md)| Comma separated list of names | [optional] 
 **offset** | [**Object**](.md)| Index of first result to retrieve | [optional] [default to 0]
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **paged** | **bool**|  | [optional] 
 **sort** | **str**| Comma separated fields to sort on | [optional] 
 **sort_sorted** | **bool**|  | [optional] 
 **sort_unsorted** | **bool**|  | [optional] 
 **sort_order** | **str**| Sorting order: ASC|DESC. Default order: DESC | [optional] 
 **unpaged** | **bool**|  | [optional] 
 **unrendered_only** | **bool**| Only retrieve the unrendered schema that was initially registered | [optional] [default to false]
 **versions** | [**list[int]**](int.md)| Comma separated list of versions | [optional] 

### Return type

[**PageDTOAnalysisType**](PageDTOAnalysisType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_analysis_type**
> AnalysisType register_analysis_type(request)

RegisterAnalysisType

Registers an analysisType schema

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
api_instance = overture_song.SchemaApi(overture_song.ApiClient(configuration))
request = overture_song.RegisterAnalysisTypeRequest() # RegisterAnalysisTypeRequest | request

try:
    # RegisterAnalysisType
    api_response = api_instance.register_analysis_type(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->register_analysis_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**RegisterAnalysisTypeRequest**](RegisterAnalysisTypeRequest.md)| request | 

### Return type

[**AnalysisType**](AnalysisType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json, application/json;charset=UTF-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

