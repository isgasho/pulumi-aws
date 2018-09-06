// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.
 * 
 * For more details, see the [Amazon Kinesis Firehose Documentation][1].
 */
export class FirehoseDeliveryStream extends pulumi.CustomResource {
    /**
     * Get an existing FirehoseDeliveryStream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirehoseDeliveryStreamState): FirehoseDeliveryStream {
        return new FirehoseDeliveryStream(name, <any>state, { id });
    }

    /**
     * The Amazon Resource Name (ARN) specifying the Stream
     */
    public readonly arn: pulumi.Output<string>;
    /**
     * This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
     */
    public readonly destination: pulumi.Output<string>;
    public readonly destinationId: pulumi.Output<string>;
    public readonly elasticsearchConfiguration: pulumi.Output<{ bufferingInterval?: number, bufferingSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }, domainArn: string, indexName: string, indexRotationPeriod?: string, processingConfiguration?: { enabled?: boolean, processors?: { parameters?: { parameterName: string, parameterValue: string }[], type: string }[] }, retryDuration?: number, roleArn: string, s3BackupMode?: string, typeName?: string } | undefined>;
    /**
     * Enhanced configuration options for the s3 destination. More details are given below.
     */
    public readonly extendedS3Configuration: pulumi.Output<{ bucketArn: string, bufferInterval?: number, bufferSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }, compressionFormat?: string, dataFormatConversionConfiguration?: { enabled?: boolean, inputFormatConfiguration: { deserializer: { hiveJsonSerDe?: { timestampFormats?: string[] }, openXJsonSerDe?: { caseInsensitive?: boolean, columnToJsonKeyMappings?: {[key: string]: string}, convertDotsInJsonKeysToUnderscores?: boolean } } }, outputFormatConfiguration: { serializer: { orcSerDe?: { blockSizeBytes?: number, bloomFilterColumns?: string[], bloomFilterFalsePositiveProbability?: number, compression?: string, dictionaryKeyThreshold?: number, enablePadding?: boolean, formatVersion?: string, paddingTolerance?: number, rowIndexStride?: number, stripeSizeBytes?: number }, parquetSerDe?: { blockSizeBytes?: number, compression?: string, enableDictionaryCompression?: boolean, maxPaddingBytes?: number, pageSizeBytes?: number, writerVersion?: string } } }, schemaConfiguration: { catalogId: string, databaseName: string, region: string, roleArn: string, tableName: string, versionId?: string } }, kmsKeyArn?: string, prefix?: string, processingConfiguration?: { enabled?: boolean, processors?: { parameters?: { parameterName: string, parameterValue: string }[], type: string }[] }, roleArn: string, s3BackupConfiguration?: { bucketArn: string, bufferInterval?: number, bufferSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }, compressionFormat?: string, kmsKeyArn?: string, prefix?: string, roleArn: string }, s3BackupMode?: string } | undefined>;
    /**
     * Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
     */
    public readonly kinesisSourceConfiguration: pulumi.Output<{ kinesisStreamArn: string, roleArn: string } | undefined>;
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Configuration options if redshift is the destination.
     * Using `redshift_configuration` requires the user to also specify a
     * `s3_configuration` block. More details are given below.
     */
    public readonly redshiftConfiguration: pulumi.Output<{ cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }, clusterJdbcurl: string, copyOptions?: string, dataTableColumns?: string, dataTableName: string, password: string, processingConfiguration?: { enabled?: boolean, processors?: { parameters?: { parameterName: string, parameterValue: string }[], type: string }[] }, retryDuration?: number, roleArn: string, s3BackupConfiguration?: { bucketArn: string, bufferInterval?: number, bufferSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }, compressionFormat?: string, kmsKeyArn?: string, prefix?: string, roleArn: string }, s3BackupMode?: string, username: string } | undefined>;
    /**
     * Configuration options for the s3 destination (or the intermediate bucket if the destination
     * is redshift). More details are given below.
     */
    public readonly s3Configuration: pulumi.Output<{ bucketArn: string, bufferInterval?: number, bufferSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }, compressionFormat?: string, kmsKeyArn?: string, prefix?: string, roleArn: string } | undefined>;
    public readonly splunkConfiguration: pulumi.Output<{ cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }, hecAcknowledgmentTimeout?: number, hecEndpoint: string, hecEndpointType?: string, hecToken: string, processingConfiguration?: { enabled?: boolean, processors?: { parameters?: { parameterName: string, parameterValue: string }[], type: string }[] }, retryDuration?: number, s3BackupMode?: string } | undefined>;
    /**
     * Specifies the table version for the output data schema. Defaults to `LATEST`.
     */
    public readonly versionId: pulumi.Output<string>;

    /**
     * Create a FirehoseDeliveryStream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FirehoseDeliveryStreamArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FirehoseDeliveryStreamArgs | FirehoseDeliveryStreamState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: FirehoseDeliveryStreamState = argsOrState as FirehoseDeliveryStreamState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["destination"] = state ? state.destination : undefined;
            inputs["destinationId"] = state ? state.destinationId : undefined;
            inputs["elasticsearchConfiguration"] = state ? state.elasticsearchConfiguration : undefined;
            inputs["extendedS3Configuration"] = state ? state.extendedS3Configuration : undefined;
            inputs["kinesisSourceConfiguration"] = state ? state.kinesisSourceConfiguration : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["redshiftConfiguration"] = state ? state.redshiftConfiguration : undefined;
            inputs["s3Configuration"] = state ? state.s3Configuration : undefined;
            inputs["splunkConfiguration"] = state ? state.splunkConfiguration : undefined;
            inputs["versionId"] = state ? state.versionId : undefined;
        } else {
            const args = argsOrState as FirehoseDeliveryStreamArgs | undefined;
            if (!args || args.destination === undefined) {
                throw new Error("Missing required property 'destination'");
            }
            inputs["arn"] = args ? args.arn : undefined;
            inputs["destination"] = args ? args.destination : undefined;
            inputs["destinationId"] = args ? args.destinationId : undefined;
            inputs["elasticsearchConfiguration"] = args ? args.elasticsearchConfiguration : undefined;
            inputs["extendedS3Configuration"] = args ? args.extendedS3Configuration : undefined;
            inputs["kinesisSourceConfiguration"] = args ? args.kinesisSourceConfiguration : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["redshiftConfiguration"] = args ? args.redshiftConfiguration : undefined;
            inputs["s3Configuration"] = args ? args.s3Configuration : undefined;
            inputs["splunkConfiguration"] = args ? args.splunkConfiguration : undefined;
            inputs["versionId"] = args ? args.versionId : undefined;
        }
        super("aws:kinesis/firehoseDeliveryStream:FirehoseDeliveryStream", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FirehoseDeliveryStream resources.
 */
