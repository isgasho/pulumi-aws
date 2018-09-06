# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ReplicationInstance(pulumi.CustomResource):
    """
    Provides a DMS (Data Migration Service) replication instance resource. DMS replication instances can be created, updated, deleted, and imported.
    """
    def __init__(__self__, __name__, __opts__=None, allocated_storage=None, apply_immediately=None, auto_minor_version_upgrade=None, availability_zone=None, engine_version=None, kms_key_arn=None, multi_az=None, preferred_maintenance_window=None, publicly_accessible=None, replication_instance_class=None, replication_instance_id=None, replication_subnet_group_id=None, tags=None, vpc_security_group_ids=None):
        """Create a ReplicationInstance resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if allocated_storage and not isinstance(allocated_storage, int):
            raise TypeError('Expected property allocated_storage to be a int')
        __self__.allocated_storage = allocated_storage
        """
        The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        """
        __props__['allocatedStorage'] = allocated_storage

        if apply_immediately and not isinstance(apply_immediately, bool):
            raise TypeError('Expected property apply_immediately to be a bool')
        __self__.apply_immediately = apply_immediately
        """
        Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.
        """
        __props__['applyImmediately'] = apply_immediately

        if auto_minor_version_upgrade and not isinstance(auto_minor_version_upgrade, bool):
            raise TypeError('Expected property auto_minor_version_upgrade to be a bool')
        __self__.auto_minor_version_upgrade = auto_minor_version_upgrade
        """
        Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.
        """
        __props__['autoMinorVersionUpgrade'] = auto_minor_version_upgrade

        if availability_zone and not isinstance(availability_zone, basestring):
            raise TypeError('Expected property availability_zone to be a basestring')
        __self__.availability_zone = availability_zone
        """
        The EC2 Availability Zone that the replication instance will be created in.
        """
        __props__['availabilityZone'] = availability_zone

        if engine_version and not isinstance(engine_version, basestring):
            raise TypeError('Expected property engine_version to be a basestring')
        __self__.engine_version = engine_version
        """
        The engine version number of the replication instance.
        """
        __props__['engineVersion'] = engine_version

        if kms_key_arn and not isinstance(kms_key_arn, basestring):
            raise TypeError('Expected property kms_key_arn to be a basestring')
        __self__.kms_key_arn = kms_key_arn
        """
        The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
        """
        __props__['kmsKeyArn'] = kms_key_arn

        if multi_az and not isinstance(multi_az, bool):
            raise TypeError('Expected property multi_az to be a bool')
        __self__.multi_az = multi_az
        """
        Specifies if the replication instance is a multi-az deployment. You cannot set the `availability_zone` parameter if the `multi_az` parameter is set to `true`.
        """
        __props__['multiAz'] = multi_az

        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, basestring):
            raise TypeError('Expected property preferred_maintenance_window to be a basestring')
        __self__.preferred_maintenance_window = preferred_maintenance_window
        """
        The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        """
        __props__['preferredMaintenanceWindow'] = preferred_maintenance_window

        if publicly_accessible and not isinstance(publicly_accessible, bool):
            raise TypeError('Expected property publicly_accessible to be a bool')
        __self__.publicly_accessible = publicly_accessible
        """
        Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.
        """
        __props__['publiclyAccessible'] = publicly_accessible

        if not replication_instance_class:
            raise TypeError('Missing required property replication_instance_class')
        elif not isinstance(replication_instance_class, basestring):
            raise TypeError('Expected property replication_instance_class to be a basestring')
        __self__.replication_instance_class = replication_instance_class
        """
        The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of `dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge`
        """
        __props__['replicationInstanceClass'] = replication_instance_class

        if not replication_instance_id:
            raise TypeError('Missing required property replication_instance_id')
        elif not isinstance(replication_instance_id, basestring):
            raise TypeError('Expected property replication_instance_id to be a basestring')
        __self__.replication_instance_id = replication_instance_id
        """
        The replication instance identifier. This parameter is stored as a lowercase string.
        """
        __props__['replicationInstanceId'] = replication_instance_id

        if replication_subnet_group_id and not isinstance(replication_subnet_group_id, basestring):
            raise TypeError('Expected property replication_subnet_group_id to be a basestring')
        __self__.replication_subnet_group_id = replication_subnet_group_id
        """
        A subnet group to associate with the replication instance.
        """
        __props__['replicationSubnetGroupId'] = replication_subnet_group_id

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError('Expected property vpc_security_group_ids to be a list')
        __self__.vpc_security_group_ids = vpc_security_group_ids
        """
        A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.
        """
        __props__['vpcSecurityGroupIds'] = vpc_security_group_ids

        __self__.replication_instance_arn = pulumi.runtime.UNKNOWN
        """
        The Amazon Resource Name (ARN) of the replication instance.
        """
        __self__.replication_instance_private_ips = pulumi.runtime.UNKNOWN
        """
        A list of the private IP addresses of the replication instance.
        """
        __self__.replication_instance_public_ips = pulumi.runtime.UNKNOWN
        """
        A list of the public IP addresses of the replication instance.
        """

        super(ReplicationInstance, __self__).__init__(
            'aws:dms/replicationInstance:ReplicationInstance',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'allocatedStorage' in outs:
            self.allocated_storage = outs['allocatedStorage']
        if 'applyImmediately' in outs:
            self.apply_immediately = outs['applyImmediately']
        if 'autoMinorVersionUpgrade' in outs:
            self.auto_minor_version_upgrade = outs['autoMinorVersionUpgrade']
        if 'availabilityZone' in outs:
            self.availability_zone = outs['availabilityZone']
        if 'engineVersion' in outs:
            self.engine_version = outs['engineVersion']
        if 'kmsKeyArn' in outs:
            self.kms_key_arn = outs['kmsKeyArn']
        if 'multiAz' in outs:
            self.multi_az = outs['multiAz']
        if 'preferredMaintenanceWindow' in outs:
            self.preferred_maintenance_window = outs['preferredMaintenanceWindow']
        if 'publiclyAccessible' in outs:
            self.publicly_accessible = outs['publiclyAccessible']
        if 'replicationInstanceArn' in outs:
            self.replication_instance_arn = outs['replicationInstanceArn']
        if 'replicationInstanceClass' in outs:
            self.replication_instance_class = outs['replicationInstanceClass']
        if 'replicationInstanceId' in outs:
            self.replication_instance_id = outs['replicationInstanceId']
        if 'replicationInstancePrivateIps' in outs:
            self.replication_instance_private_ips = outs['replicationInstancePrivateIps']
        if 'replicationInstancePublicIps' in outs:
            self.replication_instance_public_ips = outs['replicationInstancePublicIps']
        if 'replicationSubnetGroupId' in outs:
            self.replication_subnet_group_id = outs['replicationSubnetGroupId']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'vpcSecurityGroupIds' in outs:
            self.vpc_security_group_ids = outs['vpcSecurityGroupIds']
