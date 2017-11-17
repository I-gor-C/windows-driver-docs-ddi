---
UID: NS.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE
title: D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE
author: windows-driver-content
description: Specifies the color space for video processing.
old-location: display\d3d11_1ddi_video_processor_color_space.htm
ms.assetid: 2878b36e-3850-4af8-aeca-9c5d2da717f9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE
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
ms.keywords: D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE, D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE
req.iface: 
---

# D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE structure



## -description
<p>Specifies the color space for video processing.</p>


## -syntax

````
typedef struct D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE {
  UINT Usage  :1;
  UINT RGB_Range  :1;
  UINT YCbCr_Matrix  :1;
  UINT YCbCr_xvYCC  :1;
  UINT Nominal_Range  :2;
  UINT Reserved  :26;
} D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE;
````


## -struct-fields
<dl>

### -field <b>Usage</b>

<dd>
<p>Specifies whether the output is intended for playback or video processing (such as editing or authoring). The device can optimize the processing based on the type. The default state value is 0 (playback). 

</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Playback</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Video processing</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>RGB_Range</b>

<dd>
<p>Specifies the RGB color range. The default state value is 0 (full range).

</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Full range (0-255)</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Limited range (16-235)</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>YCbCr_Matrix</b>

<dd>
<p>Specifies the YCbCr transfer matrix. The default state value is 0 (BT.601).

</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>ITU-R BT.601</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>ITU-R BT.709</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>YCbCr_xvYCC</b>

<dd>
<p>Specifies whether the output uses conventional YCbCr or extended YCbCr (xvYCC). The default state value is zero (conventional YCbCr).

</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Conventional YCbCr</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Extended YCbCr (xvYCC)</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Nominal_Range</b>

<dd>
<p>[in] A UINT value that specifies that the luminance range of YUV data is described by the <a href="https://msdn.microsoft.com/library/windows/hardware/dn265173">D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE</a> enumeration. The default state value is zero, which indicates the studio luminance range of 16 to 235, inclusive [16, 235].</p>
<p>When YUV-format data is converted to RGB format, the luminance range specified by <a href="https://msdn.microsoft.com/library/windows/hardware/dn265173">D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE</a> is applied to the YUV data before the conversion to RGB.</p>
<p>For more information on luminance range, see <a href="display.yuv_format_ranges">YUV format ranges in Windows 8.1</a>.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Set to zero.</p>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265173">D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
