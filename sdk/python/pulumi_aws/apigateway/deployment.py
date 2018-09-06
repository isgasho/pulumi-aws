# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Deployment(pulumi.CustomResource):
    """
    Provides an API Gateway Deployment.
    
    -> **Note:** Depends on having `aws_api_gateway_integration` inside your rest api (which in turn depends on `aws_api_gateway_method`). To avoid race conditions
    you might need to add an explicit `depends_on = ["aws_api_gateway_integration.name"]`.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, rest_api=None, stage_description=None, stage_name=None, variables=None):
        """Create a Deployment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the deployment
        """
        __props__['description'] = description

        if not rest_api:
            raise TypeError('Missing required property rest_api')
        elif not isinstance(rest_api, basestring):
            raise TypeError('Expected property rest_api to be a basestring')
        __self__.rest_api = rest_api
        """
        The ID of the associated REST API
        """
        __props__['restApi'] = rest_api

        if stage_description and not isinstance(stage_description, basestring):
            raise TypeError('Expected property stage_description to be a basestring')
        __self__.stage_description = stage_description
        """
        The description of the stage
        """
        __props__['stageDescription'] = stage_description

        if not stage_name:
            raise TypeError('Missing required property stage_name')
        elif not isinstance(stage_name, basestring):
            raise TypeError('Expected property stage_name to be a basestring')
        __self__.stage_name = stage_name
        """
        The name of the stage
        """
        __props__['stageName'] = stage_name

        if variables and not isinstance(variables, dict):
            raise TypeError('Expected property variables to be a dict')
        __self__.variables = variables
        """
        A map that defines variables for the stage
        """
        __props__['variables'] = variables

        __self__.created_date = pulumi.runtime.UNKNOWN
        """
        The creation date of the deployment
        """
        __self__.execution_arn = pulumi.runtime.UNKNOWN
        """
        The execution ARN to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
        when allowing API Gateway to invoke a Lambda function,
        e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`
        """
        __self__.invoke_url = pulumi.runtime.UNKNOWN
        """
        The URL to invoke the API pointing to the stage,
        e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`
        """

        super(Deployment, __self__).__init__(
            'aws:apigateway/deployment:Deployment',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'createdDate' in outs:
            self.created_date = outs['createdDate']
        if 'description' in outs:
            self.description = outs['description']
        if 'executionArn' in outs:
            self.execution_arn = outs['executionArn']
        if 'invokeUrl' in outs:
            self.invoke_url = outs['invokeUrl']
        if 'restApi' in outs:
            self.rest_api = outs['restApi']
        if 'stageDescription' in outs:
            self.stage_description = outs['stageDescription']
        if 'stageName' in outs:
            self.stage_name = outs['stageName']
        if 'variables' in outs:
            self.variables = outs['variables']
