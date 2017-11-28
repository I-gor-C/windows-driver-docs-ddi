---
UID: NS.bdatypes._BDA_ISDBCAS_REQUESTHEADER
title: BDA_ISDBCAS_REQUESTHEADER
author: windows-driver-content
description: .
old-location: stream\bda_isdbcas_requestheader.htm
old-project: stream
ms.assetid: E83111C1-5A46-4AB4-B54C-F8330943070D
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BDA_ISDBCAS_REQUESTHEADER, BDA_ISDBCAS_REQUESTHEADER, *PBDA_ISDBCAS_REQUESTHEADER
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
req.alt-api: BDA_ISDBCAS_REQUESTHEADER
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

# BDA_ISDBCAS_REQUESTHEADER structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_ISDBCAS_REQUESTHEADER {
  BYTE  bInstruction;
  BYTE  bReserved[3];
  ULONG ulDataLength;
  BYTE  argbIsdbCommand[MIN_DIMENSION];
} BDA_ISDBCAS_REQUESTHEADER, *PBDA_ISDBCAS_REQUESTHEADER;
````


## -struct-fields
<dl>

### -field <b>bInstruction</b>

<dd>
<p>EMD/EMG</p>
</dd>

### -field <b>bReserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>ulDataLength</b>

<dd>
<p>Specifies the size in bytes of the <b>argbIsdbCommand</b> member.</p>
</dd>

### -field <b>argbIsdbCommand</b>

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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>