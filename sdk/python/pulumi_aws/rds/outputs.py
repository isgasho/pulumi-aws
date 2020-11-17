# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'ClusterParameterGroupParameter',
    'ClusterRestoreToPointInTime',
    'ClusterS3Import',
    'ClusterScalingConfiguration',
    'GlobalClusterGlobalClusterMember',
    'InstanceRestoreToPointInTime',
    'InstanceS3Import',
    'OptionGroupOption',
    'OptionGroupOptionOptionSetting',
    'ParameterGroupParameter',
    'ProxyAuth',
    'ProxyDefaultTargetGroupConnectionPoolConfig',
    'SecurityGroupIngress',
]

@pulumi.output_type
class ClusterParameterGroupParameter(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str,
                 apply_method: Optional[str] = None):
        """
        :param str name: The name of the DB parameter.
        :param str value: The value of the DB parameter.
        :param str apply_method: "immediate" (default), or "pending-reboot". Some
               engines can't apply some parameters without a reboot, and you will need to
               specify "pending-reboot" here.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)
        if apply_method is not None:
            pulumi.set(__self__, "apply_method", apply_method)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the DB parameter.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the DB parameter.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[str]:
        """
        "immediate" (default), or "pending-reboot". Some
        engines can't apply some parameters without a reboot, and you will need to
        specify "pending-reboot" here.
        """
        return pulumi.get(self, "apply_method")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClusterRestoreToPointInTime(dict):
    def __init__(__self__, *,
                 source_cluster_identifier: str,
                 restore_to_time: Optional[str] = None,
                 restore_type: Optional[str] = None,
                 use_latest_restorable_time: Optional[bool] = None):
        """
        :param str source_cluster_identifier: The identifier of the source database cluster from which to restore.
        :param str restore_to_time: Date and time in UTC format to restore the database cluster to. Conflicts with `use_latest_restorable_time`.
        :param str restore_type: Type of restore to be performed.
               Valid options are `full-copy` (default) and `copy-on-write`.
        :param bool use_latest_restorable_time: Set to true to restore the database cluster to the latest restorable backup time. Defaults to false. Conflicts with `restore_to_time`.
        """
        pulumi.set(__self__, "source_cluster_identifier", source_cluster_identifier)
        if restore_to_time is not None:
            pulumi.set(__self__, "restore_to_time", restore_to_time)
        if restore_type is not None:
            pulumi.set(__self__, "restore_type", restore_type)
        if use_latest_restorable_time is not None:
            pulumi.set(__self__, "use_latest_restorable_time", use_latest_restorable_time)

    @property
    @pulumi.getter(name="sourceClusterIdentifier")
    def source_cluster_identifier(self) -> str:
        """
        The identifier of the source database cluster from which to restore.
        """
        return pulumi.get(self, "source_cluster_identifier")

    @property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> Optional[str]:
        """
        Date and time in UTC format to restore the database cluster to. Conflicts with `use_latest_restorable_time`.
        """
        return pulumi.get(self, "restore_to_time")

    @property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> Optional[str]:
        """
        Type of restore to be performed.
        Valid options are `full-copy` (default) and `copy-on-write`.
        """
        return pulumi.get(self, "restore_type")

    @property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[bool]:
        """
        Set to true to restore the database cluster to the latest restorable backup time. Defaults to false. Conflicts with `restore_to_time`.
        """
        return pulumi.get(self, "use_latest_restorable_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClusterS3Import(dict):
    def __init__(__self__, *,
                 bucket_name: str,
                 ingestion_role: str,
                 source_engine: str,
                 source_engine_version: str,
                 bucket_prefix: Optional[str] = None):
        """
        :param str bucket_name: The bucket name where your backup is stored
        :param str ingestion_role: Role applied to load the data.
        :param str source_engine: Source engine for the backup
        :param str source_engine_version: Version of the source engine used to make the backup
        :param str bucket_prefix: Can be blank, but is the path to your backup
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "ingestion_role", ingestion_role)
        pulumi.set(__self__, "source_engine", source_engine)
        pulumi.set(__self__, "source_engine_version", source_engine_version)
        if bucket_prefix is not None:
            pulumi.set(__self__, "bucket_prefix", bucket_prefix)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        The bucket name where your backup is stored
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="ingestionRole")
    def ingestion_role(self) -> str:
        """
        Role applied to load the data.
        """
        return pulumi.get(self, "ingestion_role")

    @property
    @pulumi.getter(name="sourceEngine")
    def source_engine(self) -> str:
        """
        Source engine for the backup
        """
        return pulumi.get(self, "source_engine")

    @property
    @pulumi.getter(name="sourceEngineVersion")
    def source_engine_version(self) -> str:
        """
        Version of the source engine used to make the backup
        """
        return pulumi.get(self, "source_engine_version")

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[str]:
        """
        Can be blank, but is the path to your backup
        """
        return pulumi.get(self, "bucket_prefix")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ClusterScalingConfiguration(dict):
    def __init__(__self__, *,
                 auto_pause: Optional[bool] = None,
                 max_capacity: Optional[int] = None,
                 min_capacity: Optional[int] = None,
                 seconds_until_auto_pause: Optional[int] = None,
                 timeout_action: Optional[str] = None):
        """
        :param bool auto_pause: Whether to enable automatic pause. A DB cluster can be paused only when it's idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
        :param int max_capacity: The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
        :param int min_capacity: The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `1`.
        :param int seconds_until_auto_pause: The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
        :param str timeout_action: The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
        """
        if auto_pause is not None:
            pulumi.set(__self__, "auto_pause", auto_pause)
        if max_capacity is not None:
            pulumi.set(__self__, "max_capacity", max_capacity)
        if min_capacity is not None:
            pulumi.set(__self__, "min_capacity", min_capacity)
        if seconds_until_auto_pause is not None:
            pulumi.set(__self__, "seconds_until_auto_pause", seconds_until_auto_pause)
        if timeout_action is not None:
            pulumi.set(__self__, "timeout_action", timeout_action)

    @property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> Optional[bool]:
        """
        Whether to enable automatic pause. A DB cluster can be paused only when it's idle (it has no connections). If a DB cluster is paused for more than seven days, the DB cluster might be backed up with a snapshot. In this case, the DB cluster is restored when there is a request to connect to it. Defaults to `true`.
        """
        return pulumi.get(self, "auto_pause")

    @property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[int]:
        """
        The maximum capacity. The maximum capacity must be greater than or equal to the minimum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `16`.
        """
        return pulumi.get(self, "max_capacity")

    @property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> Optional[int]:
        """
        The minimum capacity. The minimum capacity must be lesser than or equal to the maximum capacity. Valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`. Defaults to `1`.
        """
        return pulumi.get(self, "min_capacity")

    @property
    @pulumi.getter(name="secondsUntilAutoPause")
    def seconds_until_auto_pause(self) -> Optional[int]:
        """
        The time, in seconds, before an Aurora DB cluster in serverless mode is paused. Valid values are `300` through `86400`. Defaults to `300`.
        """
        return pulumi.get(self, "seconds_until_auto_pause")

    @property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> Optional[str]:
        """
        The action to take when the timeout is reached. Valid values: `ForceApplyCapacityChange`, `RollbackCapacityChange`. Defaults to `RollbackCapacityChange`. See [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.timeout-action).
        """
        return pulumi.get(self, "timeout_action")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GlobalClusterGlobalClusterMember(dict):
    def __init__(__self__, *,
                 db_cluster_arn: Optional[str] = None,
                 is_writer: Optional[bool] = None):
        """
        :param str db_cluster_arn: Amazon Resource Name (ARN) of member DB Cluster
        :param bool is_writer: Whether the member is the primary DB Cluster
        """
        if db_cluster_arn is not None:
            pulumi.set(__self__, "db_cluster_arn", db_cluster_arn)
        if is_writer is not None:
            pulumi.set(__self__, "is_writer", is_writer)

    @property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of member DB Cluster
        """
        return pulumi.get(self, "db_cluster_arn")

    @property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> Optional[bool]:
        """
        Whether the member is the primary DB Cluster
        """
        return pulumi.get(self, "is_writer")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceRestoreToPointInTime(dict):
    def __init__(__self__, *,
                 restore_time: Optional[str] = None,
                 source_db_instance_identifier: Optional[str] = None,
                 source_dbi_resource_id: Optional[str] = None,
                 use_latest_restorable_time: Optional[bool] = None):
        """
        :param str restore_time: The date and time to restore from. Value must be a time in Universal Coordinated Time (UTC) format and must be before the latest restorable time for the DB instance. Cannot be specified with `use_latest_restorable_time`.
        :param str source_db_instance_identifier: The identifier of the source DB instance from which to restore. Must match the identifier of an existing DB instance. Required if `source_dbi_resource_id` is not specified.
        :param str source_dbi_resource_id: The resource ID of the source DB instance from which to restore. Required if `source_db_instance_identifier` is not specified.
        :param bool use_latest_restorable_time: A boolean value that indicates whether the DB instance is restored from the latest backup time. Defaults to `false`. Cannot be specified with `restore_time`.
        """
        if restore_time is not None:
            pulumi.set(__self__, "restore_time", restore_time)
        if source_db_instance_identifier is not None:
            pulumi.set(__self__, "source_db_instance_identifier", source_db_instance_identifier)
        if source_dbi_resource_id is not None:
            pulumi.set(__self__, "source_dbi_resource_id", source_dbi_resource_id)
        if use_latest_restorable_time is not None:
            pulumi.set(__self__, "use_latest_restorable_time", use_latest_restorable_time)

    @property
    @pulumi.getter(name="restoreTime")
    def restore_time(self) -> Optional[str]:
        """
        The date and time to restore from. Value must be a time in Universal Coordinated Time (UTC) format and must be before the latest restorable time for the DB instance. Cannot be specified with `use_latest_restorable_time`.
        """
        return pulumi.get(self, "restore_time")

    @property
    @pulumi.getter(name="sourceDbInstanceIdentifier")
    def source_db_instance_identifier(self) -> Optional[str]:
        """
        The identifier of the source DB instance from which to restore. Must match the identifier of an existing DB instance. Required if `source_dbi_resource_id` is not specified.
        """
        return pulumi.get(self, "source_db_instance_identifier")

    @property
    @pulumi.getter(name="sourceDbiResourceId")
    def source_dbi_resource_id(self) -> Optional[str]:
        """
        The resource ID of the source DB instance from which to restore. Required if `source_db_instance_identifier` is not specified.
        """
        return pulumi.get(self, "source_dbi_resource_id")

    @property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[bool]:
        """
        A boolean value that indicates whether the DB instance is restored from the latest backup time. Defaults to `false`. Cannot be specified with `restore_time`.
        """
        return pulumi.get(self, "use_latest_restorable_time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceS3Import(dict):
    def __init__(__self__, *,
                 bucket_name: str,
                 ingestion_role: str,
                 source_engine: str,
                 source_engine_version: str,
                 bucket_prefix: Optional[str] = None):
        """
        :param str bucket_name: The bucket name where your backup is stored
        :param str ingestion_role: Role applied to load the data.
        :param str source_engine: Source engine for the backup
        :param str source_engine_version: Version of the source engine used to make the backup
        :param str bucket_prefix: Can be blank, but is the path to your backup
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "ingestion_role", ingestion_role)
        pulumi.set(__self__, "source_engine", source_engine)
        pulumi.set(__self__, "source_engine_version", source_engine_version)
        if bucket_prefix is not None:
            pulumi.set(__self__, "bucket_prefix", bucket_prefix)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        The bucket name where your backup is stored
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="ingestionRole")
    def ingestion_role(self) -> str:
        """
        Role applied to load the data.
        """
        return pulumi.get(self, "ingestion_role")

    @property
    @pulumi.getter(name="sourceEngine")
    def source_engine(self) -> str:
        """
        Source engine for the backup
        """
        return pulumi.get(self, "source_engine")

    @property
    @pulumi.getter(name="sourceEngineVersion")
    def source_engine_version(self) -> str:
        """
        Version of the source engine used to make the backup
        """
        return pulumi.get(self, "source_engine_version")

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[str]:
        """
        Can be blank, but is the path to your backup
        """
        return pulumi.get(self, "bucket_prefix")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OptionGroupOption(dict):
    def __init__(__self__, *,
                 option_name: str,
                 db_security_group_memberships: Optional[Sequence[str]] = None,
                 option_settings: Optional[Sequence['outputs.OptionGroupOptionOptionSetting']] = None,
                 port: Optional[int] = None,
                 version: Optional[str] = None,
                 vpc_security_group_memberships: Optional[Sequence[str]] = None):
        """
        :param str option_name: The Name of the Option (e.g. MEMCACHED).
        :param Sequence[str] db_security_group_memberships: A list of DB Security Groups for which the option is enabled.
        :param Sequence['OptionGroupOptionOptionSettingArgs'] option_settings: A list of option settings to apply.
        :param int port: The Port number when connecting to the Option (e.g. 11211).
        :param str version: The version of the option (e.g. 13.1.0.0).
        :param Sequence[str] vpc_security_group_memberships: A list of VPC Security Groups for which the option is enabled.
        """
        pulumi.set(__self__, "option_name", option_name)
        if db_security_group_memberships is not None:
            pulumi.set(__self__, "db_security_group_memberships", db_security_group_memberships)
        if option_settings is not None:
            pulumi.set(__self__, "option_settings", option_settings)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if vpc_security_group_memberships is not None:
            pulumi.set(__self__, "vpc_security_group_memberships", vpc_security_group_memberships)

    @property
    @pulumi.getter(name="optionName")
    def option_name(self) -> str:
        """
        The Name of the Option (e.g. MEMCACHED).
        """
        return pulumi.get(self, "option_name")

    @property
    @pulumi.getter(name="dbSecurityGroupMemberships")
    def db_security_group_memberships(self) -> Optional[Sequence[str]]:
        """
        A list of DB Security Groups for which the option is enabled.
        """
        return pulumi.get(self, "db_security_group_memberships")

    @property
    @pulumi.getter(name="optionSettings")
    def option_settings(self) -> Optional[Sequence['outputs.OptionGroupOptionOptionSetting']]:
        """
        A list of option settings to apply.
        """
        return pulumi.get(self, "option_settings")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The Port number when connecting to the Option (e.g. 11211).
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the option (e.g. 13.1.0.0).
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="vpcSecurityGroupMemberships")
    def vpc_security_group_memberships(self) -> Optional[Sequence[str]]:
        """
        A list of VPC Security Groups for which the option is enabled.
        """
        return pulumi.get(self, "vpc_security_group_memberships")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class OptionGroupOptionOptionSetting(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        :param str name: The Name of the setting.
        :param str value: The Value of the setting.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The Name of the setting.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The Value of the setting.
        """
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ParameterGroupParameter(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str,
                 apply_method: Optional[str] = None):
        """
        :param str name: The name of the DB parameter.
        :param str value: The value of the DB parameter.
        :param str apply_method: "immediate" (default), or "pending-reboot". Some
               engines can't apply some parameters without a reboot, and you will need to
               specify "pending-reboot" here.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)
        if apply_method is not None:
            pulumi.set(__self__, "apply_method", apply_method)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the DB parameter.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the DB parameter.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[str]:
        """
        "immediate" (default), or "pending-reboot". Some
        engines can't apply some parameters without a reboot, and you will need to
        specify "pending-reboot" here.
        """
        return pulumi.get(self, "apply_method")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProxyAuth(dict):
    def __init__(__self__, *,
                 auth_scheme: Optional[str] = None,
                 description: Optional[str] = None,
                 iam_auth: Optional[str] = None,
                 secret_arn: Optional[str] = None):
        """
        :param str auth_scheme: The type of authentication that the proxy uses for connections from the proxy to the underlying database. One of `SECRETS`.
        :param str description: A user-specified description about the authentication used by a proxy to log in as a specific database user.
        :param str iam_auth: Whether to require or disallow AWS Identity and Access Management (IAM) authentication for connections to the proxy. One of `DISABLED`, `REQUIRED`.
        :param str secret_arn: The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.
        """
        if auth_scheme is not None:
            pulumi.set(__self__, "auth_scheme", auth_scheme)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if iam_auth is not None:
            pulumi.set(__self__, "iam_auth", iam_auth)
        if secret_arn is not None:
            pulumi.set(__self__, "secret_arn", secret_arn)

    @property
    @pulumi.getter(name="authScheme")
    def auth_scheme(self) -> Optional[str]:
        """
        The type of authentication that the proxy uses for connections from the proxy to the underlying database. One of `SECRETS`.
        """
        return pulumi.get(self, "auth_scheme")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A user-specified description about the authentication used by a proxy to log in as a specific database user.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="iamAuth")
    def iam_auth(self) -> Optional[str]:
        """
        Whether to require or disallow AWS Identity and Access Management (IAM) authentication for connections to the proxy. One of `DISABLED`, `REQUIRED`.
        """
        return pulumi.get(self, "iam_auth")

    @property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.
        """
        return pulumi.get(self, "secret_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ProxyDefaultTargetGroupConnectionPoolConfig(dict):
    def __init__(__self__, *,
                 connection_borrow_timeout: Optional[int] = None,
                 init_query: Optional[str] = None,
                 max_connections_percent: Optional[int] = None,
                 max_idle_connections_percent: Optional[int] = None,
                 session_pinning_filters: Optional[Sequence[str]] = None):
        """
        :param int connection_borrow_timeout: The number of seconds for a proxy to wait for a connection to become available in the connection pool. Only applies when the proxy has opened its maximum number of connections and all connections are busy with client sessions.
        :param str init_query: One or more SQL statements for the proxy to run when opening each new database connection. Typically used with `SET` statements to make sure that each connection has identical settings such as time zone and character set. This setting is empty by default. For multiple statements, use semicolons as the separator. You can also include multiple variables in a single `SET` statement, such as `SET x=1, y=2`.
        :param int max_connections_percent: The maximum size of the connection pool for each target in a target group. For Aurora MySQL, it is expressed as a percentage of the max_connections setting for the RDS DB instance or Aurora DB cluster used by the target group.
        :param int max_idle_connections_percent: Controls how actively the proxy closes idle database connections in the connection pool. A high value enables the proxy to leave a high percentage of idle connections open. A low value causes the proxy to close idle client connections and return the underlying database connections to the connection pool. For Aurora MySQL, it is expressed as a percentage of the max_connections setting for the RDS DB instance or Aurora DB cluster used by the target group.
        :param Sequence[str] session_pinning_filters: Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection. Including an item in the list exempts that class of SQL operations from the pinning behavior. Currently, the only allowed value is `EXCLUDE_VARIABLE_SETS`.
        """
        if connection_borrow_timeout is not None:
            pulumi.set(__self__, "connection_borrow_timeout", connection_borrow_timeout)
        if init_query is not None:
            pulumi.set(__self__, "init_query", init_query)
        if max_connections_percent is not None:
            pulumi.set(__self__, "max_connections_percent", max_connections_percent)
        if max_idle_connections_percent is not None:
            pulumi.set(__self__, "max_idle_connections_percent", max_idle_connections_percent)
        if session_pinning_filters is not None:
            pulumi.set(__self__, "session_pinning_filters", session_pinning_filters)

    @property
    @pulumi.getter(name="connectionBorrowTimeout")
    def connection_borrow_timeout(self) -> Optional[int]:
        """
        The number of seconds for a proxy to wait for a connection to become available in the connection pool. Only applies when the proxy has opened its maximum number of connections and all connections are busy with client sessions.
        """
        return pulumi.get(self, "connection_borrow_timeout")

    @property
    @pulumi.getter(name="initQuery")
    def init_query(self) -> Optional[str]:
        """
        One or more SQL statements for the proxy to run when opening each new database connection. Typically used with `SET` statements to make sure that each connection has identical settings such as time zone and character set. This setting is empty by default. For multiple statements, use semicolons as the separator. You can also include multiple variables in a single `SET` statement, such as `SET x=1, y=2`.
        """
        return pulumi.get(self, "init_query")

    @property
    @pulumi.getter(name="maxConnectionsPercent")
    def max_connections_percent(self) -> Optional[int]:
        """
        The maximum size of the connection pool for each target in a target group. For Aurora MySQL, it is expressed as a percentage of the max_connections setting for the RDS DB instance or Aurora DB cluster used by the target group.
        """
        return pulumi.get(self, "max_connections_percent")

    @property
    @pulumi.getter(name="maxIdleConnectionsPercent")
    def max_idle_connections_percent(self) -> Optional[int]:
        """
        Controls how actively the proxy closes idle database connections in the connection pool. A high value enables the proxy to leave a high percentage of idle connections open. A low value causes the proxy to close idle client connections and return the underlying database connections to the connection pool. For Aurora MySQL, it is expressed as a percentage of the max_connections setting for the RDS DB instance or Aurora DB cluster used by the target group.
        """
        return pulumi.get(self, "max_idle_connections_percent")

    @property
    @pulumi.getter(name="sessionPinningFilters")
    def session_pinning_filters(self) -> Optional[Sequence[str]]:
        """
        Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection. Including an item in the list exempts that class of SQL operations from the pinning behavior. Currently, the only allowed value is `EXCLUDE_VARIABLE_SETS`.
        """
        return pulumi.get(self, "session_pinning_filters")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SecurityGroupIngress(dict):
    def __init__(__self__, *,
                 cidr: Optional[str] = None,
                 security_group_id: Optional[str] = None,
                 security_group_name: Optional[str] = None,
                 security_group_owner_id: Optional[str] = None):
        """
        :param str cidr: The CIDR block to accept
        :param str security_group_id: The ID of the security group to authorize
        :param str security_group_name: The name of the security group to authorize
        :param str security_group_owner_id: The owner Id of the security group provided
               by `security_group_name`.
        """
        if cidr is not None:
            pulumi.set(__self__, "cidr", cidr)
        if security_group_id is not None:
            pulumi.set(__self__, "security_group_id", security_group_id)
        if security_group_name is not None:
            pulumi.set(__self__, "security_group_name", security_group_name)
        if security_group_owner_id is not None:
            pulumi.set(__self__, "security_group_owner_id", security_group_owner_id)

    @property
    @pulumi.getter
    def cidr(self) -> Optional[str]:
        """
        The CIDR block to accept
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[str]:
        """
        The ID of the security group to authorize
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter(name="securityGroupName")
    def security_group_name(self) -> Optional[str]:
        """
        The name of the security group to authorize
        """
        return pulumi.get(self, "security_group_name")

    @property
    @pulumi.getter(name="securityGroupOwnerId")
    def security_group_owner_id(self) -> Optional[str]:
        """
        The owner Id of the security group provided
        by `security_group_name`.
        """
        return pulumi.get(self, "security_group_owner_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


