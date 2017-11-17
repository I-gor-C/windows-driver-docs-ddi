---
UID: NE.d3dkmdt.DXGK_ENGINE_TYPE
title: DXGK_ENGINE_TYPE
author: windows-driver-content
description: Indicates the type of engine on a GPU node. Note the selection rules discussed in Remarks.
old-location: display\dxgk_engine_type.htm
ms.assetid: D94EF91A-784D-4AA2-A43D-6A4AE88CF0A3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_ENGINE_TYPE
req.alt-loc: D3dkmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# DXGK_ENGINE_TYPE enumeration



## -description
<p>Indicates the type of engine on a GPU node. Note the selection rules discussed in Remarks.</p>


## -syntax

````
typedef enum _DXGK_ENGINE_TYPE { 
  DXGK_ENGINE_TYPE_OTHER             = 0,
  DXGK_ENGINE_TYPE_3D                = 1,
  DXGK_ENGINE_TYPE_VIDEO_DECODE      = 2,
  DXGK_ENGINE_TYPE_VIDEO_ENCODE      = 3,
  DXGK_ENGINE_TYPE_VIDEO_PROCESSING  = 4,
  DXGK_ENGINE_TYPE_SCENE_ASSEMBLY    = 5,
  DXGK_ENGINE_TYPE_COPY              = 6,
  DXGK_ENGINE_TYPE_OVERLAY           = 7
} DXGK_ENGINE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DXGK_ENGINE_TYPE_OTHER"></a><a id="dxgk_engine_type_other"></a><b>DXGK_ENGINE_TYPE_OTHER</b>

<dd>
<p>The engine does not match any of the other <a href="https://msdn.microsoft.com/library/windows/hardware/dn265417">DXGK_ENGINE_TYPE</a> enumeration values. This value is used for proprietary or unique functionality that is not exposed by typical adapters, as well as for an engine that performs work that doesn't fall under another category.</p>
</dd>

### -field <a id="DXGK_ENGINE_TYPE_3D"></a><a id="dxgk_engine_type_3d"></a><b>DXGK_ENGINE_TYPE_3D</b>

<dd>
<p>The adapter's 3-D processing engine. All adapters that are not a <a href="https://msdn.microsoft.com/584E78DD-5D08-4A20-B59B-F35178F6595C">display-only device</a> have one 3-D engine.</p>
</dd>

### -field <a id="DXGK_ENGINE_TYPE_VIDEO_DECODE"></a><a id="dxgk_engine_type_video_decode"></a><b>DXGK_ENGINE_TYPE_VIDEO_DECODE</b>

<dd>
<p>The engine that handles video decoding, including decompression of video frames from an input stream into typical YUV surfaces.</p>
<p>The workload packets for an H.264 video codec workload test must appear on either the decode engine or the 3-D engine.</p>
</dd>

### -field <a id="DXGK_ENGINE_TYPE_VIDEO_ENCODE"></a><a id="dxgk_engine_type_video_encode"></a><b>DXGK_ENGINE_TYPE_VIDEO_ENCODE</b>

<dd>
<p>The engine that handles video encoding, including compression of typical video frames into an encoded video format.</p>
</dd>

### -field <a id="DXGK_ENGINE_TYPE_VIDEO_PROCESSING"></a><a id="dxgk_engine_type_video_processing"></a><b>DXGK_ENGINE_TYPE_VIDEO_PROCESSING</b>

<dd>
<p>The engine that is responsible for any video processing that is done after a video input stream is decoded. Such processing can include RGB surface conversion, filtering, stretching, color correction, deinterlacing, or other steps that are required before the final image is rendered to the display screen.</p>
<p>The workload packets for workload tests must appear on either the video processing engine or the 3-D engine.</p>
</dd>

### -field <a id="DXGK_ENGINE_TYPE_SCENE_ASSEMBLY"></a><a id="dxgk_engine_type_scene_assembly"></a><b>DXGK_ENGINE_TYPE_SCENE_ASSEMBLY</b>

<dd>
<p>The engine that performs vertex processing of 3-D workloads as a preliminary pass prior to the remainder of the 3-D rendering. This engine also stores vertices in bins that tile-based rendering engines use.</p>
</dd>

### -field <a id="DXGK_ENGINE_TYPE_COPY"></a><a id="dxgk_engine_type_copy"></a><b>DXGK_ENGINE_TYPE_COPY</b>

<dd>
<p>The engine that is a copy engine used for moving data. This engine can perform subresource updates, blitting, paging, or other similar data handling.</p>
<p>The workload packets for calls to <b>CopySubresourceRegion</b> or <b>UpdateSubResource</b> methods of Direct3D 10 and Direct3D 11 must appear on either the copy engine or the 3-D engine.</p>
</dd>

### -field <a id="DXGK_ENGINE_TYPE_OVERLAY"></a><a id="dxgk_engine_type_overlay"></a><b>DXGK_ENGINE_TYPE_OVERLAY</b>

<dd>
<p>The virtual engine that is used for synchronized flipping of overlays in Direct3D 9.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver should follow these rules to determine the engine type:</p>

<p>For more information on how to use this enumeration, see <a href="https://msdn.microsoft.com/822FEB3E-A39D-4B33-BD9D-F3166EF99AF8">Enumerating GPU engine capabilities</a>.</p>

<p>The display miniport driver should follow these rules to determine the engine type:</p>

<p>For more information on how to use this enumeration, see <a href="https://msdn.microsoft.com/822FEB3E-A39D-4B33-BD9D-F3166EF99AF8">Enumerating GPU engine capabilities</a>.</p>

<p>The display miniport driver should follow these rules to determine the engine type:</p>

<p>For more information on how to use this enumeration, see <a href="https://msdn.microsoft.com/822FEB3E-A39D-4B33-BD9D-F3166EF99AF8">Enumerating GPU engine capabilities</a>.</p>

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
<dt>D3dkmdt.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>