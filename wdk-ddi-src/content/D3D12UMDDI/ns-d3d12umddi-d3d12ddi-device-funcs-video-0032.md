---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_VIDEO_0032
title: D3D12DDI_DEVICE_FUNCS_VIDEO_0032
author: windows-driver-content
description: Video device functions.
old-location: display\d3d12ddi-device-funcs-video-0032.htm
ms.assetid: 2b71c48a-a028-4bfa-a8bd-ad612aa800ff
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
req.alt-api: D3D12DDI_DEVICE_FUNCS_VIDEO_0032
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
ms.keywords: D3D12DDI_DEVICE_FUNCS_VIDEO_0032, D3D12DDI_DEVICE_FUNCS_VIDEO_0032
req.iface: 
---

# D3D12DDI_DEVICE_FUNCS_VIDEO_0032 structure



## -description
<p>Video device functions.</p>


## -syntax

````
typedef struct _D3D12DDI_DEVICE_FUNCS_VIDEO_0032 {
  PFND3D12DDI_VIDEO_GETCAPS                         pfnGetCaps;
  PFND3D12DDI_CALCPRIVATEVIDEODECODERSIZE_0032      pfnCalcPrivateVideoDecoderSize;
  PFND3D12DDI_CREATEVIDEODECODER_0032               pfnCreateVideoDecoder;
  PFND3D12DDI_DESTROYVIDEODECODER_0021              pfnDestroyVideoDecoder;
  PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0032  pfnCalcPrivateVideoDecoderHeapSize;
  PFND3D12DDI_CREATEVIDEODECODERHEAP_0032           pfnCreateVideoDecoderHeap;
  PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032          pfnDestroyVideoDecoderHeap;
  PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032    pfnCalcPrivateVideoProcessorSize;
  PFND3D12DDI_CREATEVIDEOPROCESSOR_0032             pfnCreateVideoProcessor;
  PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021            pfnDestroyVideoProcessor;
} D3D12DDI_DEVICE_FUNCS_VIDEO_0032, D3D12DDI_DEVICE_FUNCS_VIDEO_0032;
````


## -struct-fields
<dl>

### -field <b>pfnGetCaps</b>

<dd>
<p>Get caps.</p>
</dd>

### -field <b>pfnCalcPrivateVideoDecoderSize</b>

<dd>
<p>Calculate private video decoder size.</p>
</dd>

### -field <b>pfnCreateVideoDecoder</b>

<dd>
<p>Create video decoder.</p>
</dd>

### -field <b>pfnDestroyVideoDecoder</b>

<dd>
<p>Destroy video decoder.</p>
</dd>

### -field <b>pfnCalcPrivateVideoDecoderHeapSize</b>

<dd>
<p>Calculate private video decoder heap size.</p>
</dd>

### -field <b>pfnCreateVideoDecoderHeap</b>

<dd>
<p>Create video decoder heap.</p>
</dd>

### -field <b>pfnDestroyVideoDecoderHeap</b>

<dd>
<p>Destroy video decoder heap.</p>
</dd>

### -field <b>pfnCalcPrivateVideoProcessorSize</b>

<dd>
<p>Calculate private video processor size.</p>
</dd>

### -field <b>pfnCreateVideoProcessor</b>

<dd>
<p>Create video processor.</p>
</dd>

### -field <b>pfnDestroyVideoProcessor</b>

<dd>
<p>Destroy video processor.</p>
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