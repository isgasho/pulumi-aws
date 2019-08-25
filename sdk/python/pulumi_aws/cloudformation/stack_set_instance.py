# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class StackSetInstance(pulumi.CustomResource):
    account_id: pulumi.Output[str]
    """
    Target AWS Account ID to create a Stack based on the Stack Set. Defaults to current account.
    """
    parameter_overrides: pulumi.Output[dict]
    """
    Key-value map of input parameters to override from the Stack Set for this Instance.
    """
    region: pulumi.Output[str]
    """
    Target AWS Region to create a Stack based on the Stack Set. Defaults to current region.
    """
    retain_stack: pulumi.Output[bool]
    """
    During resource destroy, remove Instance from Stack Set while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new Stack Set. Defaults to `false`.
    """
    stack_id: pulumi.Output[str]
    """
    Stack identifier
    """
    stack_set_name: pulumi.Output[str]
    """
    Name of the Stack Set.
    """
    def __init__(__self__, resource_name, opts=None, account_id=None, parameter_overrides=None, region=None, retain_stack=None, stack_set_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a CloudFormation Stack Set Instance. Instances are managed in the account and region of the Stack Set after the target account permissions have been configured. Additional information about Stack Sets can be found in the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).
        
        > **NOTE:** All target accounts must have an IAM Role created that matches the name of the execution role configured in the Stack Set (the `execution_role_name` argument in the `cloudformation.StackSet` resource) in a trust relationship with the administrative account or administration IAM Role. The execution role must have appropriate permissions to manage resources defined in the template along with those required for Stack Sets to operate. See the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) for more details.
        
        > **NOTE:** To retain the Stack during resource destroy, ensure `retain_stack` has been set to `true` in the state first. This must be completed _before_ a deployment that would destroy the resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Target AWS Account ID to create a Stack based on the Stack Set. Defaults to current account.
        :param pulumi.Input[dict] parameter_overrides: Key-value map of input parameters to override from the Stack Set for this Instance.
        :param pulumi.Input[str] region: Target AWS Region to create a Stack based on the Stack Set. Defaults to current region.
        :param pulumi.Input[bool] retain_stack: During resource destroy, remove Instance from Stack Set while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new Stack Set. Defaults to `false`.
        :param pulumi.Input[str] stack_set_name: Name of the Stack Set.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set_instance.html.markdown.
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

            __props__['account_id'] = account_id
            __props__['parameter_overrides'] = parameter_overrides
            __props__['region'] = region
            __props__['retain_stack'] = retain_stack
            if stack_set_name is None:
                raise TypeError("Missing required property 'stack_set_name'")
            __props__['stack_set_name'] = stack_set_name
            __props__['stack_id'] = None
        super(StackSetInstance, __self__).__init__(
            'aws:cloudformation/stackSetInstance:StackSetInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, account_id=None, parameter_overrides=None, region=None, retain_stack=None, stack_id=None, stack_set_name=None):
        """
        Get an existing StackSetInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Target AWS Account ID to create a Stack based on the Stack Set. Defaults to current account.
        :param pulumi.Input[dict] parameter_overrides: Key-value map of input parameters to override from the Stack Set for this Instance.
        :param pulumi.Input[str] region: Target AWS Region to create a Stack based on the Stack Set. Defaults to current region.
        :param pulumi.Input[bool] retain_stack: During resource destroy, remove Instance from Stack Set while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new Stack Set. Defaults to `false`.
        :param pulumi.Input[str] stack_id: Stack identifier
        :param pulumi.Input[str] stack_set_name: Name of the Stack Set.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set_instance.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["account_id"] = account_id
        __props__["parameter_overrides"] = parameter_overrides
        __props__["region"] = region
        __props__["retain_stack"] = retain_stack
        __props__["stack_id"] = stack_id
        __props__["stack_set_name"] = stack_set_name
        return StackSetInstance(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

