---
UID: NC.d3d12umddi.PFND3D12DDI_VIDEO_PROCESS_FRAME_0032
title: PFND3D12DDI_VIDEO_PROCESS_FRAME_0032
author: windows-driver-content
description: Used to process a video frame.
old-location: display\pfnd3d12ddi_video_process_frame_0032.htm
old-project: display
ms.assetid: C7923B09-FBA2-43EE-A56B-0B8B6C3403A0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC, D3DWDDM2_2DDI_SWIZZLE_PATTERN_DESC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3D12DDI_VIDEO_PROCESS_FRAME_0032
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

# PFND3D12DDI_VIDEO_PROCESS_FRAME_0032 callback



## -description
<p>Used to process a video frame.</p>


## -prototype

````
VOID APIENTRY* PFND3D12DDI_VIDEO_PROCESS_FRAME_0032(
         D3D12DDI_HCOMMANDLIST                                  hDrvCommandList,
         D3D12DDI_HVIDEOPROCESSOR_0020                          hDrvVideoProcessor,
   const D3D12DDIARG_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS_0032 *pOutputParameters,
   const D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032  *pInputStreamParameters,
         UINT                                                   NumInputStreams
);
````


## -parameters
<dl>

### -param hDrvCommandList 

<dd>
<p>The command list.</p>
</dd>

### -param hDrvVideoProcessor 

<dd>
<p>The video processor.</p>
</dd>

### -param pOutputParameters 

<dd>
<p>The output arguments for the video process.</p>
</dd>

### -param pInputStreamParameters 

<dd>
<p>The input arguments for the video process.</p>
</dd>

### -param NumInputStreams 

<dd>
<p>The number of input streams.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

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