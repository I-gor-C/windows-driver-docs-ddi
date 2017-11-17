---
UID: NS.d3dkmddi._DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
title: DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
author: windows-driver-content
description: A structure containing the flags that apply to a plane set by the driver.
old-location: display\dxgk_plane_specific_output_flags.htm
ms.assetid: 95D9C564-92F3-4165-8063-49D928F30475
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
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
ms.keywords: DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS, DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS
req.iface: 
---

# DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS structure



## -description
<p>A structure containing the flags that apply to a plane set by the driver. </p>


## -syntax

````
typedef struct _DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS {
  union {
    struct {
      UINT FlipConvertedToImmediate  :1;
      UINT  PostPresentNeeded  :1;
      UINT HsyncInterruptCompletion  :1;
      UINT Reserved  :29;
    };
    UINT Value;
  };
} DXGK_PLANE_SPECIFIC_OUTPUT_FLAGS;
````


## -struct-fields
<dl>

### -field <b>FlipConvertedToImmediate</b>

<dd>
<p>Indicates that the flip was converted to an immediate flip rather than a VSYNC flip. The driver sets FlipConvertedToImmediate when the current line is less than DXGK_MULTIPLANE_OVERLAY_PLANE3.MaxImmediateFlipLine.</p>
</dd>

### -field <b> PostPresentNeeded</b>

<dd>
<p>  Indicates that scheduler must call DXGDDI_POSTMULTIPLANEOVERLAYPRESENT for this specific plane. The driver must only set this flag for immediate flips.</p>
</dd>

### -field <b>HsyncInterruptCompletion</b>

<dd>
<p>Indicates that the scheduler should not assume that the immediate flip for this plane is completed upon the return from DdiSetVidPnSourceAddressWithMultiPlaneOverlay3 DDI. . Instead, the OS will only assume the immediate flip is completed when it receives a CrtcVsyncWithMultiPlaneOverlay2 interrupt notification with the PresentId greater or equal to pending immediate flip request. CrtcVsyncWithMultiPlaneOverlay2 interrupt notification for this flip may be an HsyncFlipCompletion, or it may be a regular VSync notification. The driver must only set this flag for immediate flips.  </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 27 bits (0xFFFFFFE0) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd></dd>
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