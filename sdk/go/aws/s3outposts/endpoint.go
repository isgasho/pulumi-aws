// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package s3outposts

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage an S3 Outposts Endpoint.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/s3outposts"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := s3outposts.NewEndpoint(ctx, "example", &s3outposts.EndpointArgs{
// 			OutpostId:       pulumi.Any(data.Aws_outposts_outpost.Example.Id),
// 			SecurityGroupId: pulumi.Any(aws_security_group.Example.Id),
// 			SubnetId:        pulumi.Any(aws_subnet.Example.Id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Endpoint struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of the endpoint.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// VPC CIDR block of the endpoint.
	CidrBlock pulumi.StringOutput `pulumi:"cidrBlock"`
	// UTC creation time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// Set of nested attributes for associated Elastic Network Interfaces (ENIs).
	NetworkInterfaces EndpointNetworkInterfaceArrayOutput `pulumi:"networkInterfaces"`
	// Identifier of the Outpost to contain this endpoint.
	OutpostId pulumi.StringOutput `pulumi:"outpostId"`
	// Identifier of the EC2 Security Group.
	SecurityGroupId pulumi.StringOutput `pulumi:"securityGroupId"`
	// Identifier of the EC2 Subnet.
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
}

// NewEndpoint registers a new resource with the given unique name, arguments, and options.
func NewEndpoint(ctx *pulumi.Context,
	name string, args *EndpointArgs, opts ...pulumi.ResourceOption) (*Endpoint, error) {
	if args == nil || args.OutpostId == nil {
		return nil, errors.New("missing required argument 'OutpostId'")
	}
	if args == nil || args.SecurityGroupId == nil {
		return nil, errors.New("missing required argument 'SecurityGroupId'")
	}
	if args == nil || args.SubnetId == nil {
		return nil, errors.New("missing required argument 'SubnetId'")
	}
	if args == nil {
		args = &EndpointArgs{}
	}
	var resource Endpoint
	err := ctx.RegisterResource("aws:s3outposts/endpoint:Endpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEndpoint gets an existing Endpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EndpointState, opts ...pulumi.ResourceOption) (*Endpoint, error) {
	var resource Endpoint
	err := ctx.ReadResource("aws:s3outposts/endpoint:Endpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Endpoint resources.
type endpointState struct {
	// Amazon Resource Name (ARN) of the endpoint.
	Arn *string `pulumi:"arn"`
	// VPC CIDR block of the endpoint.
	CidrBlock *string `pulumi:"cidrBlock"`
	// UTC creation time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).
	CreationTime *string `pulumi:"creationTime"`
	// Set of nested attributes for associated Elastic Network Interfaces (ENIs).
	NetworkInterfaces []EndpointNetworkInterface `pulumi:"networkInterfaces"`
	// Identifier of the Outpost to contain this endpoint.
	OutpostId *string `pulumi:"outpostId"`
	// Identifier of the EC2 Security Group.
	SecurityGroupId *string `pulumi:"securityGroupId"`
	// Identifier of the EC2 Subnet.
	SubnetId *string `pulumi:"subnetId"`
}

type EndpointState struct {
	// Amazon Resource Name (ARN) of the endpoint.
	Arn pulumi.StringPtrInput
	// VPC CIDR block of the endpoint.
	CidrBlock pulumi.StringPtrInput
	// UTC creation time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).
	CreationTime pulumi.StringPtrInput
	// Set of nested attributes for associated Elastic Network Interfaces (ENIs).
	NetworkInterfaces EndpointNetworkInterfaceArrayInput
	// Identifier of the Outpost to contain this endpoint.
	OutpostId pulumi.StringPtrInput
	// Identifier of the EC2 Security Group.
	SecurityGroupId pulumi.StringPtrInput
	// Identifier of the EC2 Subnet.
	SubnetId pulumi.StringPtrInput
}

func (EndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointState)(nil)).Elem()
}

type endpointArgs struct {
	// Identifier of the Outpost to contain this endpoint.
	OutpostId string `pulumi:"outpostId"`
	// Identifier of the EC2 Security Group.
	SecurityGroupId string `pulumi:"securityGroupId"`
	// Identifier of the EC2 Subnet.
	SubnetId string `pulumi:"subnetId"`
}

// The set of arguments for constructing a Endpoint resource.
type EndpointArgs struct {
	// Identifier of the Outpost to contain this endpoint.
	OutpostId pulumi.StringInput
	// Identifier of the EC2 Security Group.
	SecurityGroupId pulumi.StringInput
	// Identifier of the EC2 Subnet.
	SubnetId pulumi.StringInput
}

func (EndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointArgs)(nil)).Elem()
}