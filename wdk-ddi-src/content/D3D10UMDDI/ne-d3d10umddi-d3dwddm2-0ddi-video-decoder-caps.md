---
UID: NE.d3d10umddi.D3DWDDM2_0DDI_VIDEO_DECODER_CAPS
title: D3DWDDM2_0DDI_VIDEO_DECODER_CAPS
author: windows-driver-content
description: Describes the video decoder capabilities.
old-location: display\d3dwddm2_0ddi_video_decoder_caps.htm
ms.assetid: 1C3E07CB-917D-4B3E-979D-4DBD38957B98
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
req.alt-api: D3DWDDM2_0DDI_VIDEO_DECODER_CAPS
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

# D3DWDDM2_0DDI_VIDEO_DECODER_CAPS enumeration



## -description
<p>Describes the video decoder capabilities.</p>


## -syntax

````
typedef enum D3DWDDM2_0DDI_VIDEO_DECODER_CAPS { 
  D3DWDDM2_0DDI_VIDEO_DECODER_CAP_DOWNSAMPLE           = 0x01,
  D3DWDDM2_0DDI_VIDEO_DECODER_CAP_NON_REAL_TIME        = 0x02,
  D3DWDDM2_0DDI_VIDEO_DECODER_CAP_DOWNSAMPLE_REQUIRED  = 0x04,
  D3DWDDM2_0DDI_VIDEO_DECODER_CAP_UNSUPPORTED          = 0x08
} D3DWDDM2_0DDI_VIDEO_DECODER_CAPS;
````


## -enum-fields
<dl>

### -field <a id="D3DWDDM2_0DDI_VIDEO_DECODER_CAP_DOWNSAMPLE"></a><a id="d3dwddm2_0ddi_video_decoder_cap_downsample"></a><b>D3DWDDM2_0DDI_VIDEO_DECODER_CAP_DOWNSAMPLE</b>

<dd>
<p>Indicates that the driver can support at least some downsampling scenarios.</p>
</dd>

### -field <a id="D3DWDDM2_0DDI_VIDEO_DECODER_CAP_NON_REAL_TIME"></a><a id="d3dwddm2_0ddi_video_decoder_cap_non_real_time"></a><b>D3DWDDM2_0DDI_VIDEO_DECODER_CAP_NON_REAL_TIME</b>

<dd>
<p>The decode operation is supported, but cannot be performed real-time.  Indicates that the decode hardware cannot support the decode operation in real-time. Decode is still viable for transcode scenarios. 

</p>
<p>It is possible that decode can occur in real-time if downsampling is applied.</p>
</dd>

### -field <a id="D3DWDDM2_0DDI_VIDEO_DECODER_CAP_DOWNSAMPLE_REQUIRED"></a><a id="d3dwddm2_0ddi_video_decoder_cap_downsample_required"></a><b>D3DWDDM2_0DDI_VIDEO_DECODER_CAP_DOWNSAMPLE_REQUIRED</b>

<dd>
<p>	Indicates that the decode configuration can be supported only if down sampling is applied. </p>
</dd>

### -field <a id="D3DWDDM2_0DDI_VIDEO_DECODER_CAP_UNSUPPORTED"></a><a id="d3dwddm2_0ddi_video_decoder_cap_unsupported"></a><b>D3DWDDM2_0DDI_VIDEO_DECODER_CAP_UNSUPPORTED</b>

<dd>
<p>	Indicates that the decode configuration is not supported. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906368">QueryVideoCapabilities</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DWDDM2_0DDI_VIDEO_DECODER_CAPS enumeration%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
