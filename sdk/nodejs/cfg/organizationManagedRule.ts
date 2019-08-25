// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a Config Organization Managed Rule. More information about these rules can be found in the [Enabling AWS Config Rules Across all Accounts in Your Organization](https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html) and [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) documentation. For working with Organization Custom Rules (those invoking a custom Lambda Function), see the [`aws.cfg.OrganizationCustomRule` resource](https://www.terraform.io/docs/providers/aws/r/config_organization_custom_rule.html).
 * 
 * > **NOTE:** This resource must be created in the Organization master account and rules will include the master account unless its ID is added to the `excludedAccounts` argument.
 * 
 * > **NOTE:** Every Organization account except those configured in the `excludedAccounts` argument must have a Configuration Recorder with proper IAM permissions before the rule will successfully create or update. See also the [`aws.cfg.Recorder` resource](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html).
 * 
 * ## Example Usage
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/config_organization_managed_rule.html.markdown.
 */
export class OrganizationManagedRule extends pulumi.CustomResource {
    /**
     * Get an existing OrganizationManagedRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationManagedRuleState, opts?: pulumi.CustomResourceOptions): OrganizationManagedRule {
        return new OrganizationManagedRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:cfg/organizationManagedRule:OrganizationManagedRule';

    /**
     * Returns true if the given object is an instance of OrganizationManagedRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrganizationManagedRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrganizationManagedRule.__pulumiType;
    }

    /**
     * Amazon Resource Name (ARN) of the rule
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Description of the rule
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * List of AWS account identifiers to exclude from the rule
     */
    public readonly excludedAccounts!: pulumi.Output<string[] | undefined>;
    /**
     * A string in JSON format that is passed to the AWS Config Rule Lambda Function
     */
    public readonly inputParameters!: pulumi.Output<string | undefined>;
    /**
     * The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
     */
    public readonly maximumExecutionFrequency!: pulumi.Output<string | undefined>;
    /**
     * The name of the rule
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Identifier of the AWS resource to evaluate
     */
    public readonly resourceIdScope!: pulumi.Output<string | undefined>;
    /**
     * List of types of AWS resources to evaluate
     */
    public readonly resourceTypesScopes!: pulumi.Output<string[] | undefined>;
    /**
     * Identifier of an available AWS Config Managed Rule to call. For available values, see the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) documentation
     */
    public readonly ruleIdentifier!: pulumi.Output<string>;
    /**
     * Tag key of AWS resources to evaluate
     */
    public readonly tagKeyScope!: pulumi.Output<string | undefined>;
    /**
     * Tag value of AWS resources to evaluate
     */
    public readonly tagValueScope!: pulumi.Output<string | undefined>;

    /**
     * Create a OrganizationManagedRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OrganizationManagedRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrganizationManagedRuleArgs | OrganizationManagedRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as OrganizationManagedRuleState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["excludedAccounts"] = state ? state.excludedAccounts : undefined;
            inputs["inputParameters"] = state ? state.inputParameters : undefined;
            inputs["maximumExecutionFrequency"] = state ? state.maximumExecutionFrequency : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["resourceIdScope"] = state ? state.resourceIdScope : undefined;
            inputs["resourceTypesScopes"] = state ? state.resourceTypesScopes : undefined;
            inputs["ruleIdentifier"] = state ? state.ruleIdentifier : undefined;
            inputs["tagKeyScope"] = state ? state.tagKeyScope : undefined;
            inputs["tagValueScope"] = state ? state.tagValueScope : undefined;
        } else {
            const args = argsOrState as OrganizationManagedRuleArgs | undefined;
            if (!args || args.ruleIdentifier === undefined) {
                throw new Error("Missing required property 'ruleIdentifier'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["excludedAccounts"] = args ? args.excludedAccounts : undefined;
            inputs["inputParameters"] = args ? args.inputParameters : undefined;
            inputs["maximumExecutionFrequency"] = args ? args.maximumExecutionFrequency : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceIdScope"] = args ? args.resourceIdScope : undefined;
            inputs["resourceTypesScopes"] = args ? args.resourceTypesScopes : undefined;
            inputs["ruleIdentifier"] = args ? args.ruleIdentifier : undefined;
            inputs["tagKeyScope"] = args ? args.tagKeyScope : undefined;
            inputs["tagValueScope"] = args ? args.tagValueScope : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(OrganizationManagedRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OrganizationManagedRule resources.
 */
export interface OrganizationManagedRuleState {
    /**
     * Amazon Resource Name (ARN) of the rule
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * Description of the rule
     */
    readonly description?: pulumi.Input<string>;
    /**
     * List of AWS account identifiers to exclude from the rule
     */
    readonly excludedAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A string in JSON format that is passed to the AWS Config Rule Lambda Function
     */
    readonly inputParameters?: pulumi.Input<string>;
    /**
     * The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
     */
    readonly maximumExecutionFrequency?: pulumi.Input<string>;
    /**
     * The name of the rule
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Identifier of the AWS resource to evaluate
     */
    readonly resourceIdScope?: pulumi.Input<string>;
    /**
     * List of types of AWS resources to evaluate
     */
    readonly resourceTypesScopes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Identifier of an available AWS Config Managed Rule to call. For available values, see the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) documentation
     */
    readonly ruleIdentifier?: pulumi.Input<string>;
    /**
     * Tag key of AWS resources to evaluate
     */
    readonly tagKeyScope?: pulumi.Input<string>;
    /**
     * Tag value of AWS resources to evaluate
     */
    readonly tagValueScope?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a OrganizationManagedRule resource.
 */
export interface OrganizationManagedRuleArgs {
    /**
     * Description of the rule
     */
    readonly description?: pulumi.Input<string>;
    /**
     * List of AWS account identifiers to exclude from the rule
     */
    readonly excludedAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A string in JSON format that is passed to the AWS Config Rule Lambda Function
     */
    readonly inputParameters?: pulumi.Input<string>;
    /**
     * The maximum frequency with which AWS Config runs evaluations for a rule, if the rule is triggered at a periodic frequency. Defaults to `TwentyFour_Hours` for periodic frequency triggered rules. Valid values: `One_Hour`, `Three_Hours`, `Six_Hours`, `Twelve_Hours`, or `TwentyFour_Hours`.
     */
    readonly maximumExecutionFrequency?: pulumi.Input<string>;
    /**
     * The name of the rule
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Identifier of the AWS resource to evaluate
     */
    readonly resourceIdScope?: pulumi.Input<string>;
    /**
     * List of types of AWS resources to evaluate
     */
    readonly resourceTypesScopes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Identifier of an available AWS Config Managed Rule to call. For available values, see the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) documentation
     */
    readonly ruleIdentifier: pulumi.Input<string>;
    /**
     * Tag key of AWS resources to evaluate
     */
    readonly tagKeyScope?: pulumi.Input<string>;
    /**
     * Tag value of AWS resources to evaluate
     */
    readonly tagValueScope?: pulumi.Input<string>;
}
