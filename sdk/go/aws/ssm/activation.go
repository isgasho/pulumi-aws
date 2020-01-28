// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package ssm

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_activation.html.markdown.
type Activation struct {
	pulumi.CustomResourceState

	// The code the system generates when it processes the activation.
	ActivationCode pulumi.StringOutput `pulumi:"activationCode"`
	// The description of the resource that you want to register.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	ExpirationDate pulumi.StringOutput `pulumi:"expirationDate"`
	// If the current activation has expired.
	Expired pulumi.StringOutput `pulumi:"expired"`
	// The IAM Role to attach to the managed instance.
	IamRole pulumi.StringOutput `pulumi:"iamRole"`
	// The default name of the registered managed instance.
	Name pulumi.StringOutput `pulumi:"name"`
	// The number of managed instances that are currently registered using this activation.
	RegistrationCount pulumi.IntOutput `pulumi:"registrationCount"`
	// The maximum number of managed instances you want to register. The default value is 1 instance.
	RegistrationLimit pulumi.IntPtrOutput `pulumi:"registrationLimit"`
	// A mapping of tags to assign to the object.
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewActivation registers a new resource with the given unique name, arguments, and options.
func NewActivation(ctx *pulumi.Context,
	name string, args *ActivationArgs, opts ...pulumi.ResourceOption) (*Activation, error) {
	if args == nil || args.IamRole == nil {
		return nil, errors.New("missing required argument 'IamRole'")
	}
	if args == nil {
		args = &ActivationArgs{}
	}
	var resource Activation
	err := ctx.RegisterResource("aws:ssm/activation:Activation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetActivation gets an existing Activation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetActivation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ActivationState, opts ...pulumi.ResourceOption) (*Activation, error) {
	var resource Activation
	err := ctx.ReadResource("aws:ssm/activation:Activation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Activation resources.
type activationState struct {
	// The code the system generates when it processes the activation.
	ActivationCode *string `pulumi:"activationCode"`
	// The description of the resource that you want to register.
	Description *string `pulumi:"description"`
	ExpirationDate *string `pulumi:"expirationDate"`
	// If the current activation has expired.
	Expired *string `pulumi:"expired"`
	// The IAM Role to attach to the managed instance.
	IamRole *string `pulumi:"iamRole"`
	// The default name of the registered managed instance.
	Name *string `pulumi:"name"`
	// The number of managed instances that are currently registered using this activation.
	RegistrationCount *int `pulumi:"registrationCount"`
	// The maximum number of managed instances you want to register. The default value is 1 instance.
	RegistrationLimit *int `pulumi:"registrationLimit"`
	// A mapping of tags to assign to the object.
	Tags map[string]interface{} `pulumi:"tags"`
}

type ActivationState struct {
	// The code the system generates when it processes the activation.
	ActivationCode pulumi.StringPtrInput
	// The description of the resource that you want to register.
	Description pulumi.StringPtrInput
	ExpirationDate pulumi.StringPtrInput
	// If the current activation has expired.
	Expired pulumi.StringPtrInput
	// The IAM Role to attach to the managed instance.
	IamRole pulumi.StringPtrInput
	// The default name of the registered managed instance.
	Name pulumi.StringPtrInput
	// The number of managed instances that are currently registered using this activation.
	RegistrationCount pulumi.IntPtrInput
	// The maximum number of managed instances you want to register. The default value is 1 instance.
	RegistrationLimit pulumi.IntPtrInput
	// A mapping of tags to assign to the object.
	Tags pulumi.MapInput
}

func (ActivationState) ElementType() reflect.Type {
	return reflect.TypeOf((*activationState)(nil)).Elem()
}

type activationArgs struct {
	// The description of the resource that you want to register.
	Description *string `pulumi:"description"`
	ExpirationDate *string `pulumi:"expirationDate"`
	// The IAM Role to attach to the managed instance.
	IamRole string `pulumi:"iamRole"`
	// The default name of the registered managed instance.
	Name *string `pulumi:"name"`
	// The maximum number of managed instances you want to register. The default value is 1 instance.
	RegistrationLimit *int `pulumi:"registrationLimit"`
	// A mapping of tags to assign to the object.
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Activation resource.
type ActivationArgs struct {
	// The description of the resource that you want to register.
	Description pulumi.StringPtrInput
	ExpirationDate pulumi.StringPtrInput
	// The IAM Role to attach to the managed instance.
	IamRole pulumi.StringInput
	// The default name of the registered managed instance.
	Name pulumi.StringPtrInput
	// The maximum number of managed instances you want to register. The default value is 1 instance.
	RegistrationLimit pulumi.IntPtrInput
	// A mapping of tags to assign to the object.
	Tags pulumi.MapInput
}

func (ActivationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*activationArgs)(nil)).Elem()
}

