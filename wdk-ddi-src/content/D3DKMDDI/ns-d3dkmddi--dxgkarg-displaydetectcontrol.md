---
UID: NS.d3dkmddi._DXGKARG_DISPLAYDETECTCONTROL
title: DXGKARG_DISPLAYDETECTCONTROL
author: windows-driver-content
description: Used to hold the arguments for DXGKDDI_DISPLAYDETECTCONTROL.
old-location: display\dxgkarg_displaydetectcontrol.htm
ms.assetid: A0B5798E-FF4D-4133-BFA9-39B37CC387F6
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
req.alt-api: DXGKARG_DISPLAYDETECTCONTROL
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
ms.keywords: DXGKARG_DISPLAYDETECTCONTROL, DXGKARG_DISPLAYDETECTCONTROL
req.iface: 
---

# DXGKARG_DISPLAYDETECTCONTROL structure



## -description
<p>Used to hold the arguments for <a href="https://msdn.microsoft.com/6F10EA4D-BCDE-475E-9937-414CB83F6F2F">DXGKDDI_DISPLAYDETECTCONTROL</a>.</p>


## -syntax

````
typedef struct _DXGKARG_DISPLAYDETECTCONTROL {
  D3DDDI_VIDEO_PRESENT_TARGET_ID TargetID  :24;
  DXGK_DISPLAYDETECTCONTROLTYPE  Type  :4;
  UINT                           NonDestructiveOnly  :1;
  UINT                           Reserved  :3;
} DXGKARG_DISPLAYDETECTCONTROL, *PDXGKARG_DISPLAYDETECTCONTROL;
````


## -struct-fields
<dl>

### -field <b>TargetID</b>

<dd>
<p>The identifier of a display adapter's video present target.  Ignored if the type is not DXGK_DDCT_POLLONE.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>Detection action type requested.</p>
</dd>

### -field <b>NonDestructiveOnly</b>

<dd>
<p>Only used for polling the types of requests.
If TRUE, the driver should attempt to poll the specified target(s) without causing any visual artifacts. 
If FALSE, the driver should perform any action necessary to detect the status of the specified target(s) even if it would cause visual artifacts on the target(s) in question or other targets.
</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This value is reserved for system use.</p>
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