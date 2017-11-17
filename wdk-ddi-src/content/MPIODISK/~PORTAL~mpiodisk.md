# Declarations in the mpiodisk header
This header Mpiodisk contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PDOSCSI_ADDR structure](ns-mpiodisk--pdoscsi-addr.md) | The PDOSCSI_ADDR structure is used to represent a SCSI address. |
| [DSM_QueryUniqueId structure](ns-mpiodisk--dsm-queryuniqueid.md) | The DSM_QueryUniqueId structure is used to query the DSM for a unique identifier. |
| [ClearDevInstanceHealthCounters_IN structure](ns-mpiodisk--cleardevinstancehealthcounters-in.md) | TBD |
| [PDO_INFORMATION structure](ns-mpiodisk--pdo-information.md) | The PDO_INFORMATION structure represents a device-path pairing, which is an instance of a LUN through a particular path. |
| [DsmSetLoadBalancePolicyALUA_OUT structure](ns-mpiodisk--dsmsetloadbalancepolicyalua-out.md) | The DsmSetLoadBalancePolicyALUA_OUT structure reports the output of the DsmSetLoadBalancePolicyALUA method. |
| [DSM_Load_Balance_Policy structure](ns-mpiodisk--dsm-load-balance-policy.md) | The DSM_Load_Balance_Policy structure is used to represent a load balance policy that is applied to a LUN. |
| [MPIO_DEVINSTANCE_HEALTH_INFO structure](ns-mpiodisk--mpio-devinstance-health-info.md) | The MPIO_DEVINSTANCE_HEALTH_INFO structure is used to query the available health information for every instance of a multi-path disk on each of the paths through which it is exposed. |
| [MPIO_DEVINSTANCE_HEALTH_CLASS structure](ns-mpiodisk--mpio-devinstance-health-class.md) | The MPIO_DEVINSTANCE_HEALTH_CLASS structure holds the health information for a instance of a device exposed through the specified path identifiers. |
| [DsmSetLoadBalancePolicy_IN structure](ns-mpiodisk--dsmsetloadbalancepolicy-in.md) | The DsmSetLoadBalancePolicy_IN structure provides an input parameter to the DsmSetLoadBalancePolicy method. |
| [DSM_Load_Balance_Policy_V2 structure](ns-mpiodisk--dsm-load-balance-policy-v2.md) | The DSM_Load_Balance_Policy_V2 structure is used to represent a load balance policy that is applied to a LUN. |
| [DsmSetLoadBalancePolicy_OUT structure](ns-mpiodisk--dsmsetloadbalancepolicy-out.md) | The DsmSetLoadBalancePolicy_OUT structure reports the output parameter of the DsmSetLoadBalancePolicy method. |
| [DsmSetLoadBalancePolicyALUA_IN structure](ns-mpiodisk--dsmsetloadbalancepolicyalua-in.md) | The DsmSetLoadBalancePolicyALUA_IN structure provides the input parameter for the DsmSetLoadBalancePolicyALUA method. |
| [MPIO_DSM_Path_V2 structure](ns-mpiodisk--mpio-dsm-path-v2.md) | The MPIO_DSM_Path_V2 structure is used to represent the DSM's definition of a path. It is a superset of the previously existing MPIO_DSM_Path class. |
| [MPIO_GET_DESCRIPTOR structure](ns-mpiodisk--mpio-get-descriptor.md) | The MPIO_GET_DESCRIPTOR structure is used to query for LUN instances that correspond to various paths. |
| [DSM_QueryLBPolicy structure](ns-mpiodisk--dsm-querylbpolicy.md) | The DSM_QueryLBPolicy structure is used to query a LUN's current load balance policy. |
| [MPIO_DSM_Path structure](ns-mpiodisk--mpio-dsm-path.md) | The MPIO_DSM_Path structure is used to represent the DSM's definition of a path. |
| [DSM_QueryLBPolicy_V2 structure](ns-mpiodisk--dsm-querylbpolicy-v2.md) | The DSM_QueryLBPolicy_V2 structure is used to query a LUN's current load balance policy. It is basically the same as the DSM_QueryLBPolicy structure except that it returns the load balance information by using the DSM_Load_Balance_Policy_V2 structure. |
| [DSM_QuerySupportedLBPolicies structure](ns-mpiodisk--dsm-querysupportedlbpolicies.md) | The DSM_QuerySupportedLBPolicies structure is used to query the list of load balance policies that are supported on the LUN. |
| [DSM_QuerySupportedLBPolicies_V2 structure](ns-mpiodisk--dsm-querysupportedlbpolicies-v2.md) | The DSM_QuerySupportedLBPolicies_V2 structure is used to query the list of load balance policies that are supported on the LUN. |

This header is used in these topics:

- [Storage](..content/_Storage)
