---
UID: NS.d3d12umddi.D3D12DDI_SHADERCACHE_CALLBACKS_0021
title: D3D12DDI_SHADERCACHE_CALLBACKS_0021
author: windows-driver-content
description: Specifies shader cache callback functions.
old-location: display\d3d12ddi_shadercache_callbacks_0021.htm
old-project: display
ms.assetid: EBA976B0-3B44-4482-B1B0-31A84150C056
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_SHADERCACHE_CALLBACKS_0021, D3D12DDI_SHADERCACHE_CALLBACKS_0021
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
req.alt-api: D3D12DDI_SHADERCACHE_CALLBACKS_0021
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

# D3D12DDI_SHADERCACHE_CALLBACKS_0021 structure



## -description
<p>Specifies shader cache callback functions. </p>


## -syntax

````
typedef struct D3D12DDI_SHADERCACHE_CALLBACKS_0021 {
  PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021   pfnShaderCacheGetValueCb;
  PFND3D12DDI_SHADERCACHESTOREVALUE_CB_0021 pfnShaderCacheStoreValueCb;
} D3D12DDI_SHADERCACHE_CALLBACKS_0021;
````


## -struct-fields
<dl>

### -field pfnShaderCacheGetValueCb

<dd>
<p>A callback function that gets a shader cache value. </p>
</dd>

### -field pfnShaderCacheStoreValueCb

<dd>
<p>A callback function that stores a shader cache value. </p>
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