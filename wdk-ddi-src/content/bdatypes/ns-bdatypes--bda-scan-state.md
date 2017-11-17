---
UID: NS.bdatypes._BDA_SCAN_STATE
title: BDA_SCAN_STATE
author: windows-driver-content
description: TBD.
old-location: stream\bda_scan_state.htm
ms.assetid: C80506D2-AAB6-4A37-A62F-CDDD3DCBC7F1
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
req.alt-api: BDA_SCAN_STATE
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
ms.keywords: BDA_SCAN_STATE, BDA_SCAN_STATE, *PBDA_SCAN_STATE
req.iface: 
---

# BDA_SCAN_STATE structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_SCAN_STATE {
  PBDARESULT lResult;
  ULONG      ulSignalLock;
  ULONG      ulSecondsLeft;
  ULONG      ulCurrentFrequency;
} BDA_SCAN_STATE, *PBDA_SCAN_STATE;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulSignalLock</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulSecondsLeft</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulCurrentFrequency</b>

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