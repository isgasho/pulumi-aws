# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ClusterSnapshot(pulumi.CustomResource):
    availability_zones: pulumi.Output[list]
    """
    List of EC2 Availability Zones that instances in the DocDB cluster snapshot can be restored in.
    """
    db_cluster_identifier: pulumi.Output[str]
    """
    The DocDB Cluster Identifier from which to take the snapshot.
    """
    db_cluster_snapshot_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) for the DocDB Cluster Snapshot.
    """
    db_cluster_snapshot_identifier: pulumi.Output[str]
    """
    The Identifier for the snapshot.
    """
    engine: pulumi.Output[str]
    """
    Specifies the name of the database engine.
    """
    engine_version: pulumi.Output[str]
    """
    Version of the database engine for this DocDB cluster snapshot.
    """
    kms_key_id: pulumi.Output[str]
    """
    If storage_encrypted is true, the AWS KMS key identifier for the encrypted DocDB cluster snapshot.
    """
    port: pulumi.Output[float]
    """
    Port that the DocDB cluster was listening on at the time of the snapshot.
    """
    snapshot_type: pulumi.Output[str]
    source_db_cluster_snapshot_arn: pulumi.Output[str]
    status: pulumi.Output[str]
    """
    The status of this DocDB Cluster Snapshot.
    """
    storage_encrypted: pulumi.Output[bool]
    """
    Specifies whether the DocDB cluster snapshot is encrypted.
    """
    vpc_id: pulumi.Output[str]
    """
    The VPC ID associated with the DocDB cluster snapshot.
    """
    def __init__(__self__, resource_name, opts=None, db_cluster_identifier=None, db_cluster_snapshot_identifier=None, __name__=None, __opts__=None):
        """
        Manages a DocDB database cluster snapshot for DocDB clusters.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_cluster_identifier: The DocDB Cluster Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_cluster_snapshot_identifier: The Identifier for the snapshot.
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

        if db_cluster_identifier is None:
            raise TypeError("Missing required property 'db_cluster_identifier'")
        __props__['db_cluster_identifier'] = db_cluster_identifier

        if db_cluster_snapshot_identifier is None:
            raise TypeError("Missing required property 'db_cluster_snapshot_identifier'")
        __props__['db_cluster_snapshot_identifier'] = db_cluster_snapshot_identifier

        __props__['availability_zones'] = None
        __props__['db_cluster_snapshot_arn'] = None
        __props__['engine'] = None
        __props__['engine_version'] = None
        __props__['kms_key_id'] = None
        __props__['port'] = None
        __props__['snapshot_type'] = None
        __props__['source_db_cluster_snapshot_arn'] = None
        __props__['status'] = None
        __props__['storage_encrypted'] = None
        __props__['vpc_id'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(ClusterSnapshot, __self__).__init__(
            'aws:docdb/clusterSnapshot:ClusterSnapshot',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

