// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.CodeDeploy.Outputs
{

    [OutputType]
    public sealed class DeploymentConfigTrafficRoutingConfigTimeBasedLinear
    {
        /// <summary>
        /// The number of minutes between each incremental traffic shift of a `TimeBasedLinear` deployment.
        /// </summary>
        public readonly int? Interval;
        /// <summary>
        /// The percentage of traffic that is shifted at the start of each increment of a `TimeBasedLinear` deployment.
        /// </summary>
        public readonly int? Percentage;

        [OutputConstructor]
        private DeploymentConfigTrafficRoutingConfigTimeBasedLinear(
            int? interval,

            int? percentage)
        {
            Interval = interval;
            Percentage = percentage;
        }
    }
}