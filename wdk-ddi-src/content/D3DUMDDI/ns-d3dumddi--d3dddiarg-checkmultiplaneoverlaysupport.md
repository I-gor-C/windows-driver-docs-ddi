---
UID: NS.d3dumddi._D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT
title: D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: Used in a call to the pfnCheckMultiPlaneOverlaySupport (D3D) function to check details on hardware support for multiplane overlays.
old-location: display\d3dddiarg_checkmultiplaneoverlaysupport.htm
ms.assetid: e5b6c24a-a3a5-4736-b9ee-ebb992070a83
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT
req.alt-loc: D3dumddi.h
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
ms.keywords: D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT, D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT
req.iface: 
---

# D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT structure



## -description
<p>Used in a call to the <a href="https://msdn.microsoft.com/A439E695-D374-439A-8A69-6D4E247FF134">pfnCheckMultiPlaneOverlaySupport (D3D)</a> function to check details on hardware support for multiplane overlays.</p>


## -syntax

````
typedef struct _D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID                     VidPnSourceId;
  UINT                                               NumPlanes;
  D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO *pPlanes;
  BOOL                                               Supported;
} D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT;
````


## -struct-fields
<dl>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based video present network (VidPN) source identification number of the input for which the hardware support is queried.</p>
</dd>

### -field <b>NumPlanes</b>

<dd>
<p>[out] The number of overlay planes that the hardware supports.</p>
</dd>

### -field <b>pPlanes</b>

<dd>
<p>[out] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh780232">D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO</a> structure that specifies support attributes that the hardware provides for multiplane overlays.</p>
</dd>

### -field <b>Supported</b>

<dd>
<p>[out] <b>TRUE</b> if the hardware supports multiplane overlays, otherwise <b>FALSE</b>.
</p>
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
<dt>D3dumddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh780232">D3DDDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/A439E695-D374-439A-8A69-6D4E247FF134">pfnCheckMultiPlaneOverlaySupport (D3D)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CHECKMULTIPLANEOVERLAYSUPPORT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
