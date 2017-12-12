---
UID: NS.MPIODISK._DSM_QUERYLBPOLICY
title: _DSM_QueryLBPolicy
author: windows-driver-content
description: The DSM_QueryLBPolicy structure is used to query a LUN's current load balance policy.
old-location: storage\dsm_querylbpolicy.htm
old-project: storage
ms.assetid: f2ac985a-8fcb-48ad-b100-4137b5b1a777
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _DSM_QueryLBPolicy, DSM_QueryLBPolicy, *PDSM_QueryLBPolicy
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
---

# _DSM_QueryLBPolicy structure



## -description
The DSM_QueryLBPolicy structure is used to query a LUN's current load balance policy.



## -syntax

````
typedef struct _DSM_QueryLBPolicy {
  DSM_Load_Balance_Policy LoadBalancePolicy;
} DSM_QueryLBPolicy, *PDSM_QueryLBPolicy;
````


## -struct-fields

### -field LoadBalancePolicy

An instance of a DSM_Load_Balance_Policy structure that has information about the current load balance policy that is being applied by the DSM on the targeted pseudo-LUN.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Mpiodisk.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>