// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates a snapshot copy grant that allows AWS Redshift to encrypt copied snapshots with a customer master key from AWS KMS in a destination region.
 * 
 * Note that the grant must exist in the destination region, and not in the region of the cluster.
 */
export class SnapshotCopyGrant extends pulumi.CustomResource {
    /**
     * Get an existing SnapshotCopyGrant resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotCopyGrantState): SnapshotCopyGrant {
        return new SnapshotCopyGrant(name, <any>state, { id });
    }

    /**
     * The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
     */
    public readonly kmsKeyId: pulumi.Output<string>;
    /**
     * A friendly name for identifying the grant.
     */
    public readonly snapshotCopyGrantName: pulumi.Output<string>;
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a SnapshotCopyGrant resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SnapshotCopyGrantArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SnapshotCopyGrantArgs | SnapshotCopyGrantState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SnapshotCopyGrantState = argsOrState as SnapshotCopyGrantState | undefined;
            inputs["kmsKeyId"] = state ? state.kmsKeyId : undefined;
            inputs["snapshotCopyGrantName"] = state ? state.snapshotCopyGrantName : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as SnapshotCopyGrantArgs | undefined;
            if (!args || args.snapshotCopyGrantName === undefined) {
                throw new Error("Missing required property 'snapshotCopyGrantName'");
            }
            inputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            inputs["snapshotCopyGrantName"] = args ? args.snapshotCopyGrantName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        super("aws:redshift/snapshotCopyGrant:SnapshotCopyGrant", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SnapshotCopyGrant resources.
 */
export interface SnapshotCopyGrantState {
    /**
     * The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * A friendly name for identifying the grant.
     */
    readonly snapshotCopyGrantName?: pulumi.Input<string>;
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a SnapshotCopyGrant resource.
 */
export interface SnapshotCopyGrantArgs {
    /**
     * The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * A friendly name for identifying the grant.
     */
    readonly snapshotCopyGrantName: pulumi.Input<string>;
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
