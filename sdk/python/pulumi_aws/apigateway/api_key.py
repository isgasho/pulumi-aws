# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ApiKey(pulumi.CustomResource):
    created_date: pulumi.Output[str]
    """
    The creation date of the API key
    """
    description: pulumi.Output[str]
    """
    The API key description. Defaults to "Managed by Pulumi".
    """
    enabled: pulumi.Output[bool]
    """
    Specifies whether the API key can be used by callers. Defaults to `true`.
    """
    last_updated_date: pulumi.Output[str]
    """
    The last update date of the API key
    """
    name: pulumi.Output[str]
    """
    The name of the API key
    """
    value: pulumi.Output[str]
    """
    The value of the API key. If not specified, it will be automatically generated by AWS on creation.
    """
    def __init__(__self__, resource_name, opts=None, description=None, enabled=None, name=None, value=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an API Gateway API Key.
        
        > **NOTE:** Since the API Gateway usage plans feature was launched on August 11, 2016, usage plans are now **required** to associate an API key with an API stage.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The API key description. Defaults to "Managed by Pulumi".
        :param pulumi.Input[bool] enabled: Specifies whether the API key can be used by callers. Defaults to `true`.
        :param pulumi.Input[str] name: The name of the API key
        :param pulumi.Input[str] value: The value of the API key. If not specified, it will be automatically generated by AWS on creation.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_api_key.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if description is None:
                description = 'Managed by Pulumi'
            __props__['description'] = description
            __props__['enabled'] = enabled
            __props__['name'] = name
            __props__['value'] = value
            __props__['created_date'] = None
            __props__['last_updated_date'] = None
        super(ApiKey, __self__).__init__(
            'aws:apigateway/apiKey:ApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, created_date=None, description=None, enabled=None, last_updated_date=None, name=None, value=None):
        """
        Get an existing ApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_date: The creation date of the API key
        :param pulumi.Input[str] description: The API key description. Defaults to "Managed by Pulumi".
        :param pulumi.Input[bool] enabled: Specifies whether the API key can be used by callers. Defaults to `true`.
        :param pulumi.Input[str] last_updated_date: The last update date of the API key
        :param pulumi.Input[str] name: The name of the API key
        :param pulumi.Input[str] value: The value of the API key. If not specified, it will be automatically generated by AWS on creation.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_api_key.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["created_date"] = created_date
        __props__["description"] = description
        __props__["enabled"] = enabled
        __props__["last_updated_date"] = last_updated_date
        __props__["name"] = name
        __props__["value"] = value
        return ApiKey(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

