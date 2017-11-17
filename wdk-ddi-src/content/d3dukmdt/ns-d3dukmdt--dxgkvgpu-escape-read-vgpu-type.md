---
UID: NS.d3dukmdt._DXGKVGPU_ESCAPE_READ_VGPU_TYPE
title: DXGKVGPU_ESCAPE_READ_VGPU_TYPE
author: windows-driver-content
description: A structure used to read the VGPU type of an escape.
old-location: display\dxgkvgpu_escape_read_vgpu_type.htm
ms.assetid: 2D3D8927-74E3-438F-94CF-63456C7C7BBC
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKVGPU_ESCAPE_READ_VGPU_TYPE
req.alt-loc: d3dukmdt.h
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
ms.keywords: DXGKVGPU_ESCAPE_READ_VGPU_TYPE, DXGKVGPU_ESCAPE_READ_VGPU_TYPE
req.iface: 
---

# DXGKVGPU_ESCAPE_READ_VGPU_TYPE structure



## -description
<p>A structure used to read the VGPU type of an escape.</p>


## -syntax

````
typedef struct _DXGKVGPU_ESCAPE_READ_VGPU_TYPE {
  DXGKVGPU_ESCAPE_HEAD Header;
} DXGKVGPU_ESCAPE_READ_VGPU_TYPE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header that is being processed.</p>
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
<dt>D3dukmdt.h</dt>
</dl>
</td>
</tr>
</table>