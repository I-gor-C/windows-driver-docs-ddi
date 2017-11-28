---
UID: NS.d3dkmddi._DXGKARG_GETPOSTCOMPOSITIONCAPS
title: DXGKARG_GETPOSTCOMPOSITIONCAPS
author: windows-driver-content
description: Arguments for the DxgkDdiGetPostCompositionCaps function.
old-location: display\dxgkarg_getpostcompositioncaps.htm
old-project: display
ms.assetid: 0C8A0F83-9D12-46F1-A8B1-3BCF219A3BF7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_GETPOSTCOMPOSITIONCAPS, DXGKARG_GETPOSTCOMPOSITIONCAPS
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
req.alt-api: DXGKARG_GETPOSTCOMPOSITIONCAPS
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

# DXGKARG_GETPOSTCOMPOSITIONCAPS structure



## -description
<p>Arguments for the DxgkDdiGetPostCompositionCaps function.</p>


## -syntax

````
typedef struct _DXGKARG_GETPOSTCOMPOSITIONCAPS {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  float                          MaxStretchFactor;
  float                          MaxShrinkFactor;
} DXGKARG_GETPOSTCOMPOSITIONCAPS;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] Indicates the VidPn source for which post composition capabilities are queried.</p>
</dd>

### -field <b>MaxStretchFactor</b>

<dd>
<p>[out] Indicates the maximum stretch factor that can be applied.</p>
</dd>

### -field <b>MaxShrinkFactor</b>

<dd>
<p>[out] Indicates the maximum shrink factor that can be applied.</p>
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