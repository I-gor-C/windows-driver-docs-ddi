---
UID: NS.dxgiddi._DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT
title: DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT
author: windows-driver-content
description: Used in a call to the pfnCheckMultiPlaneOverlaySupport (DXGI) function to check details on hardware support for multiplane overlays.
old-location: display\dxgi_ddi_arg_checkmultiplaneoverlaysupport.htm
old-project: display
ms.assetid: 1b339a88-9c05-4b57-9044-b00ef1c305fb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT, DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: Dxgiddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT
req.alt-loc: Dxgiddi.h
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

# DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT structure



## -description
<p>Used in a call to the <a href="display.pfncheckmultiplaneoverlaysupport__dxgi_">pfnCheckMultiPlaneOverlaySupport (DXGI)</a> function to check details on hardware support for multiplane overlays.</p>


## -syntax

````
typedef struct _DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT {
  DXGI_DDI_HDEVICE                                     hDevice;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID                       VidPnSourceId;
  UINT                                                 NumPlaneInfo;
  DXGI_DDI_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE_INFO *pPlaneInfo;
  BOOL                                                 Supported;
} DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT;
````


## -struct-fields
<dl>

### -field hDevice

<dd>
<p>[in] A handle to the display device (graphics context) on which the driver performs the presentation. The Direct3D runtime passes this handle to the driver in the <b>hDrvDevice</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a> structure when the runtime calls the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function to create the display device. </p>
</dd>

### -field VidPnSourceId

<dd>
<p>[in] The zero-based video present network (VidPN) source identification number of the input for which the hardware support is queried.</p>
</dd>

### -field NumPlaneInfo

<dd>
<p>[out] The number of overlay planes that the hardware supports.</p>
</dd>

### -field pPlaneInfo

<dd>
<p>[out] A pointer to a <a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-check-multiplaneoverlaysupport-plane-info.md">DXGI_DDI_CHECK_MULTIPLANEOVERLAYSUPPORT_PLANE_INFO</a> structure that specifies support attributes that the hardware provides for multiplane overlays.</p>
</dd>

### -field Supported

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
<dt>Dxgiddi.h (include Dxgiddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-check-multiplaneoverlaysupport-plane-info.md">DXGI_DDI_CHECK_MULTIPLANEOVERLAYSUPPORT_PLANE_INFO</a>
</dt>
<dt>
<a href="display.pfncheckmultiplaneoverlaysupport__dxgi_">pfnCheckMultiPlaneOverlaySupport (DXGI)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_ARG_CHECKMULTIPLANEOVERLAYSUPPORT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
