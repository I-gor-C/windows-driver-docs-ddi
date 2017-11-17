---
UID: NS.mpiowmi._SetDSMCounters_IN
title: SetDSMCounters_IN
author: windows-driver-content
description: The SetDSMCounters_IN structure is used to set the timer counters for a particular DSM.
old-location: storage\setdsmcounters_in.htm
ms.assetid: fb8cebec-0cf8-4649-8b91-cd4f9935fac9
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetDSMCounters_IN
req.alt-loc: mpiowmi.h
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
ms.keywords: SetDSMCounters_IN, SetDSMCounters_IN, *PSetDSMCounters_IN
req.iface: 
---

# SetDSMCounters_IN structure



## -description
<p>The SetDSMCounters_IN structure is used to set the timer counters for a particular DSM.</p>


## -syntax

````
typedef struct _SetDSMCounters_IN {
  ULONGLONG    DsmContext;
  DSM_COUNTERS DsmCounters;
} SetDSMCounters_IN, *PSetDSMCounters_IN;
````


## -struct-fields
<dl>

### -field <b>DsmContext</b>

<dd>
<p>A 64-bitfield that provides the DSM context.</p>
</dd>

### -field <b>DsmCounters</b>

<dd>
<p>A structure of type DSM_COUNTERS.</p>
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
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>