---
UID: NS.d3d12umddi.D3D12DDI_SHADERCACHE_HASH
title: D3D12DDI_SHADERCACHE_HASH
author: windows-driver-content
description: Includes a hash value.
old-location: display\d3d12ddi_shadercache_hash.htm
old-project: display
ms.assetid: 30ACE58C-E10C-46D7-8ED5-5C693D6246CB
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_SHADERCACHE_HASH, D3D12DDI_SHADERCACHE_HASH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_SHADERCACHE_HASH
req.alt-loc: D3d12umddi.h
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

# D3D12DDI_SHADERCACHE_HASH structure



## -description
<p>Includes a hash value. </p>


## -syntax

````
typedef struct D3D12DDI_SHADERCACHE_HASH {
  BYTE Hash[16];
} D3D12DDI_SHADERCACHE_HASH;
````


## -struct-fields
<dl>

### -field Hash

<dd>
<p>A hash value.</p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>