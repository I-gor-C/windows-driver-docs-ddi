---
UID: NS.mpiodisk._DsmSetLoadBalancePolicy_IN
title: DsmSetLoadBalancePolicy_IN
author: windows-driver-content
description: The DsmSetLoadBalancePolicy_IN structure provides an input parameter to the DsmSetLoadBalancePolicy method.
old-location: storage\dsmsetloadbalancepolicy_in.htm
old-project: storage
ms.assetid: 1a249c0e-1b8d-4c50-9b01-03bfe84e0937
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DsmSetLoadBalancePolicy_IN, DsmSetLoadBalancePolicy_IN, *PDsmSetLoadBalancePolicy_IN
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
req.alt-api: DsmSetLoadBalancePolicy_IN
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

# DsmSetLoadBalancePolicy_IN structure



## -description
<p>The DsmSetLoadBalancePolicy_IN structure provides an input parameter to the DsmSetLoadBalancePolicy method.</p>


## -syntax

````
typedef struct _DsmSetLoadBalancePolicy_IN {
  DSM_Load_Balance_Policy LoadBalancePolicy;
} DsmSetLoadBalancePolicy_IN, *PDsmSetLoadBalancePolicy_IN;
````


## -struct-fields
<dl>

### -field <b>LoadBalancePolicy</b>

<dd>
<p>A structure of type DSM_Load_Balance_Policy.</p>
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