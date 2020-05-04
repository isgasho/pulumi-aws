// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `ec2.Subnet` provides details about a specific VPC subnet.
//
// This resource can prove useful when a module accepts a subnet id as
// an input variable and needs to, for example, determine the id of the
// VPC that the subnet belongs to.
func LookupSubnet(ctx *pulumi.Context, args *LookupSubnetArgs, opts ...pulumi.InvokeOption) (*LookupSubnetResult, error) {
	var rv LookupSubnetResult
	err := ctx.Invoke("aws:ec2/getSubnet:getSubnet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSubnet.
type LookupSubnetArgs struct {
	// The availability zone where the
	// subnet must reside.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// The ID of the Availability Zone for the subnet.
	AvailabilityZoneId *string `pulumi:"availabilityZoneId"`
	// The cidr block of the desired subnet.
	CidrBlock *string `pulumi:"cidrBlock"`
	// Boolean constraint for whether the desired
	// subnet must be the default subnet for its associated availability zone.
	DefaultForAz *bool `pulumi:"defaultForAz"`
	// Custom filter block as described below.
	Filters []GetSubnetFilter `pulumi:"filters"`
	// The id of the specific subnet to retrieve.
	Id *string `pulumi:"id"`
	// The Ipv6 cidr block of the desired subnet
	Ipv6CidrBlock *string `pulumi:"ipv6CidrBlock"`
	// The state that the desired subnet must have.
	State *string `pulumi:"state"`
	// A map of tags, each pair of which must exactly match
	// a pair on the desired subnet.
	Tags map[string]interface{} `pulumi:"tags"`
	// The id of the VPC that the desired subnet belongs to.
	VpcId *string `pulumi:"vpcId"`
}

// A collection of values returned by getSubnet.
type LookupSubnetResult struct {
	// The ARN of the subnet.
	Arn                         string            `pulumi:"arn"`
	AssignIpv6AddressOnCreation bool              `pulumi:"assignIpv6AddressOnCreation"`
	AvailabilityZone            string            `pulumi:"availabilityZone"`
	AvailabilityZoneId          string            `pulumi:"availabilityZoneId"`
	CidrBlock                   string            `pulumi:"cidrBlock"`
	DefaultForAz                bool              `pulumi:"defaultForAz"`
	Filters                     []GetSubnetFilter `pulumi:"filters"`
	Id                          string            `pulumi:"id"`
	Ipv6CidrBlock               string            `pulumi:"ipv6CidrBlock"`
	Ipv6CidrBlockAssociationId  string            `pulumi:"ipv6CidrBlockAssociationId"`
	MapPublicIpOnLaunch         bool              `pulumi:"mapPublicIpOnLaunch"`
	// The Amazon Resource Name (ARN) of the Outpost.
	OutpostArn string `pulumi:"outpostArn"`
	// The ID of the AWS account that owns the subnet.
	OwnerId string                 `pulumi:"ownerId"`
	State   string                 `pulumi:"state"`
	Tags    map[string]interface{} `pulumi:"tags"`
	VpcId   string                 `pulumi:"vpcId"`
}
