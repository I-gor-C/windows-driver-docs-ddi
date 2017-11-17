---
UID: NS.d3dukmdt._DXGKVGPU_ESCAPE_INITIALIZE
title: DXGKVGPU_ESCAPE_INITIALIZE
author: windows-driver-content
description: Used to initialize an escape.
old-location: display\dxgkvgpu_escape_initialize.htm
ms.assetid: 697F4A4C-349E-46E5-B891-215C4AFFC4B6
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
req.alt-api: DXGKVGPU_ESCAPE_INITIALIZE
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
ms.keywords: DXGKVGPU_ESCAPE_INITIALIZE, DXGKVGPU_ESCAPE_INITIALIZE
req.iface: 
---

# DXGKVGPU_ESCAPE_INITIALIZE structure



## -description
<p>Used to initialize an escape.</p>


## -syntax

````
typedef struct _DXGKVGPU_ESCAPE_INITIALIZE {
  DXGKVGPU_ESCAPE_HEAD Header;
} DXGKVGPU_ESCAPE_INITIALIZE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header that is being operated over.</p>
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