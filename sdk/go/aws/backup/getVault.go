// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package backup

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get information on an existing backup vault.
func LookupVault(ctx *pulumi.Context, args *LookupVaultArgs, opts ...pulumi.InvokeOption) (*LookupVaultResult, error) {
	var rv LookupVaultResult
	err := ctx.Invoke("aws:backup/getVault:getVault", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVault.
type LookupVaultArgs struct {
	// The name of the backup vault.
	Name string `pulumi:"name"`
	// Metadata that you can assign to help organize the resources that you create.
	Tags map[string]interface{} `pulumi:"tags"`
}

// A collection of values returned by getVault.
type LookupVaultResult struct {
	// The ARN of the vault.
	Arn string `pulumi:"arn"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The server-side encryption key that is used to protect your backups.
	KmsKeyArn string `pulumi:"kmsKeyArn"`
	Name      string `pulumi:"name"`
	// The number of recovery points that are stored in a backup vault.
	RecoveryPoints int `pulumi:"recoveryPoints"`
	// Metadata that you can assign to help organize the resources that you create.
	Tags map[string]interface{} `pulumi:"tags"`
}
