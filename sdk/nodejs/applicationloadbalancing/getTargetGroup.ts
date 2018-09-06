// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * ~> **Note:** `aws_alb_target_group` is known as `aws_lb_target_group`. The functionality is identical.
 * 
 * Provides information about a Load Balancer Target Group.
 * 
 * This data source can prove useful when a module accepts an LB Target Group as an
 * input variable and needs to know its attributes. It can also be used to get the ARN of
 * an LB Target Group for use in other resources, given LB Target Group name.
 */
export function getTargetGroup(args?: GetTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetTargetGroupResult> {
    args = args || {};
    return pulumi.runtime.invoke("aws:applicationloadbalancing/getTargetGroup:getTargetGroup", {
        "arn": args.arn,
        "name": args.name,
        "tags": args.tags,
    }, opts);
}

/**
 * A collection of arguments for invoking getTargetGroup.
 */
export interface GetTargetGroupArgs {
    /**
     * The full ARN of the target group.
     */
    readonly arn?: string;
    /**
     * The unique name of the target group.
     */
    readonly name?: string;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getTargetGroup.
 */
export interface GetTargetGroupResult {
    readonly arn: string;
    readonly arnSuffix: string;
    readonly deregistrationDelay: number;
    readonly healthCheck: { healthyThreshold: number, interval: number, matcher: string, path: string, port: string, protocol: string, timeout: number, unhealthyThreshold: number };
    readonly name: string;
    readonly port: number;
    readonly protocol: string;
    readonly slowStart: number;
    readonly stickiness: { cookieDuration: number, enabled: boolean, type: string };
    readonly tags: {[key: string]: any};
    readonly vpcId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
