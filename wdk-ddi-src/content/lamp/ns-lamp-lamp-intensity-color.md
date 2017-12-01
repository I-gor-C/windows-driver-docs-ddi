---
UID: NS.lamp.LAMP_INTENSITY_COLOR
title: LAMP_INTENSITY_COLOR
author: windows-driver-content
description: This structure is the I/O parameter type of IOCTL_LAMP_GET_INTENSITY_COLOR and IOCTL_LAMP_SET_INTENSITY_COLOR.
old-location: stream\lamp_intensity_color.htm
old-project: stream
ms.assetid: F87AFCA5-651C-4782-9F6F-C0AFB09010CB
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: LAMP_INTENSITY_COLOR, LAMP_INTENSITY_COLOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: lamp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LAMP_INTENSITY_COLOR
req.alt-loc: lamp.h
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
req.iface: 
---

# LAMP_INTENSITY_COLOR structure



## -description
<p>This structure is the I/O parameter type of <a href="..\lamp\ni-lamp-ioctl-lamp-get-intensity-color.md">IOCTL_LAMP_GET_INTENSITY_COLOR</a> and <a href="..\lamp\ni-lamp-ioctl-lamp-set-intensity-color.md">IOCTL_LAMP_SET_INTENSITY_COLOR</a>.</p>


## -syntax

````
typedef struct LAMP_INTENSITY_COLOR {
  BYTE Red;
  BYTE Green;
  BYTE Blue;
} LAMP_INTENSITY_COLOR;
````


## -struct-fields
<dl>

### -field <b>Red</b>

<dd>
<p>Red light intensity in percentage (0-100).</p>
</dd>

### -field <b>Green</b>

<dd>
<p>Green light intensity in percentage (0-100).</p>
</dd>

### -field <b>Blue</b>

<dd>
<p>Blue light intensity in percentage (0-100).</p>
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
<dt>Lamp.h</dt>
</dl>
</td>
</tr>
</table>