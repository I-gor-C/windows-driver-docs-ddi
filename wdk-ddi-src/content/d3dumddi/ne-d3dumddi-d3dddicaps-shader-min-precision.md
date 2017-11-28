---
UID: NE.d3dumddi.D3DDDICAPS_SHADER_MIN_PRECISION
title: D3DDDICAPS_SHADER_MIN_PRECISION
author: windows-driver-content
description: Specifies minimum precision levels that the user-mode driver supports in shaders.
old-location: display\d3dddicaps_shader_min_precision.htm
old-project: display
ms.assetid: 98856726-b426-42e4-9560-f6b56164824a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICAPS_SHADER_MIN_PRECISION
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

# D3DDDICAPS_SHADER_MIN_PRECISION enumeration



## -description
<p>Specifies minimum precision levels that the user-mode driver supports in shaders.</p>


## -syntax

````
typedef enum D3DDDICAPS_SHADER_MIN_PRECISION { 
  D3DDDICAPS_SHADER_MIN_PRECISION_10_BIT  = 0x1,
  D3DDDICAPS_SHADER_MIN_PRECISION_16_BIT  = 0x2
} D3DDDICAPS_SHADER_MIN_PRECISION;
````


## -enum-fields
<dl>

### -field <a id="D3DDDICAPS_SHADER_MIN_PRECISION_10_BIT"></a><a id="d3dddicaps_shader_min_precision_10_bit"></a><b>D3DDDICAPS_SHADER_MIN_PRECISION_10_BIT</b>

<dd>
<p>The minimum precision level is 10-bit.</p>
</dd>

### -field <a id="D3DDDICAPS_SHADER_MIN_PRECISION_16_BIT"></a><a id="d3dddicaps_shader_min_precision_16_bit"></a><b>D3DDDICAPS_SHADER_MIN_PRECISION_16_BIT</b>

<dd>
<p>The minimum precision level is 16-bit.</p>
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