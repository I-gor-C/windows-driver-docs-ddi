---
UID: NE.icm.COLORDATATYPE
title: COLORDATATYPE
author: windows-driver-content
description: The values of the COLORDATATYPE enumeration are used by WCS functions to indicate the data type of vector content.
old-location: print\colordatatype.htm
old-project: print
ms.assetid: ff7c9a81-3445-4a9e-aee3-2c63aafb0c82
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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

### -field COLOR_BYTE

<dd>
<p>Color data is stored as 8 bits per channel, with a value from 0 to 255, inclusive.</p>
</dd>

### -field COLOR_WORD

<dd>
<p>Color data is stored as 16 bits per channel, with a value from 0 to 65535, inclusive.</p>
</dd>

### -field COLOR_FLOAT

<dd>
<p>Color data is stored as 32 bits value per channel, as defined by the IEEE 32-bit floating point standard.</p>
</dd>

### -field COLOR_S2DOT13FIXED

<dd>
<p>Color data is stored as 16 bits per channel, with a fixed range of -4 to +4, inclusive. A signed format is used, with 1 bit for the sign, 2 bits for the integer portion, and 13 bits for the fractional portion.</p>
</dd>

### -field COLOR_10b_R10G10B10A2

<dd>
<p>Packed WORD per channel. data range [0, 1]</p>
</dd>

### -field COLOR_10b_R10G10B10A2_XR

<dd>
<p>Packed extended range WORD per channel. data range [-1, 3]</p>
</dd>

### -field COLOR_FLOAT16

<dd>
<p>FLOAT16 per channel.</p>
</dd>
</dl>

## -remarks
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