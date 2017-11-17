---
UID: NS.mpiodisk._DSM_QueryLBPolicy
title: DSM_QueryLBPolicy
author: windows-driver-content
description: The DSM_QueryLBPolicy structure is used to query a LUN's current load balance policy.
old-location: storage\dsm_querylbpolicy.htm
ms.assetid: f2ac985a-8fcb-48ad-b100-4137b5b1a777
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mpiodisk.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DSM_QueryLBPolicy
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
ms.keywords: DSM_QueryLBPolicy, DSM_QueryLBPolicy, *PDSM_QueryLBPolicy
req.iface: 
---

# DSM_QueryLBPolicy structure



## -description
<p>The DSM_QueryLBPolicy structure is used to query a LUN's current load balance policy.</p>


## -syntax

````
typedef struct _DSM_QueryLBPolicy {
  DSM_Load_Balance_Policy LoadBalancePolicy;
} DSM_QueryLBPolicy, *PDSM_QueryLBPolicy;
````


## -struct-fields
<dl>

### -field <b>LoadBalancePolicy</b>

<dd>
<p>An instance of a DSM_Load_Balance_Policy structure that has information about the current load balance policy that is being applied by the DSM on the targeted pseudo-LUN.</p>
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