# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GameSessionQueue(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Game Session Queue ARN.
    """
    destinations: pulumi.Output[list]
    """
    List of fleet/alias ARNs used by session queue for placing game sessions.
    """
    name: pulumi.Output[str]
    """
    Name of the session queue.
    """
    player_latency_policies: pulumi.Output[list]
    """
    One or more policies used to choose fleet based on player latency. See below.
    """
    timeout_in_seconds: pulumi.Output[float]
    """
    Maximum time a game session request can remain in the queue.
    """
    def __init__(__self__, resource_name, opts=None, destinations=None, name=None, player_latency_policies=None, timeout_in_seconds=None, __name__=None, __opts__=None):
        """
        Provides an Gamelift Game Session Queue resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] destinations: List of fleet/alias ARNs used by session queue for placing game sessions.
        :param pulumi.Input[str] name: Name of the session queue.
        :param pulumi.Input[list] player_latency_policies: One or more policies used to choose fleet based on player latency. See below.
        :param pulumi.Input[float] timeout_in_seconds: Maximum time a game session request can remain in the queue.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['destinations'] = destinations

        __props__['name'] = name

        __props__['player_latency_policies'] = player_latency_policies

        __props__['timeout_in_seconds'] = timeout_in_seconds

        __props__['arn'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(GameSessionQueue, __self__).__init__(
            'aws:gamelift/gameSessionQueue:GameSessionQueue',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

