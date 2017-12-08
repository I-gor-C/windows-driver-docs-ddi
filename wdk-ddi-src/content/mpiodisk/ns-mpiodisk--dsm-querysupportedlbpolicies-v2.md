---
UID: NS.mpiodisk._DSM_QuerySupportedLBPolicies_V2
title: DSM_QuerySupportedLBPolicies_V2
author: windows-driver-content
description: The DSM_QuerySupportedLBPolicies_V2 structure is used to query the list of load balance policies that are supported on the LUN.
old-location: storage\dsm_querysupportedlbpolicies_v2.htm
old-project: storage
ms.assetid: b62f60e2-9a5c-4346-8a77-985873a7ae20
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DSM_QuerySupportedLBPolicies_V2, DSM_QuerySupportedLBPolicies_V2, *PDSM_QuerySupportedLBPolicies_V2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiodisk.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DSM_QuerySupportedLBPolicies_V2
req.alt-loc: mpiodisk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# DSM_QuerySupportedLBPolicies_V2 structure



## -description
<p>The DSM_QuerySupportedLBPolicies_V2 structure is used to query the list of load balance policies that are supported on the LUN. It is basically the same as the DSM_QuerySupportedLBPolicies except that it passes back the supported policies as an array of DSM_Load_Balance_Policy_V2 structures instead of DSM_Load_Balance_Policy structures. The caller must direct the WMI call for querying to a pseudo-LUN that is addressed by the WMI instance name that corresponds to the pseudo-LUN. All DSMs must register and implement this class, even if they do not support any load balance policies for the devices they control.</p>


## -syntax

````
typedef struct _DSM_QuerySupportedLBPolicies_V2 {
  ULONG                      SupportedLBPoliciesCount;
  ULONG                      Reserved;
  DSM_Load_Balance_Policy_V2 Supported_LB_Policies[1];
} DSM_QuerySupportedLBPolicies_V2, *PDSM_QuerySupportedLBPolicies_V2;
````


## -struct-fields
<dl>

### -field SupportedLBPoliciesCount

<dd>
<p>An unsigned 32-bitfield that returns the number of load balance policies that are supported for the LUN by the controlling DSM.</p>
</dd>

### -field Reserved

<dd>
<p>Should be zero.</p>
</dd>

### -field Supported_LB_Policies

<dd>
<p>An array of DSM_Load_Balance_Policy_V2 structures, one for each of the supported load balance policies. The number of array elements will be the same as <i>SupportedLBPoliciesCount</i>. Each element of the array lists the supported load balance policy type. It is not expected that the element return path specifics.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mpiodisk.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>