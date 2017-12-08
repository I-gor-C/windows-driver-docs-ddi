---
UID: NE.ksmedia.KS_AMPixAspectRatio
title: KS_AMPixAspectRatio
author: windows-driver-content
description: The KS_AMPixAspectRatio enumeration defines the pixel aspect ratio that corresponds to a 720 480 NTSC video signal or a 720 × 576 PAL video signal.
old-location: stream\ks_ampixaspectratio.htm
old-project: stream
ms.assetid: 29c84529-11f6-429b-81c6-96d6a1773b3b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KS_AMPixAspectRatio
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
req.iface: 
---

# KS_AMPixAspectRatio enumeration



## -description
<p>The KS_AMPixAspectRatio enumeration defines the pixel aspect ratio that corresponds to a 720  480 NTSC video signal or a 720 × 576 PAL video signal.</p>


## -syntax

````
typedef enum  { 
  KS_PixAspectRatio_NTSC4x3   = 0,
  KS_PixAspectRatio_NTSC16x9  = 1,
  KS_PixAspectRatio_PAL4x3    = 2,
  KS_PixAspectRatio_PAL16x9   = 3
} KS_AMPixAspectRatio;
````


## -enum-fields
<dl>

### -field KS_PixAspectRatio_NTSC4x3

<dd>
<p>Specifies a 4 × 3 NTSC pixel aspect ratio.</p>
</dd>

### -field KS_PixAspectRatio_NTSC16x9

<dd>
<p>Specifies a 16 × 9 NTSC pixel aspect ratio.</p>
</dd>

### -field KS_PixAspectRatio_PAL4x3

<dd>
<p>Specifies a 4 × 3 PAL pixel aspect ratio.</p>
</dd>

### -field KS_PixAspectRatio_PAL16x9

<dd>
<p>Specifies a 16 × 9 PAL pixel aspect ratio.</p>
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