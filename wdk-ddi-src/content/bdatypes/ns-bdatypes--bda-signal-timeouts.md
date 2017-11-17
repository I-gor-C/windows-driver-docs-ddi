---
UID: NS.bdatypes._BDA_SIGNAL_TIMEOUTS
title: BDA_SIGNAL_TIMEOUTS
author: windows-driver-content
description: TBD.
old-location: stream\bda_signal_timeouts.htm
ms.assetid: CFEF848D-8268-4FFC-A629-D122021D8411
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
req.alt-api: BDA_SIGNAL_TIMEOUTS
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
ms.keywords: BDA_SIGNAL_TIMEOUTS, BDA_SIGNAL_TIMEOUTS, *PBDA_SIGNAL_TIMEOUTS
req.iface: 
---

# BDA_SIGNAL_TIMEOUTS structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_SIGNAL_TIMEOUTS {
  ULONG ulCarrierTimeoutMs;
  ULONG ulScanningTimeoutMs;
  ULONG ulTuningTimeoutMs;
} BDA_SIGNAL_TIMEOUTS, *PBDA_SIGNAL_TIMEOUTS;
````


## -struct-fields
<dl>

### -field <b>ulCarrierTimeoutMs</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulScanningTimeoutMs</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ulTuningTimeoutMs</b>

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