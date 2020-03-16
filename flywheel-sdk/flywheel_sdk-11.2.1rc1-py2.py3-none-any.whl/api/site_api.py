# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 11.2.1-rc.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flywheel.api_client import ApiClient
import flywheel.models

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

class SiteApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_provider(self, body, **kwargs):  # noqa: E501
        """Add a new provider

        This method makes a synchronous HTTP request by default.

        :param ProviderInput body: (required)
        :param bool async_: Perform the request asynchronously
        :return: CollectionNewOutput
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.add_provider_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_provider_with_http_info(body, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def add_provider_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add a new provider

        This method makes a synchronous HTTP request by default.

        :param ProviderInput body: (required)
        :param bool async: Perform the request asynchronously
        :return: CollectionNewOutput
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = flywheel.models.ProviderInput.positional_to_model(params['body'])
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/site/providers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionNewOutput',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_provider(self, provider_id, **kwargs):  # noqa: E501
        """Return the provider identified by ProviderId

        This method makes a synchronous HTTP request by default.

        :param str provider_id: The ID of the provider (required)
        :param bool async_: Perform the request asynchronously
        :return: Provider
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.get_provider_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_with_http_info(provider_id, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def get_provider_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Return the provider identified by ProviderId

        This method makes a synchronous HTTP request by default.

        :param str provider_id: The ID of the provider (required)
        :param bool async: Perform the request asynchronously
        :return: Provider
        """

        all_params = ['provider_id']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `get_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['ProviderId'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/site/providers/{ProviderId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Provider',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_provider_config(self, provider_id, **kwargs):  # noqa: E501
        """Return the configuration for provider identified by ProviderId

        The returned configuration will be redacted, with any privileged values replaced with null.
        This method makes a synchronous HTTP request by default.

        :param str provider_id: The ID of the provider (required)
        :param bool async_: Perform the request asynchronously
        :return: object
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.get_provider_config_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_provider_config_with_http_info(provider_id, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def get_provider_config_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Return the configuration for provider identified by ProviderId

        The returned configuration will be redacted, with any privileged values replaced with null.
        This method makes a synchronous HTTP request by default.

        :param str provider_id: The ID of the provider (required)
        :param bool async: Perform the request asynchronously
        :return: object
        """

        all_params = ['provider_id']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provider_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `get_provider_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['ProviderId'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/site/providers/{ProviderId}/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_providers(self, **kwargs):  # noqa: E501
        """Return a list of all providers on the site

        This method makes a synchronous HTTP request by default.

        :param str _class: Limit the response to the given provider class
        :param bool async_: Perform the request asynchronously
        :return: list[Provider]
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.get_providers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_providers_with_http_info(**kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def get_providers_with_http_info(self, **kwargs):  # noqa: E501
        """Return a list of all providers on the site

        This method makes a synchronous HTTP request by default.

        :param str _class: Limit the response to the given provider class
        :param bool async: Perform the request asynchronously
        :return: list[Provider]
        """

        all_params = ['_class']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_providers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_class' in params:
            query_params.append(('class', params['_class']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/site/providers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Provider]',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def get_site_settings(self, **kwargs):  # noqa: E501
        """Return administrative site settings

        Returns the site settings, which includes center-pays gear list. If the site settings have never been created, then center_gears will be null, rather than an empty list. 
        This method makes a synchronous HTTP request by default.

        :param bool async_: Perform the request asynchronously
        :return: ConfigSiteSettings
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.get_site_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_site_settings_with_http_info(**kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def get_site_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Return administrative site settings

        Returns the site settings, which includes center-pays gear list. If the site settings have never been created, then center_gears will be null, rather than an empty list. 
        This method makes a synchronous HTTP request by default.

        :param bool async: Perform the request asynchronously
        :return: ConfigSiteSettings
        """

        all_params = []  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_site_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/site/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigSiteSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def modify_provider(self, provider_id, body, **kwargs):  # noqa: E501
        """Update the provider identified by ProviderId

        This method makes a synchronous HTTP request by default.

        :param str provider_id: The ID of the provider (required)
        :param ProviderInput body: (required)
        :param bool async_: Perform the request asynchronously
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.modify_provider_with_http_info(provider_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_provider_with_http_info(provider_id, body, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def modify_provider_with_http_info(self, provider_id, body, **kwargs):  # noqa: E501
        """Update the provider identified by ProviderId

        This method makes a synchronous HTTP request by default.

        :param str provider_id: The ID of the provider (required)
        :param ProviderInput body: (required)
        :param bool async: Perform the request asynchronously
        :return: None
        """

        all_params = ['provider_id', 'body']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `modify_provider`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['ProviderId'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = flywheel.models.ProviderInput.positional_to_model(params['body'])
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/site/providers/{ProviderId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)

    def modify_site_settings(self, body, **kwargs):  # noqa: E501
        """Update administrative site settings

        This method makes a synchronous HTTP request by default.

        :param ConfigSiteSettingsInput body: (required)
        :param bool async_: Perform the request asynchronously
        :return: None
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.modify_site_settings_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_site_settings_with_http_info(body, **kwargs)  # noqa: E501
            if data and hasattr(data, 'return_value'):
                return data.return_value()
            return data


    def modify_site_settings_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update administrative site settings

        This method makes a synchronous HTTP request by default.

        :param ConfigSiteSettingsInput body: (required)
        :param bool async: Perform the request asynchronously
        :return: None
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('_request_out')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_site_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_site_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = flywheel.models.ConfigSiteSettingsInput.positional_to_model(params['body'])
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/site/settings', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            _request_out=params.get('_request_out'),
            collection_formats=collection_formats)
