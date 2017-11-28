---
UID: NE.d3d12umddi.D3D12DDICAPS_TYPE_VIDEO_0020
title: D3D12DDICAPS_TYPE_VIDEO_0020
author: windows-driver-content
description: Contains capability types for video.
old-location: display\d3d12ddicaps_type_video_0020.htm
old-project: display
ms.assetid: 3B95996D-EB7C-4DCF-B00C-BA5AFEFD4110
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDICAPS_TYPE_VIDEO_0020
req.alt-loc: D3d12umddi.h
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

# D3D12DDICAPS_TYPE_VIDEO_0020 enumeration



## -description
<p>Contains capability types for video.</p>


## -syntax

````
typedef enum _D3D12DDICAPS_TYPE_VIDEO_0020 { 
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_SUPPORT                       = 0,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_PROFILES                      = 1,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_FORMATS                       = 2,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_CONVERSION_SUPPORT            = 3,
  D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_BITSTREAM_ENCRYPTION_SCHEMES  = 4,
  D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_SUPPORT                      = 5,
  D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_MAX_INPUT_STREAMS            = 6,
  D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_REFERENCE_INFO               = 7
} D3D12DDICAPS_TYPE_VIDEO_0020;
````


## -enum-fields
<dl>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_SUPPORT"></a><a id="d3d12ddicaps_type_video_0020_decode_support"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_SUPPORT</b>

<dd>
<p>Check if a decode profile, bitstream encryption, resolution, and format are supported</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_PROFILES"></a><a id="d3d12ddicaps_type_video_0020_decode_profiles"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_PROFILES</b>

<dd>
<p>Retrieve the list of decode profiles supported by the adapter.  </p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_FORMATS"></a><a id="d3d12ddicaps_type_video_0020_decode_formats"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_FORMATS</b>

<dd>
<p> Retrieves the supported decode formats. </p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_CONVERSION_SUPPORT"></a><a id="d3d12ddicaps_type_video_0020_decode_conversion_support"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_CONVERSION_SUPPORT</b>

<dd>
<p>Check whether a colorspace conversion, format conversion, and scale are supported.  </p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_BITSTREAM_ENCRYPTION_SCHEMES"></a><a id="d3d12ddicaps_type_video_0020_decode_bitstream_encryption_schemes"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_DECODE_BITSTREAM_ENCRYPTION_SCHEMES</b>

<dd>
<p>Retrieve the list of bitstream encryption schemes supported by the adapter. </p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_SUPPORT"></a><a id="d3d12ddicaps_type_video_0020_process_support"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_SUPPORT</b>

<dd>
<p>Retrieves the video processor capabilities.  </p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_MAX_INPUT_STREAMS"></a><a id="d3d12ddicaps_type_video_0020_process_max_input_streams"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_MAX_INPUT_STREAMS</b>

<dd>
<p>The maximum number of streams that can be enabled at the same time.</p>
</dd>

### -field <a id="D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_REFERENCE_INFO"></a><a id="d3d12ddicaps_type_video_0020_process_reference_info"></a><b>D3D12DDICAPS_TYPE_VIDEO_0020_PROCESS_REFERENCE_INFO</b>

<dd>
<p>Retrieves the number of past and future frames required for a given deinterlace mode, filters, frame rate conversion, and features.  </p>
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
<dt>D3d12umddi.h (include D3d12umddi.h)</dt>
</dl>
</td>
</tr>
</table>