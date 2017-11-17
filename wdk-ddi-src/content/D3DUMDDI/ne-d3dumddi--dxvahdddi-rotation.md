---
UID: NE.d3dumddi._DXVAHDDDI_ROTATION
title: DXVAHDDDI_ROTATION
author: windows-driver-content
description: Specifies the clockwise rotation of the display output surface.
old-location: display\dxvahdddi_rotation.htm
ms.assetid: 667f1c5e-c342-40b2-b215-2538669288cc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_ROTATION
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# DXVAHDDDI_ROTATION enumeration



## -description
<p>Specifies the clockwise rotation of the display output surface.</p>


## -syntax

````
typedef enum _DXVAHDDDI_ROTATION { 
  DXVAHDDDI_ROTATION_IDENTITY  = 0,
  DXVAHDDDI_ROTATION_90        = 1,
  DXVAHDDDI_ROTATION_180       = 2,
  DXVAHDDDI_ROTATION_270       = 3
} DXVAHDDDI_ROTATION;
````


## -enum-fields
<dl>

### -field <a id="DXVAHDDDI_ROTATION_IDENTITY"></a><a id="dxvahdddi_rotation_identity"></a><b>DXVAHDDDI_ROTATION_IDENTITY</b>

<dd>
<p>Indicates that rotation is 0 degrees—landscape mode.</p>
</dd>

### -field <a id="DXVAHDDDI_ROTATION_90"></a><a id="dxvahdddi_rotation_90"></a><b>DXVAHDDDI_ROTATION_90</b>

<dd>
<p>Indicates that rotation is 90 degrees clockwise—portrait mode.</p>
</dd>

### -field <a id="DXVAHDDDI_ROTATION_180"></a><a id="dxvahdddi_rotation_180"></a><b>DXVAHDDDI_ROTATION_180</b>

<dd>
<p>Indicates that rotation is 180 degrees clockwise—inverted landscape mode.</p>
</dd>

### -field <a id="DXVAHDDDI_ROTATION_270"></a><a id="dxvahdddi_rotation_270"></a><b>DXVAHDDDI_ROTATION_270</b>

<dd>
<p>Indicates that rotation is 270 degrees clockwise—inverted portrait mode.</p>
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