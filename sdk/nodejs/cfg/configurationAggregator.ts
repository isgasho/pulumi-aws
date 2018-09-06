// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an AWS Config Configuration Aggregator
 */
export class ConfigurationAggregator extends pulumi.CustomResource {
    /**
     * Get an existing ConfigurationAggregator resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationAggregatorState): ConfigurationAggregator {
        return new ConfigurationAggregator(name, <any>state, { id });
    }

    /**
     * The account(s) to aggregate config data from as documented below.
     */
    public readonly accountAggregationSource: pulumi.Output<{ accountIds: string[], allRegions?: boolean, regions?: string[] } | undefined>;
    /**
     * The ARN of the aggregator
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The name of the configuration aggregator.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The organization to aggregate config data from as documented below.
     */
    public readonly organizationAggregationSource: pulumi.Output<{ allRegions?: boolean, regions?: string[], roleArn: string } | undefined>;

    /**
     * Create a ConfigurationAggregator resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ConfigurationAggregatorArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConfigurationAggregatorArgs | ConfigurationAggregatorState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ConfigurationAggregatorState = argsOrState as ConfigurationAggregatorState | undefined;
            inputs["accountAggregationSource"] = state ? state.accountAggregationSource : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["organizationAggregationSource"] = state ? state.organizationAggregationSource : undefined;
        } else {
            const args = argsOrState as ConfigurationAggregatorArgs | undefined;
            inputs["accountAggregationSource"] = args ? args.accountAggregationSource : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["organizationAggregationSource"] = args ? args.organizationAggregationSource : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:cfg/configurationAggregator:ConfigurationAggregator", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ConfigurationAggregator resources.
 */
export interface ConfigurationAggregatorState {
    /**
     * The account(s) to aggregate config data from as documented below.
     */
    readonly accountAggregationSource?: pulumi.Input<{ accountIds: pulumi.Input<pulumi.Input<string>[]>, allRegions?: pulumi.Input<boolean>, regions?: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * The ARN of the aggregator
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The name of the configuration aggregator.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The organization to aggregate config data from as documented below.
     */
    readonly organizationAggregationSource?: pulumi.Input<{ allRegions?: pulumi.Input<boolean>, regions?: pulumi.Input<pulumi.Input<string>[]>, roleArn: pulumi.Input<string> }>;
}

/**
 * The set of arguments for constructing a ConfigurationAggregator resource.
 */
export interface ConfigurationAggregatorArgs {
    /**
     * The account(s) to aggregate config data from as documented below.
     */
    readonly accountAggregationSource?: pulumi.Input<{ accountIds: pulumi.Input<pulumi.Input<string>[]>, allRegions?: pulumi.Input<boolean>, regions?: pulumi.Input<pulumi.Input<string>[]> }>;
    /**
     * The name of the configuration aggregator.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The organization to aggregate config data from as documented below.
     */
    readonly organizationAggregationSource?: pulumi.Input<{ allRegions?: pulumi.Input<boolean>, regions?: pulumi.Input<pulumi.Input<string>[]>, roleArn: pulumi.Input<string> }>;
}
