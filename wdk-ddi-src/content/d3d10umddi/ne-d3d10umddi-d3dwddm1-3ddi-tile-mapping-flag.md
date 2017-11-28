---
UID: NE.d3d10umddi.D3DWDDM1_3DDI_TILE_MAPPING_FLAG
title: D3DWDDM1_3DDI_TILE_MAPPING_FLAG
author: windows-driver-content
description: Indicates how to update a tile mapping.
old-location: display\d3dwddm1_3ddi_tile_mapping_flag.htm
old-project: display
ms.assetid: 1149547D-9165-42AA-B12A-5C7681A8EAC1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM1_3DDI_TILE_MAPPING_FLAG
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
req.iface: 
---

# D3DWDDM1_3DDI_TILE_MAPPING_FLAG enumeration



## -description
<p>Indicates how to update a tile mapping.</p>


## -syntax

````
enum D3DWDDM1_3DDI_TILE_MAPPING_FLAG {
  D3DWDDM1_3DDI_TILE_MAPPING_NO_OVERWRITE  = 0x00000001 

};
````


## -enum-fields
<dl>

### -field <a id="D3DWDDM1_3DDI_TILE_MAPPING_NO_OVERWRITE"></a><a id="d3dwddm1_3ddi_tile_mapping_no_overwrite"></a><b>D3DWDDM1_3DDI_TILE_MAPPING_NO_OVERWRITE</b>

<dd>
<p>Previously submitted commands to the 
device that may still be executing do not reference any of the tile region being updated.
This allows the device to avoid having to flush previously submitted work in order to update a tile mapping.</p>
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