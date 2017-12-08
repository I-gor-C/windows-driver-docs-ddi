---
UID: NE.ksmedia.KS_AMVP_MODE
title: KS_AMVP_MODE
author: windows-driver-content
description: The KS_AMVP_MODE enumeration defines video port display modes.
old-location: stream\ks_amvp_mode.htm
old-project: stream
ms.assetid: 9464a17a-fa09-46c5-a4a7-d5cbd58deebd
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
req.alt-api: KS_AMVP_MODE
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

# KS_AMVP_MODE enumeration



## -description
<p>The KS_AMVP_MODE enumeration defines video port display modes.</p>


## -syntax

````
typedef enum  { 
  KS_AMVP_MODE_WEAVE              = 0,
  KS_AMVP_MODE_BOBINTERLEAVED     = 1,
  KS_AMVP_MODE_BOBNONINTERLEAVED  = 2,
  KS_AMVP_MODE_SKIPEVEN           = 3,
  KS_AMVP_MODE_SKIPODD            = 4
} KS_AMVP_MODE;
````


## -enum-fields
<dl>

### -field KS_AMVP_MODE_WEAVE

<dd>
<p>Specifies the weave method to display interlaced video. In the weave mode, alternating fields are combined to form a single frame.</p>
</dd>

### -field KS_AMVP_MODE_BOBINTERLEAVED

<dd>
<p>Specifies the interleaved bob method to display video. In the interleaved bob mode, each field is displayed individually, and the gaps between fields are filled with interpolated values.</p>
</dd>

### -field KS_AMVP_MODE_BOBNONINTERLEAVED

<dd>
<p>Specifies the non-interleaved bob method to display video.</p>
</dd>

### -field KS_AMVP_MODE_SKIPEVEN

<dd>
<p>Specifies that even video fields should be skipped when displaying video.</p>
</dd>

### -field KS_AMVP_MODE_SKIPODD

<dd>
<p>Specifies that odd video fields should be skipped when displaying video.</p>
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