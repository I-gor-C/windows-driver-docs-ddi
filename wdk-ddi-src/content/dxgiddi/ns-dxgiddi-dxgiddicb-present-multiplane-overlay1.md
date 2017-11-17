---
UID: NS.dxgiddi.DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1
title: DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1
author: windows-driver-content
description: Describes multiplane overlay allocations, private driver data, and context information for each multiplane overlay plane.
old-location: display\dxgiddicb_present_multiplane_overlay1.htm
ms.assetid: AA716307-C235-47B2-BEB6-586FD6013280
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxgiddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1
req.alt-loc: dxgiddi.h
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
ms.keywords: DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1, DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1
req.iface: 
---

# DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1 structure



## -description
<p>Describes multiplane overlay allocations, private driver data, and context information for each multiplane overlay plane. </p>


## -syntax

````
typedef struct _DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1 {
  VOID                                  *pDXGIContext;
  DWORD                                 PresentPlaneCount;
  DXGIDDI_MULTIPLANE_OVERLAY_PLANE_INFO **ppPresentPlanes;
} DXGIDDICB_PRESENT_MULTIPLANE_OVERLAY1;
````


## -struct-fields
<dl>

### -field <b>pDXGIContext</b>

<dd>
<p>A handle to the DXGI context. This handle is opaque to the driver. The driver should assign the handle from the pDXGIContext member DXGI_DDI_ARG_PRESENTMULTIPLANEOVERLAY1 structure that the driver received in a call to its pfnPresentMultiplaneOverlay function to this member.</p>
</dd>

### -field <b>PresentPlaneCount</b>

<dd>
<p>The number of planes in the array that the ppPresentPlanes member specifies.</p>
</dd>

### -field <b>ppPresentPlanes</b>

<dd>
<p>An array of pointers to a structure of type DXGIDDI_MULTIPLANE_OVERLAY_PLANE_INFO that specify information about the multiplane overlay planes.</p>
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
<dt>Dxgiddi.h</dt>
</dl>
</td>
</tr>
</table>