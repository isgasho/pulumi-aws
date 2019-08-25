// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

import {RestApi} from "./restApi";

/**
 * Provides an API Gateway Deployment.
 * 
 * > **Note:** Depends on having `aws.apigateway.Integration` inside your rest api (which in turn depends on `aws.apigateway.Method`). To avoid race conditions
 * you might need to add an explicit `dependsOn = ["aws_api_gateway_integration.name"]`.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_deployment.html.markdown.
 */
export class Deployment extends pulumi.CustomResource {
    /**
     * Get an existing Deployment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentState, opts?: pulumi.CustomResourceOptions): Deployment {
        return new Deployment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:apigateway/deployment:Deployment';

    /**
     * Returns true if the given object is an instance of Deployment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Deployment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Deployment.__pulumiType;
    }

    /**
     * The creation date of the deployment
     */
    public /*out*/ readonly createdDate!: pulumi.Output<string>;
    /**
     * The description of the deployment
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The execution ARN to be used in [`lambdaPermission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `sourceArn`
     * when allowing API Gateway to invoke a Lambda function,
     * e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`
     */
    public /*out*/ readonly executionArn!: pulumi.Output<string>;
    /**
     * The URL to invoke the API pointing to the stage,
     * e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`
     */
    public /*out*/ readonly invokeUrl!: pulumi.Output<string>;
    /**
     * The ID of the associated REST API
     */
    public readonly restApi!: pulumi.Output<RestApi>;
    /**
     * The description of the stage
     */
    public readonly stageDescription!: pulumi.Output<string | undefined>;
    /**
     * The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment.
     */
    public readonly stageName!: pulumi.Output<string | undefined>;
    /**
     * A map that defines variables for the stage
     */
    public readonly variables!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Deployment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeploymentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DeploymentArgs | DeploymentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DeploymentState | undefined;
            inputs["createdDate"] = state ? state.createdDate : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["executionArn"] = state ? state.executionArn : undefined;
            inputs["invokeUrl"] = state ? state.invokeUrl : undefined;
            inputs["restApi"] = state ? state.restApi : undefined;
            inputs["stageDescription"] = state ? state.stageDescription : undefined;
            inputs["stageName"] = state ? state.stageName : undefined;
            inputs["variables"] = state ? state.variables : undefined;
        } else {
            const args = argsOrState as DeploymentArgs | undefined;
            if (!args || args.restApi === undefined) {
                throw new Error("Missing required property 'restApi'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["restApi"] = args ? args.restApi : undefined;
            inputs["stageDescription"] = args ? args.stageDescription : undefined;
            inputs["stageName"] = args ? args.stageName : undefined;
            inputs["variables"] = args ? args.variables : undefined;
            inputs["createdDate"] = undefined /*out*/;
            inputs["executionArn"] = undefined /*out*/;
            inputs["invokeUrl"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Deployment.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Deployment resources.
 */
export interface DeploymentState {
    /**
     * The creation date of the deployment
     */
    readonly createdDate?: pulumi.Input<string>;
    /**
     * The description of the deployment
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The execution ARN to be used in [`lambdaPermission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `sourceArn`
     * when allowing API Gateway to invoke a Lambda function,
     * e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod`
     */
    readonly executionArn?: pulumi.Input<string>;
    /**
     * The URL to invoke the API pointing to the stage,
     * e.g. `https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod`
     */
    readonly invokeUrl?: pulumi.Input<string>;
    /**
     * The ID of the associated REST API
     */
    readonly restApi?: pulumi.Input<RestApi>;
    /**
     * The description of the stage
     */
    readonly stageDescription?: pulumi.Input<string>;
    /**
     * The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment.
     */
    readonly stageName?: pulumi.Input<string>;
    /**
     * A map that defines variables for the stage
     */
    readonly variables?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Deployment resource.
 */
export interface DeploymentArgs {
    /**
     * The description of the deployment
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ID of the associated REST API
     */
    readonly restApi: pulumi.Input<RestApi>;
    /**
     * The description of the stage
     */
    readonly stageDescription?: pulumi.Input<string>;
    /**
     * The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment.
     */
    readonly stageName?: pulumi.Input<string>;
    /**
     * A map that defines variables for the stage
     */
    readonly variables?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
