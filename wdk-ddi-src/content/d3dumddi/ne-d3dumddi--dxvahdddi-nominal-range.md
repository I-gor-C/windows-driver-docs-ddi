---
UID: NE.d3dumddi._DXVAHDDDI_NOMINAL_RANGE
title: DXVAHDDDI_NOMINAL_RANGE
author: windows-driver-content
description: Indicates the luminance range of YUV data.
old-location: display\dxvahdddi_nominal_range.htm
old-project: display
ms.assetid: 952BE36C-0F53-47C3-9C95-E6ECAB9D36D1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_NOMINAL_RANGE
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

# DXVAHDDDI_NOMINAL_RANGE enumeration



## -description
<p>Indicates the luminance range of YUV data.</p>


## -syntax

````
typedef enum _DXVAHDDDI_NOMINAL_RANGE { 
  DXVAHDDDI_NOMINAL_RANGE_UNDEFINED  = 0,
  DXVAHDDDI_NOMINAL_RANGE_16_235     = 1,
  DXVAHDDDI_NOMINAL_RANGE_0_255      = 2
} DXVAHDDDI_NOMINAL_RANGE;
````


## -enum-fields
<dl>

### -field DXVAHDDDI_NOMINAL_RANGE_UNDEFINED

<dd>
<p>The driver default value, which is the <i>studio luminance range</i> of 16 to 235, inclusive [16, 235].</p>
</dd>

### -field DXVAHDDDI_NOMINAL_RANGE_16_235

<dd>
<p>The <i>studio luminance range</i> of 16 to 235, inclusive [16, 235].</p>
</dd>

### -field DXVAHDDDI_NOMINAL_RANGE_0_255

<dd>
<p>The <i>full luminance range</i>, or <i>extended range</i>, of 0 to 255, inclusive [0, 255].</p>
</dd>
</dl>

## -remarks
<p>For more information on luminance range, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>