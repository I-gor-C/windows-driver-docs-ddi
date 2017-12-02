---
UID: NE.ntddrilapitypes.RILCAPSTYPE
title: RILCAPSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcapstype.htm
old-project: netvista
ms.assetid: 78f372fc-75b2-47e8-ac3f-818b384c6d97
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCAPSTYPE
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

# RILCAPSTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCAPSTYPE { 
  RIL_CAPSTYPE_PERSOLOCKPWDLENGTH,
  RIL_CAPSTYPE_PBMAXREAD,
  RIL_CAPSTYPE_PBSTORELOCATIONS,
  RIL_CAPSTYPE_RADIOCONFIGURATIONS,
  RIL_CAPSTYPE_SIGNALQUALITYIMPLEMENTATION,
  RIL_CAPSTYPE_NITZNOTIFICATION,
  RIL_CAPSTYPE_CALLSUPPORT,
  RIL_CAPSTYPE_SMSSUPPORT,
  RIL_CAPSTYPE_ARG_SMALLEST,
  RIL_CAPSTYPE_ARG_LARGEST,
  RIL_CAPSTYPE_MAX
} RILCAPSTYPE;
````


## -enum-fields
<dl>

### -field RIL_CAPSTYPE_PERSOLOCKPWDLENGTH

<dd></dd>

### -field RIL_CAPSTYPE_PBMAXREAD

<dd></dd>

### -field RIL_CAPSTYPE_PBSTORELOCATIONS

<dd></dd>

### -field RIL_CAPSTYPE_RADIOCONFIGURATIONS

<dd></dd>

### -field RIL_CAPSTYPE_SIGNALQUALITYIMPLEMENTATION

<dd></dd>

### -field RIL_CAPSTYPE_NITZNOTIFICATION

<dd></dd>

### -field RIL_CAPSTYPE_CALLSUPPORT

<dd></dd>

### -field RIL_CAPSTYPE_SMSSUPPORT

<dd></dd>

### -field RIL_CAPSTYPE_ARG_SMALLEST

<dd></dd>

### -field RIL_CAPSTYPE_ARG_LARGEST

<dd></dd>

### -field RIL_CAPSTYPE_MAX

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