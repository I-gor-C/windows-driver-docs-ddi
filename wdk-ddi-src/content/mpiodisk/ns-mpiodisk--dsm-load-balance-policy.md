---
UID: NS.mpiodisk._DSM_Load_Balance_Policy
title: DSM_Load_Balance_Policy
author: windows-driver-content
description: The DSM_Load_Balance_Policy structure is used to represent a load balance policy that is applied to a LUN.
old-location: storage\dsm_load_balance_policy.htm
old-project: storage
ms.assetid: 4338e496-99e8-47d2-ba97-ce661c9cb025
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DSM_Load_Balance_Policy, DSM_Load_Balance_Policy, *PDSM_Load_Balance_Policy
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
req.alt-api: DSM_Load_Balance_Policy
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

# DSM_Load_Balance_Policy structure



## -description
<p>The DSM_Load_Balance_Policy structure is used to represent a load balance policy that is applied to a LUN.</p>


## -syntax

````
typedef struct _DSM_Load_Balance_Policy {
  ULONG         Version;
  ULONG         LoadBalancePolicy;
  ULONG         DSMPathCount;
  ULONG         Reserved;
  MPIO_DSM_Path DSM_Paths[1];
} DSM_Load_Balance_Policy, *PDSM_Load_Balance_Policy;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of WMI class supported. Set to 1.</p>
</dd>

### -field <b>LoadBalancePolicy</b>

<dd>
<p>An unsigned 32-bitfield that represents the load balance policy type that is currently being applied to the LUN if the LUN is queried, or the new policy to apply to the LUN if the LUN is being set.</p>
</dd>

### -field <b>DSMPathCount</b>

<dd>
<p>An unsigned 32-bitfield that represents the number of paths that expose the LUN's instances.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>DSM_Paths</b>

<dd>
<p>An array of MPIO_DSM_Path structures that represent path attributes for each of the LUN's instances.</p>
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