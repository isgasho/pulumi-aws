// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a [Route53 Delegation Set](https://docs.aws.amazon.com/Route53/latest/APIReference/API-actions-by-function.html#actions-by-function-reusable-delegation-sets) resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_delegation_set.html.markdown.
 */
export class DelegationSet extends pulumi.CustomResource {
    /**
     * Get an existing DelegationSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DelegationSetState, opts?: pulumi.CustomResourceOptions): DelegationSet {
        return new DelegationSet(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:route53/delegationSet:DelegationSet';

    /**
     * Returns true if the given object is an instance of DelegationSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DelegationSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DelegationSet.__pulumiType;
    }

    /**
     * A list of authoritative name servers for the hosted zone
     * (effectively a list of NS records).
     */
    public /*out*/ readonly nameServers!: pulumi.Output<string[]>;
    /**
     * This is a reference name used in Caller Reference
     * (helpful for identifying single delegation set amongst others)
     */
    public readonly referenceName!: pulumi.Output<string | undefined>;

    /**
     * Create a DelegationSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DelegationSetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DelegationSetArgs | DelegationSetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DelegationSetState | undefined;
            inputs["nameServers"] = state ? state.nameServers : undefined;
            inputs["referenceName"] = state ? state.referenceName : undefined;
        } else {
            const args = argsOrState as DelegationSetArgs | undefined;
            inputs["referenceName"] = args ? args.referenceName : undefined;
            inputs["nameServers"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DelegationSet.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DelegationSet resources.
 */
export interface DelegationSetState {
    /**
     * A list of authoritative name servers for the hosted zone
     * (effectively a list of NS records).
     */
    readonly nameServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * This is a reference name used in Caller Reference
     * (helpful for identifying single delegation set amongst others)
     */
    readonly referenceName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DelegationSet resource.
 */
export interface DelegationSetArgs {
    /**
     * This is a reference name used in Caller Reference
     * (helpful for identifying single delegation set amongst others)
     */
    readonly referenceName?: pulumi.Input<string>;
}
