---
UID: NS.d3dkmddi._DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3
title: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3
author: windows-driver-content
description: Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport3 function to check details on hardware support for multi-plane overlays.
old-location: display\dxgkarg_checkmultiplaneoverlaysupport3.htm
old-project: display
ms.assetid: 21FE4E54-5B7D-4068-AC83-A7AFFA739169
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3, DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3
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

# DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3 structure



## -description
<p>Used in a call to the DxgkDdiCheckMultiPlaneOverlaySupport3 function to check details on hardware support for multi-plane overlays.</p>


## -syntax

````
typedef struct _DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3 {
  UINT                                                    PlaneCount;
  DXGK_MULTIPLANE_OVERLAY_PLANE_WITH_SOURCE2              **ppPlanes;
  UINT                                                    PostCompositionCount;
  DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION_WITH_SOURCE    **ppPostComposition;
  BOOL                                                    Supported;
  DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO       ReturnInfo;
} DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3;
````


## -struct-fields
<dl>

### -field <b>PlaneCount</b>

<dd>
<p>The number of input planes to be enabled.</p>
</dd>

### -field <b>ppPlanes</b>

<dd>
<p>An array of pointers pointing to a DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_PLANE3 structure that specifies support attributes that the hardware provides for multi-plane overlays.</p>
</dd>

### -field <b>PostCompositionCount</b>

<dd>
<p>The number of VidPnSources for which we want to apply post composition transforms.</p>
</dd>

### -field <b>ppPostComposition</b>

<dd>
<p>An array of pointers pointing to a DXGK_CHECK_MULTIPLANE_OVERLAY_POST_COMPSOTION_WITH_SOURCE structure that specifies transforms that should be applied after the planes are composed.</p>
</dd>

### -field <b>Supported</b>

<dd>
<p>TRUE if the multi-plane overlay configuration can be supported, otherwise FALSE.</p>
</dd>

### -field <b>ReturnInfo</b>

<dd>
<p>Specifies additional information</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>