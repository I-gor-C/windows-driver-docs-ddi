---
UID: NS.ntddvdeo._DISPLAY_BRIGHTNESS
title: DISPLAY_BRIGHTNESS
author: windows-driver-content
description: The DISPLAY_BRIGHTNESS structure is reserved for system use.
old-location: display\display_brightness.htm
old-project: display
ms.assetid: 0e72c1a7-5712-46fc-a65f-20183830cb72
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DISPLAY_BRIGHTNESS, DISPLAY_BRIGHTNESS, *PDISPLAY_BRIGHTNESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddvdeo.h
req.include-header: Ntddvdeo.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DISPLAY_BRIGHTNESS
req.alt-loc: ntddvdeo.h
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

# DISPLAY_BRIGHTNESS structure



## -description
<p>The DISPLAY_BRIGHTNESS structure is reserved for system use.</p>


## -syntax

````
typedef struct _DISPLAY_BRIGHTNESS {
  UCHAR ucDisplayPolicy;
  UCHAR ucACBrightness;
  UCHAR ucDCBrightness;
} DISPLAY_BRIGHTNESS, *PDISPLAY_BRIGHTNESS;
````


## -struct-fields
<dl>

### -field ucDisplayPolicy

<dd>
<p>Reserved for system use.</p>
</dd>

### -field ucACBrightness

<dd>
<p>Reserved for system use.</p>
</dd>

### -field ucDCBrightness

<dd>
<p>Reserved for system use.</p>
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
<dt>Ntddvdeo.h (include Ntddvdeo.h)</dt>
</dl>
</td>
</tr>
</table>