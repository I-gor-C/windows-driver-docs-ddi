---
UID: NS.d3dukmdt._D3DDDI_RATIONAL
title: D3DDDI_RATIONAL
author: windows-driver-content
description: The D3DDDI_RATIONAL structure describes a fractional value that represents vertical and horizontal frequencies of a video mode (that is, vertical sync and horizontal sync).
old-location: display\d3dddi_rational.htm
ms.assetid: b6ae3b68-d9a0-45b3-bf5d-00c09b87709f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_RATIONAL
req.alt-loc: d3dukmdt.h
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
ms.keywords: D3DDDI_RATIONAL, D3DDDI_RATIONAL
req.iface: 
---

# D3DDDI_RATIONAL structure



## -description
<p>The D3DDDI_RATIONAL structure describes a fractional value that represents vertical and horizontal frequencies of a video mode (that is, vertical sync and horizontal sync). </p>


## -syntax

````
typedef struct _D3DDDI_RATIONAL {
  UINT Numerator;
  UINT Denominator;
} D3DDDI_RATIONAL;
````


## -struct-fields
<dl>

### -field <b>Numerator</b>

<dd>
<p>[in] The numerator of the frequency fraction.</p>
</dd>

### -field <b>Denominator</b>

<dd>
<p>[in] The denominator of the frequency fraction.</p>
</dd>
</dl>

## -remarks
<p>Vertical and horizontal frequencies are stored in Hertz (Hz). 
	 The dynamic range of this encoding format, given 10⁻⁷ 
	 resolution, is {0 to (2³² - 1) / 10⁷}. This 
	 range translates to {0 to 428.4967296} Hz for vertical and horizontal 
	 frequencies. This submicrosecond precision range is acceptable even for 
	 a provided application. (An error of one microsecond for video signal 
	 synchronization would imply a time drift with a cycle of 
	 10⁷/(60 x 60 x 24) = 115.741 days.)</p>

<p>For a rational number with a finite fractional sequence, use a denominator of the form 10<sup>(length of fractional sequence)</sup>. For a rational number without a finite fractional sequence, a sequence that exceeds the precision that the dynamic range of the denominator allows, or an irrational number, use an appropriate ratio of integers that best represents the value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dukmdt.h)</dt>
</dl>
</td>
</tr>
</table>