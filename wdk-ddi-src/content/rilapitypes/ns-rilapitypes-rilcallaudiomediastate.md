---
UID: NS.rilapitypes.RILCALLAUDIOMEDIASTATE
title: RILCALLAUDIOMEDIASTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallaudiomediastate_2.htm
old-project: netvista
ms.assetid: f15f609d-605b-4f4c-8f57-01c6b426d8b5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILCALLAUDIOMEDIASTATE, RILCALLAUDIOMEDIASTATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLAUDIOMEDIASTATE
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILCALLAUDIOMEDIASTATE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILCALLAUDIOMEDIASTATE {
  DWORD                dwParams;
  RILCALLAUDIOSOURCE   dwAudioSource;
  RILCALLAUDIOQUALITY  dwAudioQuality;
  DWORD                dwFlags;
} RILCALLAUDIOMEDIASTATE, RILCALLAUDIOMEDIASTATE;
````


## -struct-fields
<dl>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwAudioSource</b>

<dd></dd>

### -field <b>dwAudioQuality</b>

<dd></dd>

### -field <b>dwFlags</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>