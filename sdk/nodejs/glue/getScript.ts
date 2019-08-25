// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to generate a Glue script from a Directed Acyclic Graph (DAG).
 * 
 * ## Example Usage
 * 
 * ### Generate Python Script
 * 
 * ```typescript
 * ```
 * 
 * ### Generate Scala Code
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/glue_script.html.markdown.
 */
export function getScript(args: GetScriptArgs, opts?: pulumi.InvokeOptions): Promise<GetScriptResult> & GetScriptResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetScriptResult> = pulumi.runtime.invoke("aws:glue/getScript:getScript", {
        "dagEdges": args.dagEdges,
        "dagNodes": args.dagNodes,
        "language": args.language,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getScript.
 */
export interface GetScriptArgs {
    /**
     * A list of the edges in the DAG. Defined below.
     */
    readonly dagEdges: inputs.glue.GetScriptDagEdge[];
    /**
     * A list of the nodes in the DAG. Defined below.
     */
    readonly dagNodes: inputs.glue.GetScriptDagNode[];
    /**
     * The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.
     */
    readonly language?: string;
}

/**
 * A collection of values returned by getScript.
 */
export interface GetScriptResult {
    readonly dagEdges: outputs.glue.GetScriptDagEdge[];
    readonly dagNodes: outputs.glue.GetScriptDagNode[];
    readonly language?: string;
    /**
     * The Python script generated from the DAG when the `language` argument is set to `PYTHON`.
     */
    readonly pythonScript: string;
    /**
     * The Scala code generated from the DAG when the `language` argument is set to `SCALA`.
     */
    readonly scalaCode: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
