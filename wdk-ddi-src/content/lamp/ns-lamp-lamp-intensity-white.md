---
UID: NS.lamp.LAMP_INTENSITY_WHITE
title: LAMP_INTENSITY_WHITE
author: windows-driver-content
description: This structure is the I/O parameter type of IOCTL_LAMP_GET_INTENSITY_WHITE and IOCTL_LAMP_SET_INTENSITY_WHITE.
old-location: stream\lamp_intensity_white.htm
ms.assetid: BDE53311-589F-4458-9510-1B02F1BD0289
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: lamp.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LAMP_INTENSITY_WHITE
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
ms.keywords: LAMP_INTENSITY_WHITE, LAMP_INTENSITY_WHITE
req.iface: 
---

# LAMP_INTENSITY_WHITE structure



## -description
<p>This structure is the I/O parameter type of <a href="https://msdn.microsoft.com/9B9FD4A1-F005-4CB8-80E3-D8AA74F6B9FB">IOCTL_LAMP_GET_INTENSITY_WHITE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/dn925078">IOCTL_LAMP_SET_INTENSITY_WHITE</a>.</p>


## -syntax

````
typedef struct LAMP_INTENSITY_WHITE {
  BYTE Value;
} LAMP_INTENSITY_WHITE;
````


## -struct-fields
<dl>

### -field <b>Value</b>

<dd>
<p>White light intensity in percentage (0-100).</p>
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