# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Certificate(pulumi.CustomResource):
    """
    Provides a DMS (Data Migration Service) certificate resource. DMS certificates can be created, deleted, and imported.
    
    ~> **Note:** All arguments including the PEM encoded certificate will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    """
    def __init__(__self__, __name__, __opts__=None, certificate_id=None, certificate_pem=None, certificate_wallet=None):
        """Create a Certificate resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not certificate_id:
            raise TypeError('Missing required property certificate_id')
        elif not isinstance(certificate_id, basestring):
            raise TypeError('Expected property certificate_id to be a basestring')
        __self__.certificate_id = certificate_id
        """
        The certificate identifier.
        """
        __props__['certificateId'] = certificate_id

        if certificate_pem and not isinstance(certificate_pem, basestring):
            raise TypeError('Expected property certificate_pem to be a basestring')
        __self__.certificate_pem = certificate_pem
        """
        The contents of the .pem X.509 certificate file for the certificate. Either `certificate_pem` or `certificate_wallet` must be set.
        """
        __props__['certificatePem'] = certificate_pem

        if certificate_wallet and not isinstance(certificate_wallet, basestring):
            raise TypeError('Expected property certificate_wallet to be a basestring')
        __self__.certificate_wallet = certificate_wallet
        """
        The contents of the Oracle Wallet certificate for use with SSL. Either `certificate_pem` or `certificate_wallet` must be set.
        """
        __props__['certificateWallet'] = certificate_wallet

        __self__.certificate_arn = pulumi.runtime.UNKNOWN
        """
        The Amazon Resource Name (ARN) for the certificate.
        """

        super(Certificate, __self__).__init__(
            'aws:dms/certificate:Certificate',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'certificateArn' in outs:
            self.certificate_arn = outs['certificateArn']
        if 'certificateId' in outs:
            self.certificate_id = outs['certificateId']
        if 'certificatePem' in outs:
            self.certificate_pem = outs['certificatePem']
        if 'certificateWallet' in outs:
            self.certificate_wallet = outs['certificateWallet']
