---
UID: NS.d3d12umddi.D3D12DDI_VIEW_INSTANCING_DESC
title: D3D12DDI_VIEW_INSTANCING_DESC
author: windows-driver-content
description: View instancing description.
old-location: display\d3d12ddi-view-instancing-desc.htm
ms.assetid: 4d942de6-d829-499c-80cf-3cff8266aee4
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
req.alt-api: D3D12DDI_VIEW_INSTANCING_DESC
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
ms.keywords: D3D12DDI_VIEW_INSTANCING_DESC, D3D12DDI_VIEW_INSTANCING_DESC
req.iface: 
---

# D3D12DDI_VIEW_INSTANCING_DESC structure



## -description
<p>View instancing description.</p>


## -syntax

````
typedef struct _D3D12DDI_VIEW_INSTANCING_DESC {
  UINT                                     ViewInstanceCount;
  const D3D12DDI_VIEW_INSTANCE_LOCATION *  pViewInstanceLocations;
  D3D12DDI_VIEW_INSTANCING_FLAGS           Flags;
} D3D12DDI_VIEW_INSTANCING_DESC, D3D12DDI_VIEW_INSTANCING_DESC;
````


## -struct-fields
<dl>

### -field <b>ViewInstanceCount</b>

<dd>
<p>View instance count.</p>
</dd>

### -field <b>pViewInstanceLocations</b>

<dd>
<p>View instance locations.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags.</p>
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