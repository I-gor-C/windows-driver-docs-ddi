---
UID: NS.ks.PKSE_PIN
title: PKSE_PIN
author: windows-driver-content
description: .
old-location: stream\kse_pin.htm
old-project: stream
ms.assetid: 6936F732-ECAA-4CA7-B2AF-CA22A5C93FC9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSE_PIN, KSE_PIN, *PKSE_PIN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSE_PIN
req.alt-loc: Ks.h
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

# PKSE_PIN structure



## -description
<p></p>


## -syntax

````
typedef struct {
  ULONG Event;
  ULONG PinId;
  ULONG Reserved;
} KSE_PIN, *PKSE_PIN;
````


## -struct-fields
<dl>

### -field Event

<dd></dd>

### -field PinId

<dd></dd>

### -field Reserved

<dd></dd>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>