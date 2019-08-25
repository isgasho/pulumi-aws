# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Vault(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the vault.
    """
    kms_key_arn: pulumi.Output[str]
    """
    The server-side encryption key that is used to protect your backups.
    """
    name: pulumi.Output[str]
    """
    Name of the backup vault to create.
    """
    recovery_points: pulumi.Output[float]
    """
    The number of recovery points that are stored in a backup vault.
    """
    tags: pulumi.Output[dict]
    """
    Metadata that you can assign to help organize the resources that you create.
    """
    def __init__(__self__, resource_name, opts=None, kms_key_arn=None, name=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an AWS Backup vault resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kms_key_arn: The server-side encryption key that is used to protect your backups.
        :param pulumi.Input[str] name: Name of the backup vault to create.
        :param pulumi.Input[dict] tags: Metadata that you can assign to help organize the resources that you create.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/backup_vault.html.markdown.
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

            __props__['kms_key_arn'] = kms_key_arn
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['recovery_points'] = None
        super(Vault, __self__).__init__(
            'aws:backup/vault:Vault',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, kms_key_arn=None, name=None, recovery_points=None, tags=None):
        """
        Get an existing Vault resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the vault.
        :param pulumi.Input[str] kms_key_arn: The server-side encryption key that is used to protect your backups.
        :param pulumi.Input[str] name: Name of the backup vault to create.
        :param pulumi.Input[float] recovery_points: The number of recovery points that are stored in a backup vault.
        :param pulumi.Input[dict] tags: Metadata that you can assign to help organize the resources that you create.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/backup_vault.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["arn"] = arn
        __props__["kms_key_arn"] = kms_key_arn
        __props__["name"] = name
        __props__["recovery_points"] = recovery_points
        __props__["tags"] = tags
        return Vault(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

