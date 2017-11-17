---
UID: NS.ksmedia.tagKS_RGBQUAD
title: tagKS_RGBQUAD
author: windows-driver-content
description: The KS_RGBQUAD structure describes a color consisting of relative intensities of red, green, and blue, ranging from 0 to 255 (0x0 to 0xff).
old-location: stream\ks_rgbquad.htm
ms.assetid: 49231293-286b-486d-b8f9-b44bdb845e7b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_RGBQUAD
req.alt-loc: ksmedia.h
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
ms.keywords: tagKS_RGBQUAD, KS_RGBQUAD, *PKS_RGBQUAD
req.iface: 
---

# tagKS_RGBQUAD structure



## -description
<p>The KS_RGBQUAD structure describes a color consisting of relative intensities of red, green, and blue, ranging from 0 to 255 (0x0 to 0xff).</p>


## -syntax

````
typedef struct tagKS_RGBQUAD {
  BYTE rgbBlue;
  BYTE rgbGreen;
  BYTE rgbRed;
  BYTE rgbReserved;
} KS_RGBQUAD, *PKS_RGBQUAD;
````


## -struct-fields
<dl>

### -field <b>rgbBlue</b>

<dd>
<p>Specifies the intensity of blue in the color.</p>
</dd>

### -field <b>rgbGreen</b>

<dd>
<p>Specifies the intensity of green in the color.</p>
</dd>

### -field <b>rgbRed</b>

<dd>
<p>Specifies the intensity of red in the color.</p>
</dd>

### -field <b>rgbReserved</b>

<dd>
<p>Reserved. This member must be zero.</p>
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
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>