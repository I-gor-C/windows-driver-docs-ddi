---
UID: NS.bdatypes._BDA_RATING_PINRESET
title: BDA_RATING_PINRESET
author: windows-driver-content
description: .
old-location: stream\bda_rating_pinreset.htm
old-project: stream
ms.assetid: 237463EC-3C57-4DCA-9757-870B5F55C584
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_RATING_PINRESET, BDA_RATING_PINRESET, *PBDA_RATING_PINRESET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_RATING_PINRESET
req.alt-loc: Bdatypes.h
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

# BDA_RATING_PINRESET structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_RATING_PINRESET {
  BYTE bPinLength;
  BYTE argbNewPin[MIN_DIMENSION];
} BDA_RATING_PINRESET, *PBDA_RATING_PINRESET;
````


## -struct-fields
<dl>

### -field <b>bPinLength</b>

<dd>
<p>Specifies the buffer size including a null termination.</p>
</dd>

### -field <b>argbNewPin</b>

<dd>
<p>Specifies null-terminated UTF8. Use an empty string if the pin is disabled.</p>
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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>