# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Domain(pulumi.CustomResource):
    """
    Creates a domain resource for the specified domain (e.g., example.com).
    You cannot register a new domain name using Lightsail. You must register
    a domain name using Amazon Route 53 or another domain name registrar.
    If you have already registered your domain, you can enter its name in
    this parameter to manage the DNS records for that domain.
    
    ~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details
    """
    def __init__(__self__, __name__, __opts__=None, domain_name=None):
        """Create a Domain resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not domain_name:
            raise TypeError('Missing required property domain_name')
        elif not isinstance(domain_name, basestring):
            raise TypeError('Expected property domain_name to be a basestring')
        __self__.domain_name = domain_name
        """
        The name of the Lightsail domain to manage
        """
        __props__['domainName'] = domain_name

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the Lightsail domain
        """

        super(Domain, __self__).__init__(
            'aws:lightsail/domain:Domain',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'domainName' in outs:
            self.domain_name = outs['domainName']
