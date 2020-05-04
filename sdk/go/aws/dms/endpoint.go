// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dms

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.
//
// > **Note:** All arguments including the password will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
type Endpoint struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) for the certificate.
	CertificateArn pulumi.StringOutput `pulumi:"certificateArn"`
	// The name of the endpoint database.
	DatabaseName pulumi.StringPtrOutput `pulumi:"databaseName"`
	// Configuration block with Elasticsearch settings. Detailed below.
	ElasticsearchSettings EndpointElasticsearchSettingsPtrOutput `pulumi:"elasticsearchSettings"`
	// The Amazon Resource Name (ARN) for the endpoint.
	EndpointArn pulumi.StringOutput `pulumi:"endpointArn"`
	// The database endpoint identifier.
	EndpointId pulumi.StringOutput `pulumi:"endpointId"`
	// The type of endpoint. Can be one of `source | target`.
	EndpointType pulumi.StringOutput `pulumi:"endpointType"`
	// The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
	EngineName pulumi.StringOutput `pulumi:"engineName"`
	// Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
	ExtraConnectionAttributes pulumi.StringOutput `pulumi:"extraConnectionAttributes"`
	// Configuration block with Kafka settings. Detailed below.
	KafkaSettings EndpointKafkaSettingsPtrOutput `pulumi:"kafkaSettings"`
	// Configuration block with Kinesis settings. Detailed below.
	KinesisSettings EndpointKinesisSettingsPtrOutput `pulumi:"kinesisSettings"`
	// The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
	KmsKeyArn pulumi.StringOutput `pulumi:"kmsKeyArn"`
	// Configuration block with MongoDB settings. Detailed below.
	MongodbSettings EndpointMongodbSettingsPtrOutput `pulumi:"mongodbSettings"`
	// The password to be used to login to the endpoint database.
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// The port used by the endpoint database.
	Port pulumi.IntPtrOutput `pulumi:"port"`
	// Configuration block with S3 settings. Detailed below.
	S3Settings EndpointS3SettingsPtrOutput `pulumi:"s3Settings"`
	// The host name of the server.
	ServerName pulumi.StringPtrOutput `pulumi:"serverName"`
	// The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
	ServiceAccessRole pulumi.StringPtrOutput `pulumi:"serviceAccessRole"`
	// The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
	SslMode pulumi.StringOutput `pulumi:"sslMode"`
	// A map of tags to assign to the resource.
	Tags pulumi.MapOutput `pulumi:"tags"`
	// The user name to be used to login to the endpoint database.
	Username pulumi.StringPtrOutput `pulumi:"username"`
}

