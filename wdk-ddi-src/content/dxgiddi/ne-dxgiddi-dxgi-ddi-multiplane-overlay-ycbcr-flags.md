---
UID: NE.dxgiddi.DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS
title: DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS
author: windows-driver-content
description: Identifies YUV range and conversion info that describes a multiplane overlay.
old-location: display\dxgi_ddi_multiplane_overlay_ycbcr_flags.htm
ms.assetid: fa915ec0-167f-441c-b2de-0ae2b852c432
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS
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

# DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS enumeration



## -description
<p>Identifies YUV range and conversion info that describes a multiplane overlay.</p>


## -syntax

````
typedef enum DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS { 
  DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE  = 0x1,
  DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709          = 0x2,
  DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC          = 0x4
} DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE"></a><a id="dxgi_ddi_multiplane_overlay_ycbcr_flag_nominal_range"></a><a id="DXGI_DDI_MULTIPLANE_OVERLAY_YCBCR_FLAG_NOMINAL_RANGE"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE</b>

<dd>
<p>YUV values range from 16 to 235, inclusive, instead of the default range of 0 to 255, inclusive.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709"></a><a id="dxgi_ddi_multiplane_overlay_ycbcr_flag_bt709"></a><a id="DXGI_DDI_MULTIPLANE_OVERLAY_YCBCR_FLAG_BT709"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709</b>

<dd>
<p>YUV values should be converted using the BT.709 standard, instead of the default BT.601 conversion.</p>
</dd>

### -field <a id="DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC"></a><a id="dxgi_ddi_multiplane_overlay_ycbcr_flag_xvycc"></a><a id="DXGI_DDI_MULTIPLANE_OVERLAY_YCBCR_FLAG_XVYCC"></a><b>DXGI_DDI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC</b>

<dd>
<p>YUV values contain xvYCC data, instead of conventional YCbCr data.</p>
</dd>
</dl>

## -remarks
<p>For more info on how YUV ranges are defined and converted, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.</p>

<p>For more info on how YUV ranges are defined and converted, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.</p>

<p>For more info on how YUV ranges are defined and converted, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.</p>

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
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>