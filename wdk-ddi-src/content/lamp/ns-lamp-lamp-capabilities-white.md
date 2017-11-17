---
UID: NS.lamp.LAMP_CAPABILITIES_WHITE
title: LAMP_CAPABILITIES_WHITE
author: windows-driver-content
description: This structure is the I/O parameter type of IOCTL_LAMP_{GET|SET}_INTENSITY_WHITE.
old-location: stream\lamp_capabilities_white.htm
ms.assetid: F407B953-8B03-4053-A5F4-3E96E9F9645E
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
req.alt-api: LAMP_CAPABILITIES_WHITE
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
ms.keywords: LAMP_CAPABILITIES_WHITE, LAMP_CAPABILITIES_WHITE
req.iface: 
---

# LAMP_CAPABILITIES_WHITE structure



## -description
<p>This structure is the I/O parameter type of <b>IOCTL_LAMP_{GET|SET}_INTENSITY_WHITE</b>.</p>


## -syntax

````
typedef struct LAMP_CAPABILITIES_WHITE {
  BOOLEAN IsLightIntensityAdjustable;
} LAMP_CAPABILITIES_WHITE;
````


## -struct-fields
<dl>

### -field <b>IsLightIntensityAdjustable</b>

<dd>
<p>If this field evaluates <b>TRUE</b>, a client can get/set light intensity by calling <a href="https://msdn.microsoft.com/9B9FD4A1-F005-4CB8-80E3-D8AA74F6B9FB">IOCTL_LAMP_GET_INTENSITY_WHITE</a>  and <a href="https://msdn.microsoft.com/library/windows/hardware/dn925078">IOCTL_LAMP_SET_INTENSITY_WHITE</a>.</p>
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