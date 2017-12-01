---
UID: NE.d3dkmdt._D3DKMDT_MONITOR_ORIENTATION_AWARENESS
title: D3DKMDT_MONITOR_ORIENTATION_AWARENESS
author: windows-driver-content
description: The D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration is used to describe the ability of a video output device (on the display adapter) to detect changes in the orientation (rotation angle) of a connected external display device.
old-location: display\d3dkmdt_monitor_orientation_awareness.htm
old-project: display
ms.assetid: cea11e84-bff5-4189-9ed4-830049a44a4b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_ORIENTATION_AWARENESS
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration



## -description
<p>The D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration is used to describe the ability of a video output device (on the display adapter) to detect changes in the orientation (rotation angle) of a connected external display device.</p>


## -syntax

````
typedef enum _D3DKMDT_MONITOR_ORIENTATION_AWARENESS { 
  D3DKMDT_MOA_UNINITIALIZED  = 0,
  D3DKMDT_MOA_NONE           = 1,
  D3DKMDT_MOA_POLLED         = 2,
  D3DKMDT_MOA_INTERRUPTIBLE  = 3
} D3DKMDT_MONITOR_ORIENTATION_AWARENESS;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_MOA_UNINITIALIZED"></a><a id="d3dkmdt_moa_uninitialized"></a><b>D3DKMDT_MOA_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_MONITOR_ORIENTATION_AWARENESS has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_MOA_NONE"></a><a id="d3dkmdt_moa_none"></a><b>D3DKMDT_MOA_NONE</b>

<dd>
<p>Indicates that the video output device is unable to determine the orientation of a connected external display device.</p>
</dd>

### -field <a id="D3DKMDT_MOA_POLLED"></a><a id="d3dkmdt_moa_polled"></a><b>D3DKMDT_MOA_POLLED</b>

<dd>
<p>Indicates that the video output device can determine the orientation of a connected external display device, and the display miniport driver can be aware of changes in orientation by polling the video output device.</p>
</dd>

### -field <a id="D3DKMDT_MOA_INTERRUPTIBLE"></a><a id="d3dkmdt_moa_interruptible"></a><b>D3DKMDT_MOA_INTERRUPTIBLE</b>

<dd>
<p>Indicates that the video output device can generate an interrupt when the orientation of a connected external display device changes.</p>
</dd>
</dl>

## -remarks
<p>The <b>ChildCapabilities</b> member of a <a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structure is a <a href="..\dispmprt\ns-dispmprt--dxgk-child-capabilities.md">DXGK_CHILD_CAPABILITIES</a> structure. The <b>Type.VideoOutput</b> member of a CHILD_CAPABILITIES structure is a <a href="..\dispmprt\ns-dispmprt--dxgk-video-output-capabilities.md">DXGK_VIDEO_OUTPUT_CAPABILITIES</a> structure. The <b>MonitorOrientationAwareness</b> member of a VIDEO_OUTPUT_CAPABILITIES structure is a D3DKMDT_MONITOR_ORIENTATION_AWARENESS value.</p>

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
<a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MONITOR_ORIENTATION_AWARENESS enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
