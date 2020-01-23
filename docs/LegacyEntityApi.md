# overture_song.LegacyEntityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_legacy_entities**](LegacyEntityApi.md#find_legacy_entities) | **GET** /entities | FindLegacyEntities
[**get_legacy_entity**](LegacyEntityApi.md#get_legacy_entity) | **GET** /entities/{id} | GetLegacyEntity


# **find_legacy_entities**
> JsonNode find_legacy_entities(access=access, fields=fields, file_name=file_name, gnos_id=gnos_id, id=id, offset=offset, page=page, page_number=page_number, page_size=page_size, paged=paged, project_code=project_code, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, unpaged=unpaged)

FindLegacyEntities

Page through LegacyEntity data

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.LegacyEntityApi()
access = 'access_example' # str |  (optional)
fields = NULL # object | fields (optional)
file_name = 'file_name_example' # str |  (optional)
gnos_id = 'gnos_id_example' # str |  (optional)
id = 'id_example' # str |  (optional)
offset = 789 # int |  (optional)
page = overture_song.Object() # Object | Results page you want to retrieve (0..N) (optional)
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)
paged = true # bool |  (optional)
project_code = 'project_code_example' # str |  (optional)
size = overture_song.Object() # Object | Number of records per page. (optional)
sort_sorted = true # bool |  (optional)
sort_unsorted = true # bool |  (optional)
unpaged = true # bool |  (optional)

try:
    # FindLegacyEntities
    api_response = api_instance.find_legacy_entities(access=access, fields=fields, file_name=file_name, gnos_id=gnos_id, id=id, offset=offset, page=page, page_number=page_number, page_size=page_size, paged=paged, project_code=project_code, size=size, sort_sorted=sort_sorted, sort_unsorted=sort_unsorted, unpaged=unpaged)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyEntityApi->find_legacy_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access** | **str**|  | [optional] 
 **fields** | [**object**](.md)| fields | [optional] 
 **file_name** | **str**|  | [optional] 
 **gnos_id** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **page** | [**Object**](.md)| Results page you want to retrieve (0..N) | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **paged** | **bool**|  | [optional] 
 **project_code** | **str**|  | [optional] 
 **size** | [**Object**](.md)| Number of records per page. | [optional] 
 **sort_sorted** | **bool**|  | [optional] 
 **sort_unsorted** | **bool**|  | [optional] 
 **unpaged** | **bool**|  | [optional] 

### Return type

[**JsonNode**](JsonNode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legacy_entity**
> Legacy get_legacy_entity(id)

GetLegacyEntity

Read entity data for a legacy entity id

### Example
```python
from __future__ import print_function
import time
import overture_song
from overture_song.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = overture_song.LegacyEntityApi()
id = 'id_example' # str | id

try:
    # GetLegacyEntity
    api_response = api_instance.get_legacy_entity(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegacyEntityApi->get_legacy_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**Legacy**](Legacy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

