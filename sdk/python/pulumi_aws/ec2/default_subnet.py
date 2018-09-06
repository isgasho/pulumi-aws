# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class DefaultSubnet(pulumi.CustomResource):
    """
    Provides a resource to manage a [default AWS VPC subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html#default-vpc-basics)
    in the current region.
    
    The `aws_default_subnet` behaves differently from normal resources, in that
    Terraform does not _create_ this resource, but instead "adopts" it
    into management.
    """
    def __init__(__self__, __name__, __opts__=None, availability_zone=None, map_public_ip_on_launch=None, tags=None):
        """Create a DefaultSubnet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not availability_zone:
            raise TypeError('Missing required property availability_zone')
        elif not isinstance(availability_zone, basestring):
            raise TypeError('Expected property availability_zone to be a basestring')
        __self__.availability_zone = availability_zone
        __props__['availabilityZone'] = availability_zone

        if map_public_ip_on_launch and not isinstance(map_public_ip_on_launch, bool):
            raise TypeError('Expected property map_public_ip_on_launch to be a bool')
        __self__.map_public_ip_on_launch = map_public_ip_on_launch
        """
        Specify true to indicate
        that instances launched into the subnet should be assigned
        a public IP address.
        """
        __props__['mapPublicIpOnLaunch'] = map_public_ip_on_launch

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.arn = pulumi.runtime.UNKNOWN
        __self__.assign_ipv6_address_on_creation = pulumi.runtime.UNKNOWN
        __self__.cidr_block = pulumi.runtime.UNKNOWN
        """
        The CIDR block for the subnet.
        """
        __self__.ipv6_cidr_block = pulumi.runtime.UNKNOWN
        """
        The IPv6 CIDR block.
        """
        __self__.ipv6_cidr_block_association_id = pulumi.runtime.UNKNOWN
        __self__.vpc_id = pulumi.runtime.UNKNOWN
        """
        The VPC ID.
        """

        super(DefaultSubnet, __self__).__init__(
            'aws:ec2/defaultSubnet:DefaultSubnet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'assignIpv6AddressOnCreation' in outs:
            self.assign_ipv6_address_on_creation = outs['assignIpv6AddressOnCreation']
        if 'availabilityZone' in outs:
            self.availability_zone = outs['availabilityZone']
        if 'cidrBlock' in outs:
            self.cidr_block = outs['cidrBlock']
        if 'ipv6CidrBlock' in outs:
            self.ipv6_cidr_block = outs['ipv6CidrBlock']
        if 'ipv6CidrBlockAssociationId' in outs:
            self.ipv6_cidr_block_association_id = outs['ipv6CidrBlockAssociationId']
        if 'mapPublicIpOnLaunch' in outs:
            self.map_public_ip_on_launch = outs['mapPublicIpOnLaunch']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'vpcId' in outs:
            self.vpc_id = outs['vpcId']
