---
UID: NF.ks.KsFreeDefaultClock
title: KsFreeDefaultClock
author: windows-driver-content
description: The KsFreeDefaultClock function frees a default clock structure previously allocated with KsAllocateDefaultClock, taking into account any currently running timer DPCs.
old-location: stream\ksfreedefaultclock.htm
old-project: stream
ms.assetid: e2fc87c9-e48f-4e18-ae1b-52a7cc701e91
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsFreeDefaultClock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFreeDefaultClock
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsFreeDefaultClock function



## -description
<p>The <b>KsFreeDefaultClock</b> function frees a default clock structure previously allocated with <a href="..\ks\nf-ks-ksallocatedefaultclock.md">KsAllocateDefaultClock</a>, taking into account any currently running timer DPCs. This assumes that all instances of the clock have been closed. This may actually just decrement the internal reference counter and allow a pending DPC to free the structure asynchronously.</p>
<p>This may only be called at PASSIVE_LEVEL.</p>


## -syntax

````
VOID KsFreeDefaultClock(
  _In_ PKSDEFAULTCLOCK DefaultClock
);
````


## -parameters
<dl>

### -param <i>DefaultClock</i> [in]

<dd>
<p>Specifies the previously allocated structure to free.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>