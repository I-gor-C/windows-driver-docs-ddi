---
UID: NS.d3dkmdt._DXGK_TARGETMODE_DETAIL_TIMING
title: DXGK_TARGETMODE_DETAIL_TIMING
author: windows-driver-content
description: The DXGK_TARGETMODE_DETAIL_TIMING structure describes a video present target's additional timing modes that are compatible with the display device.
old-location: display\dxgk_targetmode_detail_timing.htm
old-project: display
ms.assetid: bf5e53fa-bafd-4325-be8e-97d1c6aa334e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_TARGETMODE_DETAIL_TIMING, DXGK_TARGETMODE_DETAIL_TIMING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_TARGETMODE_DETAIL_TIMING
req.alt-loc: d3dkmdt.h
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

# DXGK_TARGETMODE_DETAIL_TIMING structure



## -description
<p>The DXGK_TARGETMODE_DETAIL_TIMING structure describes a video present target's additional timing modes that are compatible with the display device.</p>


## -syntax

````
typedef struct _DXGK_TARGETMODE_DETAIL_TIMING {
  D3DKMDT_VIDEO_SIGNAL_STANDARD    VideoStandard;
  UINT                             TimingId;
  DISPLAYID_DETAILED_TIMING_TYPE_I DetailTiming;
} DXGK_TARGETMODE_DETAIL_TIMING;
````


## -struct-fields
<dl>

### -field <b>VideoStandard</b>

<dd>
<p>[in] A <a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-video-signal-standard.md">D3DKMDT_VIDEO_SIGNAL_STANDARD</a>-typed value that indicates the supported video signal standard.</p>
</dd>

### -field <b>TimingId</b>

<dd>
<p>[in] A UINT value that describes the registry ID of the video standard data described by <b>VideoStandard</b>. The high 8 bits indicate the target mode's video standard. The low 24 bits indicate the mode index in the video standard.</p>
</dd>

### -field <b>DetailTiming</b>

<dd>
<p>[in] A <a href="..\d3dkmdt\ns-d3dkmdt--displayid-detailed-timing-type-i.md">DISPLAYID_DETAILED_TIMING_TYPE_I</a>-typed value that indicates the target mode data for a video present target.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-video-signal-standard.md">D3DKMDT_VIDEO_SIGNAL_STANDARD</a>
</dt>
<dt>
<a href="..\d3dkmdt\ns-d3dkmdt--displayid-detailed-timing-type-i.md">DISPLAYID_DETAILED_TIMING_TYPE_I</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_TARGETMODE_DETAIL_TIMING structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
