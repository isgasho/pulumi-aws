# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities

class GetAutoscalingGroupsResult(object):
    """
    A collection of values returned by getAutoscalingGroups.
    """
    def __init__(__self__, names=None, id=None):
        if names and not isinstance(names, list):
            raise TypeError('Expected argument names to be a list')
        __self__.names = names
        """
        A list of the Autoscaling Groups in the current region.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_autoscaling_groups(filters=None):
    """
    The Autoscaling Groups data source allows access to the list of AWS
    ASGs within a specific region. This will allow you to pass a list of AutoScaling Groups to other resources.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __ret__ = pulumi.runtime.invoke('aws:index/getAutoscalingGroups:getAutoscalingGroups', __args__)

    return GetAutoscalingGroupsResult(
        names=__ret__.get('names'),
        id=__ret__.get('id'))
