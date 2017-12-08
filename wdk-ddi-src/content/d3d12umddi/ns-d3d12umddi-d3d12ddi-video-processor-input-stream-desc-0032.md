---
UID: NS.d3d12umddi.D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032
title: D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032
author: windows-driver-content
description: Describes input stream properties for the video processor.
old-location: display\d3d12ddi_video_processor_input_stream_desc_0032.htm
old-project: display
ms.assetid: 3A4D19FD-FC65-4B78-8F0E-9792EB0A9B03
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032, D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032
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
req.alt-api: D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032
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

# D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032 structure



## -description
<p>Describes input stream properties for the video processor.</p>


## -syntax

````
typedef struct _D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032 {
  DXGI_FORMAT                                Format;
  DXGI_COLOR_SPACE_TYPE                      ColorSpace;
  DXGI_RATIONAL                              SourceAspectRatio;
  DXGI_RATIONAL                              DestinationAspectRatio;
  DXGI_RATIONAL                              FrameRate;
  D3D12DDI_VIDEO_SIZE_RANGE                  SourceSizeRange;
  D3D12DDI_VIDEO_SIZE_RANGE                  DestinationSizeRanges;
  BOOL                                       EnableOrientation;
  D3D12DDI_VIDEO_PROCESS_ALPHA_BLENDING_0020 FilterFlags;
  D3D12DDI_VIDEO_PROCESS_FILTER_FLAGS_0020   StereoFormat;
  D3D12DDI_VIDEO_FIELD_TYPE_0020             FieldType;
  D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_0020    DeinterlaceMode;
  BOOL                                       EnableAlphaBlending;
  D3D12DDI_VIDEO_PROCESS_LUMA_KEY_0020       LumaKey;
  UINT                                       NumPastFrames;
  UINT                                       NumFutureFrames;
  BOOL                                       EnableAutoProcessing;
} D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032;
````


## -struct-fields
<dl>

### -field Format

<dd>
<p>The DXGI format of the input texture and references.</p>
</dd>

### -field ColorSpace

<dd>
<p>A DXGI_COLOR_SPACE_TYPE value that specifies the colorspace for the video processor input and reference surfaces.</p>
</dd>

### -field SourceAspectRatio

<dd>
<p>The source aspect ratio.</p>
</dd>

### -field DestinationAspectRatio

<dd>
<p>The destination aspect ratio.</p>
</dd>

### -field FrameRate

<dd>
<p>The frame rate of the input video stream, specified as a DXGI_RATIONAL structure.</p>
</dd>

### -field SourceSizeRange

<dd>
<p>Describes the minimum and maximum source rectangle size.  Video processor should allocate to handle all cases within the range.</p>
</dd>

### -field DestinationSizeRanges

<dd>
<p>Describes the minimum and maximum destination rectangle size.  Video processor should allocate to handle all cases within the range.</p>
</dd>

### -field EnableOrientation

<dd>
<p>Enable all transforms specified in D3D12DDI_VIDEO_PROCESS_ORIENTATION.</p>
</dd>

### -field FilterFlags

<dd>
<p>A bitwise OR of one or more flags from the D3D12DDI_VIDEO_PROCESS_FILTER_FLAGS enumeration specifies the filters to enable.</p>
</dd>

### -field StereoFormat

<dd>
<p>Specifies whether the stream is stereo or not. If D3D12DDI_VIDEO_FRAME_STEREO_FORMAT_SEPARATE, we have two sets of input textures and references (for the stereo interlaced case).</p>
</dd>

### -field FieldType

<dd>
<p>Specifies the frame format as progressive or interlaced for the input stream.  See D3D12DDI_VIDEO_FIELD_TYPE.</p>
</dd>

### -field DeinterlaceMode

<dd>
<p>The deinterlace mode to use.  See D3D12DDI_VIDEO_PROCESS_DEINTERLACE_FLAGS.</p>
</dd>

### -field EnableAlphaBlending

<dd>
<p>The planar alpha for an input stream on the video processor.  See D3D12DDI_VIDEO_PROCESS_ALPHA_BLENDING.</p>
</dd>

### -field LumaKey

<dd>
<p>The luma key for an input stream on the video processor.  See D3D12DDI_VIDEO_PROCESS_LUMA_KEY for more details.</p>
</dd>

### -field NumPastFrames

<dd>
<p>The number of past frames.</p>
</dd>

### -field NumFutureFrames

<dd>
<p>The number of future frames.</p>
</dd>

### -field EnableAutoProcessing

<dd>
<p>Enables or disables automatic processing features on the video processor.</p>
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