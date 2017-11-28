---
UID: NS.d3dkmdt._D3DKMDT_2DREGION
title: D3DKMDT_2DREGION
author: windows-driver-content
description: The D3DKMDT_2DREGION structure is used to represent a point or an offset in a two-dimensional space.
old-location: display\d3dkmdt_2dregion.htm
old-project: display
ms.assetid: 24f703c5-d025-4233-a32d-7cb8bcb5c6b7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_2DREGION,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_2DREGION
req.alt-loc: d3dkmdt.h
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

# D3DKMDT_2DREGION structure



## -description
<p>The D3DKMDT_2DREGION structure is used to represent a point or an offset in a two-dimensional space.</p>


## -syntax

````
typedef struct _D3DKMDT_2DREGION {
  UINT cx;
  UINT cy;
} D3DKMDT_2DREGION;
````


## -struct-fields
<dl>

### -field <b>cx</b>

<dd>
<p>The horizontal component of the point or offset.</p>
</dd>

### -field <b>cy</b>

<dd>
<p>The vertical component of the point or offset.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>