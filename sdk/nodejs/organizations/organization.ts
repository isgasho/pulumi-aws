// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a resource to create an organization.
 * 
 * ## Example Usage:
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/organizations_organization.html.markdown.
 */
export class Organization extends pulumi.CustomResource {
    /**
     * Get an existing Organization resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationState, opts?: pulumi.CustomResourceOptions): Organization {
        return new Organization(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:organizations/organization:Organization';

    /**
     * Returns true if the given object is an instance of Organization.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Organization {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Organization.__pulumiType;
    }

    /**
     * List of organization accounts including the master account. For a list excluding the master account, see the `nonMasterAccounts` attribute. All elements have these attributes:
     */
    public /*out*/ readonly accounts!: pulumi.Output<outputs.organizations.OrganizationAccount[]>;
    /**
     * ARN of the root
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `featureSet` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
     */
    public readonly awsServiceAccessPrincipals!: pulumi.Output<string[] | undefined>;
    /**
     * List of Organizations policy types to enable in the Organization Root. Organization must have `featureSet` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
     */
    public readonly enabledPolicyTypes!: pulumi.Output<string[] | undefined>;
    /**
     * Specify "ALL" (default) or "CONSOLIDATED_BILLING".
     */
    public readonly featureSet!: pulumi.Output<string | undefined>;
    /**
     * ARN of the master account
     */
    public /*out*/ readonly masterAccountArn!: pulumi.Output<string>;
    /**
     * Email address of the master account
     */
    public /*out*/ readonly masterAccountEmail!: pulumi.Output<string>;
    /**
     * Identifier of the master account
     */
    public /*out*/ readonly masterAccountId!: pulumi.Output<string>;
    /**
     * List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
     */
    public /*out*/ readonly nonMasterAccounts!: pulumi.Output<outputs.organizations.OrganizationNonMasterAccount[]>;
    /**
     * List of organization roots. All elements have these attributes:
     */
    public /*out*/ readonly roots!: pulumi.Output<outputs.organizations.OrganizationRoot[]>;

    /**
     * Create a Organization resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: OrganizationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrganizationArgs | OrganizationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as OrganizationState | undefined;
            inputs["accounts"] = state ? state.accounts : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["awsServiceAccessPrincipals"] = state ? state.awsServiceAccessPrincipals : undefined;
            inputs["enabledPolicyTypes"] = state ? state.enabledPolicyTypes : undefined;
            inputs["featureSet"] = state ? state.featureSet : undefined;
            inputs["masterAccountArn"] = state ? state.masterAccountArn : undefined;
            inputs["masterAccountEmail"] = state ? state.masterAccountEmail : undefined;
            inputs["masterAccountId"] = state ? state.masterAccountId : undefined;
            inputs["nonMasterAccounts"] = state ? state.nonMasterAccounts : undefined;
            inputs["roots"] = state ? state.roots : undefined;
        } else {
            const args = argsOrState as OrganizationArgs | undefined;
            inputs["awsServiceAccessPrincipals"] = args ? args.awsServiceAccessPrincipals : undefined;
            inputs["enabledPolicyTypes"] = args ? args.enabledPolicyTypes : undefined;
            inputs["featureSet"] = args ? args.featureSet : undefined;
            inputs["accounts"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["masterAccountArn"] = undefined /*out*/;
            inputs["masterAccountEmail"] = undefined /*out*/;
            inputs["masterAccountId"] = undefined /*out*/;
            inputs["nonMasterAccounts"] = undefined /*out*/;
            inputs["roots"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Organization.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Organization resources.
 */
export interface OrganizationState {
    /**
     * List of organization accounts including the master account. For a list excluding the master account, see the `nonMasterAccounts` attribute. All elements have these attributes:
     */
    readonly accounts?: pulumi.Input<pulumi.Input<inputs.organizations.OrganizationAccount>[]>;
    /**
     * ARN of the root
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `featureSet` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
     */
    readonly awsServiceAccessPrincipals?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of Organizations policy types to enable in the Organization Root. Organization must have `featureSet` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
     */
    readonly enabledPolicyTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specify "ALL" (default) or "CONSOLIDATED_BILLING".
     */
    readonly featureSet?: pulumi.Input<string>;
    /**
     * ARN of the master account
     */
    readonly masterAccountArn?: pulumi.Input<string>;
    /**
     * Email address of the master account
     */
    readonly masterAccountEmail?: pulumi.Input<string>;
    /**
     * Identifier of the master account
     */
    readonly masterAccountId?: pulumi.Input<string>;
    /**
     * List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
     */
    readonly nonMasterAccounts?: pulumi.Input<pulumi.Input<inputs.organizations.OrganizationNonMasterAccount>[]>;
    /**
     * List of organization roots. All elements have these attributes:
     */
    readonly roots?: pulumi.Input<pulumi.Input<inputs.organizations.OrganizationRoot>[]>;
}

/**
 * The set of arguments for constructing a Organization resource.
 */
export interface OrganizationArgs {
    /**
     * List of AWS service principal names for which you want to enable integration with your organization. This is typically in the form of a URL, such as service-abbreviation.amazonaws.com. Organization must have `featureSet` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
     */
    readonly awsServiceAccessPrincipals?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of Organizations policy types to enable in the Organization Root. Organization must have `featureSet` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
     */
    readonly enabledPolicyTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Specify "ALL" (default) or "CONSOLIDATED_BILLING".
     */
    readonly featureSet?: pulumi.Input<string>;
}
