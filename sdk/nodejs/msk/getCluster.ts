// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Get information on an Amazon MSK Cluster.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_cluster.html.markdown.
 */
export function getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult> & GetClusterResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetClusterResult> = pulumi.runtime.invoke("aws:msk/getCluster:getCluster", {
        "clusterName": args.clusterName,
        "tags": args.tags,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getCluster.
 */
export interface GetClusterArgs {
    /**
     * Name of the cluster.
     */
    readonly clusterName: string;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getCluster.
 */
export interface GetClusterResult {
    /**
     * Amazon Resource Name (ARN) of the MSK cluster.
     */
    readonly arn: string;
    /**
     * A comma separated list of one or more hostname:port pairs of Kafka brokers suitable to boostrap connectivity to the Kafka cluster.
     */
    readonly bootstrapBrokers: string;
    /**
     * A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster.
     */
    readonly bootstrapBrokersTls: string;
    readonly clusterName: string;
    /**
     * Apache Kafka version.
     */
    readonly kafkaVersion: string;
    /**
     * Number of broker nodes in the cluster.
     */
    readonly numberOfBrokerNodes: number;
    /**
     * Map of key-value pairs assigned to the cluster.
     */
    readonly tags: {[key: string]: any};
    /**
     * A comma separated list of one or more IP:port pairs to use to connect to the Apache Zookeeper cluster.
     */
    readonly zookeeperConnectString: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
