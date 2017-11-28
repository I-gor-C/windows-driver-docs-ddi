---
UID: NE.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
title: D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_stereo_format.htm
old-project: display
ms.assetid: dd26ac4b-ecef-4b4d-a050-d3e429ff0542
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT
req.alt-loc: D3dkmthk.h
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

# D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef enum D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT { 
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO                = 0,
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL          = 1,
  D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL            = 2,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE            = 3,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET         = 4,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED     = 5,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED  = 6,
  DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD        = 7
} D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO"></a><a id="dxgkmt_multiplane_overlay_stereo_format_mono"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</b>

<dd></dd>

### -field <a id="D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL"></a><a id="d3dkmt_multiplane_overlay_stereo_format_horizontal"></a><b>D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL</b>

<dd></dd>

### -field <a id="D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL"></a><a id="d3dkmt_multiplane_overlay_stereo_format_vertical"></a><b>D3DKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL</b>

<dd></dd>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE"></a><a id="dxgkmt_multiplane_overlay_stereo_format_separate"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE</b>

<dd></dd>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET"></a><a id="dxgkmt_multiplane_overlay_stereo_format_mono_offset"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET</b>

<dd></dd>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED"></a><a id="dxgkmt_multiplane_overlay_stereo_format_row_interleaved"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED</b>

<dd></dd>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED"></a><a id="dxgkmt_multiplane_overlay_stereo_format_column_interleaved"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED</b>

<dd></dd>

### -field <a id="DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD"></a><a id="dxgkmt_multiplane_overlay_stereo_format_checkerboard"></a><b>DXGKMT_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD</b>

<dd></dd>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>