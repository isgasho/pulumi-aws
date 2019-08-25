// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get the Account ID of the [AWS Redshift Service Account](http://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html#db-auditing-enable-logging)
 * in a given region for the purpose of allowing Redshift to store audit data in S3.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/redshift_service_account.html.markdown.
 */
export function getServiceAccount(args?: GetServiceAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceAccountResult> & GetServiceAccountResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetServiceAccountResult> = pulumi.runtime.invoke("aws:redshift/getServiceAccount:getServiceAccount", {
        "region": args.region,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getServiceAccount.
 */
export interface GetServiceAccountArgs {
    /**
     * Name of the region whose AWS Redshift account ID is desired.
     * Defaults to the region from the AWS provider configuration.
     */
    readonly region?: string;
}

/**
 * A collection of values returned by getServiceAccount.
 */
export interface GetServiceAccountResult {
    /**
     * The ARN of the AWS Redshift service account in the selected region.
     */
    readonly arn: string;
    readonly region?: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
