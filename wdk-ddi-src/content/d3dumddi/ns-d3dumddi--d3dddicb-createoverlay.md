---
UID: NS.d3dumddi._D3DDDICB_CREATEOVERLAY
title: D3DDDICB_CREATEOVERLAY
author: windows-driver-content
description: The D3DDDICB_CREATEOVERLAY structure describes overlay hardware.
old-location: display\d3dddicb_createoverlay.htm
old-project: display
ms.assetid: 52f95379-7bfd-4606-9199-ea253ccd6f35
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_CREATEOVERLAY, D3DDDICB_CREATEOVERLAY
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
req.alt-api: D3DDDICB_CREATEOVERLAY
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

# D3DDDICB_CREATEOVERLAY structure



## -description
<p>The D3DDDICB_CREATEOVERLAY structure describes overlay hardware.</p>


## -syntax

````
typedef struct _D3DDDICB_CREATEOVERLAY {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DDDI_KERNELOVERLAYINFO       OverlayInfo;
  D3DKMT_HANDLE                  hKernelOverlay;
} D3DDDICB_CREATEOVERLAY;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology to overlay on (that is, the identifier of the primary surface to overlay on). </p>
</dd>

### -field <b>OverlayInfo</b>

<dd>
<p>[in] A <a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-kerneloverlayinfo.md">D3DDDI_KERNELOVERLAYINFO</a> structure that describes information about the kernel-mode overlay object.</p>
</dd>

### -field <b>hKernelOverlay</b>

<dd>
<p>[out] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the kernel-mode overlay object. This overlay object represents the overlay hardware in subsequent calls by the user-mode display driver to the Microsoft Direct3D runtime.</p>
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
<a href="..\d3dukmdt\ns-d3dukmdt--d3dddi-kerneloverlayinfo.md">D3DDDI_KERNELOVERLAYINFO</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createoverlaycb.md">pfnCreateOverlayCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_CREATEOVERLAY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
