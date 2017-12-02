---
UID: NE.d3d12umddi.D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032
title: D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032
author: windows-driver-content
description: The write buffer immediate mode.
old-location: display\d3d12ddi-writebufferimmediate-mode-0032.htm
old-project: display
ms.assetid: 4d968e4c-fb5b-47d6-b4ca-5f9d1d9c4739
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032
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
req.iface: 
---

# D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032 enumeration



## -description
<p>The write buffer immediate mode.</p>


## -syntax

````
typedef enum _D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032 { 
  D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_DEFAULT,
  D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_MARKER_IN,
  D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_MARKER_OUT
} D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032;
````


## -enum-fields
<dl>

### -field D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_DEFAULT

<dd>
<p>The write buffer immediate default value is 0x0.</p>
</dd>

### -field D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_MARKER_IN

<dd>
<p>The write buffer immediate mode is marker in, and the value is 0x1.</p>
</dd>

### -field D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_MARKER_OUT

<dd>
<p>The write buffer immediate  mode is marker out, and the value is 0x2.</p>
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