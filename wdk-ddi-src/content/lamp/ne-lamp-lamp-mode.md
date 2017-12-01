---
UID: NE.lamp.LAMP_MODE
title: LAMP_MODE
author: windows-driver-content
description: This enumeration contains the operating modes of a lamp device.
old-location: stream\lamp_mode.htm
old-project: stream
ms.assetid: B379B6EF-C3AD-4E6F-B32D-F85228DB6A72
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: OPTIMAL_WEIGHT_TOTALS, OPTIMAL_WEIGHT_TOTALS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: lamp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LAMP_MODE
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

# LAMP_MODE enumeration



## -description
<p>This enumeration contains the operating modes of a lamp device.</p>


## -syntax

````
typedef enum _LAMP_MODE { 
  LAMP_MODE_WHITE  = 0,
  LAMP_MODE_COLOR
} LAMP_MODE;
````


## -enum-fields
<dl>

### -field <a id="LAMP_MODE_WHITE"></a><a id="lamp_mode_white"></a><b>LAMP_MODE_WHITE</b>

<dd>
<p>Required. White light only.</p>
</dd>

### -field <a id="LAMP_MODE_COLOR"></a><a id="lamp_mode_color"></a><b>LAMP_MODE_COLOR</b>

<dd>
<p>Optional. Color light.</p>
</dd>
</dl>

## -remarks
<p>This is the I/O parameter type of <a href="..\lamp\ni-lamp-ioctl-lamp-get-mode.md">IOCTL_LAMP_GET_MODE</a> and <a href="..\lamp\ni-lamp-ioctl-lamp-set-mode.md">IOCTL_LAMP_SET_MODE</a>.</p>

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