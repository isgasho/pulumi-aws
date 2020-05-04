// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Lambda.Outputs
{

    [OutputType]
    public sealed class EventSourceMappingDestinationConfig
    {
        /// <summary>
        /// The destination configuration for failed invocations. Detailed below.
        /// </summary>
        public readonly Outputs.EventSourceMappingDestinationConfigOnFailure? OnFailure;

        [OutputConstructor]
        private EventSourceMappingDestinationConfig(Outputs.EventSourceMappingDestinationConfigOnFailure? onFailure)
        {
            OnFailure = onFailure;
        }
    }
}