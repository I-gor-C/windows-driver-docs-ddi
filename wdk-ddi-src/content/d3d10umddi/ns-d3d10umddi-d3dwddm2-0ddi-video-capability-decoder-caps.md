---
UID: NS.d3d10umddi.D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS
title: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS
author: windows-driver-content
description: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS contains information describing the capabilities of the video decoder.
old-location: display\d3dwddm2_0ddi_video_capability_decoder_caps.htm
old-project: display
ms.assetid: C248B20E-A9A1-4C79-9053-16AC2059205E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS, D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS
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

# D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS structure



## -description
<p><b>D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS</b> contains information describing the capabilities of the video decoder.</p>


## -syntax

````
typedef struct D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS {
  GUID          DecodeProfile;
  UINT          SampleWidth;
  UINT          SampleHeight;
  DXGI_RATIONAL FrameRate;
  UINT          Caps;
} D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS;
````


## -struct-fields
<dl>

### -field <b>DecodeProfile</b>

<dd>
<p>Indicates the decode profile for which the capabilities are queried.</p>
</dd>

### -field <b>SampleWidth</b>

<dd>
<p>Indicates the video width for which the capabilities are queried.</p>
</dd>

### -field <b>SampleHeight</b>

<dd>
<p>Indicates the video height for which the capabilities are queried.</p>
</dd>

### -field <b>FrameRate</b>

<dd>
<p>Indicates the frame rate of the video content.</p>
</dd>

### -field <b>Caps</b>

<dd>
<p>Returns a combination of <a href="https://msdn.microsoft.com/library/windows/hardware/dn894620">D3DWDDM2_0DDI_VIDEO_DECODER_CAPS</a> enumeration values combined together using a bitwise <i>OR</i> operation.</p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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