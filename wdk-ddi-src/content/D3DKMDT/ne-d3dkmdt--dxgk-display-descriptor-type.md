---
UID: NE.d3dkmdt._DXGK_DISPLAY_DESCRIPTOR_TYPE
title: DXGK_DISPLAY_DESCRIPTOR_TYPE
author: windows-driver-content
description: Enum used to express the display descriptor type.
old-location: display\dxgk_display_descriptor_type.htm
ms.assetid: 2AC0B5CF-67FB-462F-9118-E30FEDE9A019
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DISPLAY_DESCRIPTOR_TYPE
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

# DXGK_DISPLAY_DESCRIPTOR_TYPE enumeration



## -description
<p>Enum used to express the display descriptor type.</p>


## -syntax

````
typedef enum _DXGK_DISPLAY_DESCRIPTOR_TYPE { 
  DXGK_DDT_INVALID  = 0,
  DXGK_DDT_EDID
} DXGK_DISPLAY_DESCRIPTOR_TYPE, *PDXGK_DISPLAY_DESCRIPTOR_TYPE ;
````


## -enum-fields
<dl>

### -field <a id="DXGK_DDT_INVALID"></a><a id="dxgk_ddt_invalid"></a><b>DXGK_DDT_INVALID</b>

<dd>
<p>Invalid type.</p>
</dd>

### -field <a id="DXGK_DDT_EDID"></a><a id="dxgk_ddt_edid"></a><b>DXGK_DDT_EDID</b>

<dd>
<p>A VESA EDID descriptor.</p>
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
<dt>D3dkmdt.h</dt>
</dl>
</td>
</tr>
</table>