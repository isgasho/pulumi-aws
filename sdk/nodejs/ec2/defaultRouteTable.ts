// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a resource to manage a Default VPC Routing Table.
 * 
 * Each VPC created in AWS comes with a Default Route Table that can be managed, but not
 * destroyed. **This is an advanced resource**, and has special caveats to be aware
 * of when using it. Please read this document in its entirety before using this
 * resource. It is recommended you **do not** use both `aws.ec2.DefaultRouteTable` to
 * manage the default route table **and** use the `aws.ec2.MainRouteTableAssociation`,
 * due to possible conflict in routes.
 * 
 * The `aws.ec2.DefaultRouteTable` behaves differently from normal resources, in that
 * this provider does not _create_ this resource, but instead attempts to "adopt" it
 * into management. We can do this because each VPC created has a Default Route
 * Table that cannot be destroyed, and is created with a single route.
 * 
 * When this provider first adopts the Default Route Table, it **immediately removes all
 * defined routes**. It then proceeds to create any routes specified in the
 * configuration. This step is required so that only the routes specified in the
 * configuration present in the Default Route Table.
 * 
 * For more information about Route Tables, see the AWS Documentation on
 * [Route Tables][aws-route-tables].
 * 
 * For more information about managing normal Route Tables in this provider, see our
 * documentation on [aws.ec2.RouteTable][tf-route-tables].
 * 
 * > **NOTE on Route Tables and Routes:** This provider currently
 * provides both a standalone Route resource and a Route Table resource with routes
 * defined in-line. At this time you cannot use a Route Table with in-line routes
 * in conjunction with any Route resources. Doing so will cause
 * a conflict of rule settings and will overwrite routes.
 * 
 * 
 * ## Example usage with tags:
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_route_table.html.markdown.
 */
export class DefaultRouteTable extends pulumi.CustomResource {
    /**
     * Get an existing DefaultRouteTable resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultRouteTableState, opts?: pulumi.CustomResourceOptions): DefaultRouteTable {
        return new DefaultRouteTable(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/defaultRouteTable:DefaultRouteTable';

    /**
     * Returns true if the given object is an instance of DefaultRouteTable.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DefaultRouteTable {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DefaultRouteTable.__pulumiType;
    }

    /**
     * The ID of the Default Routing Table.
     */
    public readonly defaultRouteTableId!: pulumi.Output<string>;
    /**
     * The ID of the AWS account that owns the route table
     */
    public /*out*/ readonly ownerId!: pulumi.Output<string>;
    /**
     * A list of virtual gateways for propagation.
     */
    public readonly propagatingVgws!: pulumi.Output<string[] | undefined>;
    /**
     * A list of route objects. Their keys are documented below.
     * This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    public readonly routes!: pulumi.Output<outputs.ec2.DefaultRouteTableRoute[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    public /*out*/ readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a DefaultRouteTable resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DefaultRouteTableArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DefaultRouteTableArgs | DefaultRouteTableState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DefaultRouteTableState | undefined;
            inputs["defaultRouteTableId"] = state ? state.defaultRouteTableId : undefined;
            inputs["ownerId"] = state ? state.ownerId : undefined;
            inputs["propagatingVgws"] = state ? state.propagatingVgws : undefined;
            inputs["routes"] = state ? state.routes : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as DefaultRouteTableArgs | undefined;
            if (!args || args.defaultRouteTableId === undefined) {
                throw new Error("Missing required property 'defaultRouteTableId'");
            }
            inputs["defaultRouteTableId"] = args ? args.defaultRouteTableId : undefined;
            inputs["propagatingVgws"] = args ? args.propagatingVgws : undefined;
            inputs["routes"] = args ? args.routes : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["ownerId"] = undefined /*out*/;
            inputs["vpcId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DefaultRouteTable.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DefaultRouteTable resources.
 */
export interface DefaultRouteTableState {
    /**
     * The ID of the Default Routing Table.
     */
    readonly defaultRouteTableId?: pulumi.Input<string>;
    /**
     * The ID of the AWS account that owns the route table
     */
    readonly ownerId?: pulumi.Input<string>;
    /**
     * A list of virtual gateways for propagation.
     */
    readonly propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of route objects. Their keys are documented below.
     * This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    readonly routes?: pulumi.Input<pulumi.Input<inputs.ec2.DefaultRouteTableRoute>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    readonly vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DefaultRouteTable resource.
 */
export interface DefaultRouteTableArgs {
    /**
     * The ID of the Default Routing Table.
     */
    readonly defaultRouteTableId: pulumi.Input<string>;
    /**
     * A list of virtual gateways for propagation.
     */
    readonly propagatingVgws?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A list of route objects. Their keys are documented below.
     * This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
     */
    readonly routes?: pulumi.Input<pulumi.Input<inputs.ec2.DefaultRouteTableRoute>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
