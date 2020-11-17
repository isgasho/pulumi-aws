// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Fsx
{
    /// <summary>
    /// Manages a FSx Windows File System. See the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) for more information.
    /// 
    /// &gt; **NOTE:** Either the `active_directory_id` argument or `self_managed_active_directory` configuration block must be specified.
    /// 
    /// ## Example Usage
    /// ### Using AWS Directory Service
    /// 
    /// Additional information for using AWS Directory Service with Windows File Systems can be found in the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsx-aws-managed-ad.html).
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.Fsx.WindowsFileSystem("example", new Aws.Fsx.WindowsFileSystemArgs
    ///         {
    ///             ActiveDirectoryId = aws_directory_service_directory.Example.Id,
    ///             KmsKeyId = aws_kms_key.Example.Arn,
    ///             StorageCapacity = 300,
    ///             SubnetIds = 
    ///             {
    ///                 aws_subnet.Example.Id,
    ///             },
    ///             ThroughputCapacity = 1024,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Using a Self-Managed Microsoft Active Directory
    /// 
    /// Additional information for using AWS Directory Service with Windows File Systems can be found in the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html).
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.Fsx.WindowsFileSystem("example", new Aws.Fsx.WindowsFileSystemArgs
    ///         {
    ///             KmsKeyId = aws_kms_key.Example.Arn,
    ///             StorageCapacity = 300,
    ///             SubnetIds = 
    ///             {
    ///                 aws_subnet.Example.Id,
    ///             },
    ///             ThroughputCapacity = 1024,
    ///             SelfManagedActiveDirectory = new Aws.Fsx.Inputs.WindowsFileSystemSelfManagedActiveDirectoryArgs
    ///             {
    ///                 DnsIps = 
    ///                 {
    ///                     "10.0.0.111",
    ///                     "10.0.0.222",
    ///                 },
    ///                 DomainName = "corp.example.com",
    ///                 Password = "avoid-plaintext-passwords",
    ///                 Username = "Admin",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class WindowsFileSystem : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
        /// </summary>
        [Output("activeDirectoryId")]
        public Output<string?> ActiveDirectoryId { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name of the file system.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The number of days to retain automatic backups. Minimum of `0` and maximum of `90`. Defaults to `7`. Set to `0` to disable.
        /// </summary>
        [Output("automaticBackupRetentionDays")]
        public Output<int?> AutomaticBackupRetentionDays { get; private set; } = null!;

        /// <summary>
        /// A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
        /// </summary>
        [Output("copyTagsToBackups")]
        public Output<bool?> CopyTagsToBackups { get; private set; } = null!;

        /// <summary>
        /// The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
        /// </summary>
        [Output("dailyAutomaticBackupStartTime")]
        public Output<string> DailyAutomaticBackupStartTime { get; private set; } = null!;

        /// <summary>
        /// Specifies the file system deployment type, valid values are `MULTI_AZ_1`, `SINGLE_AZ_1` and `SINGLE_AZ_2`. Default value is `SINGLE_AZ_1`.
        /// </summary>
        [Output("deploymentType")]
        public Output<string?> DeploymentType { get; private set; } = null!;

        /// <summary>
        /// DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
        /// </summary>
        [Output("dnsName")]
        public Output<string> DnsName { get; private set; } = null!;

        /// <summary>
        /// ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// Set of Elastic Network Interface identifiers from which the file system is accessible.
        /// </summary>
        [Output("networkInterfaceIds")]
        public Output<ImmutableArray<string>> NetworkInterfaceIds { get; private set; } = null!;

        /// <summary>
        /// AWS account identifier that created the file system.
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// The IP address of the primary, or preferred, file server.
        /// </summary>
        [Output("preferredFileServerIp")]
        public Output<string> PreferredFileServerIp { get; private set; } = null!;

        /// <summary>
        /// Specifies the subnet in which you want the preferred file server to be located. Required for when deployment type is `MULTI_AZ_1`.
        /// </summary>
        [Output("preferredSubnetId")]
        public Output<string> PreferredSubnetId { get; private set; } = null!;

        /// <summary>
        /// For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell. For `SINGLE_AZ_1` deployment types, this is the DNS name of the file system.
        /// </summary>
        [Output("remoteAdministrationEndpoint")]
        public Output<string> RemoteAdministrationEndpoint { get; private set; } = null!;

        /// <summary>
        /// A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
        /// </summary>
        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        /// <summary>
        /// Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
        /// </summary>
        [Output("selfManagedActiveDirectory")]
        public Output<Outputs.WindowsFileSystemSelfManagedActiveDirectory?> SelfManagedActiveDirectory { get; private set; } = null!;

        /// <summary>
        /// When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
        /// </summary>
        [Output("skipFinalBackup")]
        public Output<bool?> SkipFinalBackup { get; private set; } = null!;

        /// <summary>
        /// Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536. If the storage type is set to `HDD` the minimum value is 2000.
        /// </summary>
        [Output("storageCapacity")]
        public Output<int> StorageCapacity { get; private set; } = null!;

        /// <summary>
        /// Specifies the storage type, Valid values are `SSD` and `HDD`. `HDD` is supported on `SINGLE_AZ_2` and `MULTI_AZ_1` Windows file system deployment types. Default value is `SSD`.
        /// </summary>
        [Output("storageType")]
        public Output<string?> StorageType { get; private set; } = null!;

        /// <summary>
        /// A list of IDs for the subnets that the file system will be accessible from. To specify more than a single subnet set `deployment_type` to `MULTI_AZ_1`.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the file system.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
        /// </summary>
        [Output("throughputCapacity")]
        public Output<int> ThroughputCapacity { get; private set; } = null!;

        /// <summary>
        /// Identifier of the Virtual Private Cloud for the file system.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;

        /// <summary>
        /// The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
        /// </summary>
        [Output("weeklyMaintenanceStartTime")]
        public Output<string> WeeklyMaintenanceStartTime { get; private set; } = null!;


        /// <summary>
        /// Create a WindowsFileSystem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public WindowsFileSystem(string name, WindowsFileSystemArgs args, CustomResourceOptions? options = null)
            : base("aws:fsx/windowsFileSystem:WindowsFileSystem", name, args ?? new WindowsFileSystemArgs(), MakeResourceOptions(options, ""))
        {
        }

        private WindowsFileSystem(string name, Input<string> id, WindowsFileSystemState? state = null, CustomResourceOptions? options = null)
            : base("aws:fsx/windowsFileSystem:WindowsFileSystem", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing WindowsFileSystem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static WindowsFileSystem Get(string name, Input<string> id, WindowsFileSystemState? state = null, CustomResourceOptions? options = null)
        {
            return new WindowsFileSystem(name, id, state, options);
        }
    }

    public sealed class WindowsFileSystemArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
        /// </summary>
        [Input("activeDirectoryId")]
        public Input<string>? ActiveDirectoryId { get; set; }

        /// <summary>
        /// The number of days to retain automatic backups. Minimum of `0` and maximum of `90`. Defaults to `7`. Set to `0` to disable.
        /// </summary>
        [Input("automaticBackupRetentionDays")]
        public Input<int>? AutomaticBackupRetentionDays { get; set; }

        /// <summary>
        /// A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
        /// </summary>
        [Input("copyTagsToBackups")]
        public Input<bool>? CopyTagsToBackups { get; set; }

        /// <summary>
        /// The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
        /// </summary>
        [Input("dailyAutomaticBackupStartTime")]
        public Input<string>? DailyAutomaticBackupStartTime { get; set; }

        /// <summary>
        /// Specifies the file system deployment type, valid values are `MULTI_AZ_1`, `SINGLE_AZ_1` and `SINGLE_AZ_2`. Default value is `SINGLE_AZ_1`.
        /// </summary>
        [Input("deploymentType")]
        public Input<string>? DeploymentType { get; set; }

        /// <summary>
        /// ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// Specifies the subnet in which you want the preferred file server to be located. Required for when deployment type is `MULTI_AZ_1`.
        /// </summary>
        [Input("preferredSubnetId")]
        public Input<string>? PreferredSubnetId { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        /// <summary>
        /// Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
        /// </summary>
        [Input("selfManagedActiveDirectory")]
        public Input<Inputs.WindowsFileSystemSelfManagedActiveDirectoryArgs>? SelfManagedActiveDirectory { get; set; }

        /// <summary>
        /// When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
        /// </summary>
        [Input("skipFinalBackup")]
        public Input<bool>? SkipFinalBackup { get; set; }

        /// <summary>
        /// Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536. If the storage type is set to `HDD` the minimum value is 2000.
        /// </summary>
        [Input("storageCapacity", required: true)]
        public Input<int> StorageCapacity { get; set; } = null!;

        /// <summary>
        /// Specifies the storage type, Valid values are `SSD` and `HDD`. `HDD` is supported on `SINGLE_AZ_2` and `MULTI_AZ_1` Windows file system deployment types. Default value is `SSD`.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// A list of IDs for the subnets that the file system will be accessible from. To specify more than a single subnet set `deployment_type` to `MULTI_AZ_1`.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the file system.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
        /// </summary>
        [Input("throughputCapacity", required: true)]
        public Input<int> ThroughputCapacity { get; set; } = null!;

        /// <summary>
        /// The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
        /// </summary>
        [Input("weeklyMaintenanceStartTime")]
        public Input<string>? WeeklyMaintenanceStartTime { get; set; }

        public WindowsFileSystemArgs()
        {
        }
    }

    public sealed class WindowsFileSystemState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
        /// </summary>
        [Input("activeDirectoryId")]
        public Input<string>? ActiveDirectoryId { get; set; }

        /// <summary>
        /// Amazon Resource Name of the file system.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The number of days to retain automatic backups. Minimum of `0` and maximum of `90`. Defaults to `7`. Set to `0` to disable.
        /// </summary>
        [Input("automaticBackupRetentionDays")]
        public Input<int>? AutomaticBackupRetentionDays { get; set; }

        /// <summary>
        /// A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
        /// </summary>
        [Input("copyTagsToBackups")]
        public Input<bool>? CopyTagsToBackups { get; set; }

        /// <summary>
        /// The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
        /// </summary>
        [Input("dailyAutomaticBackupStartTime")]
        public Input<string>? DailyAutomaticBackupStartTime { get; set; }

        /// <summary>
        /// Specifies the file system deployment type, valid values are `MULTI_AZ_1`, `SINGLE_AZ_1` and `SINGLE_AZ_2`. Default value is `SINGLE_AZ_1`.
        /// </summary>
        [Input("deploymentType")]
        public Input<string>? DeploymentType { get; set; }

        /// <summary>
        /// DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
        /// </summary>
        [Input("dnsName")]
        public Input<string>? DnsName { get; set; }

        /// <summary>
        /// ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("networkInterfaceIds")]
        private InputList<string>? _networkInterfaceIds;

        /// <summary>
        /// Set of Elastic Network Interface identifiers from which the file system is accessible.
        /// </summary>
        public InputList<string> NetworkInterfaceIds
        {
            get => _networkInterfaceIds ?? (_networkInterfaceIds = new InputList<string>());
            set => _networkInterfaceIds = value;
        }

        /// <summary>
        /// AWS account identifier that created the file system.
        /// </summary>
        [Input("ownerId")]
        public Input<string>? OwnerId { get; set; }

        /// <summary>
        /// The IP address of the primary, or preferred, file server.
        /// </summary>
        [Input("preferredFileServerIp")]
        public Input<string>? PreferredFileServerIp { get; set; }

        /// <summary>
        /// Specifies the subnet in which you want the preferred file server to be located. Required for when deployment type is `MULTI_AZ_1`.
        /// </summary>
        [Input("preferredSubnetId")]
        public Input<string>? PreferredSubnetId { get; set; }

        /// <summary>
        /// For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell. For `SINGLE_AZ_1` deployment types, this is the DNS name of the file system.
        /// </summary>
        [Input("remoteAdministrationEndpoint")]
        public Input<string>? RemoteAdministrationEndpoint { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        /// <summary>
        /// Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
        /// </summary>
        [Input("selfManagedActiveDirectory")]
        public Input<Inputs.WindowsFileSystemSelfManagedActiveDirectoryGetArgs>? SelfManagedActiveDirectory { get; set; }

        /// <summary>
        /// When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
        /// </summary>
        [Input("skipFinalBackup")]
        public Input<bool>? SkipFinalBackup { get; set; }

        /// <summary>
        /// Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536. If the storage type is set to `HDD` the minimum value is 2000.
        /// </summary>
        [Input("storageCapacity")]
        public Input<int>? StorageCapacity { get; set; }

        /// <summary>
        /// Specifies the storage type, Valid values are `SSD` and `HDD`. `HDD` is supported on `SINGLE_AZ_2` and `MULTI_AZ_1` Windows file system deployment types. Default value is `SSD`.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// A list of IDs for the subnets that the file system will be accessible from. To specify more than a single subnet set `deployment_type` to `MULTI_AZ_1`.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the file system.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
        /// </summary>
        [Input("throughputCapacity")]
        public Input<int>? ThroughputCapacity { get; set; }

        /// <summary>
        /// Identifier of the Virtual Private Cloud for the file system.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        /// <summary>
        /// The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
        /// </summary>
        [Input("weeklyMaintenanceStartTime")]
        public Input<string>? WeeklyMaintenanceStartTime { get; set; }

        public WindowsFileSystemState()
        {
        }
    }
}
