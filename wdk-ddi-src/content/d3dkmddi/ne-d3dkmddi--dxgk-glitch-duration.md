---
UID: NE.d3dkmddi._DXGK_GLITCH_DURATION
title: DXGK_GLITCH_DURATION
author: windows-driver-content
description: Enumeration that describes the duration of a user visible effect of a glitch during a SetTimingsFromVidPn call.
old-location: display\dxgk_glitch_duration.htm
old-project: display
ms.assetid: 8B6597A7-D652-4143-9320-7FB8E98FE8EC
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_GLITCH_DURATION
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

# DXGK_GLITCH_DURATION enumeration



## -description
<p>Enumeration that describes the duration of a user visible effect of a glitch during a SetTimingsFromVidPn call.</p>


## -syntax

````
typedef enum _DXGK_GLITCH_DURATION { 
  DXGK_GLITCH_DURATION_INDEFINITE    = 0,
  DXGK_GLITCH_DURATION_MULTI_FRAME   = 1,
  DXGK_GLITCH_DURATION_SINGLE_FRAME  = 2,
  DXGK_GLITCH_DURATION_MULTI_LINE    = 3,
  DXGK_GLITCH_DURATION_SINGLE_LINE   = 4,
  DXGK_GLITCH_DURATION_NONE          = 255
} DXGK_GLITCH_DURATION;
````


## -enum-fields
<dl>

### -field DXGK_GLITCH_DURATION_INDEFINITE

<dd>
<p>Indicates that a glitch is unresolved.</p>
</dd>

### -field DXGK_GLITCH_DURATION_MULTI_FRAME

<dd>
<p>Indicates that a glitch lasted for multiple frames.</p>
</dd>

### -field DXGK_GLITCH_DURATION_SINGLE_FRAME

<dd>
<p>Indicates that a glitch lasted for no more than one frame.</p>
</dd>

### -field DXGK_GLITCH_DURATION_MULTI_LINE

<dd>
<p>Indicates that a glitch lasted for multiple lines within a frame.</p>
</dd>

### -field DXGK_GLITCH_DURATION_SINGLE_LINE

<dd>
<p>Indicates that a glitch lasted for no more than one line.</p>
</dd>

### -field DXGK_GLITCH_DURATION_NONE

<dd>
<p>Indicates that there was no user visible glitch.</p>
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