# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetCredentialsResult:
    """
    A collection of values returned by getCredentials.
    """
    def __init__(__self__, authorization_token=None, expires_at=None, proxy_endpoint=None, registry_id=None, id=None):
        if authorization_token and not isinstance(authorization_token, str):
            raise TypeError("Expected argument 'authorization_token' to be a str")
        __self__.authorization_token = authorization_token
        if expires_at and not isinstance(expires_at, str):
            raise TypeError("Expected argument 'expires_at' to be a str")
        __self__.expires_at = expires_at
        if proxy_endpoint and not isinstance(proxy_endpoint, str):
            raise TypeError("Expected argument 'proxy_endpoint' to be a str")
        __self__.proxy_endpoint = proxy_endpoint
        if registry_id and not isinstance(registry_id, str):
            raise TypeError("Expected argument 'registry_id' to be a str")
        __self__.registry_id = registry_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_credentials(registry_id=None,opts=None):
    __args__ = dict()

    __args__['registryId'] = registry_id
 .   if opts is None:
         opts = pulumi.ResourceOptions()
     if opts.version is None:
         opts.version = utilities.get_version()
    __ret__ = await pulumi.runtime.invoke('aws:ecr/getCredentials:getCredentials', __args__, opts=opts)

    return GetCredentialsResult(
        authorization_token=__ret__.get('authorizationToken'),
        expires_at=__ret__.get('expiresAt'),
        proxy_endpoint=__ret__.get('proxyEndpoint'),
        registry_id=__ret__.get('registryId'),
        id=__ret__.get('id'))
