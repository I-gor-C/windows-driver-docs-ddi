---
UID: NS.bdatypes._BDA_SCAN_START
title: BDA_SCAN_START
author: windows-driver-content
description: TBD.
old-location: stream\bda_scan_start.htm
ms.assetid: 931CC532-BC46-4B64-B6BA-29D20827EC0A
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
req.alt-api: BDA_SCAN_START
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
ms.keywords: BDA_SCAN_START, BDA_SCAN_START, *PBDA_SCAN_START
req.iface: 
---

# BDA_SCAN_START structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_SCAN_START {
  PBDARESULT lResult;
  ULONG      LowerFrequency;
  ULONG      HigerFrequency;
} BDA_SCAN_START, *PBDA_SCAN_START;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>LowerFrequency</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>HigerFrequency</b>

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