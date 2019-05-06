// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an RDS DB option group resource. Documentation of the available options for various RDS engines can be found at:
 * * [MariaDB Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html)
 * * [Microsoft SQL Server Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)
 * * [MySQL Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html)
 * * [Oracle Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.rds.OptionGroup("example", {
 *     engineName: "sqlserver-ee",
 *     majorEngineVersion: "11.00",
 *     options: [
 *         {
 *             optionName: "Timezone",
 *             optionSettings: [{
 *                 name: "TIME_ZONE",
 *                 value: "UTC",
 *             }],
 *         },
 *         {
 *             optionName: "SQLSERVER_BACKUP_RESTORE",
 *             optionSettings: [{
 *                 name: "IAM_ROLE_ARN",
 *                 value: aws_iam_role_example.arn,
 *             }],
 *         },
 *         {
 *             optionName: "TDE",
 *         },
 *     ],
 *     optionGroupDescription: "Terraform Option Group",
 * });
 * ```
 * 
 * > **Note**: Any modifications to the `db_option_group` are set to happen immediately as we default to applying immediately.
 */
export class OptionGroup extends pulumi.CustomResource {
    /**
     * Get an existing OptionGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OptionGroupState, opts?: pulumi.CustomResourceOptions): OptionGroup {
        return new OptionGroup(name, <any>state, { ...opts, id: id });
    }

    /**
     * The ARN of the db option group.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Specifies the name of the engine that this option group should be associated with.
     */
    public readonly engineName!: pulumi.Output<string>;
    /**
     * Specifies the major version of the engine that this option group should be associated with.
     */
    public readonly majorEngineVersion!: pulumi.Output<string>;
    /**
     * The Name of the setting.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.
     */
    public readonly namePrefix!: pulumi.Output<string>;
    /**
     * A list of Options to apply.
     */
    public readonly options!: pulumi.Output<{ dbSecurityGroupMemberships?: string[], optionName: string, optionSettings?: { name: string, value: string }[], port?: number, version?: string, vpcSecurityGroupMemberships?: string[] }[] | undefined>;
    /**
     * The description of the option group. Defaults to "Managed by Terraform".
     */
    public readonly optionGroupDescription!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a OptionGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OptionGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OptionGroupArgs | OptionGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as OptionGroupState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["engineName"] = state ? state.engineName : undefined;
            inputs["majorEngineVersion"] = state ? state.majorEngineVersion : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["namePrefix"] = state ? state.namePrefix : undefined;
            inputs["options"] = state ? state.options : undefined;
            inputs["optionGroupDescription"] = state ? state.optionGroupDescription : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as OptionGroupArgs | undefined;
            if (!args || args.engineName === undefined) {
                throw new Error("Missing required property 'engineName'");
            }
            if (!args || args.majorEngineVersion === undefined) {
                throw new Error("Missing required property 'majorEngineVersion'");
            }
            inputs["engineName"] = args ? args.engineName : undefined;
            inputs["majorEngineVersion"] = args ? args.majorEngineVersion : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["namePrefix"] = args ? args.namePrefix : undefined;
            inputs["options"] = args ? args.options : undefined;
            inputs["optionGroupDescription"] = (args ? args.optionGroupDescription : undefined) || "Managed by Pulumi";
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super("aws:rds/optionGroup:OptionGroup", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OptionGroup resources.
 */
export interface OptionGroupState {
    /**
     * The ARN of the db option group.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * Specifies the name of the engine that this option group should be associated with.
     */
    readonly engineName?: pulumi.Input<string>;
    /**
     * Specifies the major version of the engine that this option group should be associated with.
     */
    readonly majorEngineVersion?: pulumi.Input<string>;
    /**
     * The Name of the setting.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.
     */
    readonly namePrefix?: pulumi.Input<string>;
    /**
     * A list of Options to apply.
     */
    readonly options?: pulumi.Input<pulumi.Input<{ dbSecurityGroupMemberships?: pulumi.Input<pulumi.Input<string>[]>, optionName: pulumi.Input<string>, optionSettings?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, value: pulumi.Input<string> }>[]>, port?: pulumi.Input<number>, version?: pulumi.Input<string>, vpcSecurityGroupMemberships?: pulumi.Input<pulumi.Input<string>[]> }>[]>;
    /**
     * The description of the option group. Defaults to "Managed by Terraform".
     */
    readonly optionGroupDescription?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a OptionGroup resource.
 */
export interface OptionGroupArgs {
    /**
     * Specifies the name of the engine that this option group should be associated with.
     */
    readonly engineName: pulumi.Input<string>;
    /**
     * Specifies the major version of the engine that this option group should be associated with.
     */
    readonly majorEngineVersion: pulumi.Input<string>;
    /**
     * The Name of the setting.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.
     */
    readonly namePrefix?: pulumi.Input<string>;
    /**
     * A list of Options to apply.
     */
    readonly options?: pulumi.Input<pulumi.Input<{ dbSecurityGroupMemberships?: pulumi.Input<pulumi.Input<string>[]>, optionName: pulumi.Input<string>, optionSettings?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, value: pulumi.Input<string> }>[]>, port?: pulumi.Input<number>, version?: pulumi.Input<string>, vpcSecurityGroupMemberships?: pulumi.Input<pulumi.Input<string>[]> }>[]>;
    /**
     * The description of the option group. Defaults to "Managed by Terraform".
     */
    readonly optionGroupDescription?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
