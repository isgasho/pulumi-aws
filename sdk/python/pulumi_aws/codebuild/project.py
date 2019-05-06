# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Project(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the CodeBuild project.
    """
    artifacts: pulumi.Output[dict]
    """
    Information about the project's build output artifacts. Artifact blocks are documented below.
    """
    badge_enabled: pulumi.Output[bool]
    """
    Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
    """
    badge_url: pulumi.Output[str]
    """
    The URL of the build badge when `badge_enabled` is enabled.
    """
    build_timeout: pulumi.Output[float]
    """
    How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
    """
    cache: pulumi.Output[dict]
    """
    Information about the cache storage for the project. Cache blocks are documented below.
    """
    description: pulumi.Output[str]
    """
    A short description of the project.
    """
    encryption_key: pulumi.Output[str]
    """
    The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.
    """
    environment: pulumi.Output[dict]
    """
    Information about the project's build environment. Environment blocks are documented below.
    """
    name: pulumi.Output[str]
    """
    The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
    """
    secondary_artifacts: pulumi.Output[list]
    """
    A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
    """
    secondary_sources: pulumi.Output[list]
    """
    A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
    """
    service_role: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
    """
    source: pulumi.Output[dict]
    """
    Information about the project's input source code. Source blocks are documented below.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    vpc_config: pulumi.Output[dict]
    """
    Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
    """
    def __init__(__self__, resource_name, opts=None, artifacts=None, badge_enabled=None, build_timeout=None, cache=None, description=None, encryption_key=None, environment=None, name=None, secondary_artifacts=None, secondary_sources=None, service_role=None, source=None, tags=None, vpc_config=None, __name__=None, __opts__=None):
        """
        Provides a CodeBuild Project resource. See also the [`aws_codebuild_webhook` resource](https://www.terraform.io/docs/providers/aws/r/codebuild_webhook.html), which manages the webhook to the source (e.g. the "rebuild every time a code change is pushed" option in the CodeBuild web console).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] artifacts: Information about the project's build output artifacts. Artifact blocks are documented below.
        :param pulumi.Input[bool] badge_enabled: Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.
        :param pulumi.Input[float] build_timeout: How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
        :param pulumi.Input[dict] cache: Information about the cache storage for the project. Cache blocks are documented below.
        :param pulumi.Input[str] description: A short description of the project.
        :param pulumi.Input[str] encryption_key: The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.
        :param pulumi.Input[dict] environment: Information about the project's build environment. Environment blocks are documented below.
        :param pulumi.Input[str] name: The name of the project. If `type` is set to `S3`, this is the name of the output artifact object
        :param pulumi.Input[list] secondary_artifacts: A set of secondary artifacts to be used inside the build. Secondary artifacts blocks are documented below.
        :param pulumi.Input[list] secondary_sources: A set of secondary sources to be used inside the build. Secondary sources blocks are documented below.
        :param pulumi.Input[str] service_role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
        :param pulumi.Input[dict] source: Information about the project's input source code. Source blocks are documented below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[dict] vpc_config: Configuration for the builds to run inside a VPC. VPC config blocks are documented below.
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

        if artifacts is None:
            raise TypeError("Missing required property 'artifacts'")
        __props__['artifacts'] = artifacts

        __props__['badge_enabled'] = badge_enabled

        __props__['build_timeout'] = build_timeout

        __props__['cache'] = cache

        __props__['description'] = description

        __props__['encryption_key'] = encryption_key

        if environment is None:
            raise TypeError("Missing required property 'environment'")
        __props__['environment'] = environment

        __props__['name'] = name

        __props__['secondary_artifacts'] = secondary_artifacts

        __props__['secondary_sources'] = secondary_sources

        if service_role is None:
            raise TypeError("Missing required property 'service_role'")
        __props__['service_role'] = service_role

        if source is None:
            raise TypeError("Missing required property 'source'")
        __props__['source'] = source

        __props__['tags'] = tags

        __props__['vpc_config'] = vpc_config

        __props__['arn'] = None
        __props__['badge_url'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(Project, __self__).__init__(
            'aws:codebuild/project:Project',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

