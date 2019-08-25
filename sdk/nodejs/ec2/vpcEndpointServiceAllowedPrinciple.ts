// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a resource to allow a principal to discover a VPC endpoint service.
 * 
 * > **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** This provider provides
 * both a standalone VPC Endpoint Service Allowed Principal resource
 * and a VPC Endpoint Service resource with an `allowedPrincipals` attribute. Do not use the same principal ARN in both
 * a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
 * and will overwrite the association.
 * 
 * ## Example Usage
 * 
 * Basic usage:
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/vpc_endpoint_service_allowed_principal.html.markdown.
 */
export class VpcEndpointServiceAllowedPrinciple extends pulumi.CustomResource {
    /**
     * Get an existing VpcEndpointServiceAllowedPrinciple resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VpcEndpointServiceAllowedPrincipleState, opts?: pulumi.CustomResourceOptions): VpcEndpointServiceAllowedPrinciple {
        return new VpcEndpointServiceAllowedPrinciple(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/vpcEndpointServiceAllowedPrinciple:VpcEndpointServiceAllowedPrinciple';

    /**
     * Returns true if the given object is an instance of VpcEndpointServiceAllowedPrinciple.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VpcEndpointServiceAllowedPrinciple {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VpcEndpointServiceAllowedPrinciple.__pulumiType;
    }

    /**
     * The ARN of the principal to allow permissions.
     */
    public readonly principalArn!: pulumi.Output<string>;
    /**
     * The ID of the VPC endpoint service to allow permission.
     */
    public readonly vpcEndpointServiceId!: pulumi.Output<string>;

    /**
     * Create a VpcEndpointServiceAllowedPrinciple resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VpcEndpointServiceAllowedPrincipleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VpcEndpointServiceAllowedPrincipleArgs | VpcEndpointServiceAllowedPrincipleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VpcEndpointServiceAllowedPrincipleState | undefined;
            inputs["principalArn"] = state ? state.principalArn : undefined;
            inputs["vpcEndpointServiceId"] = state ? state.vpcEndpointServiceId : undefined;
        } else {
            const args = argsOrState as VpcEndpointServiceAllowedPrincipleArgs | undefined;
            if (!args || args.principalArn === undefined) {
                throw new Error("Missing required property 'principalArn'");
            }
            if (!args || args.vpcEndpointServiceId === undefined) {
                throw new Error("Missing required property 'vpcEndpointServiceId'");
            }
            inputs["principalArn"] = args ? args.principalArn : undefined;
            inputs["vpcEndpointServiceId"] = args ? args.vpcEndpointServiceId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(VpcEndpointServiceAllowedPrinciple.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VpcEndpointServiceAllowedPrinciple resources.
 */
export interface VpcEndpointServiceAllowedPrincipleState {
    /**
     * The ARN of the principal to allow permissions.
     */
    readonly principalArn?: pulumi.Input<string>;
    /**
     * The ID of the VPC endpoint service to allow permission.
     */
    readonly vpcEndpointServiceId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VpcEndpointServiceAllowedPrinciple resource.
 */
export interface VpcEndpointServiceAllowedPrincipleArgs {
    /**
     * The ARN of the principal to allow permissions.
     */
    readonly principalArn: pulumi.Input<string>;
    /**
     * The ID of the VPC endpoint service to allow permission.
     */
    readonly vpcEndpointServiceId: pulumi.Input<string>;
}
