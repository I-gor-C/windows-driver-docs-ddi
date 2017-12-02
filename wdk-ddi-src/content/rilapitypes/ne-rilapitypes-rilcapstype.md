---
UID: NE.rilapitypes.RILCAPSTYPE
title: RILCAPSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcapstype_2.htm
old-project: netvista
ms.assetid: 492436da-9d6f-462b-9c4d-4466cb2f78f6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCAPSTYPE
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

# RILCAPSTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>