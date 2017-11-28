---
UID: NS.bdatypes._BDA_CAS_CLOSE_MMIDIALOG
title: BDA_CAS_CLOSE_MMIDIALOG
author: windows-driver-content
description: .
old-location: stream\bda_cas_close_mmidialog.htm
old-project: stream
ms.assetid: 430580CF-F2FB-4684-B681-361E74D8EABD
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BDA_CAS_CLOSE_MMIDIALOG, BDA_CAS_CLOSE_MMIDIALOG, *PBDA_CAS_CLOSE_MMIDIALOG
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
req.alt-api: BDA_CAS_CLOSE_MMIDIALOG
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

# BDA_CAS_CLOSE_MMIDIALOG structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_CAS_CLOSE_MMIDIALOG {
  PBDARESULT lResult;
  ULONG      ulDescrambleStatus;
} BDA_CAS_CLOSE_MMIDIALOG, *PBDA_CAS_CLOSE_MMIDIALOG;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd></dd>

### -field <b>ulDescrambleStatus</b>

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