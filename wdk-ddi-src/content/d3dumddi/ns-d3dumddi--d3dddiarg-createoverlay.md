---
UID: NS.d3dumddi._D3DDDIARG_CREATEOVERLAY
title: D3DDDIARG_CREATEOVERLAY
author: windows-driver-content
description: The D3DDDIARG_CREATEOVERLAY structure describes an overlay to create.
old-location: display\d3dddiarg_createoverlay.htm
old-project: display
ms.assetid: 74252431-5250-408a-91cc-cc529396f720
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_CREATEOVERLAY, D3DDDIARG_CREATEOVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_CREATEOVERLAY
req.alt-loc: d3dumddi.h
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

# D3DDDIARG_CREATEOVERLAY structure



## -description
<p>The D3DDDIARG_CREATEOVERLAY structure describes an overlay to create. </p>


## -syntax

````
typedef struct _D3DDDIARG_CREATEOVERLAY {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DDDI_OVERLAYINFO             OverlayInfo;
  HANDLE                         hOverlay;
} D3DDDIARG_CREATEOVERLAY;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology to overlay on (that is, the identifier of the primary surface to overlay on).</p>
</dd>

### -field <b>OverlayInfo</b>

<dd>
<p>[in] A pointer to the <a href="..\d3dumddi\ns-d3dumddi--d3dddi-overlayinfo.md">D3DDDI_OVERLAYINFO</a> structure that describes information about the overlay. </p>
</dd>

### -field <b>hOverlay</b>

<dd>
<p>[out] A handle to the overlay. The user-mode display driver must set this handle to a value that the Microsoft Direct3D runtime can use to identify the overlay hardware in subsequent calls.</p>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createoverlay.md">CreateOverlay</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-overlayinfo.md">D3DDDI_OVERLAYINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CREATEOVERLAY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
