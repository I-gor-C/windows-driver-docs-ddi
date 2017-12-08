---
UID: NS.d3dkmddi._DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3
title: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3
author: windows-driver-content
description: Contains arguments for the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay3 function.
old-location: display\dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay3.htm
old-project: display
ms.assetid: 1C6324DB-18E2-4CBC-9589-73DF3EB79503
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3, DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3
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
req.alt-api: DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3
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

# DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 structure



## -description
<p>Contains arguments for the DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay3 function.</p>


## -syntax

````
typedef struct _DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3 {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID           VidPnSourceId;
  DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS   InputFlags;
  DXGK_SETVIDPNSOURCEADDRESS_OUTPUT_FLAGS  OutputFlags;
  UINT                                     PlaneCount;
  DXGK_MULTIPLANE_OVERLAY_PLANE3           **ppPlanes;
  DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION *pPostComposition;
  UINT                                     Duration;
  DXGK_HDR_METADATA                        *pHDRMetaData;
} DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY3;
````


## -struct-fields
<dl>

### -field VidPnSourceId

<dd>
<p>An integer that identifies a video present source on the display adapter.</p>
</dd>

### -field InputFlags

<dd>
<p>A DXGK_SETVIDPNSOURCEADDRESS_INPUT_FLAGS structure that identifies the type of display operation to perform.</p>
</dd>

### -field OutputFlags

<dd>
<p>A DXGK_SETVIPNSOURCEADDRESS_OUTPUT_FLAGS structure that returns information from the driver.</p>
</dd>

### -field PlaneCount

<dd>
<p>The number of overlay planes in the ppPlanes list.</p>
</dd>

### -field ppPlanes

<dd>
<p>An array of pointers to a DXGK_MULTIPLANE_OVERLAY_PLANE3 structures that specify the overlay planes to display.</p>
</dd>

### -field pPostComposition

<dd>
<p>Pointer to a DXGK_MULTIPLANE_OVERLAY_POST_COMPOSITION structure containing virtual mode information and other transform information that should be applied after the planes have been composed.</p>
<p>If NULL, no post composition transforms should be applied.</p>
</dd>

### -field Duration

<dd>
<p>The length of time, in units of 100 nanoseconds, between when the current present operation flips to the screen and the next vertical blanking interrupt occurs.</p>
<p>If zero, the refresh rate should be the default rate based on the current mode.</p>
</dd>

### -field pHDRMetaData

<dd>
<p>Pointer to a DXGK_HDR_METADATA structure indicating any metadata information that might be available. A NULL value indicates that no new metadata is available.</p>
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