---
UID: NS.rilapitypes.RILCALLMEDIASTATE~r1
title: RILCALLMEDIASTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediastate_2.htm
old-project: netvista
ms.assetid: d3b89502-667c-45dd-af1c-05b7c8613d6c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILCALLMEDIASTATE,
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
req.alt-api: RILCALLMEDIASTATE
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

# RILCALLMEDIASTATE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILCALLMEDIASTATE {
  RILCALLMEDIADIRECTION    dwDirection;
  RILCALLMEDIATYPE         dwCallMediaType;
  NULL                     RILCALLMEDIASTATEUNION;
  RILCALLMEDIASTATEUNION   mediaStateUnion;
  NULL                     switch_is;
  NULL                     dwCallMediaType;
  RILCALLAUDIOMEDIASTATE   stAudioState;
  NULL                     case;
  NULL                     RIL_CALLMEDIATYPE_AUDIO;
  RILCALLVIDEOMEDIASTATE   stVideoState;
  NULL                     case;
  NULL                     RIL_CALLMEDIATYPE_VIDEO;
  RILCALLCUSTOMMEDIASTATE  dwCustomStateSpecific;
  NULL                     case;
  NULL                     RIL_CALLMEDIATYPE_CUSTOM;
  DWORD [16]               pad;
  NULL                     case;
  NULL                     RIL_CALLMEDIATYPE_UNKNOWN;
} RILCALLMEDIASTATE, RILCALLMEDIASTATE;
````


## -struct-fields
<dl>

### -field <b>dwDirection</b>

<dd></dd>

### -field <b>dwCallMediaType</b>

<dd></dd>

### -field <b>RILCALLMEDIASTATEUNION</b>

<dd></dd>

### -field <b>mediaStateUnion</b>

<dd></dd>

### -field <b>switch_is</b>

<dd></dd>

### -field <b>dwCallMediaType</b>

<dd></dd>

### -field <b>stAudioState</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CALLMEDIATYPE_AUDIO</b>

<dd></dd>

### -field <b>stVideoState</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CALLMEDIATYPE_VIDEO</b>

<dd></dd>

### -field <b>dwCustomStateSpecific</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CALLMEDIATYPE_CUSTOM</b>

<dd></dd>

### -field <b>pad</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_CALLMEDIATYPE_UNKNOWN</b>

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