# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Instance']


class Instance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 blueprint_id: Optional[pulumi.Input[str]] = None,
                 bundle_id: Optional[pulumi.Input[str]] = None,
                 key_pair_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Lightsail Instance. Amazon Lightsail is a service to provide easy virtual private servers
        with custom software already setup. See [What is Amazon Lightsail?](https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail)
        for more information.

        > **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new GitLab Lightsail Instance
        gitlab_test = aws.lightsail.Instance("gitlabTest",
            availability_zone="us-east-1b",
            blueprint_id="string",
            bundle_id="string",
            key_pair_name="some_key_name",
            tags={
                "foo": "bar",
            })
        ```
        ## Availability Zones

        Lightsail currently supports the following Availability Zones (e.g. `us-east-1a`):

        - `ap-northeast-1{a,c,d}`
        - `ap-northeast-2{a,c}`
        - `ap-south-1{a,b}`
        - `ap-southeast-1{a,b,c}`
        - `ap-southeast-2{a,b,c}`
        - `ca-central-1{a,b}`
        - `eu-central-1{a,b,c}`
        - `eu-west-1{a,b,c}`
        - `eu-west-2{a,b,c}`
        - `eu-west-3{a,b,c}`
        - `us-east-1{a,b,c,d,e,f}`
        - `us-east-2{a,b,c}`
        - `us-west-2{a,b,c}`

        ## Bundles

        Lightsail currently supports the following Bundle IDs (e.g. an instance in `ap-northeast-1` would use `small_2_0`):

        ### Prefix

        A Bundle ID starts with one of the below size prefixes:

        - `nano_`
        - `micro_`
        - `small_`
        - `medium_`
        - `large_`
        - `xlarge_`
        - `2xlarge_`

        ### Suffix

        A Bundle ID ends with one of the following suffixes depending on Availability Zone:

        - ap-northeast-1: `2_0`
        - ap-northeast-2: `2_0`
        - ap-south-1: `2_1`
        - ap-southeast-1: `2_0`
        - ap-southeast-2: `2_2`
        - ca-central-1: `2_0`
        - eu-central-1: `2_0`
        - eu-west-1: `2_0`
        - eu-west-2: `2_0`
        - eu-west-3: `2_0`
        - us-east-1: `2_0`
        - us-east-2: `2_0`
        - us-west-2: `2_0`

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your
               instance (see list below)
        :param pulumi.Input[str] blueprint_id: The ID for a virtual private server image. A list of available blueprint IDs can be obtained using the AWS CLI command: `aws lightsail get-blueprints`
        :param pulumi.Input[str] bundle_id: The bundle of specification information (see list below)
        :param pulumi.Input[str] key_pair_name: The name of your key pair. Created in the
               Lightsail console (cannot use `ec2.KeyPair` at this time)
        :param pulumi.Input[str] name: The name of the Lightsail Instance. Names be unique within each AWS Region in your Lightsail account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. To create a key-only tag, use an empty string as the value.
        :param pulumi.Input[str] user_data: launch script to configure server with additional user data
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if availability_zone is None:
                raise TypeError("Missing required property 'availability_zone'")
            __props__['availability_zone'] = availability_zone
            if blueprint_id is None:
                raise TypeError("Missing required property 'blueprint_id'")
            __props__['blueprint_id'] = blueprint_id
            if bundle_id is None:
                raise TypeError("Missing required property 'bundle_id'")
            __props__['bundle_id'] = bundle_id
            __props__['key_pair_name'] = key_pair_name
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['user_data'] = user_data
            __props__['arn'] = None
            __props__['cpu_count'] = None
            __props__['created_at'] = None
            __props__['ipv6_address'] = None
            __props__['is_static_ip'] = None
            __props__['private_ip_address'] = None
            __props__['public_ip_address'] = None
            __props__['ram_size'] = None
            __props__['username'] = None
        super(Instance, __self__).__init__(
            'aws:lightsail/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            blueprint_id: Optional[pulumi.Input[str]] = None,
            bundle_id: Optional[pulumi.Input[str]] = None,
            cpu_count: Optional[pulumi.Input[int]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            ipv6_address: Optional[pulumi.Input[str]] = None,
            is_static_ip: Optional[pulumi.Input[bool]] = None,
            key_pair_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_ip_address: Optional[pulumi.Input[str]] = None,
            public_ip_address: Optional[pulumi.Input[str]] = None,
            ram_size: Optional[pulumi.Input[float]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            user_data: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Lightsail instance (matches `id`).
        :param pulumi.Input[str] availability_zone: The Availability Zone in which to create your
               instance (see list below)
        :param pulumi.Input[str] blueprint_id: The ID for a virtual private server image. A list of available blueprint IDs can be obtained using the AWS CLI command: `aws lightsail get-blueprints`
        :param pulumi.Input[str] bundle_id: The bundle of specification information (see list below)
        :param pulumi.Input[str] created_at: The timestamp when the instance was created.
               * `availability_zone`
               * `blueprint_id`
               * `bundle_id`
               * `key_pair_name`
               * `user_data`
        :param pulumi.Input[str] key_pair_name: The name of your key pair. Created in the
               Lightsail console (cannot use `ec2.KeyPair` at this time)
        :param pulumi.Input[str] name: The name of the Lightsail Instance. Names be unique within each AWS Region in your Lightsail account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. To create a key-only tag, use an empty string as the value.
        :param pulumi.Input[str] user_data: launch script to configure server with additional user data
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["availability_zone"] = availability_zone
        __props__["blueprint_id"] = blueprint_id
        __props__["bundle_id"] = bundle_id
        __props__["cpu_count"] = cpu_count
        __props__["created_at"] = created_at
        __props__["ipv6_address"] = ipv6_address
        __props__["is_static_ip"] = is_static_ip
        __props__["key_pair_name"] = key_pair_name
        __props__["name"] = name
        __props__["private_ip_address"] = private_ip_address
        __props__["public_ip_address"] = public_ip_address
        __props__["ram_size"] = ram_size
        __props__["tags"] = tags
        __props__["user_data"] = user_data
        __props__["username"] = username
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Lightsail instance (matches `id`).
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[str]:
        """
        The Availability Zone in which to create your
        instance (see list below)
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Output[str]:
        """
        The ID for a virtual private server image. A list of available blueprint IDs can be obtained using the AWS CLI command: `aws lightsail get-blueprints`
        """
        return pulumi.get(self, "blueprint_id")

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[str]:
        """
        The bundle of specification information (see list below)
        """
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> pulumi.Output[int]:
        return pulumi.get(self, "cpu_count")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The timestamp when the instance was created.
        * `availability_zone`
        * `blueprint_id`
        * `bundle_id`
        * `key_pair_name`
        * `user_data`
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ipv6_address")

    @property
    @pulumi.getter(name="isStaticIp")
    def is_static_ip(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_static_ip")

    @property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of your key pair. Created in the
        Lightsail console (cannot use `ec2.KeyPair` at this time)
        """
        return pulumi.get(self, "key_pair_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Lightsail Instance. Names be unique within each AWS Region in your Lightsail account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[str]:
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> pulumi.Output[str]:
        return pulumi.get(self, "public_ip_address")

    @property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> pulumi.Output[float]:
        return pulumi.get(self, "ram_size")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. To create a key-only tag, use an empty string as the value.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[str]]:
        """
        launch script to configure server with additional user data
        """
        return pulumi.get(self, "user_data")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        return pulumi.get(self, "username")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