export interface FirehoseDeliveryStreamState {
    /**
     * The Amazon Resource Name (ARN) specifying the Stream
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
     */
    readonly destination?: pulumi.Input<string>;
    readonly destinationId?: pulumi.Input<string>;
    readonly elasticsearchConfiguration?: pulumi.Input<{ bufferingInterval?: pulumi.Input<number>, bufferingSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, domainArn: pulumi.Input<string>, indexName: pulumi.Input<string>, indexRotationPeriod?: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, retryDuration?: pulumi.Input<number>, roleArn: pulumi.Input<string>, s3BackupMode?: pulumi.Input<string>, typeName?: pulumi.Input<string> }>;
    /**
     * Enhanced configuration options for the s3 destination. More details are given below.
     */
    readonly extendedS3Configuration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, dataFormatConversionConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, inputFormatConfiguration: pulumi.Input<{ deserializer: pulumi.Input<{ hiveJsonSerDe?: pulumi.Input<{ timestampFormats?: pulumi.Input<pulumi.Input<string>[]> }>, openXJsonSerDe?: pulumi.Input<{ caseInsensitive?: pulumi.Input<boolean>, columnToJsonKeyMappings?: pulumi.Input<{[key: string]: pulumi.Input<string>}>, convertDotsInJsonKeysToUnderscores?: pulumi.Input<boolean> }> }> }>, outputFormatConfiguration: pulumi.Input<{ serializer: pulumi.Input<{ orcSerDe?: pulumi.Input<{ blockSizeBytes?: pulumi.Input<number>, bloomFilterColumns?: pulumi.Input<pulumi.Input<string>[]>, bloomFilterFalsePositiveProbability?: pulumi.Input<number>, compression?: pulumi.Input<string>, dictionaryKeyThreshold?: pulumi.Input<number>, enablePadding?: pulumi.Input<boolean>, formatVersion?: pulumi.Input<string>, paddingTolerance?: pulumi.Input<number>, rowIndexStride?: pulumi.Input<number>, stripeSizeBytes?: pulumi.Input<number> }>, parquetSerDe?: pulumi.Input<{ blockSizeBytes?: pulumi.Input<number>, compression?: pulumi.Input<string>, enableDictionaryCompression?: pulumi.Input<boolean>, maxPaddingBytes?: pulumi.Input<number>, pageSizeBytes?: pulumi.Input<number>, writerVersion?: pulumi.Input<string> }> }> }>, schemaConfiguration: pulumi.Input<{ catalogId?: pulumi.Input<string>, databaseName: pulumi.Input<string>, region?: pulumi.Input<string>, roleArn: pulumi.Input<string>, tableName: pulumi.Input<string>, versionId?: pulumi.Input<string> }> }>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, roleArn: pulumi.Input<string>, s3BackupConfiguration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, roleArn: pulumi.Input<string> }>, s3BackupMode?: pulumi.Input<string> }>;
    /**
     * Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
     */
    readonly kinesisSourceConfiguration?: pulumi.Input<{ kinesisStreamArn: pulumi.Input<string>, roleArn: pulumi.Input<string> }>;
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Configuration options if redshift is the destination.
     * Using `redshift_configuration` requires the user to also specify a
     * `s3_configuration` block. More details are given below.
     */
    readonly redshiftConfiguration?: pulumi.Input<{ cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, clusterJdbcurl: pulumi.Input<string>, copyOptions?: pulumi.Input<string>, dataTableColumns?: pulumi.Input<string>, dataTableName: pulumi.Input<string>, password: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, retryDuration?: pulumi.Input<number>, roleArn: pulumi.Input<string>, s3BackupConfiguration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, roleArn: pulumi.Input<string> }>, s3BackupMode?: pulumi.Input<string>, username: pulumi.Input<string> }>;
    /**
     * Configuration options for the s3 destination (or the intermediate bucket if the destination
     * is redshift). More details are given below.
     */
    readonly s3Configuration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, roleArn: pulumi.Input<string> }>;
    readonly splunkConfiguration?: pulumi.Input<{ cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, hecAcknowledgmentTimeout?: pulumi.Input<number>, hecEndpoint: pulumi.Input<string>, hecEndpointType?: pulumi.Input<string>, hecToken: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, retryDuration?: pulumi.Input<number>, s3BackupMode?: pulumi.Input<string> }>;
    /**
     * Specifies the table version for the output data schema. Defaults to `LATEST`.
     */
    readonly versionId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FirehoseDeliveryStream resource.
 */
