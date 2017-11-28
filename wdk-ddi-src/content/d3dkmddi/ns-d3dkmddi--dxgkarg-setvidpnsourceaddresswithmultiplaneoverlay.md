---
UID: NS.d3dkmddi._DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY
title: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY
author: windows-driver-content
description: Contains arguments for the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay function.
old-location: display\dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay.htm
old-project: display
ms.assetid: 12266cb0-20c1-4077-b3c5-fb902f3805d3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY, DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY
req.alt-loc: D3dkmddi.h
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

# DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY structure



## -description
<p>Contains arguments for the <a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a> function.</p>


## -syntax

````
typedef struct _DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY {
  UINT                             ContextCount;
  HANDLE                           Context[1+D3DDDI_MAX_BROADCAST_CONTEXT];
  DXGK_SETVIDPNSOURCEADDRESS_FLAGS Flags;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID   VidPnSourceId;
  UINT                             PlaneCount;
  DXGK_MULTIPLANE_OVERLAY_PLANE    *pPlanes;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3)
  UINT                             Duration;
#endif 
} DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY;
````


## -struct-fields
<dl>

### -field <b>ContextCount</b>

<dd>
<p>[in] The number of contexts in the array that the <b>Context</b> member specifies.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>[in] An array of handles to the contexts that contributed to a display operation.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a> structure that identifies the type of display operation to perform.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>An integer that identifies a video present source on the display adapter.</p>
</dd>

### -field <b>PlaneCount</b>

<dd>
<p>The number of overlay planes that the hardware supports.

</p>
</dd>

### -field <b>pPlanes</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh780305">DXGK_MULTIPLANE_OVERLAY_PLANE</a> structure that specifies the first overlay plane to display.</p>
</dd>

### -field <b>Duration</b>

<dd>
<p>The length of time, in units of 100 nanoseconds, between when the current present operation flips to the screen and the next vertical blanking interrupt occurs.</p>
<p>If zero, the refresh rate should be the default rate based on the current mode.</p>
<p>Must be supported by WDDM 1.3 and later drivers. Available starting with Windows 8.1.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562052">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>
</dt>
<dt>
<a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
