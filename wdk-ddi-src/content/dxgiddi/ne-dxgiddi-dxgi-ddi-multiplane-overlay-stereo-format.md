---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT
title: DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT
author: windows-driver-content
description: Identifies the overlay plane's stereo presentation format. Only the DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO value is supported.
old-location: display\dxgi_ddi_multiplane_overlay_stereo_format.htm
ms.assetid: 035edf74-43a0-4de9-805f-c40aba870751
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: dxgiddi.h
req.include-header: Dxgiddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT
req.alt-loc: Dxgiddi.h
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
ms.keywords: DxApiGetVersion
req.iface: 
---

# DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT enumeration



## -description
<p>Identifies the overlay plane's stereo presentation format. Only the <b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</b> value is supported.</p>


## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT { 
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO                = 0,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL          = 1,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL            = 2,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE            = 3,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET         = 4,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED     = 5,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED  = 6,
  DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD        = 7
} DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_mono"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO</b>

<dd>
<p>The overplay plane data is presented in mono (non-stereo) format.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_horizontal"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_HORIZONTAL</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_vertical"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_VERTICAL</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_separate"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_SEPARATE</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_mono_offset"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_MONO_OFFSET</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_row_interleaved"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_ROW_INTERLEAVED</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_column_interleaved"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_COLUMN_INTERLEAVED</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD"></a><a id="dxgi_ddi_multiplane_overlay_stereo_format_checkerboard"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_STEREO_FORMAT_CHECKERBOARD</b>

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
<dt>Dxgiddi.h (include Dxgiddi.h)</dt>
</dl>
</td>
</tr>
</table>