// NewEndpoint registers a new resource with the given unique name, arguments, and options.
func NewEndpoint(ctx *pulumi.Context,
	name string, args *EndpointArgs, opts ...pulumi.ResourceOption) (*Endpoint, error) {
	if args == nil || args.EndpointId == nil {
		return nil, errors.New("missing required argument 'EndpointId'")
	}
	if args == nil || args.EndpointType == nil {
		return nil, errors.New("missing required argument 'EndpointType'")
	}
	if args == nil || args.EngineName == nil {
		return nil, errors.New("missing required argument 'EngineName'")
	}
	if args == nil {
		args = &EndpointArgs{}
	}
	var resource Endpoint
	err := ctx.RegisterResource("aws:dms/endpoint:Endpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEndpoint gets an existing Endpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EndpointState, opts ...pulumi.ResourceOption) (*Endpoint, error) {
	var resource Endpoint
	err := ctx.ReadResource("aws:dms/endpoint:Endpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Endpoint resources.
type endpointState struct {
	// The Amazon Resource Name (ARN) for the certificate.
	CertificateArn *string `pulumi:"certificateArn"`
	// The name of the endpoint database.
	DatabaseName *string `pulumi:"databaseName"`
	// Configuration block with Elasticsearch settings. Detailed below.
	ElasticsearchSettings *EndpointElasticsearchSettings `pulumi:"elasticsearchSettings"`
	// The Amazon Resource Name (ARN) for the endpoint.
	EndpointArn *string `pulumi:"endpointArn"`
	// The database endpoint identifier.
	EndpointId *string `pulumi:"endpointId"`
	// The type of endpoint. Can be one of `source | target`.
	EndpointType *string `pulumi:"endpointType"`
	// The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
	EngineName *string `pulumi:"engineName"`
	// Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
	ExtraConnectionAttributes *string `pulumi:"extraConnectionAttributes"`
	// Configuration block with Kafka settings. Detailed below.
	KafkaSettings *EndpointKafkaSettings `pulumi:"kafkaSettings"`
	// Configuration block with Kinesis settings. Detailed below.
	KinesisSettings *EndpointKinesisSettings `pulumi:"kinesisSettings"`
	// The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
	KmsKeyArn *string `pulumi:"kmsKeyArn"`
	// Configuration block with MongoDB settings. Detailed below.
	MongodbSettings *EndpointMongodbSettings `pulumi:"mongodbSettings"`
	// The password to be used to login to the endpoint database.
	Password *string `pulumi:"password"`
	// The port used by the endpoint database.
	Port *int `pulumi:"port"`
	// Configuration block with S3 settings. Detailed below.
	S3Settings *EndpointS3Settings `pulumi:"s3Settings"`
	// The host name of the server.
	ServerName *string `pulumi:"serverName"`
	// The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
	ServiceAccessRole *string `pulumi:"serviceAccessRole"`
	// The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
	SslMode *string `pulumi:"sslMode"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
	// The user name to be used to login to the endpoint database.
	Username *string `pulumi:"username"`
}

type EndpointState struct {
	// The Amazon Resource Name (ARN) for the certificate.
	CertificateArn pulumi.StringPtrInput
	// The name of the endpoint database.
	DatabaseName pulumi.StringPtrInput
	// Configuration block with Elasticsearch settings. Detailed below.
	ElasticsearchSettings EndpointElasticsearchSettingsPtrInput
	// The Amazon Resource Name (ARN) for the endpoint.
	EndpointArn pulumi.StringPtrInput
	// The database endpoint identifier.
	EndpointId pulumi.StringPtrInput
	// The type of endpoint. Can be one of `source | target`.
	EndpointType pulumi.StringPtrInput
	// The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
	EngineName pulumi.StringPtrInput
	// Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
	ExtraConnectionAttributes pulumi.StringPtrInput
	// Configuration block with Kafka settings. Detailed below.
	KafkaSettings EndpointKafkaSettingsPtrInput
	// Configuration block with Kinesis settings. Detailed below.
	KinesisSettings EndpointKinesisSettingsPtrInput
	// The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
	KmsKeyArn pulumi.StringPtrInput
	// Configuration block with MongoDB settings. Detailed below.
	MongodbSettings EndpointMongodbSettingsPtrInput
	// The password to be used to login to the endpoint database.
	Password pulumi.StringPtrInput
	// The port used by the endpoint database.
	Port pulumi.IntPtrInput
	// Configuration block with S3 settings. Detailed below.
	S3Settings EndpointS3SettingsPtrInput
	// The host name of the server.
	ServerName pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
	ServiceAccessRole pulumi.StringPtrInput
	// The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
	SslMode pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
	// The user name to be used to login to the endpoint database.
	Username pulumi.StringPtrInput
}

func (EndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointState)(nil)).Elem()
}

type endpointArgs struct {
	// The Amazon Resource Name (ARN) for the certificate.
	CertificateArn *string `pulumi:"certificateArn"`
	// The name of the endpoint database.
	DatabaseName *string `pulumi:"databaseName"`
	// Configuration block with Elasticsearch settings. Detailed below.
	ElasticsearchSettings *EndpointElasticsearchSettings `pulumi:"elasticsearchSettings"`
	// The database endpoint identifier.
	EndpointId string `pulumi:"endpointId"`
	// The type of endpoint. Can be one of `source | target`.
	EndpointType string `pulumi:"endpointType"`
	// The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
	EngineName string `pulumi:"engineName"`
	// Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
	ExtraConnectionAttributes *string `pulumi:"extraConnectionAttributes"`
	// Configuration block with Kafka settings. Detailed below.
	KafkaSettings *EndpointKafkaSettings `pulumi:"kafkaSettings"`
	// Configuration block with Kinesis settings. Detailed below.
	KinesisSettings *EndpointKinesisSettings `pulumi:"kinesisSettings"`
	// The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
	KmsKeyArn *string `pulumi:"kmsKeyArn"`
	// Configuration block with MongoDB settings. Detailed below.
	MongodbSettings *EndpointMongodbSettings `pulumi:"mongodbSettings"`
	// The password to be used to login to the endpoint database.
	Password *string `pulumi:"password"`
	// The port used by the endpoint database.
	Port *int `pulumi:"port"`
	// Configuration block with S3 settings. Detailed below.
	S3Settings *EndpointS3Settings `pulumi:"s3Settings"`
	// The host name of the server.
	ServerName *string `pulumi:"serverName"`
	// The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
	ServiceAccessRole *string `pulumi:"serviceAccessRole"`
	// The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
	SslMode *string `pulumi:"sslMode"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
	// The user name to be used to login to the endpoint database.
	Username *string `pulumi:"username"`
}

// The set of arguments for constructing a Endpoint resource.
type EndpointArgs struct {
	// The Amazon Resource Name (ARN) for the certificate.
	CertificateArn pulumi.StringPtrInput
	// The name of the endpoint database.
	DatabaseName pulumi.StringPtrInput
	// Configuration block with Elasticsearch settings. Detailed below.
	ElasticsearchSettings EndpointElasticsearchSettingsPtrInput
	// The database endpoint identifier.
	EndpointId pulumi.StringInput
	// The type of endpoint. Can be one of `source | target`.
	EndpointType pulumi.StringInput
	// The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
	EngineName pulumi.StringInput
	// Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
	ExtraConnectionAttributes pulumi.StringPtrInput
	// Configuration block with Kafka settings. Detailed below.
	KafkaSettings EndpointKafkaSettingsPtrInput
	// Configuration block with Kinesis settings. Detailed below.
	KinesisSettings EndpointKinesisSettingsPtrInput
	// The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kmsKeyArn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
	KmsKeyArn pulumi.StringPtrInput
	// Configuration block with MongoDB settings. Detailed below.
	MongodbSettings EndpointMongodbSettingsPtrInput
	// The password to be used to login to the endpoint database.
	Password pulumi.StringPtrInput
	// The port used by the endpoint database.
	Port pulumi.IntPtrInput
	// Configuration block with S3 settings. Detailed below.
	S3Settings EndpointS3SettingsPtrInput
	// The host name of the server.
	ServerName pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
	ServiceAccessRole pulumi.StringPtrInput
	// The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
	SslMode pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
	// The user name to be used to login to the endpoint database.
	Username pulumi.StringPtrInput
}

func (EndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointArgs)(nil)).Elem()
}
