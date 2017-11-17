---
UID: NE.icm.COLORDATATYPE
title: COLORDATATYPE
author: windows-driver-content
description: The values of the COLORDATATYPE enumeration are used by WCS functions to indicate the data type of vector content.
old-location: print\colordatatype.htm
ms.assetid: ff7c9a81-3445-4a9e-aee3-2c63aafb0c82
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: print
req.header: icm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Included in Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: COLORDATATYPE
req.alt-loc: icm.h
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
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
req.iface: 
---

# COLORDATATYPE enumeration



## -description
<p>The values of the COLORDATATYPE enumeration are used by WCS functions to indicate the data type of vector content.</p>


## -syntax

````
typedef enum  { 
  COLOR_BYTE                = 1,
  COLOR_WORD                = 2,
  COLOR_FLOAT               = 3,
  COLOR_S2DOT13FIXED        = 4,
  COLOR_10b_R10G10B10A2     = 5,
  COLOR_10b_R10G10B10A2_XR  = 6,
  COLOR_FLOAT16             = 7
} COLORDATATYPE;
````


## -enum-fields
<dl>

### -field <a id="COLOR_BYTE"></a><a id="color_byte"></a><b>COLOR_BYTE</b>

<dd>
<p>Color data is stored as 8 bits per channel, with a value from 0 to 255, inclusive.</p>
</dd>

### -field <a id="COLOR_WORD"></a><a id="color_word"></a><b>COLOR_WORD</b>

<dd>
<p>Color data is stored as 16 bits per channel, with a value from 0 to 65535, inclusive.</p>
</dd>

### -field <a id="COLOR_FLOAT"></a><a id="color_float"></a><b>COLOR_FLOAT</b>

<dd>
<p>Color data is stored as 32 bits value per channel, as defined by the IEEE 32-bit floating point standard.</p>
</dd>

### -field <a id="COLOR_S2DOT13FIXED"></a><a id="color_s2dot13fixed"></a><b>COLOR_S2DOT13FIXED</b>

<dd>
<p>Color data is stored as 16 bits per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</p>
</dd>

### -field <a id="COLOR_10b_R10G10B10A2"></a><a id="color_10b_r10g10b10a2"></a><a id="COLOR_10B_R10G10B10A2"></a><b>COLOR_10b_R10G10B10A2</b>

<dd>
<p>Packed WORD per channel. data range [0, 1]</p>
</dd>

### -field <a id="COLOR_10b_R10G10B10A2_XR"></a><a id="color_10b_r10g10b10a2_xr"></a><a id="COLOR_10B_R10G10B10A2_XR"></a><b>COLOR_10b_R10G10B10A2_XR</b>

<dd>
<p>Packed extended range WORD per channel. data range [-1, 3]</p>
</dd>

### -field <a id="COLOR_FLOAT16"></a><a id="color_float16"></a><b>COLOR_FLOAT16</b>

<dd>
<p>FLOAT16 per channel.</p>
</dd>
</dl>

## -remarks
<p>The PCOLORDATATYPE and LPCOLORDATATYPE data types are defined as pointers to this enumeration:</p>

<p>The PCOLORDATATYPE and LPCOLORDATATYPE data types are defined as pointers to this enumeration:</p>

<p>The PCOLORDATATYPE and LPCOLORDATATYPE data types are defined as pointers to this enumeration:</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Included in Windows Vista and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Icm.h</dt>
</dl>
</td>
</tr>
</table>