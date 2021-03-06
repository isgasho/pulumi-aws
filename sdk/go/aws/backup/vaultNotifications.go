// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package backup

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an AWS Backup vault notifications resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/backup"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/sns"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		testTopic, err := sns.NewTopic(ctx, "testTopic", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = sns.NewTopicPolicy(ctx, "testTopicPolicy", &sns.TopicPolicyArgs{
// 			Arn: testTopic.Arn,
// 			Policy: testPolicyDocument.ApplyT(func(testPolicyDocument iam.GetPolicyDocumentResult) (string, error) {
// 				return testPolicyDocument.Json, nil
// 			}).(pulumi.StringOutput),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = backup.NewVaultNotifications(ctx, "testVaultNotifications", &backup.VaultNotificationsArgs{
// 			BackupVaultName: pulumi.String("example_backup_vault"),
// 			SnsTopicArn:     testTopic.Arn,
// 			BackupVaultEvents: pulumi.StringArray{
// 				pulumi.String("BACKUP_JOB_STARTED"),
// 				pulumi.String("RESTORE_JOB_COMPLETED"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Backup vault notifications can be imported using the `name`, e.g.
//
// ```sh
//  $ pulumi import aws:backup/vaultNotifications:VaultNotifications test TestVault
// ```
type VaultNotifications struct {
	pulumi.CustomResourceState

	// The ARN of the vault.
	BackupVaultArn pulumi.StringOutput `pulumi:"backupVaultArn"`
	// An array of events that indicate the status of jobs to back up resources to the backup vault.
	BackupVaultEvents pulumi.StringArrayOutput `pulumi:"backupVaultEvents"`
	// Name of the backup vault to add notifications for.
	BackupVaultName pulumi.StringOutput `pulumi:"backupVaultName"`
	// The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events
	SnsTopicArn pulumi.StringOutput `pulumi:"snsTopicArn"`
}

// NewVaultNotifications registers a new resource with the given unique name, arguments, and options.
func NewVaultNotifications(ctx *pulumi.Context,
	name string, args *VaultNotificationsArgs, opts ...pulumi.ResourceOption) (*VaultNotifications, error) {
	if args == nil || args.BackupVaultEvents == nil {
		return nil, errors.New("missing required argument 'BackupVaultEvents'")
	}
	if args == nil || args.BackupVaultName == nil {
		return nil, errors.New("missing required argument 'BackupVaultName'")
	}
	if args == nil || args.SnsTopicArn == nil {
		return nil, errors.New("missing required argument 'SnsTopicArn'")
	}
	if args == nil {
		args = &VaultNotificationsArgs{}
	}
	var resource VaultNotifications
	err := ctx.RegisterResource("aws:backup/vaultNotifications:VaultNotifications", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVaultNotifications gets an existing VaultNotifications resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVaultNotifications(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VaultNotificationsState, opts ...pulumi.ResourceOption) (*VaultNotifications, error) {
	var resource VaultNotifications
	err := ctx.ReadResource("aws:backup/vaultNotifications:VaultNotifications", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VaultNotifications resources.
type vaultNotificationsState struct {
	// The ARN of the vault.
	BackupVaultArn *string `pulumi:"backupVaultArn"`
	// An array of events that indicate the status of jobs to back up resources to the backup vault.
	BackupVaultEvents []string `pulumi:"backupVaultEvents"`
	// Name of the backup vault to add notifications for.
	BackupVaultName *string `pulumi:"backupVaultName"`
	// The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events
	SnsTopicArn *string `pulumi:"snsTopicArn"`
}

type VaultNotificationsState struct {
	// The ARN of the vault.
	BackupVaultArn pulumi.StringPtrInput
	// An array of events that indicate the status of jobs to back up resources to the backup vault.
	BackupVaultEvents pulumi.StringArrayInput
	// Name of the backup vault to add notifications for.
	BackupVaultName pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events
	SnsTopicArn pulumi.StringPtrInput
}

func (VaultNotificationsState) ElementType() reflect.Type {
	return reflect.TypeOf((*vaultNotificationsState)(nil)).Elem()
}

type vaultNotificationsArgs struct {
	// An array of events that indicate the status of jobs to back up resources to the backup vault.
	BackupVaultEvents []string `pulumi:"backupVaultEvents"`
	// Name of the backup vault to add notifications for.
	BackupVaultName string `pulumi:"backupVaultName"`
	// The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events
	SnsTopicArn string `pulumi:"snsTopicArn"`
}

// The set of arguments for constructing a VaultNotifications resource.
type VaultNotificationsArgs struct {
	// An array of events that indicate the status of jobs to back up resources to the backup vault.
	BackupVaultEvents pulumi.StringArrayInput
	// Name of the backup vault to add notifications for.
	BackupVaultName pulumi.StringInput
	// The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events
	SnsTopicArn pulumi.StringInput
}

func (VaultNotificationsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vaultNotificationsArgs)(nil)).Elem()
}

type VaultNotificationsInput interface {
	pulumi.Input

	ToVaultNotificationsOutput() VaultNotificationsOutput
	ToVaultNotificationsOutputWithContext(ctx context.Context) VaultNotificationsOutput
}

func (VaultNotifications) ElementType() reflect.Type {
	return reflect.TypeOf((*VaultNotifications)(nil)).Elem()
}

func (i VaultNotifications) ToVaultNotificationsOutput() VaultNotificationsOutput {
	return i.ToVaultNotificationsOutputWithContext(context.Background())
}

func (i VaultNotifications) ToVaultNotificationsOutputWithContext(ctx context.Context) VaultNotificationsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VaultNotificationsOutput)
}

type VaultNotificationsOutput struct {
	*pulumi.OutputState
}

func (VaultNotificationsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VaultNotificationsOutput)(nil)).Elem()
}

func (o VaultNotificationsOutput) ToVaultNotificationsOutput() VaultNotificationsOutput {
	return o
}

func (o VaultNotificationsOutput) ToVaultNotificationsOutputWithContext(ctx context.Context) VaultNotificationsOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(VaultNotificationsOutput{})
}
