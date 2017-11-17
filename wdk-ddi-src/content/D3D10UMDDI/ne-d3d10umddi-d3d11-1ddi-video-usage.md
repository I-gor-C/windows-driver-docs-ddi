---
UID: NE.d3d10umddi.D3D11_1DDI_VIDEO_USAGE
title: D3D11_1DDI_VIDEO_USAGE
author: windows-driver-content
description: Identifies how the decode device plays video.
old-location: display\d3d11_1ddi_video_usage.htm
ms.assetid: f107b9a8-d124-4fc3-80b3-dd20a87f9a86
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_VIDEO_USAGE
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# D3D11_1DDI_VIDEO_USAGE enumeration



## -description
<p>Identifies how the decode device plays video.</p>


## -syntax

````
typedef enum D3D11_1DDI_VIDEO_USAGE { 
  D3D11_1DDI_VIDEO_USAGE_PLAYBACK_NORMAL  = 0,
  D3D11_1DDI_VIDEO_USAGE_OPTIMAL_SPEED    = 1,
  D3D11_1DDI_VIDEO_USAGE_OPTIMAL_QUALITY  = 2
} D3D11_1DDI_VIDEO_USAGE;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_VIDEO_USAGE_PLAYBACK_NORMAL"></a><a id="d3d11_1ddi_video_usage_playback_normal"></a><b>D3D11_1DDI_VIDEO_USAGE_PLAYBACK_NORMAL</b>

<dd>
<p>Specifies that the device plays video at normal speed.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_USAGE_OPTIMAL_SPEED"></a><a id="d3d11_1ddi_video_usage_optimal_speed"></a><b>D3D11_1DDI_VIDEO_USAGE_OPTIMAL_SPEED</b>

<dd>
<p>Specifies that the device plays video at optimal speed.</p>
</dd>

### -field <a id="D3D11_1DDI_VIDEO_USAGE_OPTIMAL_QUALITY"></a><a id="d3d11_1ddi_video_usage_optimal_quality"></a><b>D3D11_1DDI_VIDEO_USAGE_OPTIMAL_QUALITY</b>

<dd>
<p>Specifies that the device plays video at optimal quality.</p>
</dd>
</dl>

## -remarks
<p>A value of type <b>D3D11_1DDI_VIDEO_USAGE</b> is specified in the <b>Usage</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450943">D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO</a> structure to help describe a decode device.</p>

<p>A value of type <b>D3D11_1DDI_VIDEO_USAGE</b> is specified in the <b>Usage</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450943">D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO</a> structure to help describe a decode device.</p>

<p>A value of type <b>D3D11_1DDI_VIDEO_USAGE</b> is specified in the <b>Usage</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/hh450943">D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO</a> structure to help describe a decode device.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450943">D3D11_1DDI_VIDEO_DECODER_BUFFER_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_VIDEO_USAGE enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
