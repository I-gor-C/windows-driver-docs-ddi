---
UID: NS.d3dkmddi._DXGKARG_SETTIMINGSFROMVIDPN
title: DXGKARG_SETTIMINGSFROMVIDPN
author: windows-driver-content
description: Used to hold the arguments for DXGKDDI_SETTIMINGSFROMVIDPN.
old-location: display\dxgkarg_settimingsfromvidpn.htm
ms.assetid: 14D652C4-9812-481E-8E69-A6D7923F01A3
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
req.alt-api: DXGKARG_SETTIMINGSFROMVIDPN
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
ms.keywords: DXGKARG_SETTIMINGSFROMVIDPN, DXGKARG_SETTIMINGSFROMVIDPN
req.iface: 
---

# DXGKARG_SETTIMINGSFROMVIDPN structure



## -description
<p>Used to hold the arguments for <a href="https://msdn.microsoft.com/7E991251-1738-41AD-83D6-60DD7E183D68">DXGKDDI_SETTIMINGSFROMVIDPN</a>.</p>


## -syntax

````
typedef struct _DXGKARG_SETTIMINGSFROMVIDPN {
  D3DKMDT_HVIDPN            hFunctionalVidPn;
  DXGK_SET_TIMING_FLAGS     SetFlags;
  PDXGK_SET_TIMING_RESULTS  pResultsFlags;
  UINT                      PathCount;
  DXGK_SET_TIMING_PATH_INFO *pSetTimingPathInfo;
} DXGKARG_SETTIMINGSFROMVIDPN, *PDXGKARG_SETTIMINGSFROMVIDPN;
````


## -struct-fields
<dl>

### -field <b>hFunctionalVidPn</b>

<dd>
<p>Handle to a functional VidPn which describes the display configuration the OS is attempting to apply.</p>
</dd>

### -field <b>SetFlags</b>

<dd>
<p> A DXGK_SET_TIMING_FLAGS structure that requests specific actions from the driver on the SetTimingsFromVidPn call.</p>
</dd>

### -field <b>pResultsFlags</b>

<dd>
<p>Pointer to a DXGK_SET_TIMING_RESULTS structure that the driver should use to report overall results from the SetTimingsFromVidPn call.</p>
</dd>

### -field <b>PathCount</b>

<dd>
<p>Number of pointers in the array pointed to by pSetTimingPathInfo.</p>
</dd>

### -field <b>pSetTimingPathInfo</b>

<dd>
<p>An array of pointers to DXGK_SET_TIMING_PATH_INFO structures that specify per path details of the timings to be set. It also allows feedback from the driver on additional work the OS needs to do either before the timings changes can be made, or after changes are complete.</p>
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