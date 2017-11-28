---
UID: NS.d3dkmdt._D3DKMDT_VIDEO_PRESENT_TARGET
title: D3DKMDT_VIDEO_PRESENT_TARGET
author: windows-driver-content
description: The D3DKMDT_VIDEO_PRESENT_TARGET structure contains information about a video present target.
old-location: display\d3dkmdt_video_present_target.htm
old-project: display
ms.assetid: e36aba12-51fc-486c-a92c-47f72a4bcb0a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_VIDEO_PRESENT_TARGET,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDEO_PRESENT_TARGET
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

# D3DKMDT_VIDEO_PRESENT_TARGET structure



## -description
<p>The D3DKMDT_VIDEO_PRESENT_TARGET structure contains information about a video present target.</p>


## -syntax

````
typedef struct _D3DKMDT_VIDEO_PRESENT_TARGET {
  D3DDDI_VIDEO_PRESENT_TARGET_ID        Id;
  D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY       VideoOutputTechnology;
  DXGK_CHILD_DEVICE_HPD_AWARENESS       VideoOutputHpdAwareness;
  D3DKMDT_MONITOR_ORIENTATION_AWARENESS MonitorOrientationAwareness;
  BOOLEAN                               SupportsSdtvModes;
} D3DKMDT_VIDEO_PRESENT_TARGET;
````


## -struct-fields
<dl>

### -field <b>Id</b>

<dd>
<p>An integer that uniquely identifies the video present target.</p>
</dd>

### -field <b>VideoOutputTechnology</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546605">D3DKMDT_VIDEO_OUTPUT_TECHNOLOGY</a> enumerator that indicates the target's output technology (for example HD15, DVI, HDMI).</p>
</dd>

### -field <b>VideoOutputHpdAwareness</b>

<dd>
<p>A value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561006">DXGK_CHILD_DEVICE_HPD_AWARENESS</a> enumeration that indicates the target's ability to detect that a monitor has been hot plugged or unplugged.</p>
</dd>

### -field <b>MonitorOrientationAwareness</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546127">D3DKMDT_MONITOR_ORIENTATION_AWARENESS</a> enumerator that indicates the target's ability to detect that a connected monitor (or other display device) has been rotated.</p>
</dd>

### -field <b>SupportsSdtvModes</b>

<dd>
<p>Indicates whether the video output supports standard definition TV (SDTV) modes.</p>
</dd>
</dl>

## -remarks
<p>The D3DDDI_VIDEO_PRESENT_TARGET_ID data type is defined in <i>D3dukmdt.h</i>.</p>

<p>Video present target identifiers are assigned by the display miniport driver. <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>, implemented by the display miniport driver, returns an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561001">DXGK_CHILD_DESCRIPTOR</a> structures, each of which contains an identifier.</p>

<p>For more information about video present targets, see <a href="https://msdn.microsoft.com/62a92f00-b1da-41c2-99af-eef8140b064e">Introduction to Video Present Networks</a>.</p>

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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546614">D3DKMDT_VIDEO_PRESENT_SOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546647">D3DKMDT_VIDPN_PRESENT_PATH</a>
</dt>
<dt>
<a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561001">DXGK_CHILD_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_VIDEO_PRESENT_TARGET structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