export interface FirehoseDeliveryStreamArgs {
    /**
     * The Amazon Resource Name (ARN) specifying the Stream
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, `elasticsearch`, and `splunk`.
     */
    readonly destination: pulumi.Input<string>;
    readonly destinationId?: pulumi.Input<string>;
    readonly elasticsearchConfiguration?: pulumi.Input<{ bufferingInterval?: pulumi.Input<number>, bufferingSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, domainArn: pulumi.Input<string>, indexName: pulumi.Input<string>, indexRotationPeriod?: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, retryDuration?: pulumi.Input<number>, roleArn: pulumi.Input<string>, s3BackupMode?: pulumi.Input<string>, typeName?: pulumi.Input<string> }>;
    /**
     * Enhanced configuration options for the s3 destination. More details are given below.
     */
    readonly extendedS3Configuration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, dataFormatConversionConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, inputFormatConfiguration: pulumi.Input<{ deserializer: pulumi.Input<{ hiveJsonSerDe?: pulumi.Input<{ timestampFormats?: pulumi.Input<pulumi.Input<string>[]> }>, openXJsonSerDe?: pulumi.Input<{ caseInsensitive?: pulumi.Input<boolean>, columnToJsonKeyMappings?: pulumi.Input<{[key: string]: pulumi.Input<string>}>, convertDotsInJsonKeysToUnderscores?: pulumi.Input<boolean> }> }> }>, outputFormatConfiguration: pulumi.Input<{ serializer: pulumi.Input<{ orcSerDe?: pulumi.Input<{ blockSizeBytes?: pulumi.Input<number>, bloomFilterColumns?: pulumi.Input<pulumi.Input<string>[]>, bloomFilterFalsePositiveProbability?: pulumi.Input<number>, compression?: pulumi.Input<string>, dictionaryKeyThreshold?: pulumi.Input<number>, enablePadding?: pulumi.Input<boolean>, formatVersion?: pulumi.Input<string>, paddingTolerance?: pulumi.Input<number>, rowIndexStride?: pulumi.Input<number>, stripeSizeBytes?: pulumi.Input<number> }>, parquetSerDe?: pulumi.Input<{ blockSizeBytes?: pulumi.Input<number>, compression?: pulumi.Input<string>, enableDictionaryCompression?: pulumi.Input<boolean>, maxPaddingBytes?: pulumi.Input<number>, pageSizeBytes?: pulumi.Input<number>, writerVersion?: pulumi.Input<string> }> }> }>, schemaConfiguration: pulumi.Input<{ catalogId?: pulumi.Input<string>, databaseName: pulumi.Input<string>, region?: pulumi.Input<string>, roleArn: pulumi.Input<string>, tableName: pulumi.Input<string>, versionId?: pulumi.Input<string> }> }>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, roleArn: pulumi.Input<string>, s3BackupConfiguration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, roleArn: pulumi.Input<string> }>, s3BackupMode?: pulumi.Input<string> }>;
    /**
     * Allows the ability to specify the kinesis stream that is used as the source of the firehose delivery stream.
     */
    readonly kinesisSourceConfiguration?: pulumi.Input<{ kinesisStreamArn: pulumi.Input<string>, roleArn: pulumi.Input<string> }>;
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Configuration options if redshift is the destination.
     * Using `redshift_configuration` requires the user to also specify a
     * `s3_configuration` block. More details are given below.
     */
    readonly redshiftConfiguration?: pulumi.Input<{ cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, clusterJdbcurl: pulumi.Input<string>, copyOptions?: pulumi.Input<string>, dataTableColumns?: pulumi.Input<string>, dataTableName: pulumi.Input<string>, password: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, retryDuration?: pulumi.Input<number>, roleArn: pulumi.Input<string>, s3BackupConfiguration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, roleArn: pulumi.Input<string> }>, s3BackupMode?: pulumi.Input<string>, username: pulumi.Input<string> }>;
    /**
     * Configuration options for the s3 destination (or the intermediate bucket if the destination
     * is redshift). More details are given below.
     */
    readonly s3Configuration?: pulumi.Input<{ bucketArn: pulumi.Input<string>, bufferInterval?: pulumi.Input<number>, bufferSize?: pulumi.Input<number>, cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, compressionFormat?: pulumi.Input<string>, kmsKeyArn?: pulumi.Input<string>, prefix?: pulumi.Input<string>, roleArn: pulumi.Input<string> }>;
    readonly splunkConfiguration?: pulumi.Input<{ cloudwatchLoggingOptions?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, logGroupName?: pulumi.Input<string>, logStreamName?: pulumi.Input<string> }>, hecAcknowledgmentTimeout?: pulumi.Input<number>, hecEndpoint: pulumi.Input<string>, hecEndpointType?: pulumi.Input<string>, hecToken: pulumi.Input<string>, processingConfiguration?: pulumi.Input<{ enabled?: pulumi.Input<boolean>, processors?: pulumi.Input<pulumi.Input<{ parameters?: pulumi.Input<pulumi.Input<{ parameterName: pulumi.Input<string>, parameterValue: pulumi.Input<string> }>[]>, type: pulumi.Input<string> }>[]> }>, retryDuration?: pulumi.Input<number>, s3BackupMode?: pulumi.Input<string> }>;
    /**
     * Specifies the table version for the output data schema. Defaults to `LATEST`.
     */
    readonly versionId?: pulumi.Input<string>;
}
