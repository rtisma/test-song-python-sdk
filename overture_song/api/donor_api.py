# coding: utf-8

"""
    Song API

    Song API reference for developers. SONG is an open source system for validating and tracking metadata about raw data submissions, assigning identifiers to entities of interest, and managing the state of the raw data with regards to publication and access  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from overture_song.api_client import ApiClient


class DonorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_donors(self, ids, study_id, **kwargs):  # noqa: E501
        """DeleteDonors  # noqa: E501

        Deletes donor data and all dependent specimens and samples for donorIds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_donors(ids, study_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: Comma separated list of donorIds (required)
        :param str study_id: studyId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_donors_with_http_info(ids, study_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_donors_with_http_info(ids, study_id, **kwargs)  # noqa: E501
            return data

    def delete_donors_with_http_info(self, ids, study_id, **kwargs):  # noqa: E501
        """DeleteDonors  # noqa: E501

        Deletes donor data and all dependent specimens and samples for donorIds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_donors_with_http_info(ids, study_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: Comma separated list of donorIds (required)
        :param str study_id: studyId (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'study_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_donors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `delete_donors`")  # noqa: E501
        # verify the required parameter 'study_id' is set
        if ('study_id' not in params or
                params['study_id'] is None):
            raise ValueError("Missing the required parameter `study_id` when calling `delete_donors`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ids' in params:
            path_params['ids'] = params['ids']  # noqa: E501
        if 'study_id' in params:
            path_params['studyId'] = params['study_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/studies/{studyId}/donors/{ids}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_donor(self, id, study_id, **kwargs):  # noqa: E501
        """GetDonor  # noqa: E501

        Retrieves donor data for a donorId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_donor(id, study_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param str study_id: studyId (required)
        :return: Donor
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_donor_with_http_info(id, study_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_donor_with_http_info(id, study_id, **kwargs)  # noqa: E501
            return data

    def get_donor_with_http_info(self, id, study_id, **kwargs):  # noqa: E501
        """GetDonor  # noqa: E501

        Retrieves donor data for a donorId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_donor_with_http_info(id, study_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param str study_id: studyId (required)
        :return: Donor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'study_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_donor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_donor`")  # noqa: E501
        # verify the required parameter 'study_id' is set
        if ('study_id' not in params or
                params['study_id'] is None):
            raise ValueError("Missing the required parameter `study_id` when calling `get_donor`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'study_id' in params:
            path_params['studyId'] = params['study_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/studies/{studyId}/donors/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Donor',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
