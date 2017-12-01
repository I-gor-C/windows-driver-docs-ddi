---
UID: NS.mpiodisk._DsmSetLoadBalancePolicy_OUT
title: DsmSetLoadBalancePolicy_OUT
author: windows-driver-content
description: The DsmSetLoadBalancePolicy_OUT structure reports the output parameter of the DsmSetLoadBalancePolicy method.
old-location: storage\dsmsetloadbalancepolicy_out.htm
old-project: storage
ms.assetid: d3479656-310f-4e2d-a671-296bc3e2f1ab
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DsmSetLoadBalancePolicy_OUT, DsmSetLoadBalancePolicy_OUT, *PDsmSetLoadBalancePolicy_OUT
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
req.alt-api: DsmSetLoadBalancePolicy_OUT
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

# DsmSetLoadBalancePolicy_OUT structure



## -description
<p>The <b>DsmSetLoadBalancePolicy_OUT</b> structure reports the output parameter of the <a href="storage.dsmsetloadbalancepolicy">DsmSetLoadBalancePolicy</a> method.</p>


## -syntax

````
typedef struct _DsmSetLoadBalancePolicy_OUT {
  ULONG Status;
} DsmSetLoadBalancePolicy_OUT, *PDsmSetLoadBalancePolicy_OUT;
````


## -struct-fields
<dl>

### -field <b>Status</b>

<dd>
<p>The status of the <a href="storage.dsmsetloadbalancepolicy">DsmSetLoadBalancePolicy</a> operation.</p>
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