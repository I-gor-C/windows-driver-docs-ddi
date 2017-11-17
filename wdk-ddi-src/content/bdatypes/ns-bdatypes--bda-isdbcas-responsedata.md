---
UID: NS.bdatypes._BDA_ISDBCAS_RESPONSEDATA
title: BDA_ISDBCAS_RESPONSEDATA
author: windows-driver-content
description: TBD.
old-location: stream\bda_isdbcas_responsedata.htm
ms.assetid: 70BD9007-6CA4-49EC-8A30-3544FE62C18E
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
req.alt-api: BDA_ISDBCAS_RESPONSEDATA
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
ms.keywords: BDA_ISDBCAS_RESPONSEDATA, BDA_ISDBCAS_RESPONSEDATA, *PBDA_ISDBCAS_RESPONSEDATA
req.iface: 
---

# BDA_ISDBCAS_RESPONSEDATA structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_ISDBCAS_RESPONSEDATA {
  PBDARESULT lResult;
  ULONG      ulRequestID;
  ULONG      ulIsdbStatus;
  ULONG      ulIsdbDataSize;
  BYTE       argbIsdbCommandData[MIN_DIMENSION];
} BDA_ISDBCAS_RESPONSEDATA, *PBDA_ISDBCAS_RESPONSEDATA;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulRequestID</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulIsdbStatus</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulIsdbDataSize</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>argbIsdbCommandData</b>

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