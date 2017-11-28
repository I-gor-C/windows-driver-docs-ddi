---
UID: NE.d3dkmthk.D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
title: D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\d3dkmt_multiplane_overlay_ycbcr_flags.htm
old-project: display
ms.assetid: 3bfcd424-961f-4efe-a928-2ee7fbd29f4a
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
req.alt-api: D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS
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

# D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef enum D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS { 
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE  = 0x1,
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709          = 0x2,
  D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC          = 0x4
} D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE"></a><a id="d3dkmt_multiplane_overlay_ycbcr_flag_nominal_range"></a><a id="D3DKMT_MULTIPLANE_OVERLAY_YCBCR_FLAG_NOMINAL_RANGE"></a><b>D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE</b>

<dd></dd>

### -field <a id="D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709"></a><a id="d3dkmt_multiplane_overlay_ycbcr_flag_bt709"></a><a id="D3DKMT_MULTIPLANE_OVERLAY_YCBCR_FLAG_BT709"></a><b>D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709</b>

<dd></dd>

### -field <a id="D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC"></a><a id="d3dkmt_multiplane_overlay_ycbcr_flag_xvycc"></a><a id="D3DKMT_MULTIPLANE_OVERLAY_YCBCR_FLAG_XVYCC"></a><b>D3DKMT_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC</b>

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