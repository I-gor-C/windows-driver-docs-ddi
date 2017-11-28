---
UID: NS.d3dkmddi._DXGKARG_UPDATEHWCONTEXTSTATE
title: DXGKARG_UPDATEHWCONTEXTSTATE
author: windows-driver-content
description: Used to update the context state.
old-location: display\dxgkarg_updatehwcontextstate.htm
old-project: display
ms.assetid: 39BF7EBF-DD13-41F0-9F54-78E5D82CAB4F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_UPDATEHWCONTEXTSTATE, DXGKARG_UPDATEHWCONTEXTSTATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_UPDATEHWCONTEXTSTATE
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGKARG_UPDATEHWCONTEXTSTATE structure



## -description
<p>Used to update the context state.</p>


## -syntax

````
typedef struct _DXGKARG_UPDATEHWCONTEXTSTATE {
  HANDLE                          hHwContext;
  UINT64                          ContextSwitchFence;
  UINT                            Priority;
  DXGK_UPDATEHWCONTEXTSTATE_FLAGS Flags;
} DXGKARG_UPDATEHWCONTEXTSTATE;
````


## -struct-fields
<dl>

### -field <b>hHwContext</b>

<dd>
<p>The hardware context whose priority or execution state is being changed.</p>
</dd>

### -field <b>ContextSwitchFence</b>

<dd>
<p>Context switch fence value associated with this state change request.</p>
</dd>

### -field <b>Priority</b>

<dd>
<p>Execution priority of this context relative to other running contexts on this node.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Context execution state flags.
</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>