---
UID: NS.d3dkmddi._DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2
title: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2
author: windows-driver-content
description: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 is passed to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to change the overlay configuration being displayed.DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 is passed to the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2 function to change the overlay configuration being displayed.
old-location: display\dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay2.htm
old-project: display
ms.assetid: 6138BAF5-F953-47E7-A572-BE4673CF7046
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2, DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2
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

# DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 structure



## -description
<p>
<p><b>DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2</b> is passed to the  <a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay2">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2</a> function to change the overlay configuration being displayed.</p>
</p>
<p><b>DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2</b> is passed to the  <a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay2">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2</a> function to change the overlay configuration being displayed.</p>


## -syntax

````
typedef struct _DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 {
  UINT                             ContextCount;
  HANDLE                           Context[1+D3DDDI_MAX_BROADCAST_CONTEXT];
  DXGK_SETVIDPNSOURCEADDRESS_FLAGS Flags;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID   VidPnSourceId;
  UINT                             PlaneCount;
  DXGK_MULTIPLANE_OVERLAY_PLANE2   pPlanes;
  UINT                             Duration;
} DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2;
````


## -struct-fields
<dl>

### -field <b>ContextCount</b>

<dd>
<p>The number of contexts in the array that the <b>Context</b> member specifies.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>An array of handles to the contexts that contributed to a display operation.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a> structure that identifies the type of display operation to perform.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>An integer that identifies a video present source on the display adapter.</p>
</dd>

### -field <b>PlaneCount</b>

<dd>
<p>The number of overlay planes in the <b>pPlanes</b> list.</p>
</dd>

### -field <b>pPlanes</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/dn914478">DXGK_MULTIPLANE_OVERLAY_PLANE2</a> structures that specify the overlay planes to display.</p>
</dd>

### -field <b>Duration</b>

<dd>
<p>The length of time, in 100 nanoseconds units, between when the current present operation flips to the screen and the next vertical blanking interrupt occurs.</p>
<p>If zero, the refresh rate should be the default rate based on the current mode.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay2">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn914478">DXGK_MULTIPLANE_OVERLAY_PLANE2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
