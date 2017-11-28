---
UID: NS.bdatypes._BDA_GDDS_DATATYPE
title: BDA_GDDS_DATATYPE
author: windows-driver-content
description: .
old-location: stream\bda_gdds_datatype.htm
old-project: stream
ms.assetid: D2E6A110-EC0F-4753-BAF1-7A9F84ECDD35
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BDA_GDDS_DATATYPE, BDA_GDDS_DATATYPE, *P_BDA_GDDS_DATATYPE
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
req.alt-api: BDA_GDDS_DATATYPE
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

# BDA_GDDS_DATATYPE structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_GDDS_DATATYPE {
  PBDARESULT lResult;
  GUID       uuidDataType;
} BDA_GDDS_DATATYPE, *P_BDA_GDDS_DATATYPE;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd></dd>

### -field <b>uuidDataType</b>

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