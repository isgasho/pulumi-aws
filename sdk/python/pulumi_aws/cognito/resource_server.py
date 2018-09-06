# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ResourceServer(pulumi.CustomResource):
    """
    Provides a Cognito Resource Server.
    """
    def __init__(__self__, __name__, __opts__=None, identifier=None, name=None, scopes=None, user_pool_id=None):
        """Create a ResourceServer resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not identifier:
            raise TypeError('Missing required property identifier')
        elif not isinstance(identifier, basestring):
            raise TypeError('Expected property identifier to be a basestring')
        __self__.identifier = identifier
        """
        An identifier for the resource server.
        """
        __props__['identifier'] = identifier

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A name for the resource server.
        """
        __props__['name'] = name

        if scopes and not isinstance(scopes, list):
            raise TypeError('Expected property scopes to be a list')
        __self__.scopes = scopes
        """
        A list of Authorization Scope.
        """
        __props__['scopes'] = scopes

        if not user_pool_id:
            raise TypeError('Missing required property user_pool_id')
        elif not isinstance(user_pool_id, basestring):
            raise TypeError('Expected property user_pool_id to be a basestring')
        __self__.user_pool_id = user_pool_id
        __props__['userPoolId'] = user_pool_id

        __self__.scope_identifiers = pulumi.runtime.UNKNOWN
        """
        A list of all scopes configured for this resource server in the format identifier/scope_name.
        """

        super(ResourceServer, __self__).__init__(
            'aws:cognito/resourceServer:ResourceServer',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'identifier' in outs:
            self.identifier = outs['identifier']
        if 'name' in outs:
            self.name = outs['name']
        if 'scopes' in outs:
            self.scopes = outs['scopes']
        if 'scopeIdentifiers' in outs:
            self.scope_identifiers = outs['scopeIdentifiers']
        if 'userPoolId' in outs:
            self.user_pool_id = outs['userPoolId']
