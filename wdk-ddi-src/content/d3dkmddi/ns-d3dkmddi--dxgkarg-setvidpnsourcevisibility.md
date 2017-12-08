---
UID: NS.d3dkmddi._DXGKARG_SETVIDPNSOURCEVISIBILITY
title: DXGKARG_SETVIDPNSOURCEVISIBILITY
author: windows-driver-content
description: The DXGKARG_SETVIDPNSOURCEVISIBILITY structure contains arguments for the DxgkDdiSetVidPnSourceVisibility function.
old-location: display\dxgkarg_setvidpnsourcevisibility.htm
old-project: display
ms.assetid: 073fbcc4-57d8-4709-9605-a3440b5e8e17
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SETVIDPNSOURCEVISIBILITY, DXGKARG_SETVIDPNSOURCEVISIBILITY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SETVIDPNSOURCEVISIBILITY
req.alt-loc: d3dkmddi.h
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

# DXGKARG_SETVIDPNSOURCEVISIBILITY structure



## -description
<p>The DXGKARG_SETVIDPNSOURCEVISIBILITY structure contains arguments for the <a href="display.dxgkddisetvidpnsourcevisibility">DxgkDdiSetVidPnSourceVisibility</a> function.</p>


## -syntax

````
typedef struct _DXGKARG_SETVIDPNSOURCEVISIBILITY {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  BOOLEAN                        Visible;
} DXGKARG_SETVIDPNSOURCEVISIBILITY;
````


## -struct-fields
<dl>

### -field VidPnSourceId

<dd>
<p>An integer that identifies a video present source on the display adapter.</p>
</dd>

### -field Visible

<dd>
<p>A Boolean value that specifies whether the video output codec associated with the source must start scanning or stop scanning the source's primary surface. If <b>Visible</b> is <b>TRUE</b>, the codec must start scanning. </p>
<p>If <b>Visible</b> is <b>FALSE</b>, the codec must stop scanning. However, a VSync signal should be generated even if a call to the <a href="display.dxgkddisetvidpnsourcevisibility">DxgkDdiSetVidPnSourceVisibility</a> function sets <b>Visible</b> to <b>FALSE</b>.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddisetvidpnsourcevisibility">DxgkDdiSetVidPnSourceVisibility</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETVIDPNSOURCEVISIBILITY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
