---
UID: NS.d3d12umddi.D3D12DDI_VIEW_INSTANCE_LOCATION
title: D3D12DDI_VIEW_INSTANCE_LOCATION
author: windows-driver-content
description: View instance location.
old-location: display\d3d12ddi-view-instance-location.htm
ms.assetid: 1b31ac34-233b-4246-a1c3-d0aac0f35db6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIEW_INSTANCE_LOCATION
req.alt-loc: d3d12umddi.h
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
ms.keywords: D3D12DDI_VIEW_INSTANCE_LOCATION, D3D12DDI_VIEW_INSTANCE_LOCATION
req.iface: 
---

# D3D12DDI_VIEW_INSTANCE_LOCATION structure



## -description
<p>View instance location.</p>


## -syntax

````
typedef struct _D3D12DDI_VIEW_INSTANCE_LOCATION {
  UINT  ViewportArrayIndex;
  UINT  RenderTargetArrayIndex;
} D3D12DDI_VIEW_INSTANCE_LOCATION, D3D12DDI_VIEW_INSTANCE_LOCATION;
````


## -struct-fields
<dl>

### -field <b>ViewportArrayIndex</b>

<dd>
<p>Viewport array index.</p>
</dd>

### -field <b>RenderTargetArrayIndex</b>

<dd>
<p>Render target array index.</p>
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
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>