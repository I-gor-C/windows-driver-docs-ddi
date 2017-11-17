---
UID: NE.d3dkmdt._D3DKMDT_MONITOR_DESCRIPTOR_TYPE
title: D3DKMDT_MONITOR_DESCRIPTOR_TYPE
author: windows-driver-content
description: The D3DKMDT_MONITOR_DESCRIPTOR_TYPE enumeration is used to indicate a particular type of monitor descriptor.
old-location: display\d3dkmdt_monitor_descriptor_type.htm
ms.assetid: f5ec761f-fc20-4baf-a012-c32356644a6c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_DESCRIPTOR_TYPE
req.alt-loc: d3dkmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# D3DKMDT_MONITOR_DESCRIPTOR_TYPE enumeration



## -description
<p>The D3DKMDT_MONITOR_DESCRIPTOR_TYPE enumeration is used to indicate a particular type of monitor descriptor.</p>


## -syntax

````
typedef enum _D3DKMDT_MONITOR_DESCRIPTOR_TYPE { 
  D3DKMDT_MDT_UNINITIALIZED           = 0,
  D3DKMDT_MDT_VESA_EDID_V1_BASEBLOCK  = 1,
  D3DKMDT_MDT_VESA_EDID_V1_BLOCKMAP   = 2,
  D3DKMDT_MDT_OTHER                   = 255
} D3DKMDT_MONITOR_DESCRIPTOR_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_MDT_UNINITIALIZED"></a><a id="d3dkmdt_mdt_uninitialized"></a><b>D3DKMDT_MDT_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_MONITOR_DESCRIPTOR_TYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_MDT_VESA_EDID_V1_BASEBLOCK"></a><a id="d3dkmdt_mdt_vesa_edid_v1_baseblock"></a><b>D3DKMDT_MDT_VESA_EDID_V1_BASEBLOCK</b>

<dd>
<p>Indicates that the descriptor is an Extended Display Identification Data (EDID) base block.</p>
</dd>

### -field <a id="D3DKMDT_MDT_VESA_EDID_V1_BLOCKMAP"></a><a id="d3dkmdt_mdt_vesa_edid_v1_blockmap"></a><b>D3DKMDT_MDT_VESA_EDID_V1_BLOCKMAP</b>

<dd>
<p>Indicates that the descriptor is an EDID block map.</p>
</dd>

### -field <a id="D3DKMDT_MDT_OTHER"></a><a id="d3dkmdt_mdt_other"></a><b>D3DKMDT_MDT_OTHER</b>

<dd>
<p>Indicates that the descriptor has a type other than those indicated by the previous values of this enumeration.</p>
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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>