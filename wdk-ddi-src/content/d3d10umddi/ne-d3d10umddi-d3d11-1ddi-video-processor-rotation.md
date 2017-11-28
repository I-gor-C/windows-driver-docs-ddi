---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_PROCESSOR_ROTATION
title: D3D11_1DDI_VIDEO_PROCESSOR_ROTATION
author: windows-driver-content
description: Specifies the clockwise rotation of the input stream of the video processor.
old-location: display\d3d11_1ddi_video_processor_rotation.htm
old-project: display
ms.assetid: 4fe01ddd-723f-4b3c-884a-a18d4f8512e5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_PROCESSOR_ROTATION
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
req.iface: 
---

# D3D11_1DDI_VIDEO_PROCESSOR_ROTATION enumeration



## -description
<p>Specifies the clockwise rotation of the input stream of the video processor.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_PROCESSOR_ROTATION { 
  D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_IDENTITY  = 0,
  D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_90        = 1,
  D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_180       = 2,
  D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_270       = 3
} D3D11_1DDI_VIDEO_PROCESSOR_ROTATION;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_IDENTITY"></a><a id="d3d11_1ddi_video_processor_rotation_identity"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_IDENTITY</b>

<dd>
<p>Indicates that rotation is 0 degrees—landscape mode.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_90"></a><a id="d3d11_1ddi_video_processor_rotation_90"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_90</b>

<dd>
<p>Indicates that rotation is 90 degrees clockwise—portrait mode.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_180"></a><a id="d3d11_1ddi_video_processor_rotation_180"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_180</b>

<dd>
<p>Indicates that rotation is 180 degrees clockwise—inverted landscape mode.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_270"></a><a id="d3d11_1ddi_video_processor_rotation_270"></a><b>D3D11_1DDI_VIDEO_PROCESSOR_ROTATION_270</b>

<dd>
<p>Indicates that rotation is 270 degrees clockwise—inverted portrait mode.</p>
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