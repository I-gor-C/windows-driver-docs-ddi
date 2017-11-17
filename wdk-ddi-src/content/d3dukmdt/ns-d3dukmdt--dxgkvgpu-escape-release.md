---
UID: NS.d3dukmdt._DXGKVGPU_ESCAPE_RELEASE
title: DXGKVGPU_ESCAPE_RELEASE
author: windows-driver-content
description: Indicates that an escape has been released.
old-location: display\dxgkvgpu_escape_release.htm
ms.assetid: 96BA0967-BA65-483D-9165-C7ADE05C0216
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
req.alt-api: DXGKVGPU_ESCAPE_RELEASE
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
ms.keywords: DXGKVGPU_ESCAPE_RELEASE, DXGKVGPU_ESCAPE_RELEASE
req.iface: 
---

# DXGKVGPU_ESCAPE_RELEASE structure



## -description
<p>Indicates that an escape has been released.</p>


## -syntax

````
typedef struct _DXGKVGPU_ESCAPE_RELEASE {
  DXGKVGPU_ESCAPE_HEAD Header;
} DXGKVGPU_ESCAPE_RELEASE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header that is being operated on.</p>
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