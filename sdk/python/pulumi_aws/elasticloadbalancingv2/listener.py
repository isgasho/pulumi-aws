# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Listener(pulumi.CustomResource):
    """
    Provides a Load Balancer Listener resource.
    
    ~> **Note:** `aws_alb_listener` is known as `aws_lb_listener`. The functionality is identical.
    """
    def __init__(__self__, __name__, __opts__=None, certificate_arn=None, default_action=None, load_balancer_arn=None, port=None, protocol=None, ssl_policy=None):
        """Create a Listener resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if certificate_arn and not isinstance(certificate_arn, basestring):
            raise TypeError('Expected property certificate_arn to be a basestring')
        __self__.certificate_arn = certificate_arn
        """
        The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the [`aws_lb_listener_certificate` resource](https://www.terraform.io/docs/providers/aws/r/lb_listener_certificate.html).
        """
        __props__['certificateArn'] = certificate_arn

        if not default_action:
            raise TypeError('Missing required property default_action')
        elif not isinstance(default_action, dict):
            raise TypeError('Expected property default_action to be a dict')
        __self__.default_action = default_action
        """
        An Action block. Action blocks are documented below.
        """
        __props__['defaultAction'] = default_action

        if not load_balancer_arn:
            raise TypeError('Missing required property load_balancer_arn')
        elif not isinstance(load_balancer_arn, basestring):
            raise TypeError('Expected property load_balancer_arn to be a basestring')
        __self__.load_balancer_arn = load_balancer_arn
        """
        The ARN of the load balancer.
        """
        __props__['loadBalancerArn'] = load_balancer_arn

        if not port:
            raise TypeError('Missing required property port')
        elif not isinstance(port, int):
            raise TypeError('Expected property port to be a int')
        __self__.port = port
        """
        The port on which the load balancer is listening.
        """
        __props__['port'] = port

        if protocol and not isinstance(protocol, basestring):
            raise TypeError('Expected property protocol to be a basestring')
        __self__.protocol = protocol
        """
        The protocol for connections from clients to the load balancer. Valid values are `TCP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.
        """
        __props__['protocol'] = protocol

        if ssl_policy and not isinstance(ssl_policy, basestring):
            raise TypeError('Expected property ssl_policy to be a basestring')
        __self__.ssl_policy = ssl_policy
        """
        The name of the SSL Policy for the listener. Required if `protocol` is `HTTPS`.
        """
        __props__['sslPolicy'] = ssl_policy

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the listener (matches `id`)
        """

        super(Listener, __self__).__init__(
            'aws:elasticloadbalancingv2/listener:Listener',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'certificateArn' in outs:
            self.certificate_arn = outs['certificateArn']
        if 'defaultAction' in outs:
            self.default_action = outs['defaultAction']
        if 'loadBalancerArn' in outs:
            self.load_balancer_arn = outs['loadBalancerArn']
        if 'port' in outs:
            self.port = outs['port']
        if 'protocol' in outs:
            self.protocol = outs['protocol']
        if 'sslPolicy' in outs:
            self.ssl_policy = outs['sslPolicy']
