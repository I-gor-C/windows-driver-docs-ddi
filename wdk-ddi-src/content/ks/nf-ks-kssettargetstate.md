---
UID: NF.ks.KsSetTargetState
title: KsSetTargetState function
author: windows-driver-content
description: Sets the enabled state of a target device associated with the specified object header.
old-location: stream\kssettargetstate.htm
old-project: stream
ms.assetid: 36f14936-8cc6-4488-aa0f-343e4fbb84e3
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
---

# KsSetTargetState function



## -description
Sets the enabled state of a target device associated with the specified object header.


## -syntax

````
VOID KsSetTargetState(
  _In_ KSOBJECT_HEADER Header,
  _In_ KSTARGET_STATE  TargetState
);
````


## -parameters

### -param Header [in]

Points to a header previously allocated by <a href="stream.ksallocatedeviceheader">KsAllocateDeviceHeader</a>.

### -param TargetState [in]

Contains the new state of the target associated with this object header. This may be either KSTARGET_STATE_DISABLED or KSTARGET_STATE_ENABLED.

## -returns
None.

## -remarks
Assumes that such a target has been set with <a href="stream.kssettargetdeviceobject">KsSetTargetDeviceObject</a>. The target is initially disabled, and is ignored when recalculating stack depth. For WDM Streaming devices, this is called on a transition back to a Stop state, after having enabled the target and used <a href="stream.ksrecalculatestackdepth">KsRecalculateStackDepth</a> on a transition to Acquire state. This allows the stack depth to be minimized.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>