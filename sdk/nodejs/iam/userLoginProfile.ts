// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an IAM User Login Profile with limited support for password creation during this provider resource creation. Uses PGP to encrypt the password for safe transport to the user. PGP keys can be obtained from Keybase.
 * 
 * > To reset an IAM User login password via this provider, you can use delete and recreate this resource or change any of the arguments.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_user_login_profile.html.markdown.
 */
export class UserLoginProfile extends pulumi.CustomResource {
    /**
     * Get an existing UserLoginProfile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserLoginProfileState, opts?: pulumi.CustomResourceOptions): UserLoginProfile {
        return new UserLoginProfile(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:iam/userLoginProfile:UserLoginProfile';

    /**
     * Returns true if the given object is an instance of UserLoginProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserLoginProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserLoginProfile.__pulumiType;
    }

    /**
     * The encrypted password, base64 encoded. Only available if password was handled on this provider resource creation, not import.
     */
    public /*out*/ readonly encryptedPassword!: pulumi.Output<string>;
    /**
     * The fingerprint of the PGP key used to encrypt the password. Only available if password was handled on this provider resource creation, not import.
     */
    public /*out*/ readonly keyFingerprint!: pulumi.Output<string>;
    /**
     * The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    public readonly passwordLength!: pulumi.Output<number | undefined>;
    /**
     * Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    public readonly passwordResetRequired!: pulumi.Output<boolean | undefined>;
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    public readonly pgpKey!: pulumi.Output<string>;
    /**
     * The IAM user's name.
     */
    public readonly user!: pulumi.Output<string>;

    /**
     * Create a UserLoginProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserLoginProfileArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserLoginProfileArgs | UserLoginProfileState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as UserLoginProfileState | undefined;
            inputs["encryptedPassword"] = state ? state.encryptedPassword : undefined;
            inputs["keyFingerprint"] = state ? state.keyFingerprint : undefined;
            inputs["passwordLength"] = state ? state.passwordLength : undefined;
            inputs["passwordResetRequired"] = state ? state.passwordResetRequired : undefined;
            inputs["pgpKey"] = state ? state.pgpKey : undefined;
            inputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as UserLoginProfileArgs | undefined;
            if (!args || args.pgpKey === undefined) {
                throw new Error("Missing required property 'pgpKey'");
            }
            if (!args || args.user === undefined) {
                throw new Error("Missing required property 'user'");
            }
            inputs["passwordLength"] = args ? args.passwordLength : undefined;
            inputs["passwordResetRequired"] = args ? args.passwordResetRequired : undefined;
            inputs["pgpKey"] = args ? args.pgpKey : undefined;
            inputs["user"] = args ? args.user : undefined;
            inputs["encryptedPassword"] = undefined /*out*/;
            inputs["keyFingerprint"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(UserLoginProfile.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering UserLoginProfile resources.
 */
export interface UserLoginProfileState {
    /**
     * The encrypted password, base64 encoded. Only available if password was handled on this provider resource creation, not import.
     */
    readonly encryptedPassword?: pulumi.Input<string>;
    /**
     * The fingerprint of the PGP key used to encrypt the password. Only available if password was handled on this provider resource creation, not import.
     */
    readonly keyFingerprint?: pulumi.Input<string>;
    /**
     * The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    readonly passwordLength?: pulumi.Input<number>;
    /**
     * Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    readonly passwordResetRequired?: pulumi.Input<boolean>;
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    readonly pgpKey?: pulumi.Input<string>;
    /**
     * The IAM user's name.
     */
    readonly user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a UserLoginProfile resource.
 */
export interface UserLoginProfileArgs {
    /**
     * The length of the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    readonly passwordLength?: pulumi.Input<number>;
    /**
     * Whether the user should be forced to reset the generated password on resource creation. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    readonly passwordResetRequired?: pulumi.Input<boolean>;
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`. Only applies on resource creation. Drift detection is not possible with this argument.
     */
    readonly pgpKey: pulumi.Input<string>;
    /**
     * The IAM user's name.
     */
    readonly user: pulumi.Input<string>;
}
