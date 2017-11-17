---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE
title: D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE
author: windows-driver-content
description: Indicates the luminance range of YUV data.
old-location: display\d3d11_1ddi_video_processor_nominal_range.htm
ms.assetid: E8D77D49-9E7C-45B3-850C-1E814B44464B
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_NOMINAL_RANGE
req.alt-loc: D3d10umddi.h
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE enumeration



## -description
<p>Indicates the luminance range of YUV data.</p>


## -syntax

````
typedef enum _DXVAHDDDI_NOMINAL_RANGE { 
  D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED  = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235     = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255      = 2
} DXVAHDDDI_NOMINAL_RANGE;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED"></a><a id="d3d11_1ddi_video_processor_nominal_range_undefined"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_UNDEFINED</b>

<dd>
<p>The driver default value, which is the <i>studio luminance range</i> of 16 to 235, inclusive [16, 235].</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235"></a><a id="d3d11_1ddi_video_processor_nominal_range_16_235"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_16_235</b>

<dd>
<p>The <i>studio luminance range</i> of 16 to 235, inclusive [16, 235].</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255"></a><a id="d3d11_1ddi_video_processor_nominal_range_0_255"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE_0_255</b>

<dd>
<p>The <i>full luminance range</i>, or <i>extended range</i>, of 0 to 255, inclusive [0, 255].</p>
</dd>
</dl>

## -remarks
<p>For more information on luminance range, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.</p>

<p>For more information on luminance range, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.</p>

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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>