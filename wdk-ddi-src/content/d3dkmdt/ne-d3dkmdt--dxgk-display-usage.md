---
UID: NE.d3dkmdt._DXGK_DISPLAY_USAGE
title: DXGK_DISPLAY_USAGE
author: windows-driver-content
description: Enum used to specify the display type being used.
old-location: display\dxgk_display_usage.htm
old-project: display
ms.assetid: 07B51679-4E9B-4360-AA4A-D5BD9BADB4FC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_DISPLAY_USAGE
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
req.iface: 
---

# DXGK_DISPLAY_USAGE enumeration



## -description
<p>Enum used to specify the display type being used.</p>


## -syntax

````
typedef enum _DXGK_DISPLAY_USAGE { 
  DXGK_DU_INVALID  = 0,
  DXGK_DU_GENERIC,
  DXGK_DU_AR,
  DXGK_DU_VR
} DXGK_DISPLAY_USAGE, *PDXGK_DISPLAY_USAGE;
````


## -enum-fields
<dl>

### -field DXGK_DU_INVALID

<dd>
<p>Invalid type.</p>
</dd>

### -field DXGK_DU_GENERIC

<dd>
<p>Generic display type.</p>
</dd>

### -field DXGK_DU_AR

<dd>
<p>A head mounted augmented reality display.  </p>
</dd>

### -field DXGK_DU_VR

<dd>
<p>A head mounted virtual reality display.  </p>
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