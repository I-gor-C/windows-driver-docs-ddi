---
UID: NS.mpiowmi._MPIO_TIMERS_COUNTERS
title: MPIO_TIMERS_COUNTERS
author: windows-driver-content
description: The MPIO_TIMERS_COUNTERS structure controls the timer counters that affect all devices whose controlling DSMs do not implement independent timer counter settings.
old-location: storage\mpio_timers_counters.htm
old-project: storage
ms.assetid: edbca8b0-53c1-4538-ac96-52238d75168d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_TIMERS_COUNTERS, MPIO_TIMERS_COUNTERS, *PMPIO_TIMERS_COUNTERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_TIMERS_COUNTERS
req.alt-loc: mpiowmi.h
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

# MPIO_TIMERS_COUNTERS structure



## -description
<p>The MPIO_TIMERS_COUNTERS structure controls the timer counters that affect all devices whose controlling DSMs do not implement independent timer counter settings. To query or set the global counters, the request must be directed to the MPIO control object by using its WMI instance name.</p>


## -syntax

````
typedef struct _MPIO_TIMERS_COUNTERS {
  ULONG PathVerifyEnabled;
  ULONG PathVerificationPeriod;
  ULONG PDORemovePeriod;
  ULONG RetryCount;
  ULONG RetryInterval;
} MPIO_TIMERS_COUNTERS, *PMPIO_TIMERS_COUNTERS;
````


## -struct-fields
<dl>

### -field <b>PathVerifyEnabled</b>

<dd>
<p>An unsigned 32-bitfield that is used as a flag. This field indicates whether path verification must be performed by MPIO on all paths periodically.</p>
</dd>

### -field <b>PathVerificationPeriod</b>

<dd>
<p>An unsigned 32-bitfield that is used to indicate the periodicity (in seconds) with which MPIO has been requested to perform path verification. This field is valid if <i>PathVerifyEnabled</i> is <b>TRUE</b>.</p>
</dd>

### -field <b>PDORemovePeriod</b>

<dd>
<p>An unsigned 32-bitfield that controls the amount of time (in seconds) that the pseudo-LUN remains in system memory, even after losing all its path information.</p>
</dd>

### -field <b>RetryCount</b>

<dd>
<p>An unsigned 32-bitfield that specifies the number of times a failed I/O can be retried.</p>
</dd>

### -field <b>RetryInterval</b>

<dd>
<p>An unsigned 32-bitfield that specifies the interval of time (in seconds) after which a failed request is retried.</p>
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
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>