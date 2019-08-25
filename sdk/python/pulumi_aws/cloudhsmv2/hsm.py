# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Hsm(pulumi.CustomResource):
    availability_zone: pulumi.Output[str]
    """
    The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.
    """
    cluster_id: pulumi.Output[str]
    """
    The ID of Cloud HSM v2 cluster to which HSM will be added.
    """
    hsm_eni_id: pulumi.Output[str]
    """
    The id of the ENI interface allocated for HSM module.
    """
    hsm_id: pulumi.Output[str]
    """
    The id of the HSM module.
    """
    hsm_state: pulumi.Output[str]
    """
    The state of the HSM module.
    """
    ip_address: pulumi.Output[str]
    """
    The IP address of HSM module. Must be within the CIDR of selected subnet.
    """
    subnet_id: pulumi.Output[str]
    """
    The ID of subnet in which HSM module will be located.
    """
    def __init__(__self__, resource_name, opts=None, availability_zone=None, cluster_id=None, ip_address=None, subnet_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates an HSM module in Amazon CloudHSM v2 cluster.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.
        :param pulumi.Input[str] cluster_id: The ID of Cloud HSM v2 cluster to which HSM will be added.
        :param pulumi.Input[str] ip_address: The IP address of HSM module. Must be within the CIDR of selected subnet.
        :param pulumi.Input[str] subnet_id: The ID of subnet in which HSM module will be located.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudhsm_v2_hsm.html.markdown.
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

            __props__['availability_zone'] = availability_zone
            if cluster_id is None:
                raise TypeError("Missing required property 'cluster_id'")
            __props__['cluster_id'] = cluster_id
            __props__['ip_address'] = ip_address
            __props__['subnet_id'] = subnet_id
            __props__['hsm_eni_id'] = None
            __props__['hsm_id'] = None
            __props__['hsm_state'] = None
        super(Hsm, __self__).__init__(
            'aws:cloudhsmv2/hsm:Hsm',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, availability_zone=None, cluster_id=None, hsm_eni_id=None, hsm_id=None, hsm_state=None, ip_address=None, subnet_id=None):
        """
        Get an existing Hsm resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The IDs of AZ in which HSM module will be located. Do not use together with subnet_id.
        :param pulumi.Input[str] cluster_id: The ID of Cloud HSM v2 cluster to which HSM will be added.
        :param pulumi.Input[str] hsm_eni_id: The id of the ENI interface allocated for HSM module.
        :param pulumi.Input[str] hsm_id: The id of the HSM module.
        :param pulumi.Input[str] hsm_state: The state of the HSM module.
        :param pulumi.Input[str] ip_address: The IP address of HSM module. Must be within the CIDR of selected subnet.
        :param pulumi.Input[str] subnet_id: The ID of subnet in which HSM module will be located.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudhsm_v2_hsm.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["availability_zone"] = availability_zone
        __props__["cluster_id"] = cluster_id
        __props__["hsm_eni_id"] = hsm_eni_id
        __props__["hsm_id"] = hsm_id
        __props__["hsm_state"] = hsm_state
        __props__["ip_address"] = ip_address
        __props__["subnet_id"] = subnet_id
        return Hsm(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

