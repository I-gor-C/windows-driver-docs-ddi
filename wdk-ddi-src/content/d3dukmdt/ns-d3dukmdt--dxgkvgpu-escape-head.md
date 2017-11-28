---
UID: NS.d3dukmdt._DXGKVGPU_ESCAPE_HEAD
title: DXGKVGPU_ESCAPE_HEAD
author: windows-driver-content
description: A structure describing the escape head.
old-location: display\dxgkvgpu_escape_head_.htm
old-project: display
ms.assetid: BB9D12EB-A1B1-4D7B-A1E4-40A932F62C88
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKVGPU_ESCAPE_HEAD, DXGKVGPU_ESCAPE_HEAD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKVGPU_ESCAPE_HEAD
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
req.iface: 
---

# DXGKVGPU_ESCAPE_HEAD structure



## -description
<p>A structure describing the escape head.</p>


## -syntax

````
typedef struct _DXGKVGPU_ESCAPE_HEAD  {
  GPUP_DRIVER_ESCAPE_INPUT Luid;
  DXGKVGPU_ESCAPE_TYPE     Type;
} DXGKVGPU_ESCAPE_HEAD ;
````


## -struct-fields
<dl>

### -field <b>Luid</b>

<dd>
<p>The ID of the escape input.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>The escape type.</p>
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