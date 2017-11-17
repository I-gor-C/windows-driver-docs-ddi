---
UID: NS.bdatypes._BDA_CAS_OPENMMIDATA
title: BDA_CAS_OPENMMIDATA
author: windows-driver-content
description: TBD.
old-location: stream\bda_cas_openmmidata.htm
ms.assetid: FAF30768-5DE4-4284-8CB5-2E518A2E37E7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_CAS_OPENMMIDATA
req.alt-loc: 
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
ms.keywords: BDA_CAS_OPENMMIDATA, BDA_CAS_OPENMMIDATA, *PBDA_CAS_OPENMMIDATA
req.iface: 
---

# BDA_CAS_OPENMMIDATA structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_CAS_OPENMMIDATA {
  ULONG  ulDialogNumber;
  ULONG  ulDialogRequest;
  GUID   uuidDialogType;
  USHORT usDialogDataLength;
  BYTE   argbDialogData[MIN_DIMENSION];
} BDA_CAS_OPENMMIDATA, *PBDA_CAS_OPENMMIDATA;
````


## -struct-fields
<dl>

### -field <b>ulDialogNumber</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulDialogRequest</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>uuidDialogType</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>usDialogDataLength</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>argbDialogData</b>

<dd>
<p>TBD</p>
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