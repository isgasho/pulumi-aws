// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Gets the contents of the specified Systems Manager document.
 * 
 * ## Example Usage
 * 
 * To get the contents of the document owned by AWS.
 * 
 * ```typescript
 * ```
 * To get the contents of the custom document.
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ssm_document.html.markdown.
 */
export function getDocument(args: GetDocumentArgs, opts?: pulumi.InvokeOptions): Promise<GetDocumentResult> & GetDocumentResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetDocumentResult> = pulumi.runtime.invoke("aws:ssm/getDocument:getDocument", {
        "documentFormat": args.documentFormat,
        "documentVersion": args.documentVersion,
        "name": args.name,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getDocument.
 */
export interface GetDocumentArgs {
    /**
     * Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.
     */
    readonly documentFormat?: string;
    /**
     * The document version for which you want information.
     */
    readonly documentVersion?: string;
    /**
     * The name of the Systems Manager document.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getDocument.
 */
export interface GetDocumentResult {
    /**
     * The ARN of the document.
     */
    readonly arn: string;
    /**
     * The contents of the document.
     */
    readonly content: string;
    readonly documentFormat?: string;
    /**
     * The type of the document.
     */
    readonly documentType: string;
    readonly documentVersion?: string;
    readonly name: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
