---
UID: NS.d3dkmddi._DXGK_UPDATEHWCONTEXTSTATE_FLAGS
title: DXGK_UPDATEHWCONTEXTSTATE_FLAGS
author: windows-driver-content
description: Used to update the HW context state flags.
old-location: display\dxgk_updatehwcontextstate_flags.htm
old-project: display
ms.assetid: 23F0679A-05BB-4988-AF83-B6CC91C4CB79
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_UPDATEHWCONTEXTSTATE_FLAGS, DXGK_UPDATEHWCONTEXTSTATE_FLAGS
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
req.alt-api: DXGK_UPDATEHWCONTEXTSTATE_FLAGS
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

# DXGK_UPDATEHWCONTEXTSTATE_FLAGS structure



## -description
<p>Used to update the HW context state flags.</p>


## -syntax

````
typedef struct _DXGK_UPDATEHWCONTEXTSTATE_FLAGS {
  union {
    struct {
      UINT Suspended;
      UINT InterruptOnSwitchCompletion;
      UINT Reserved;
    };
    UINT Value;
  };
} DXGK_UPDATEHWCONTEXTSTATE_FLAGS;
````


## -struct-fields
<dl>

### -field Suspended

<dd>
<p>Used to suspend the context. Otherwise, the context is runnable.</p>
</dd>

### -field InterruptOnSwitchCompletion

<dd>
<p>Used when the context state update is effective on the GPU.</p>
</dd>

### -field Reserved

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field Value

<dd>
<p>Used to operate over the rest of values.</p>
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