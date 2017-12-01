---
UID: NS.dispmprt._DXGK_VIDEO_OUTPUT_CAPABILITIES
title: DXGK_VIDEO_OUTPUT_CAPABILITIES
author: windows-driver-content
description: The DXGK_VIDEO_OUTPUT_CAPABILITIES structure contains information about the capabilities of a video output on a display adapter.
old-location: display\dxgk_video_output_capabilities.htm
old-project: display
ms.assetid: a673bcea-1a56-48dc-9c63-67583e953571
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_VIDEO_OUTPUT_CAPABILITIES, DXGK_VIDEO_OUTPUT_CAPABILITIES, *PDXGK_VIDEO_OUTPUT_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_VIDEO_OUTPUT_CAPABILITIES
req.alt-loc: dispmprt.h
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
req.iface: 
---

# DXGK_VIDEO_OUTPUT_CAPABILITIES structure



## -description
<p>The DXGK_VIDEO_OUTPUT_CAPABILITIES structure contains information about the capabilities of a video output on a display adapter.</p>


## -syntax

````
typedef struct _DXGK_VIDEO_OUTPUT_CAPABILITIES {
  D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY       InterfaceTechnology;
  D3DKMDT_MONITOR_ORIENTATION_AWARENESS MonitorOrientationAwareness;
  BOOLEAN                               SupportsSdtvModes;
} DXGK_VIDEO_OUTPUT_CAPABILITIES, *PDXGK_VIDEO_OUTPUT_CAPABILITIES;
````


## -struct-fields
<dl>

### -field <b>InterfaceTechnology</b>

<dd>
<p>A <a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-video-output-technology.md">D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY</a> enumerator that indicates the type of connector the video output uses to connect to an external display device.</p>
</dd>

### -field <b>MonitorOrientationAwareness</b>

<dd>
<p>A <a href="..\d3dkmdt\ne-d3dkmdt--d3dkmdt-monitor-orientation-awareness.md">D3DKMDT_MONITOR_ORIENTATION_AWARENESS</a> enumerator that describes the video output's ability to detect the rotation angle of an external display device.</p>
</dd>

### -field <b>SupportsSdtvModes</b>

<dd>
<p>Indicates whether the video output supports standard definition TV (SDTV) modes.</p>
</dd>
</dl>

## -remarks
<p>All child devices of a display adapter are onboard devices. Monitors and other external devices that connect to the display adapter are not considered child devices. Display adapters have two types of child devices: <b>TypeVideoOutput</b> and <b>TypeOther</b>. This structure applies only to child devices of type <b>TypeVideoOutput</b>.</p>

<p>The <b>ChildCapabilities</b> member of a <a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structure is a DXGK_CHILD_CAPABILITIES structure. The <b>Type.VideoOutput</b> member of a DXGK_CHILD_CAPABILITIES structure is a DXGK_VIDEO_OUTPUT_CAPABILITIES structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>
</dt>
<dt>
<a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\dispmprt\ns-dispmprt--dxgk-child-capabilities.md">DXGK_CHILD_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_VIDEO_OUTPUT_CAPABILITIES structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
