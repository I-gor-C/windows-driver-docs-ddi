---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_VIDEO_0033
title: D3D12DDI_DEVICE_FUNCS_VIDEO_0033
author: windows-driver-content
description: The device functions of video.
old-location: display\d3d12ddi-device-funcs-video-0033.htm
old-project: display
ms.assetid: faaaf6e5-9f4d-4051-a656-92c1394cda24
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_DEVICE_FUNCS_VIDEO_0033, D3D12DDI_DEVICE_FUNCS_VIDEO_0033
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
req.alt-api: D3D12DDI_DEVICE_FUNCS_VIDEO_0033
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

# D3D12DDI_DEVICE_FUNCS_VIDEO_0033 structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The device functions of video.</p>


## -syntax

````
typedef struct _D3D12DDI_DEVICE_FUNCS_VIDEO_0033 {
  PFND3D12DDI_VIDEO_GETCAPS                         pfnGetCaps;
  PFND3D12DDI_CALCPRIVATEVIDEODECODERSIZE_0032      pfnCalcPrivateVideoDecoderSize;
  PFND3D12DDI_CREATEVIDEODECODER_0032               pfnCreateVideoDecoder;
  PFND3D12DDI_DESTROYVIDEODECODER_0021              pfnDestroyVideoDecoder;
  PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0033  pfnCalcPrivateVideoDecoderHeapSize;
  PFND3D12DDI_CREATEVIDEODECODERHEAP_0033           pfnCreateVideoDecoderHeap;
  PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032          pfnDestroyVideoDecoderHeap;
  PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032    pfnCalcPrivateVideoProcessorSize;
  PFND3D12DDI_CREATEVIDEOPROCESSOR_0032             pfnCreateVideoProcessor;
  PFND3D12DDI_DESTROYVIDEOPROCESSOR_0021            pfnDestroyVideoProcessor;
} D3D12DDI_DEVICE_FUNCS_VIDEO_0033, D3D12DDI_DEVICE_FUNCS_VIDEO_0033;
````


## -struct-fields
<dl>

### -field pfnGetCaps

<dd>
<p>Get caps.</p>
</dd>

### -field pfnCalcPrivateVideoDecoderSize

<dd>
<p>Calculates the private video decoder size.</p>
</dd>

### -field pfnCreateVideoDecoder

<dd>
<p>Creates a video decoder.</p>
</dd>

### -field pfnDestroyVideoDecoder

<dd>
<p>Destroys the video decoder.</p>
</dd>

### -field pfnCalcPrivateVideoDecoderHeapSize

<dd>
<p>Calculates the private video decoder heap size.</p>
</dd>

### -field pfnCreateVideoDecoderHeap

<dd>
<p>Creates the video decoder heap.</p>
</dd>

### -field pfnDestroyVideoDecoderHeap

<dd>
<p>Destroys the video decoder heap.</p>
</dd>

### -field pfnCalcPrivateVideoProcessorSize

<dd>
<p>Calculates the private video processor size.</p>
</dd>

### -field pfnCreateVideoProcessor

<dd>
<p>Creates the video processor.</p>
</dd>

### -field pfnDestroyVideoProcessor

<dd>
<p>Destroys the video processor.</p>
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