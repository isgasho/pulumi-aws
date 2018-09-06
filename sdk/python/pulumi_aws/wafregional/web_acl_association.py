# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class WebAclAssociation(pulumi.CustomResource):
    """
    Provides a resource to create an association between a WAF Regional WebACL and Application Load Balancer.
    
    -> **Note:** An Application Load Balancer can only be associated with one WAF Regional WebACL.
    """
    def __init__(__self__, __name__, __opts__=None, resource_arn=None, web_acl_id=None):
        """Create a WebAclAssociation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not resource_arn:
            raise TypeError('Missing required property resource_arn')
        elif not isinstance(resource_arn, basestring):
            raise TypeError('Expected property resource_arn to be a basestring')
        __self__.resource_arn = resource_arn
        """
        Application Load Balancer ARN to associate with.
        """
        __props__['resourceArn'] = resource_arn

        if not web_acl_id:
            raise TypeError('Missing required property web_acl_id')
        elif not isinstance(web_acl_id, basestring):
            raise TypeError('Expected property web_acl_id to be a basestring')
        __self__.web_acl_id = web_acl_id
        """
        The ID of the WAF Regional WebACL to create an association.
        """
        __props__['webAclId'] = web_acl_id

        super(WebAclAssociation, __self__).__init__(
            'aws:wafregional/webAclAssociation:WebAclAssociation',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'resourceArn' in outs:
            self.resource_arn = outs['resourceArn']
        if 'webAclId' in outs:
            self.web_acl_id = outs['webAclId']
