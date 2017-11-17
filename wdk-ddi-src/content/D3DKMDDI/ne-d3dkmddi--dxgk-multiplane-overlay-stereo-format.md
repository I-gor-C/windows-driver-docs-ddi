---
UID: NE.d3dkmddi._DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT
title: DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT
author: windows-driver-content
description: Identifies the overlay plane's stereo presentation format. Only the DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO value is supported.
old-location: display\dxgk_multiplane_overlay_stereo_format.htm
ms.assetid: ce9ad02d-645a-4333-9208-27f0805508a5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT
req.alt-loc: D3dkmddi.h
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration



## -description
<p>Identifies the overlay plane's stereo presentation format. Only the <b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</b> value is supported.</p>


## -syntax

````
typedef enum _DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT { 
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO                = 0,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL          = 1,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL            = 2,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE            = 3,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET         = 4,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED     = 5,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED  = 6,
  DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD        = 7
} DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO"></a><a id="dxgk_multiplane_overlay_stereo_format_mono"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</b>

<dd>
<p>The overplay plane data is presented in mono (non-stereo) format.</p>
</dd>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL"></a><a id="dxgk_multiplane_overlay_stereo_format_horizontal"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL"></a><a id="dxgk_multiplane_overlay_stereo_format_vertical"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE"></a><a id="dxgk_multiplane_overlay_stereo_format_separate"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET"></a><a id="dxgk_multiplane_overlay_stereo_format_mono_offset"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED"></a><a id="dxgk_multiplane_overlay_stereo_format_row_interleaved"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED"></a><a id="dxgk_multiplane_overlay_stereo_format_column_interleaved"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD"></a><a id="dxgk_multiplane_overlay_stereo_format_checkerboard"></a><b>DXGK_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>