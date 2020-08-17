# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'AssociationOutputLocation',
    'AssociationTarget',
    'DocumentAttachmentsSource',
    'DocumentParameter',
    'MaintenanceWindowTargetTarget',
    'MaintenanceWindowTaskLoggingInfo',
    'MaintenanceWindowTaskTarget',
    'MaintenanceWindowTaskTaskInvocationParameters',
    'MaintenanceWindowTaskTaskInvocationParametersAutomationParameters',
    'MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter',
    'MaintenanceWindowTaskTaskInvocationParametersLambdaParameters',
    'MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters',
    'MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig',
    'MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter',
    'MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters',
    'MaintenanceWindowTaskTaskParameter',
    'PatchBaselineApprovalRule',
    'PatchBaselineApprovalRulePatchFilter',
    'PatchBaselineGlobalFilter',
    'ResourceDataSyncS3Destination',
]

@pulumi.output_type
class AssociationOutputLocation(dict):
    def __init__(__self__, *,
                 s3_bucket_name: str,
                 s3_key_prefix: Optional[str] = None):
        """
        :param str s3_bucket_name: The S3 bucket name.
        :param str s3_key_prefix: The S3 bucket prefix. Results stored in the root if not configured.
        """
        pulumi.set(__self__, "s3_bucket_name", s3_bucket_name)
        if s3_key_prefix is not None:
            pulumi.set(__self__, "s3_key_prefix", s3_key_prefix)

    @property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> str:
        """
        The S3 bucket name.
        """
        return pulumi.get(self, "s3_bucket_name")

    @property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> Optional[str]:
        """
        The S3 bucket prefix. Results stored in the root if not configured.
        """
        return pulumi.get(self, "s3_key_prefix")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AssociationTarget(dict):
    def __init__(__self__, *,
                 key: str,
                 values: List[str]):
        """
        :param str key: Either `InstanceIds` or `tag:Tag Name` to specify an EC2 tag.
        :param List[str] values: A list of instance IDs or tag values. AWS currently limits this list size to one value.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Either `InstanceIds` or `tag:Tag Name` to specify an EC2 tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        A list of instance IDs or tag values. AWS currently limits this list size to one value.
        """
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DocumentAttachmentsSource(dict):
    def __init__(__self__, *,
                 key: str,
                 values: List[str],
                 name: Optional[str] = None):
        """
        :param str key: The key describing the location of an attachment to a document. Valid key types include: `SourceUrl` and `S3FileUrl`
        :param List[str] values: The value describing the location of an attachment to a document
        :param str name: The name of the document attachment file
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key describing the location of an attachment to a document. Valid key types include: `SourceUrl` and `S3FileUrl`
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        The value describing the location of an attachment to a document
        """
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the document attachment file
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DocumentParameter(dict):
    def __init__(__self__, *,
                 default_value: Optional[str] = None,
                 description: Optional[str] = None,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str description: The description of the document.
        :param str name: The name of the document.
        """
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[str]:
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the document.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the document.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTargetTarget(dict):
    def __init__(__self__, *,
                 key: str,
                 values: List[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskLoggingInfo(dict):
    def __init__(__self__, *,
                 s3_bucket_name: str,
                 s3_region: str,
                 s3_bucket_prefix: Optional[str] = None):
        pulumi.set(__self__, "s3_bucket_name", s3_bucket_name)
        pulumi.set(__self__, "s3_region", s3_region)
        if s3_bucket_prefix is not None:
            pulumi.set(__self__, "s3_bucket_prefix", s3_bucket_prefix)

    @property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> str:
        return pulumi.get(self, "s3_bucket_name")

    @property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> str:
        return pulumi.get(self, "s3_region")

    @property
    @pulumi.getter(name="s3BucketPrefix")
    def s3_bucket_prefix(self) -> Optional[str]:
        return pulumi.get(self, "s3_bucket_prefix")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTarget(dict):
    def __init__(__self__, *,
                 key: str,
                 values: List[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParameters(dict):
    def __init__(__self__, *,
                 automation_parameters: Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParameters'] = None,
                 lambda_parameters: Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersLambdaParameters'] = None,
                 run_command_parameters: Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters'] = None,
                 step_functions_parameters: Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters'] = None):
        """
        :param 'MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgs' automation_parameters: The parameters for an AUTOMATION task type. Documented below.
        :param 'MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgs' lambda_parameters: The parameters for a LAMBDA task type. Documented below.
        :param 'MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgs' run_command_parameters: The parameters for a RUN_COMMAND task type. Documented below.
        :param 'MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgs' step_functions_parameters: The parameters for a STEP_FUNCTIONS task type. Documented below.
        """
        if automation_parameters is not None:
            pulumi.set(__self__, "automation_parameters", automation_parameters)
        if lambda_parameters is not None:
            pulumi.set(__self__, "lambda_parameters", lambda_parameters)
        if run_command_parameters is not None:
            pulumi.set(__self__, "run_command_parameters", run_command_parameters)
        if step_functions_parameters is not None:
            pulumi.set(__self__, "step_functions_parameters", step_functions_parameters)

    @property
    @pulumi.getter(name="automationParameters")
    def automation_parameters(self) -> Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParameters']:
        """
        The parameters for an AUTOMATION task type. Documented below.
        """
        return pulumi.get(self, "automation_parameters")

    @property
    @pulumi.getter(name="lambdaParameters")
    def lambda_parameters(self) -> Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersLambdaParameters']:
        """
        The parameters for a LAMBDA task type. Documented below.
        """
        return pulumi.get(self, "lambda_parameters")

    @property
    @pulumi.getter(name="runCommandParameters")
    def run_command_parameters(self) -> Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters']:
        """
        The parameters for a RUN_COMMAND task type. Documented below.
        """
        return pulumi.get(self, "run_command_parameters")

    @property
    @pulumi.getter(name="stepFunctionsParameters")
    def step_functions_parameters(self) -> Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters']:
        """
        The parameters for a STEP_FUNCTIONS task type. Documented below.
        """
        return pulumi.get(self, "step_functions_parameters")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersAutomationParameters(dict):
    def __init__(__self__, *,
                 document_version: Optional[str] = None,
                 parameters: Optional[List['outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter']] = None):
        """
        :param str document_version: The version of an Automation document to use during task execution.
        :param List['MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgs'] parameters: The parameters for the RUN_COMMAND task execution. Documented below.
        """
        if document_version is not None:
            pulumi.set(__self__, "document_version", document_version)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[str]:
        """
        The version of an Automation document to use during task execution.
        """
        return pulumi.get(self, "document_version")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[List['outputs.MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter']]:
        """
        The parameters for the RUN_COMMAND task execution. Documented below.
        """
        return pulumi.get(self, "parameters")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter(dict):
    def __init__(__self__, *,
                 name: str,
                 values: List[str]):
        """
        :param str name: The parameter name.
        :param List[str] values: The array of strings.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The parameter name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        The array of strings.
        """
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersLambdaParameters(dict):
    def __init__(__self__, *,
                 client_context: Optional[str] = None,
                 payload: Optional[str] = None,
                 qualifier: Optional[str] = None):
        """
        :param str client_context: Pass client-specific information to the Lambda function that you are invoking.
        :param str payload: JSON to provide to your Lambda function as input.
        :param str qualifier: Specify a Lambda function version or alias name.
        """
        if client_context is not None:
            pulumi.set(__self__, "client_context", client_context)
        if payload is not None:
            pulumi.set(__self__, "payload", payload)
        if qualifier is not None:
            pulumi.set(__self__, "qualifier", qualifier)

    @property
    @pulumi.getter(name="clientContext")
    def client_context(self) -> Optional[str]:
        """
        Pass client-specific information to the Lambda function that you are invoking.
        """
        return pulumi.get(self, "client_context")

    @property
    @pulumi.getter
    def payload(self) -> Optional[str]:
        """
        JSON to provide to your Lambda function as input.
        """
        return pulumi.get(self, "payload")

    @property
    @pulumi.getter
    def qualifier(self) -> Optional[str]:
        """
        Specify a Lambda function version or alias name.
        """
        return pulumi.get(self, "qualifier")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters(dict):
    def __init__(__self__, *,
                 comment: Optional[str] = None,
                 document_hash: Optional[str] = None,
                 document_hash_type: Optional[str] = None,
                 notification_config: Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig'] = None,
                 output_s3_bucket: Optional[str] = None,
                 output_s3_key_prefix: Optional[str] = None,
                 parameters: Optional[List['outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter']] = None,
                 service_role_arn: Optional[str] = None,
                 timeout_seconds: Optional[float] = None):
        """
        :param str comment: Information about the command(s) to execute.
        :param str document_hash: The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
        :param str document_hash_type: SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: `Sha256` and `Sha1`
        :param 'MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgs' notification_config: Configurations for sending notifications about command status changes on a per-instance basis. Documented below.
        :param str output_s3_bucket: The name of the Amazon S3 bucket.
        :param str output_s3_key_prefix: The Amazon S3 bucket subfolder.
        :param List['MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgs'] parameters: The parameters for the RUN_COMMAND task execution. Documented below.
        :param str service_role_arn: The IAM service role to assume during task execution.
        :param float timeout_seconds: If this time is reached and the command has not already started executing, it doesn't run.
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if document_hash is not None:
            pulumi.set(__self__, "document_hash", document_hash)
        if document_hash_type is not None:
            pulumi.set(__self__, "document_hash_type", document_hash_type)
        if notification_config is not None:
            pulumi.set(__self__, "notification_config", notification_config)
        if output_s3_bucket is not None:
            pulumi.set(__self__, "output_s3_bucket", output_s3_bucket)
        if output_s3_key_prefix is not None:
            pulumi.set(__self__, "output_s3_key_prefix", output_s3_key_prefix)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if service_role_arn is not None:
            pulumi.set(__self__, "service_role_arn", service_role_arn)
        if timeout_seconds is not None:
            pulumi.set(__self__, "timeout_seconds", timeout_seconds)

    @property
    @pulumi.getter
    def comment(self) -> Optional[str]:
        """
        Information about the command(s) to execute.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="documentHash")
    def document_hash(self) -> Optional[str]:
        """
        The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
        """
        return pulumi.get(self, "document_hash")

    @property
    @pulumi.getter(name="documentHashType")
    def document_hash_type(self) -> Optional[str]:
        """
        SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: `Sha256` and `Sha1`
        """
        return pulumi.get(self, "document_hash_type")

    @property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional['outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig']:
        """
        Configurations for sending notifications about command status changes on a per-instance basis. Documented below.
        """
        return pulumi.get(self, "notification_config")

    @property
    @pulumi.getter(name="outputS3Bucket")
    def output_s3_bucket(self) -> Optional[str]:
        """
        The name of the Amazon S3 bucket.
        """
        return pulumi.get(self, "output_s3_bucket")

    @property
    @pulumi.getter(name="outputS3KeyPrefix")
    def output_s3_key_prefix(self) -> Optional[str]:
        """
        The Amazon S3 bucket subfolder.
        """
        return pulumi.get(self, "output_s3_key_prefix")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[List['outputs.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter']]:
        """
        The parameters for the RUN_COMMAND task execution. Documented below.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> Optional[str]:
        """
        The IAM service role to assume during task execution.
        """
        return pulumi.get(self, "service_role_arn")

    @property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[float]:
        """
        If this time is reached and the command has not already started executing, it doesn't run.
        """
        return pulumi.get(self, "timeout_seconds")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig(dict):
    def __init__(__self__, *,
                 notification_arn: Optional[str] = None,
                 notification_events: Optional[List[str]] = None,
                 notification_type: Optional[str] = None):
        """
        :param str notification_arn: An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        :param List[str] notification_events: The different events for which you can receive notifications. Valid values: `All`, `InProgress`, `Success`, `TimedOut`, `Cancelled`, and `Failed`
        :param str notification_type: When specified with `Command`, receive notification when the status of a command changes. When specified with `Invocation`, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: `Command` and `Invocation`
        """
        if notification_arn is not None:
            pulumi.set(__self__, "notification_arn", notification_arn)
        if notification_events is not None:
            pulumi.set(__self__, "notification_events", notification_events)
        if notification_type is not None:
            pulumi.set(__self__, "notification_type", notification_type)

    @property
    @pulumi.getter(name="notificationArn")
    def notification_arn(self) -> Optional[str]:
        """
        An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
        """
        return pulumi.get(self, "notification_arn")

    @property
    @pulumi.getter(name="notificationEvents")
    def notification_events(self) -> Optional[List[str]]:
        """
        The different events for which you can receive notifications. Valid values: `All`, `InProgress`, `Success`, `TimedOut`, `Cancelled`, and `Failed`
        """
        return pulumi.get(self, "notification_events")

    @property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[str]:
        """
        When specified with `Command`, receive notification when the status of a command changes. When specified with `Invocation`, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: `Command` and `Invocation`
        """
        return pulumi.get(self, "notification_type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter(dict):
    def __init__(__self__, *,
                 name: str,
                 values: List[str]):
        """
        :param str name: The parameter name.
        :param List[str] values: The array of strings.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The parameter name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        """
        The array of strings.
        """
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters(dict):
    def __init__(__self__, *,
                 input: Optional[str] = None,
                 name: Optional[str] = None):
        """
        :param str input: The inputs for the STEP_FUNCTION task.
        :param str name: The name of the STEP_FUNCTION task.
        """
        if input is not None:
            pulumi.set(__self__, "input", input)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def input(self) -> Optional[str]:
        """
        The inputs for the STEP_FUNCTION task.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the STEP_FUNCTION task.
        """
        return pulumi.get(self, "name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MaintenanceWindowTaskTaskParameter(dict):
    def __init__(__self__, *,
                 name: str,
                 values: List[str]):
        """
        :param str name: The name of the maintenance window task.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the maintenance window task.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PatchBaselineApprovalRule(dict):
    def __init__(__self__, *,
                 approve_after_days: float,
                 patch_filters: List['outputs.PatchBaselineApprovalRulePatchFilter'],
                 compliance_level: Optional[str] = None,
                 enable_non_security: Optional[bool] = None):
        """
        :param float approve_after_days: The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100.
        :param List['PatchBaselineApprovalRulePatchFilterArgs'] patch_filters: The patch filter group that defines the criteria for the rule. Up to 5 patch filters can be specified per approval rule using Key/Value pairs. Valid Keys are `PATCH_SET | PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.
        :param str compliance_level: Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.
        :param bool enable_non_security: Boolean enabling the application of non-security updates. The default value is 'false'. Valid for Linux instances only.
        """
        pulumi.set(__self__, "approve_after_days", approve_after_days)
        pulumi.set(__self__, "patch_filters", patch_filters)
        if compliance_level is not None:
            pulumi.set(__self__, "compliance_level", compliance_level)
        if enable_non_security is not None:
            pulumi.set(__self__, "enable_non_security", enable_non_security)

    @property
    @pulumi.getter(name="approveAfterDays")
    def approve_after_days(self) -> float:
        """
        The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100.
        """
        return pulumi.get(self, "approve_after_days")

    @property
    @pulumi.getter(name="patchFilters")
    def patch_filters(self) -> List['outputs.PatchBaselineApprovalRulePatchFilter']:
        """
        The patch filter group that defines the criteria for the rule. Up to 5 patch filters can be specified per approval rule using Key/Value pairs. Valid Keys are `PATCH_SET | PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.
        """
        return pulumi.get(self, "patch_filters")

    @property
    @pulumi.getter(name="complianceLevel")
    def compliance_level(self) -> Optional[str]:
        """
        Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.
        """
        return pulumi.get(self, "compliance_level")

    @property
    @pulumi.getter(name="enableNonSecurity")
    def enable_non_security(self) -> Optional[bool]:
        """
        Boolean enabling the application of non-security updates. The default value is 'false'. Valid for Linux instances only.
        """
        return pulumi.get(self, "enable_non_security")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PatchBaselineApprovalRulePatchFilter(dict):
    def __init__(__self__, *,
                 key: str,
                 values: List[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PatchBaselineGlobalFilter(dict):
    def __init__(__self__, *,
                 key: str,
                 values: List[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> List[str]:
        return pulumi.get(self, "values")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ResourceDataSyncS3Destination(dict):
    def __init__(__self__, *,
                 bucket_name: str,
                 region: str,
                 kms_key_arn: Optional[str] = None,
                 prefix: Optional[str] = None,
                 sync_format: Optional[str] = None):
        """
        :param str bucket_name: Name of S3 bucket where the aggregated data is stored.
        :param str region: Region with the bucket targeted by the Resource Data Sync.
        :param str kms_key_arn: ARN of an encryption key for a destination in Amazon S3.
        :param str prefix: Prefix for the bucket.
        :param str sync_format: A supported sync format. Only JsonSerDe is currently supported. Defaults to JsonSerDe.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "region", region)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if sync_format is not None:
            pulumi.set(__self__, "sync_format", sync_format)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        Name of S3 bucket where the aggregated data is stored.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        Region with the bucket targeted by the Resource Data Sync.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[str]:
        """
        ARN of an encryption key for a destination in Amazon S3.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        Prefix for the bucket.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="syncFormat")
    def sync_format(self) -> Optional[str]:
        """
        A supported sync format. Only JsonSerDe is currently supported. Defaults to JsonSerDe.
        """
        return pulumi.get(self, "sync_format")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

