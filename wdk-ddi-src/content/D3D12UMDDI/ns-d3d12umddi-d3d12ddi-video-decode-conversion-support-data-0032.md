---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
title: D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
author: windows-driver-content
description: Video decode conversion support data.
old-location: display\d3d12ddi-video-decode-conversion-support-data-0032.htm
ms.assetid: 1395fe30-9bbf-433c-8696-a0f842bad10e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
req.alt-loc: d3d12umddi.h
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
ms.keywords: D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032, D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032
req.iface: 
---

# D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032 structure



## -description
<p>Video decode conversion support data.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032 {
  UINT                                                 NodeIndex;
  D3D12DDI_VIDEO_DECODE_CONFIGURATION_0020             Configuration;
  D3D12DDI_VIDEO_SAMPLE_DESCRIPTION_0020               DecodeSample;
  D3D12DDI_VIDEO_FORMAT_DESCRIPTION_0020               OutputFormat;
  DXGI_RATIONAL                                        FrameRate;
  UINT                                                 BitRate;
  D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_FLAGS_0020  SupportFlags;
  D3D12DDI_VIDEO_SCALE_SUPPORT_0032                    ScaleSupport;
} D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032, D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032;
````


## -struct-fields
<dl>

### -field <b>NodeIndex</b>

<dd>
<p>Node index.</p>
</dd>

### -field <b>Configuration</b>

<dd>
<p>Configuration.</p>
</dd>

### -field <b>DecodeSample</b>

<dd>
<p>Decode sample.</p>
</dd>

### -field <b>OutputFormat</b>

<dd>
<p>Output format.</p>
</dd>

### -field <b>FrameRate</b>

<dd>
<p>Frame rate.</p>
</dd>

### -field <b>BitRate</b>

<dd>
<p>Bitrate.</p>
</dd>

### -field <b>SupportFlags</b>

<dd>
<p>Support flags.</p>
</dd>

### -field <b>ScaleSupport</b>

<dd>
<p>Scale support.</p>
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
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>