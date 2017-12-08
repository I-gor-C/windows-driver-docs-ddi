---
UID: NS.D3DKMDDI._DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT
title: _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport function to check details on hardware support for multiplane overlays.
old-location: display\dxgkarg_checkmultiplaneoverlaysupport.htm
old-project: display
ms.assetid: BAFC7DD1-56F8-47CE-8914-54531BBC3165
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT, DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT
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
req.alt-api: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT
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
---

# _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT structure



## -description
Used in a call to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport.md">DxgkDdiCheckMultiPlaneOverlaySupport</a> function to check details on hardware support for multiplane overlays.


## -syntax

````
typedef struct _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT {
  UINT                                              PlaneCount;
  DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE       *pPlanes;
  BOOL                                              Supported;
  DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO ReturnInfo;
} DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT, *PDXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT;
````


## -struct-fields

### -field PlaneCount

The number of overlay planes that the hardware supports.

### -field pPlanes

A pointer to a <a href="display.dxgk_check_multiplane_overlay_support_plane">DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE</a> structure that specifies support attributes that the hardware provides for multiplane overlays.

### -field Supported

<b>TRUE</b> if the hardware supports multiplane overlays, otherwise <b>FALSE</b>.

### -field ReturnInfo

Specifies limitations on hardware support of multiplane overlays.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="display.dxgk_check_multiplane_overlay_support_plane">DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport.md">DxgkDdiCheckMultiPlaneOverlaySupport</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>