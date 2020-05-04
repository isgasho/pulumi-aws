// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Dms.Outputs
{

    [OutputType]
    public sealed class EndpointMongodbSettings
    {
        /// <summary>
        /// Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
        /// </summary>
        public readonly string? AuthMechanism;
        /// <summary>
        /// Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
        /// </summary>
        public readonly string? AuthSource;
        /// <summary>
        /// Authentication type to access the MongoDB source endpoint. Defaults to `password`.
        /// </summary>
        public readonly string? AuthType;
        /// <summary>
        /// Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
        /// </summary>
        public readonly string? DocsToInvestigate;
        /// <summary>
        /// Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
        /// </summary>
        public readonly string? ExtractDocId;
        /// <summary>
        /// Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).
        /// </summary>
        public readonly string? NestingLevel;

        [OutputConstructor]
        private EndpointMongodbSettings(
            string? authMechanism,

            string? authSource,

            string? authType,

            string? docsToInvestigate,

            string? extractDocId,

            string? nestingLevel)
        {
            AuthMechanism = authMechanism;
            AuthSource = authSource;
            AuthType = authType;
            DocsToInvestigate = docsToInvestigate;
            ExtractDocId = extractDocId;
            NestingLevel = nestingLevel;
        }
    }
}
