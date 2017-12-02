---
UID: NS.d3dumddi.D3DDDICAPS_ARCHITECTURE_INFO
title: D3DDDICAPS_ARCHITECTURE_INFO
author: windows-driver-content
description: Describes information about display adapter architecture.
old-location: display\d3dddicaps_architecture_info.htm
old-project: display
ms.assetid: ad35cd3f-87bd-4d57-ab13-4cb2b268ad35
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICAPS_ARCHITECTURE_INFO, D3DDDICAPS_ARCHITECTURE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICAPS_ARCHITECTURE_INFO
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
req.iface: 
---

# D3DDDICAPS_ARCHITECTURE_INFO structure



## -description
<p>Describes information about display adapter architecture.</p>


## -syntax

````
typedef struct D3DDDICAPS_ARCHITECTURE_INFO {
  BOOL TileBasedDeferredRenderer;
} D3DDDICAPS_ARCHITECTURE_INFO;
````


## -struct-fields
<dl>

### -field TileBasedDeferredRenderer

<dd>
<p>Specifies whether a rendering device batches rendering commands and performs multipass rendering into tiles or bins over a render area. The value is <b>TRUE</b> if the rendering device batches rendering commands and <b>FALSE</b> otherwise.</p>
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