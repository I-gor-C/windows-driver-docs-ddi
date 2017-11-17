---
UID: NS.d3d10umddi.D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE
title: D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE
author: windows-driver-content
description: Specifies the (x, y, z) coordinate values below the index tiles of a tiled resource, along with the respective subresource. Note that the coordinate values do not indicate pixels or bytes.
old-location: display\d3dwddm1_3ddi_tiled_resource_coordinate.htm
ms.assetid: A927CAF9-EF7F-47CC-9BDE-B6E13597368E
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE
req.alt-loc: D3d10umddi.h
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
ms.keywords: D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE, D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE
req.iface: 
---

# D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE structure



## -description
<p>Specifies the (<i>x</i>, <i>y</i>, <i>z</i>) coordinate values below the index tiles  of a tiled resource, along with the respective subresource. Note that the coordinate values do not indicate pixels or bytes.</p>


## -syntax

````
typedef struct D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE {
  UINT X;
  UINT Y;
  UINT Z;
  UINT Subresource;
} D3DWDDM1_3DDI_TILED_RESOURCE_COORDINATE;
````


## -struct-fields
<dl>

### -field <b>X</b>

<dd>
<p>The <i>x</i> coordinate of the tiled resource. Used for buffer, 1-D, 2-D, and 3-D rendering.</p>
</dd>

### -field <b>Y</b>

<dd>
<p>The <i>y</i> coordinate of the tiled resource. Used for 2-D and 3-D rendering.</p>
</dd>

### -field <b>Z</b>

<dd>
<p>The <i>z</i> coordinate of the tiled resource. Used for 3-D rendering.</p>
</dd>

### -field <b>Subresource</b>

<dd>
<p>The subresource of the tiled resource. Used to index into mipmaps and arrays for 1-D, 2-D, and 3-D rendering.</p>
<p>If mipmaps are packed into a single tile, any subresource value that indicates any of the packed mipmaps refers to the same tile.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3</p>
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