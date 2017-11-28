---
UID: NS.d3d10umddi.D3D10DDI_VERTEX_CACHE_DESC
title: D3D10DDI_VERTEX_CACHE_DESC
author: windows-driver-content
description: The D3D10DDI_VERTEX_CACHE_DESC structure describes mesh-optimization data.
old-location: display\d3d10ddi_vertex_cache_desc.htm
old-project: display
ms.assetid: c6cff037-436c-4c7e-85b8-02c9d7827f95
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D10DDI_VERTEX_CACHE_DESC, D3D10DDI_VERTEX_CACHE_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10DDI_VERTEX_CACHE_DESC
req.alt-loc: d3d10umddi.h
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

# D3D10DDI_VERTEX_CACHE_DESC structure



## -description
<p>The D3D10DDI_VERTEX_CACHE_DESC structure describes mesh-optimization data.</p>


## -syntax

````
typedef struct D3D10DDI_VERTEX_CACHE_DESC {
  UINT Pattern;
  UINT OptMethod;
  UINT CacheSize;
  UINT MagicNumber;
} D3D10DDI_VERTEX_CACHE_DESC;
````


## -struct-fields
<dl>

### -field <b>Pattern</b>

<dd>
<p>[out] The bit pattern. The driver must specify the bit pattern as a CACH four-character code (FOURCC) value. The driver can use the following MAKEFOURCC macro to specify the FOURCC value as CACH:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>MAKEFOURCC('C', 'A', 'C', 'H'); </pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>OptMethod</b>

<dd>
<p>[out] The method of mesh optimization. The driver can use one of the following values to specify the mesh optimization that it uses.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>Longest strips optimization</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Vertex-cache-based optimization</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CacheSize</b>

<dd>
<p>[out] The effective size, in entries, that the driver optimizes the vertex cache for. The actual cache size is not required to be the size that is specified in <b>CacheSize</b> because the actual cache size is larger in most situations. The driver specifies an optimized size in <b>CacheSize</b> only if it also specifies 1 in the <b>OptMethod</b> member.</p>
</dd>

### -field <b>MagicNumber</b>

<dd>
<p>[out] The number that should be used as part of a trial-and-error procedure when you are determining when to restart the strips list. This number can be from 1 through the value that is specified in the <b>CacheSize</b> member. Typically, the best values are near <b>CacheSize</b>/2. The driver specifies a number in <b>MagicNumber</b> only if it also specifies 0 in the <b>OptMethod</b> member. </p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>