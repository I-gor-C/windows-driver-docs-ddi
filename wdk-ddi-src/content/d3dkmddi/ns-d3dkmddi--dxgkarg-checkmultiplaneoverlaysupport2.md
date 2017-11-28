---
UID: NS.d3dkmddi._DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2
title: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2
author: windows-driver-content
description: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 is passed to the DxgkDdiCheckMultiPlaneOverlaySupport2 function to determine whether a specific multi-plane overlay configuration is supported.
old-location: display\dxgkarg_checkmultiplaneoverlaysupport2.htm
old-project: display
ms.assetid: 477EBC8A-04A5-4904-AC62-0FA7DB861ACC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2, DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2
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
req.alt-api: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2
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

# DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 structure



## -description
<p><b>DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2</b> is passed to the  <a href="display.dxgkddicheckmultiplaneoverlaysupport2">DxgkDdiCheckMultiPlaneOverlaySupport2</a> function to determine whether a specific multi-plane overlay configuration is supported. </p>


## -syntax

````
typedef struct _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 {
  UINT                                              PlaneCount;
  DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE*        pPlanes;
  BOOL                                              Supported;
  DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO ReturnInfo;
} DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2;
````


## -struct-fields
<dl>

### -field <b>PlaneCount</b>

<dd>
<p>The number of planes to be enabled.</p>
</dd>

### -field <b>pPlanes</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn914479">DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE</a> 
                                                                        structure that specifies support attributes that the hardware
                                                                        provides for multi-plane overlays.</p>
</dd>

### -field <b>Supported</b>

<dd>
<p><b>TRUE</b> if the multi-plane overlay configuration can be supported, otherwise <b>FALSE</b>.</p>
</dd>

### -field <b>ReturnInfo</b>

<dd>
<p>Specifies additional information.</p>
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
<a href="display.dxgkddicheckmultiplaneoverlaysupport2">DxgkDdiCheckMultiPlaneOverlaySupport2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn914479">DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
