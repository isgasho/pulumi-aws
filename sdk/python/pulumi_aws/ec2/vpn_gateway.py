# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class VpnGateway(pulumi.CustomResource):
    """
    Provides a resource to create a VPC VPN Gateway.
    """
    def __init__(__self__, __name__, __opts__=None, amazon_side_asn=None, availability_zone=None, tags=None, vpc_id=None):
        """Create a VpnGateway resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if amazon_side_asn and not isinstance(amazon_side_asn, basestring):
            raise TypeError('Expected property amazon_side_asn to be a basestring')
        __self__.amazon_side_asn = amazon_side_asn
        """
        The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don't specify an ASN, the virtual private gateway is created with the default ASN.
        """
        __props__['amazonSideAsn'] = amazon_side_asn

        if availability_zone and not isinstance(availability_zone, basestring):
            raise TypeError('Expected property availability_zone to be a basestring')
        __self__.availability_zone = availability_zone
        """
        The Availability Zone for the virtual private gateway.
        """
        __props__['availabilityZone'] = availability_zone

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if vpc_id and not isinstance(vpc_id, basestring):
            raise TypeError('Expected property vpc_id to be a basestring')
        __self__.vpc_id = vpc_id
        """
        The VPC ID to create in.
        """
        __props__['vpcId'] = vpc_id

        super(VpnGateway, __self__).__init__(
            'aws:ec2/vpnGateway:VpnGateway',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'amazonSideAsn' in outs:
            self.amazon_side_asn = outs['amazonSideAsn']
        if 'availabilityZone' in outs:
            self.availability_zone = outs['availabilityZone']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'vpcId' in outs:
            self.vpc_id = outs['vpcId']
