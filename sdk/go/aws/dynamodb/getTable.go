// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dynamodb

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides information about a DynamoDB table.
func LookupTable(ctx *pulumi.Context, args *LookupTableArgs, opts ...pulumi.InvokeOption) (*LookupTableResult, error) {
	var rv LookupTableResult
	err := ctx.Invoke("aws:dynamodb/getTable:getTable", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTable.
type LookupTableArgs struct {
	// The name of the DynamoDB table.
	Name                 string                        `pulumi:"name"`
	ServerSideEncryption *GetTableServerSideEncryption `pulumi:"serverSideEncryption"`
	Tags                 map[string]interface{}        `pulumi:"tags"`
}

// A collection of values returned by getTable.
type LookupTableResult struct {
	Arn                    string                         `pulumi:"arn"`
	Attributes             []GetTableAttribute            `pulumi:"attributes"`
	BillingMode            string                         `pulumi:"billingMode"`
	GlobalSecondaryIndexes []GetTableGlobalSecondaryIndex `pulumi:"globalSecondaryIndexes"`
	HashKey                string                         `pulumi:"hashKey"`
	// id is the provider-assigned unique ID for this managed resource.
	Id                    string                        `pulumi:"id"`
	LocalSecondaryIndexes []GetTableLocalSecondaryIndex `pulumi:"localSecondaryIndexes"`
	Name                  string                        `pulumi:"name"`
	PointInTimeRecovery   GetTablePointInTimeRecovery   `pulumi:"pointInTimeRecovery"`
	RangeKey              string                        `pulumi:"rangeKey"`
	ReadCapacity          int                           `pulumi:"readCapacity"`
	Replicas              []GetTableReplica             `pulumi:"replicas"`
	ServerSideEncryption  GetTableServerSideEncryption  `pulumi:"serverSideEncryption"`
	StreamArn             string                        `pulumi:"streamArn"`
	StreamEnabled         bool                          `pulumi:"streamEnabled"`
	StreamLabel           string                        `pulumi:"streamLabel"`
	StreamViewType        string                        `pulumi:"streamViewType"`
	Tags                  map[string]interface{}        `pulumi:"tags"`
	Ttl                   GetTableTtl                   `pulumi:"ttl"`
	WriteCapacity         int                           `pulumi:"writeCapacity"`
}
