---
UID: NS.mpiodisk._DSM_Load_Balance_Policy_V2
title: DSM_Load_Balance_Policy_V2
author: windows-driver-content
description: The DSM_Load_Balance_Policy_V2 structure is used to represent a load balance policy that is applied to a LUN.
old-location: storage\dsm_load_balance_policy_v2.htm
ms.assetid: b1522320-110c-46dc-be50-df7c05d61351
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
req.alt-api: DSM_Load_Balance_Policy_V2
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
ms.keywords: DSM_Load_Balance_Policy_V2, DSM_Load_Balance_Policy_V2, *PDSM_Load_Balance_Policy_V2
req.iface: 
---

# DSM_Load_Balance_Policy_V2 structure



## -description
<p>The DSM_Load_Balance_Policy_V2 structure is used to represent a load balance policy that is applied to a LUN. It is similar to the DSM_Load_Balance_Policy structure, except that it uses the MPIO_DSM_Path_V2 structure to capture and expose path information.</p>


## -syntax

````
typedef struct _DSM_Load_Balance_Policy_V2 {
  ULONG            Version;
  ULONG            LoadBalancePolicy;
  ULONG            DSMPathCount;
  ULONG            Reserved;
  MPIO_DSM_Path_V2 DSM_Paths[1];
} DSM_Load_Balance_Policy_V2, *PDSM_Load_Balance_Policy_V2;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of WMI class supported. Set to 2.</p>
</dd>

### -field <b>LoadBalancePolicy</b>

<dd>
<p>An unsigned 32-bitfield that represents the load balance policy type that is currently being applied to the LUN if the LUN is being queried, or the new policy to apply to the LUN if the LUN is being set.</p>
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
<p>An array of MPIO_DSM_Path_V2 structures that represent path attributes for each of the LUN's instances.</p>
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