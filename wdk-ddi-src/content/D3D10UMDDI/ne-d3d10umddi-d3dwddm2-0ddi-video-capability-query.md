---
UID: NE.d3d10umddi.D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY
title: D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY
author: windows-driver-content
description: Describes the video capabilities to query.
old-location: display\d3dwddm2_0ddi_video_capability_query.htm
ms.assetid: A8BA3FF9-A821-43ED-91CB-EECD0ABA0954
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY
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

# D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY enumeration



## -description
<p>Describes the video capabilities to query.</p>


## -syntax

````
typedef enum D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY { 
  D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_DECODER_CAPS                    = 1,
  D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_DECODER_DOWNSAMPLING            = 2,
  D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_RECOMMEND_DECODER_DOWNSAMPLING  = 3
} D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY;
````


## -enum-fields
<dl>

### -field <a id="D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_DECODER_CAPS"></a><a id="d3dwddm2_0ddi_video_capability_query_decoder_caps"></a><b>D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_DECODER_CAPS</b>

<dd>
<p>Indicates that the driver should return video decoder capabilities.

</p>
<p>The input structure is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn894614">D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS</a>.
</p>
</dd>

### -field <a id="D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_DECODER_DOWNSAMPLING"></a><a id="d3dwddm2_0ddi_video_capability_query_decoder_downsampling"></a><b>D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_DECODER_DOWNSAMPLING</b>

<dd>
<p>Indicates that the driver should return support for the specified down sampling parameters specified.

</p>
<p>The input structure is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn894615">D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING</a>.</p>
</dd>

### -field <a id="D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_RECOMMEND_DECODER_DOWNSAMPLING"></a><a id="d3dwddm2_0ddi_video_capability_query_recommend_decoder_downsampling"></a><b>D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY_RECOMMEND_DECODER_DOWNSAMPLING</b>

<dd>
<p>Indicates that the driver should recommend down sampling parameters.

</p>
<p>The input structure is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn894617">D3DWDDM2_0DDI_VIDEO_CAPABILITY_RECOMMEND_DECODER_DOWNSAMPLING</a>.</p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894614">D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894615">D3DWDDM2_0DDI_VIDEO_CAPABILITY_DECODER_DOWNSAMPLING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894617">D3DWDDM2_0DDI_VIDEO_CAPABILITY_RECOMMEND_DECODER_DOWNSAMPLING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DWDDM2_0DDI_VIDEO_CAPABILITY_QUERY enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
