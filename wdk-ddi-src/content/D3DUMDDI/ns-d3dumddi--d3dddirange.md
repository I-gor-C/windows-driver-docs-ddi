---
UID: NS.d3dumddi._D3DDDIRANGE
title: D3DDDIRANGE
author: windows-driver-content
description: Specifies a range of memory within a buffer.
old-location: display\d3dddirange.htm
ms.assetid: 3A64DB04-EDAE-419C-947B-67201ECA8068
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIRANGE
req.alt-loc: D3dumddi.h
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
ms.keywords: D3DDDIRANGE, D3DDDIRANGE
req.iface: 
---

# D3DDDIRANGE structure



## -description
<p>Specifies a range of memory within a buffer.</p>


## -syntax

````
typedef struct _D3DDDIRANGE {
  UINT Offset;
  UINT Size;
} D3DDDIRANGE;
````


## -struct-fields
<dl>

### -field <b>Offset</b>

<dd>
<p>An offset, in bytes, from the start of the buffer.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of a block of memory that begins at the buffer location specified by the <b>Offset</b> member.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>