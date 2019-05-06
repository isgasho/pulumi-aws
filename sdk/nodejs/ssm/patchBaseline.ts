// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an SSM Patch Baseline resource
 * 
 * > **NOTE on Patch Baselines:** The `approved_patches` and `approval_rule` are 
 * both marked as optional fields, but the Patch Baseline requires that at least one
 * of them is specified.
 * 
 * ## Example Usage
 * 
 * Basic usage using `approved_patches` only
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const production = new aws.ssm.PatchBaseline("production", {
 *     approvedPatches: ["KB123456"],
 * });
 * ```
 * 
 * Advanced usage, specifying patch filters
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const production = new aws.ssm.PatchBaseline("production", {
 *     approvalRules: [
 *         {
 *             approveAfterDays: 7,
 *             complianceLevel: "HIGH",
 *             patchFilters: [
 *                 {
 *                     key: "PRODUCT",
 *                     values: ["WindowsServer2016"],
 *                 },
 *                 {
 *                     key: "CLASSIFICATION",
 *                     values: [
 *                         "CriticalUpdates",
 *                         "SecurityUpdates",
 *                         "Updates",
 *                     ],
 *                 },
 *                 {
 *                     key: "MSRC_SEVERITY",
 *                     values: [
 *                         "Critical",
 *                         "Important",
 *                         "Moderate",
 *                     ],
 *                 },
 *             ],
 *         },
 *         {
 *             approveAfterDays: 7,
 *             patchFilters: [{
 *                 key: "PRODUCT",
 *                 values: ["WindowsServer2012"],
 *             }],
 *         },
 *     ],
 *     approvedPatches: [
 *         "KB123456",
 *         "KB456789",
 *     ],
 *     description: "Patch Baseline Description",
 *     globalFilters: [
 *         {
 *             key: "PRODUCT",
 *             values: ["WindowsServer2008"],
 *         },
 *         {
 *             key: "CLASSIFICATION",
 *             values: ["ServicePacks"],
 *         },
 *         {
 *             key: "MSRC_SEVERITY",
 *             values: ["Low"],
 *         },
 *     ],
 *     rejectedPatches: ["KB987654"],
 * });
 * ```
 */
export class PatchBaseline extends pulumi.CustomResource {
    /**
     * Get an existing PatchBaseline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PatchBaselineState, opts?: pulumi.CustomResourceOptions): PatchBaseline {
        return new PatchBaseline(name, <any>state, { ...opts, id: id });
    }

    /**
     * A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.
     */
    public readonly approvalRules!: pulumi.Output<{ approveAfterDays: number, complianceLevel?: string, enableNonSecurity?: boolean, patchFilters: { key: string, values: string[] }[] }[] | undefined>;
    /**
     * A list of explicitly approved patches for the baseline.
     */
    public readonly approvedPatches!: pulumi.Output<string[] | undefined>;
    /**
     * Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.
     */
    public readonly approvedPatchesComplianceLevel!: pulumi.Output<string | undefined>;
    /**
     * The description of the patch baseline.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.
     */
    public readonly globalFilters!: pulumi.Output<{ key: string, values: string[] }[] | undefined>;
    /**
     * The name of the patch baseline.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.
     */
    public readonly operatingSystem!: pulumi.Output<string | undefined>;
    /**
     * A list of rejected patches.
     */
    public readonly rejectedPatches!: pulumi.Output<string[] | undefined>;
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a PatchBaseline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PatchBaselineArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PatchBaselineArgs | PatchBaselineState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PatchBaselineState | undefined;
            inputs["approvalRules"] = state ? state.approvalRules : undefined;
            inputs["approvedPatches"] = state ? state.approvedPatches : undefined;
            inputs["approvedPatchesComplianceLevel"] = state ? state.approvedPatchesComplianceLevel : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["globalFilters"] = state ? state.globalFilters : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["operatingSystem"] = state ? state.operatingSystem : undefined;
            inputs["rejectedPatches"] = state ? state.rejectedPatches : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as PatchBaselineArgs | undefined;
            inputs["approvalRules"] = args ? args.approvalRules : undefined;
            inputs["approvedPatches"] = args ? args.approvedPatches : undefined;
            inputs["approvedPatchesComplianceLevel"] = args ? args.approvedPatchesComplianceLevel : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["globalFilters"] = args ? args.globalFilters : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["operatingSystem"] = args ? args.operatingSystem : undefined;
            inputs["rejectedPatches"] = args ? args.rejectedPatches : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super("aws:ssm/patchBaseline:PatchBaseline", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PatchBaseline resources.
 */
export interface PatchBaselineState {
    /**
     * A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.
     */
    readonly approvalRules?: pulumi.Input<pulumi.Input<{ approveAfterDays: pulumi.Input<number>, complianceLevel?: pulumi.Input<string>, enableNonSecurity?: pulumi.Input<boolean>, patchFilters: pulumi.Input<pulumi.Input<{ key: pulumi.Input<string>, values: pulumi.Input<pulumi.Input<string>[]> }>[]> }>[]>;
    /**
     * A list of explicitly approved patches for the baseline.
     */
    readonly approvedPatches?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.
     */
    readonly approvedPatchesComplianceLevel?: pulumi.Input<string>;
    /**
     * The description of the patch baseline.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.
     */
    readonly globalFilters?: pulumi.Input<pulumi.Input<{ key: pulumi.Input<string>, values: pulumi.Input<pulumi.Input<string>[]> }>[]>;
    /**
     * The name of the patch baseline.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.
     */
    readonly operatingSystem?: pulumi.Input<string>;
    /**
     * A list of rejected patches.
     */
    readonly rejectedPatches?: pulumi.Input<pulumi.Input<string>[]>;
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a PatchBaseline resource.
 */
export interface PatchBaselineArgs {
    /**
     * A set of rules used to include patches in the baseline. up to 10 approval rules can be specified. Each approval_rule block requires the fields documented below.
     */
    readonly approvalRules?: pulumi.Input<pulumi.Input<{ approveAfterDays: pulumi.Input<number>, complianceLevel?: pulumi.Input<string>, enableNonSecurity?: pulumi.Input<boolean>, patchFilters: pulumi.Input<pulumi.Input<{ key: pulumi.Input<string>, values: pulumi.Input<pulumi.Input<string>[]> }>[]> }>[]>;
    /**
     * A list of explicitly approved patches for the baseline.
     */
    readonly approvedPatches?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.
     */
    readonly approvedPatchesComplianceLevel?: pulumi.Input<string>;
    /**
     * The description of the patch baseline.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A set of global filters used to exclude patches from the baseline. Up to 4 global filters can be specified using Key/Value pairs. Valid Keys are `PRODUCT | CLASSIFICATION | MSRC_SEVERITY | PATCH_ID`.
     */
    readonly globalFilters?: pulumi.Input<pulumi.Input<{ key: pulumi.Input<string>, values: pulumi.Input<pulumi.Input<string>[]> }>[]>;
    /**
     * The name of the patch baseline.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.
     */
    readonly operatingSystem?: pulumi.Input<string>;
    /**
     * A list of rejected patches.
     */
    readonly rejectedPatches?: pulumi.Input<pulumi.Input<string>[]>;
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
