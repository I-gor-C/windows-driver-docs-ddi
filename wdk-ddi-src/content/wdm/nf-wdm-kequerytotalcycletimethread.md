---
UID: NF.wdm.KeQueryTotalCycleTimeThread
title: KeQueryTotalCycleTimeThread
author: windows-driver-content
description: The KeQueryTotalCycleTimeThread routine returns the accumulated cycle time for the specified thread.
old-location: kernel\kequerytotalcycletimethread_.htm
old-project: kernel
ms.assetid: EC3A5F02-3D04-466E-8EB4-4BDA9CE47886
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeQueryTotalCycleTimeThread
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeQueryTotalCycleTimeThread
req.alt-loc: Wdm.h
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
req.product: Windows 10 or later.
---

# KeQueryTotalCycleTimeThread function



## -description
<p>The <b>KeQueryTotalCycleTimeThread</b> routine returns the accumulated cycle time for the specified thread.</p>


## -syntax

````
ULONG64 KeQueryTotalCycleTimeThread (
  _Inout_ PKTHREAD Thread,
  _Out_   PULONG64 CycleTimeStamp
);
````


## -parameters
<dl>

### -param <i>Thread</i> [in, out]

<dd>
<p>A pointer to a dispatcher object of type KTHREAD.</p>
</dd>

### -param <i>CycleTimeStamp</i> [out]

<dd>
<p>A pointer to the cycle counter value at the time of the query.</p>
</dd>
</dl>

## -returns
<p>The accumulated cycle time for the thread.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>