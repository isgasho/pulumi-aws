# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Ami(pulumi.CustomResource):
    """
    The AMI resource allows the creation and management of a completely-custom
    *Amazon Machine Image* (AMI).
    
    If you just want to duplicate an existing AMI, possibly copying it to another
    region, it's better to use `aws_ami_copy` instead.
    
    If you just want to share an existing AMI with another AWS account,
    it's better to use `aws_ami_launch_permission` instead.
    """
    def __init__(__self__, __name__, __opts__=None, architecture=None, description=None, ebs_block_devices=None, ena_support=None, ephemeral_block_devices=None, image_location=None, kernel_id=None, name=None, ramdisk_id=None, root_device_name=None, sriov_net_support=None, tags=None, virtualization_type=None):
        """Create a Ami resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if architecture and not isinstance(architecture, basestring):
            raise TypeError('Expected property architecture to be a basestring')
        __self__.architecture = architecture
        """
        Machine architecture for created instances. Defaults to "x86_64".
        """
        __props__['architecture'] = architecture

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A longer, human-readable description for the AMI.
        """
        __props__['description'] = description

        if ebs_block_devices and not isinstance(ebs_block_devices, list):
            raise TypeError('Expected property ebs_block_devices to be a list')
        __self__.ebs_block_devices = ebs_block_devices
        """
        Nested block describing an EBS block device that should be
        attached to created instances. The structure of this block is described below.
        """
        __props__['ebsBlockDevices'] = ebs_block_devices

        if ena_support and not isinstance(ena_support, bool):
            raise TypeError('Expected property ena_support to be a bool')
        __self__.ena_support = ena_support
        """
        Specifies whether enhanced networking with ENA is enabled. Defaults to `false`.
        """
        __props__['enaSupport'] = ena_support

        if ephemeral_block_devices and not isinstance(ephemeral_block_devices, list):
            raise TypeError('Expected property ephemeral_block_devices to be a list')
        __self__.ephemeral_block_devices = ephemeral_block_devices
        """
        Nested block describing an ephemeral block device that
        should be attached to created instances. The structure of this block is described below.
        """
        __props__['ephemeralBlockDevices'] = ephemeral_block_devices

        if image_location and not isinstance(image_location, basestring):
            raise TypeError('Expected property image_location to be a basestring')
        __self__.image_location = image_location
        """
        Path to an S3 object containing an image manifest, e.g. created
        by the `ec2-upload-bundle` command in the EC2 command line tools.
        """
        __props__['imageLocation'] = image_location

        if kernel_id and not isinstance(kernel_id, basestring):
            raise TypeError('Expected property kernel_id to be a basestring')
        __self__.kernel_id = kernel_id
        """
        The id of the kernel image (AKI) that will be used as the paravirtual
        kernel in created instances.
        """
        __props__['kernelId'] = kernel_id

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A region-unique name for the AMI.
        """
        __props__['name'] = name

        if ramdisk_id and not isinstance(ramdisk_id, basestring):
            raise TypeError('Expected property ramdisk_id to be a basestring')
        __self__.ramdisk_id = ramdisk_id
        """
        The id of an initrd image (ARI) that will be used when booting the
        created instances.
        """
        __props__['ramdiskId'] = ramdisk_id

        if root_device_name and not isinstance(root_device_name, basestring):
            raise TypeError('Expected property root_device_name to be a basestring')
        __self__.root_device_name = root_device_name
        """
        The name of the root device (for example, `/dev/sda1`, or `/dev/xvda`).
        """
        __props__['rootDeviceName'] = root_device_name

        if sriov_net_support and not isinstance(sriov_net_support, basestring):
            raise TypeError('Expected property sriov_net_support to be a basestring')
        __self__.sriov_net_support = sriov_net_support
        """
        When set to "simple" (the default), enables enhanced networking
        for created instances. No other value is supported at this time.
        """
        __props__['sriovNetSupport'] = sriov_net_support

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        __props__['tags'] = tags

        if virtualization_type and not isinstance(virtualization_type, basestring):
            raise TypeError('Expected property virtualization_type to be a basestring')
        __self__.virtualization_type = virtualization_type
        """
        Keyword to choose what virtualization mode created instances
        will use. Can be either "paravirtual" (the default) or "hvm". The choice of virtualization type
        changes the set of further arguments that are required, as described below.
        """
        __props__['virtualizationType'] = virtualization_type

        __self__.manage_ebs_snapshots = pulumi.runtime.UNKNOWN
        __self__.root_snapshot_id = pulumi.runtime.UNKNOWN
        """
        The Snapshot ID for the root volume (for EBS-backed AMIs)
        """

        super(Ami, __self__).__init__(
            'aws:ec2/ami:Ami',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'architecture' in outs:
            self.architecture = outs['architecture']
        if 'description' in outs:
            self.description = outs['description']
        if 'ebsBlockDevices' in outs:
            self.ebs_block_devices = outs['ebsBlockDevices']
        if 'enaSupport' in outs:
            self.ena_support = outs['enaSupport']
        if 'ephemeralBlockDevices' in outs:
            self.ephemeral_block_devices = outs['ephemeralBlockDevices']
        if 'imageLocation' in outs:
            self.image_location = outs['imageLocation']
        if 'kernelId' in outs:
            self.kernel_id = outs['kernelId']
        if 'manageEbsSnapshots' in outs:
            self.manage_ebs_snapshots = outs['manageEbsSnapshots']
        if 'name' in outs:
            self.name = outs['name']
        if 'ramdiskId' in outs:
            self.ramdisk_id = outs['ramdiskId']
        if 'rootDeviceName' in outs:
            self.root_device_name = outs['rootDeviceName']
        if 'rootSnapshotId' in outs:
            self.root_snapshot_id = outs['rootSnapshotId']
        if 'sriovNetSupport' in outs:
            self.sriov_net_support = outs['sriovNetSupport']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'virtualizationType' in outs:
            self.virtualization_type = outs['virtualizationType']
