// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package sns

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an SNS topic policy resource
// 
// > **NOTE:** If a Principal is specified as just an AWS account ID rather than an ARN, AWS silently converts it to the ARN for the root user, causing future deployments to differ. To avoid this problem, just specify the full ARN, e.g. `arn:aws:iam::123456789012:root`
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic_policy.html.markdown.
type TopicPolicy struct {
	pulumi.CustomResourceState

	// The ARN of the SNS topic
	Arn pulumi.StringOutput `pulumi:"arn"`
	Policy pulumi.StringOutput `pulumi:"policy"`
}

// NewTopicPolicy registers a new resource with the given unique name, arguments, and options.
func NewTopicPolicy(ctx *pulumi.Context,
	name string, args *TopicPolicyArgs, opts ...pulumi.ResourceOption) (*TopicPolicy, error) {
	if args == nil || args.Arn == nil {
		return nil, errors.New("missing required argument 'Arn'")
	}
	if args == nil || args.Policy == nil {
		return nil, errors.New("missing required argument 'Policy'")
	}
	if args == nil {
		args = &TopicPolicyArgs{}
	}
	var resource TopicPolicy
	err := ctx.RegisterResource("aws:sns/topicPolicy:TopicPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTopicPolicy gets an existing TopicPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTopicPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TopicPolicyState, opts ...pulumi.ResourceOption) (*TopicPolicy, error) {
	var resource TopicPolicy
	err := ctx.ReadResource("aws:sns/topicPolicy:TopicPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TopicPolicy resources.
type topicPolicyState struct {
	// The ARN of the SNS topic
	Arn *string `pulumi:"arn"`
	Policy *string `pulumi:"policy"`
}

type TopicPolicyState struct {
	// The ARN of the SNS topic
	Arn pulumi.StringPtrInput
	Policy pulumi.StringPtrInput
}

func (TopicPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*topicPolicyState)(nil)).Elem()
}

type topicPolicyArgs struct {
	// The ARN of the SNS topic
	Arn string `pulumi:"arn"`
	Policy string `pulumi:"policy"`
}

// The set of arguments for constructing a TopicPolicy resource.
type TopicPolicyArgs struct {
	// The ARN of the SNS topic
	Arn pulumi.StringInput
	Policy pulumi.StringInput
}

func (TopicPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*topicPolicyArgs)(nil)).Elem()
}

