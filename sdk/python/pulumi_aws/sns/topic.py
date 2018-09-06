# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Topic(pulumi.CustomResource):
    """
    Provides an SNS topic resource
    """
    def __init__(__self__, __name__, __opts__=None, application_failure_feedback_role_arn=None, application_success_feedback_role_arn=None, application_success_feedback_sample_rate=None, delivery_policy=None, display_name=None, http_failure_feedback_role_arn=None, http_success_feedback_role_arn=None, http_success_feedback_sample_rate=None, lambda_failure_feedback_role_arn=None, lambda_success_feedback_role_arn=None, lambda_success_feedback_sample_rate=None, name=None, name_prefix=None, policy=None, sqs_failure_feedback_role_arn=None, sqs_success_feedback_role_arn=None, sqs_success_feedback_sample_rate=None):
        """Create a Topic resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if application_failure_feedback_role_arn and not isinstance(application_failure_feedback_role_arn, basestring):
            raise TypeError('Expected property application_failure_feedback_role_arn to be a basestring')
        __self__.application_failure_feedback_role_arn = application_failure_feedback_role_arn
        """
        IAM role for failure feedback
        """
        __props__['applicationFailureFeedbackRoleArn'] = application_failure_feedback_role_arn

        if application_success_feedback_role_arn and not isinstance(application_success_feedback_role_arn, basestring):
            raise TypeError('Expected property application_success_feedback_role_arn to be a basestring')
        __self__.application_success_feedback_role_arn = application_success_feedback_role_arn
        """
        The IAM role permitted to receive success feedback for this topic
        """
        __props__['applicationSuccessFeedbackRoleArn'] = application_success_feedback_role_arn

        if application_success_feedback_sample_rate and not isinstance(application_success_feedback_sample_rate, int):
            raise TypeError('Expected property application_success_feedback_sample_rate to be a int')
        __self__.application_success_feedback_sample_rate = application_success_feedback_sample_rate
        """
        Percentage of success to sample
        """
        __props__['applicationSuccessFeedbackSampleRate'] = application_success_feedback_sample_rate

        if delivery_policy and not isinstance(delivery_policy, basestring):
            raise TypeError('Expected property delivery_policy to be a basestring')
        __self__.delivery_policy = delivery_policy
        """
        The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
        """
        __props__['deliveryPolicy'] = delivery_policy

        if display_name and not isinstance(display_name, basestring):
            raise TypeError('Expected property display_name to be a basestring')
        __self__.display_name = display_name
        """
        The display name for the SNS topic
        """
        __props__['displayName'] = display_name

        if http_failure_feedback_role_arn and not isinstance(http_failure_feedback_role_arn, basestring):
            raise TypeError('Expected property http_failure_feedback_role_arn to be a basestring')
        __self__.http_failure_feedback_role_arn = http_failure_feedback_role_arn
        """
        IAM role for failure feedback
        """
        __props__['httpFailureFeedbackRoleArn'] = http_failure_feedback_role_arn

        if http_success_feedback_role_arn and not isinstance(http_success_feedback_role_arn, basestring):
            raise TypeError('Expected property http_success_feedback_role_arn to be a basestring')
        __self__.http_success_feedback_role_arn = http_success_feedback_role_arn
        """
        The IAM role permitted to receive success feedback for this topic
        """
        __props__['httpSuccessFeedbackRoleArn'] = http_success_feedback_role_arn

        if http_success_feedback_sample_rate and not isinstance(http_success_feedback_sample_rate, int):
            raise TypeError('Expected property http_success_feedback_sample_rate to be a int')
        __self__.http_success_feedback_sample_rate = http_success_feedback_sample_rate
        """
        Percentage of success to sample
        """
        __props__['httpSuccessFeedbackSampleRate'] = http_success_feedback_sample_rate

        if lambda_failure_feedback_role_arn and not isinstance(lambda_failure_feedback_role_arn, basestring):
            raise TypeError('Expected property lambda_failure_feedback_role_arn to be a basestring')
        __self__.lambda_failure_feedback_role_arn = lambda_failure_feedback_role_arn
        """
        IAM role for failure feedback
        """
        __props__['lambdaFailureFeedbackRoleArn'] = lambda_failure_feedback_role_arn

        if lambda_success_feedback_role_arn and not isinstance(lambda_success_feedback_role_arn, basestring):
            raise TypeError('Expected property lambda_success_feedback_role_arn to be a basestring')
        __self__.lambda_success_feedback_role_arn = lambda_success_feedback_role_arn
        """
        The IAM role permitted to receive success feedback for this topic
        """
        __props__['lambdaSuccessFeedbackRoleArn'] = lambda_success_feedback_role_arn

        if lambda_success_feedback_sample_rate and not isinstance(lambda_success_feedback_sample_rate, int):
            raise TypeError('Expected property lambda_success_feedback_sample_rate to be a int')
        __self__.lambda_success_feedback_sample_rate = lambda_success_feedback_sample_rate
        """
        Percentage of success to sample
        """
        __props__['lambdaSuccessFeedbackSampleRate'] = lambda_success_feedback_sample_rate

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The friendly name for the SNS topic. By default generated by Terraform.
        """
        __props__['name'] = name

        if name_prefix and not isinstance(name_prefix, basestring):
            raise TypeError('Expected property name_prefix to be a basestring')
        __self__.name_prefix = name_prefix
        """
        The friendly name for the SNS topic. Conflicts with `name`.
        """
        __props__['namePrefix'] = name_prefix

        if policy and not isinstance(policy, basestring):
            raise TypeError('Expected property policy to be a basestring')
        __self__.policy = policy
        """
        The fully-formed AWS policy as JSON
        """
        __props__['policy'] = policy

        if sqs_failure_feedback_role_arn and not isinstance(sqs_failure_feedback_role_arn, basestring):
            raise TypeError('Expected property sqs_failure_feedback_role_arn to be a basestring')
        __self__.sqs_failure_feedback_role_arn = sqs_failure_feedback_role_arn
        """
        IAM role for failure feedback
        """
        __props__['sqsFailureFeedbackRoleArn'] = sqs_failure_feedback_role_arn

        if sqs_success_feedback_role_arn and not isinstance(sqs_success_feedback_role_arn, basestring):
            raise TypeError('Expected property sqs_success_feedback_role_arn to be a basestring')
        __self__.sqs_success_feedback_role_arn = sqs_success_feedback_role_arn
        """
        The IAM role permitted to receive success feedback for this topic
        """
        __props__['sqsSuccessFeedbackRoleArn'] = sqs_success_feedback_role_arn

        if sqs_success_feedback_sample_rate and not isinstance(sqs_success_feedback_sample_rate, int):
            raise TypeError('Expected property sqs_success_feedback_sample_rate to be a int')
        __self__.sqs_success_feedback_sample_rate = sqs_success_feedback_sample_rate
        """
        Percentage of success to sample
        """
        __props__['sqsSuccessFeedbackSampleRate'] = sqs_success_feedback_sample_rate

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the SNS topic, as a more obvious property (clone of id)
        """

        super(Topic, __self__).__init__(
            'aws:sns/topic:Topic',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'applicationFailureFeedbackRoleArn' in outs:
            self.application_failure_feedback_role_arn = outs['applicationFailureFeedbackRoleArn']
        if 'applicationSuccessFeedbackRoleArn' in outs:
            self.application_success_feedback_role_arn = outs['applicationSuccessFeedbackRoleArn']
        if 'applicationSuccessFeedbackSampleRate' in outs:
            self.application_success_feedback_sample_rate = outs['applicationSuccessFeedbackSampleRate']
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'deliveryPolicy' in outs:
            self.delivery_policy = outs['deliveryPolicy']
        if 'displayName' in outs:
            self.display_name = outs['displayName']
        if 'httpFailureFeedbackRoleArn' in outs:
            self.http_failure_feedback_role_arn = outs['httpFailureFeedbackRoleArn']
        if 'httpSuccessFeedbackRoleArn' in outs:
            self.http_success_feedback_role_arn = outs['httpSuccessFeedbackRoleArn']
        if 'httpSuccessFeedbackSampleRate' in outs:
            self.http_success_feedback_sample_rate = outs['httpSuccessFeedbackSampleRate']
        if 'lambdaFailureFeedbackRoleArn' in outs:
            self.lambda_failure_feedback_role_arn = outs['lambdaFailureFeedbackRoleArn']
        if 'lambdaSuccessFeedbackRoleArn' in outs:
            self.lambda_success_feedback_role_arn = outs['lambdaSuccessFeedbackRoleArn']
        if 'lambdaSuccessFeedbackSampleRate' in outs:
            self.lambda_success_feedback_sample_rate = outs['lambdaSuccessFeedbackSampleRate']
        if 'name' in outs:
            self.name = outs['name']
        if 'namePrefix' in outs:
            self.name_prefix = outs['namePrefix']
        if 'policy' in outs:
            self.policy = outs['policy']
        if 'sqsFailureFeedbackRoleArn' in outs:
            self.sqs_failure_feedback_role_arn = outs['sqsFailureFeedbackRoleArn']
        if 'sqsSuccessFeedbackRoleArn' in outs:
            self.sqs_success_feedback_role_arn = outs['sqsSuccessFeedbackRoleArn']
        if 'sqsSuccessFeedbackSampleRate' in outs:
            self.sqs_success_feedback_sample_rate = outs['sqsSuccessFeedbackSampleRate']
