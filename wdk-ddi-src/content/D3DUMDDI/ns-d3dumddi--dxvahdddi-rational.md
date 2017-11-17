---
UID: NS.d3dumddi._DXVAHDDDI_RATIONAL
title: DXVAHDDDI_RATIONAL
author: windows-driver-content
description: The DXVAHDDDI_RATIONAL structure describes a fractional value that represents the vertical and horizontal frequencies of a video mode (that is, vertical sync and horizontal sync).
old-location: display\dxvahdddi_rational.htm
ms.assetid: 4560fb48-24c3-4beb-acc3-b8d2ed3a81d3
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: DXVAHDDDI_RATIONAL is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVAHDDDI_RATIONAL
req.alt-loc: d3dumddi.h
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
ms.keywords: DXVAHDDDI_RATIONAL, DXVAHDDDI_RATIONAL
req.iface: 
---

# DXVAHDDDI_RATIONAL structure



## -description
<p>The DXVAHDDDI_RATIONAL structure describes a fractional value that represents the vertical and horizontal frequencies of a video mode (that is, vertical sync and horizontal sync). </p>


## -syntax

````
typedef struct _DXVAHDDDI_RATIONAL {
  UINT Numerator;
  UINT Denominator;
} DXVAHDDDI_RATIONAL;
````


## -struct-fields
<dl>

### -field <b>Numerator</b>

<dd>
<p>[in] The numerator of the frequency fraction. </p>
</dd>

### -field <b>Denominator</b>

<dd>
<p>[in] The denominator of the frequency fraction. </p>
</dd>
</dl>

## -remarks
<p>An output rate of 0/0 is valid. The driver interprets 0/0 as 0/1. The driver interprets 0/any value as zero. </p>

<p>The NTSC frame rate is 30000/1001, and the PAL frame rate is 25/1. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>DXVAHDDDI_RATIONAL is supported beginning with the Windows 7 operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>