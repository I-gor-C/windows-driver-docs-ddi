---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_VIDEO_0030
title: D3D12DDI_DEVICE_FUNCS_VIDEO_0030
author: windows-driver-content
description: Video device functions.
old-location: display\d3d12ddi-device-funcs-video-0030.htm
old-project: display
ms.assetid: 39647e7d-d89f-43f4-916a-cbfa5ba28611
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_DEVICE_FUNCS_VIDEO_0030, D3D12DDI_DEVICE_FUNCS_VIDEO_0030
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
req.alt-api: D3D12DDI_DEVICE_FUNCS_VIDEO_0030
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

# D3D12DDI_DEVICE_FUNCS_VIDEO_0030 structure



## -description
<p>Video device functions.</p>


## -syntax

````
typedef struct _D3D12DDI_DEVICE_FUNCS_VIDEO_0030 {
  PFND3D12DDI_VIDEO_GETCAPS                                     pfnGetCaps;
  PFND3D12DDI_CALCPRIVATEVIDEODECODERSIZE_0021                  pfnCalcPrivateVideoDecoderSize;
  PFND3D12DDI_CREATEVIDEODECODER_0021                           pfnCreateVideoDecoder;
  PFND3D12DDI_DESTROYVIDEODECODER_0021                          pfnDestroyVideoDecoder;
  PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0021                pfnCalcPrivateVideoProcessorSize;
  PFND3D12DDI_CREATEVIDEOPROCESSOR_0021                         pfnCreateVideoProcessor;
  PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021                        pfnDestroyVideoProcessor;
  PFND3D12DDI_VIDEO_GET_DECODE_PROFILE_COUNT_0020               pfnGetDecodeProfileCount;
  PFND3D12DDI_VIDEO_GET_DECODE_FORMAT_COUNT_0020                pfnGetDecodeFormatCount;
  PFND3D12DDI_VIDEO_GET_BITSTREAM_ENCRYPTION_SCHEME_COUNT_0020  pfnGetBitstreamEncryptionSchemeCount;
  PFND3D12DDI_VIDEO_DECODER_TRIM_ALLOCATIONS_0021               pfnDecoderTrimAllocations;
  PFND3D12DDI_VIDEO_PROCESSOR_TRIM_ALLOCATIONS_0021             pfnProcessorTrimAllocations;
} D3D12DDI_DEVICE_FUNCS_VIDEO_0030, D3D12DDI_DEVICE_FUNCS_VIDEO_0030;
````


## -struct-fields
<dl>

### -field pfnGetCaps

<dd>
<p>Get caps.</p>
</dd>

### -field pfnCalcPrivateVideoDecoderSize

<dd>
<p>Calculate private video decoder size.</p>
</dd>

### -field pfnCreateVideoDecoder

<dd>
<p>Create video decoder.</p>
</dd>

### -field pfnDestroyVideoDecoder

<dd>
<p>Destroy video decoder.</p>
</dd>

### -field pfnCalcPrivateVideoProcessorSize

<dd>
<p>Calculate private video processor size.</p>
</dd>

### -field pfnCreateVideoProcessor

<dd>
<p>Create video processor.</p>
</dd>

### -field pfnDestroyVideoProcessor

<dd>
<p>Destroy video processor.</p>
</dd>

### -field pfnGetDecodeProfileCount

<dd>
<p>Get decode profile count.</p>
</dd>

### -field pfnGetDecodeFormatCount

<dd>
<p>Get decode format count.</p>
</dd>

### -field pfnGetBitstreamEncryptionSchemeCount

<dd>
<p>Get bitstream encryption scheme count.</p>
</dd>

### -field pfnDecoderTrimAllocations

<dd>
<p>Decoder trim allocations.</p>
</dd>

### -field pfnProcessorTrimAllocations

<dd>
<p>Processor trim allocations.</p>
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