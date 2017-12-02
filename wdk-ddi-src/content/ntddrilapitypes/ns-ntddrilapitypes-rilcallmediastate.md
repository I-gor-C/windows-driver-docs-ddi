---
UID: NS.ntddrilapitypes.RILCALLMEDIASTATE
title: RILCALLMEDIASTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediastate.htm
old-project: netvista
ms.assetid: 1fe4b90e-f89a-4ccc-bc92-b6f2edfb0b98
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILCALLMEDIASTATE, RILCALLMEDIASTATE, *LPRILCALLMEDIASTATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLMEDIASTATE
req.alt-loc: ntddrilapitypes.h
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

# RILCALLMEDIASTATE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILCALLMEDIASTATE {
  RILCALLMEDIADIRECTION    dwDirection;
  RILCALLMEDIATYPE         dwCallMediaType;
  NULL                     RILCALLMEDIASTATEUNION;
  RILCALLMEDIASTATEUNION   mediaStateUnion;
  RILCALLAUDIOMEDIASTATE   stAudioState;
  RILCALLVIDEOMEDIASTATE   stVideoState;
  RILCALLCUSTOMMEDIASTATE  dwCustomStateSpecific;
  DWORD [16]               pad;
} RILCALLMEDIASTATE, RILCALLMEDIASTATE;
````


## -struct-fields
<dl>

### -field dwDirection

<dd></dd>

### -field dwCallMediaType

<dd></dd>

### -field RILCALLMEDIASTATEUNION

<dd></dd>

### -field mediaStateUnion

<dd></dd>

### -field stAudioState

<dd></dd>

### -field stVideoState

<dd></dd>

### -field dwCustomStateSpecific

<dd></dd>

### -field pad

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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>