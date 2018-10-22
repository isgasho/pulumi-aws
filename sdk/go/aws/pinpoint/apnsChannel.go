// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type ApnsChannel struct {
	s *pulumi.ResourceState
}

// NewApnsChannel registers a new resource with the given unique name, arguments, and options.
func NewApnsChannel(ctx *pulumi.Context,
	name string, args *ApnsChannelArgs, opts ...pulumi.ResourceOpt) (*ApnsChannel, error) {
	if args == nil || args.ApplicationId == nil {
		return nil, errors.New("missing required argument 'ApplicationId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["applicationId"] = nil
		inputs["bundleId"] = nil
		inputs["certificate"] = nil
		inputs["defaultAuthenticationMethod"] = nil
		inputs["enabled"] = nil
		inputs["privateKey"] = nil
		inputs["teamId"] = nil
		inputs["tokenKey"] = nil
		inputs["tokenKeyId"] = nil
	} else {
		inputs["applicationId"] = args.ApplicationId
		inputs["bundleId"] = args.BundleId
		inputs["certificate"] = args.Certificate
		inputs["defaultAuthenticationMethod"] = args.DefaultAuthenticationMethod
		inputs["enabled"] = args.Enabled
		inputs["privateKey"] = args.PrivateKey
		inputs["teamId"] = args.TeamId
		inputs["tokenKey"] = args.TokenKey
		inputs["tokenKeyId"] = args.TokenKeyId
	}
	s, err := ctx.RegisterResource("aws:pinpoint/apnsChannel:ApnsChannel", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ApnsChannel{s: s}, nil
}

// GetApnsChannel gets an existing ApnsChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApnsChannel(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ApnsChannelState, opts ...pulumi.ResourceOpt) (*ApnsChannel, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["applicationId"] = state.ApplicationId
		inputs["bundleId"] = state.BundleId
		inputs["certificate"] = state.Certificate
		inputs["defaultAuthenticationMethod"] = state.DefaultAuthenticationMethod
		inputs["enabled"] = state.Enabled
		inputs["privateKey"] = state.PrivateKey
		inputs["teamId"] = state.TeamId
		inputs["tokenKey"] = state.TokenKey
		inputs["tokenKeyId"] = state.TokenKeyId
	}
	s, err := ctx.ReadResource("aws:pinpoint/apnsChannel:ApnsChannel", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ApnsChannel{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ApnsChannel) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ApnsChannel) ID() *pulumi.IDOutput {
	return r.s.ID
}

func (r *ApnsChannel) ApplicationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["applicationId"])
}

func (r *ApnsChannel) BundleId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bundleId"])
}

func (r *ApnsChannel) Certificate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificate"])
}

func (r *ApnsChannel) DefaultAuthenticationMethod() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultAuthenticationMethod"])
}

func (r *ApnsChannel) Enabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enabled"])
}

func (r *ApnsChannel) PrivateKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateKey"])
}

func (r *ApnsChannel) TeamId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["teamId"])
}

func (r *ApnsChannel) TokenKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tokenKey"])
}

func (r *ApnsChannel) TokenKeyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tokenKeyId"])
}

// Input properties used for looking up and filtering ApnsChannel resources.
type ApnsChannelState struct {
	ApplicationId interface{}
	BundleId interface{}
	Certificate interface{}
	DefaultAuthenticationMethod interface{}
	Enabled interface{}
	PrivateKey interface{}
	TeamId interface{}
	TokenKey interface{}
	TokenKeyId interface{}
}

// The set of arguments for constructing a ApnsChannel resource.
type ApnsChannelArgs struct {
	ApplicationId interface{}
	BundleId interface{}
	Certificate interface{}
	DefaultAuthenticationMethod interface{}
	Enabled interface{}
	PrivateKey interface{}
	TeamId interface{}
	TokenKey interface{}
	TokenKeyId interface{}
}