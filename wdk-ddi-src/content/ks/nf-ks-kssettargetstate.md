---
UID: NF.ks.KsSetTargetState
title: KsSetTargetState
author: windows-driver-content
description: Sets the enabled state of a target device associated with the specified object header.
old-location: stream\kssettargetstate.htm
old-project: stream
ms.assetid: 36f14936-8cc6-4488-aa0f-343e4fbb84e3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsSetTargetState
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
req.alt-api: KsSetTargetState
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

# KsSetTargetState function



## -description
<p>Sets the enabled state of a target device associated with the specified object header.</p>


## -syntax

````
VOID KsSetTargetState(
  _In_ KSOBJECT_HEADER Header,
  _In_ KSTARGET_STATE  TargetState
);
````


## -parameters
<dl>

### -param Header [in]

<dd>
<p>Points to a header previously allocated by <a href="..\ks\nf-ks-ksallocatedeviceheader.md">KsAllocateDeviceHeader</a>.</p>
</dd>

### -param TargetState [in]

<dd>
<p>Contains the new state of the target associated with this object header. This may be either KSTARGET_STATE_DISABLED or KSTARGET_STATE_ENABLED.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Assumes that such a target has been set with <a href="..\ks\nf-ks-kssettargetdeviceobject.md">KsSetTargetDeviceObject</a>. The target is initially disabled, and is ignored when recalculating stack depth. For WDM Streaming devices, this is called on a transition back to a Stop state, after having enabled the target and used <a href="..\ks\nf-ks-ksrecalculatestackdepth.md">KsRecalculateStackDepth</a> on a transition to Acquire state. This allows the stack depth to be minimized.</p>

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