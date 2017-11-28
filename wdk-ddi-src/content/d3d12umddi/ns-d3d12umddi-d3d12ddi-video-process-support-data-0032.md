---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
title: D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
author: windows-driver-content
description: Video process support data.
old-location: display\d3d12ddi-video-process-support-data-0032.htm
old-project: display
ms.assetid: ea2dabc5-6853-4491-8c1f-f3f5ae516952
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032, D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032
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
req.iface: 
---

# D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032 structure



## -description
<p>Video process support data.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032 {
  UINT                                                                               NodeIndex;
  D3D12DDI_VIDEO_SAMPLE_DESCRIPTION_0020                                             InputSample;
  D3D12DDI_VIDEO_FIELD_TYPE_0020                                                     InputFieldType;
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020                                            InputStereoFormat;
  DXGI_RATIONAL                                                                      InputFrameRate;
  D3D12DDI_VIDEO_FORMAT_DESCRIPTION_0020                                             OutputFormat;
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020                                            OutputStereoFormat;
  DXGI_RATIONAL                                                                      OutputFrameRate;
  D3D12DDI_VIDEO_PROCESS_SUPPORT_FLAGS_0022                                          SupportFlags;
  D3D12DDI_VIDEO_SCALE_SUPPORT_0032                                                  ScaleSupport;
  D3D12DDI_VIDEO_PROCESS_FEATURE_SUPPORT_FLAGS_0020                                  FeatureSupport;
  D3D12DDI_VIDEO_PROCESS_DEINTERLACE_FLAGS_0020                                      DeinterlaceSupport;
  D3D12DDI_VIDEO_PROCESS_AUTO_PROCESSING_FLAGS_0022                                  AutoProcessingSupport;
  D3D12DDI_VIDEO_PROCESS_FILTER_FLAGS_0020                                           FilterSupport;
  D3D12DDI_VIDEO_PROCESS_FILTER_RANGE_0020 [D3D12DDI_VIDEO_PROCESS_MAX_FILTERS_0020] FilterRangeSupport;
} D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032, D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032;
````


## -struct-fields
<dl>

### -field <b>NodeIndex</b>

<dd>
<p>Node index.</p>
</dd>

### -field <b>InputSample</b>

<dd>
<p>Input sample.</p>
</dd>

### -field <b>InputFieldType</b>

<dd>
<p>Input field type.</p>
</dd>

### -field <b>InputStereoFormat</b>

<dd>
<p>Input stereo format.</p>
</dd>

### -field <b>InputFrameRate</b>

<dd>
<p>Input frame rate.</p>
</dd>

### -field <b>OutputFormat</b>

<dd>
<p>Output format.</p>
</dd>

### -field <b>OutputStereoFormat</b>

<dd>
<p>Output stereo format.</p>
</dd>

### -field <b>OutputFrameRate</b>

<dd>
<p>Output frame rate.</p>
</dd>

### -field <b>SupportFlags</b>

<dd>
<p>Support flags.</p>
</dd>

### -field <b>ScaleSupport</b>

<dd>
<p>Scale support.</p>
</dd>

### -field <b>FeatureSupport</b>

<dd>
<p>Feature support.</p>
</dd>

### -field <b>DeinterlaceSupport</b>

<dd>
<p>Deinterlace support.</p>
</dd>

### -field <b>AutoProcessingSupport</b>

<dd>
<p>Auto processing support.</p>
</dd>

### -field <b>FilterSupport</b>

<dd>
<p>Filter support.</p>
</dd>

### -field <b>FilterRangeSupport</b>

<dd>
<p>Filter range support.</p>
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