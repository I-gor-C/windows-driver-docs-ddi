---
UID: NS.mpiowmi._DSM_COUNTERS
title: DSM_COUNTERS
author: windows-driver-content
description: The DSM_COUNTERS structure holds the various timer counters that are applicable to all LUNs that are controlled by the DSM.
old-location: storage\dsm_counters.htm
ms.assetid: 3202aec4-d95e-4162-86a1-17595ed2a5b5
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DSM_COUNTERS
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
ms.keywords: DSM_COUNTERS, DSM_COUNTERS, *PDSM_COUNTERS
req.iface: 
---

# DSM_COUNTERS structure



## -description
<p>The DSM_COUNTERS structure holds the various timer counters that are applicable to all LUNs that are controlled by the DSM.</p>


## -syntax

````
typedef struct _DSM_COUNTERS {
  ULONG     PathVerifyEnabled;
  ULONG     PathVerificationPeriod;
  ULONG     PDORemovePeriod;
  ULONG     RetryCount;
  ULONG     RetryInterval;
  ULONG     Reserved32;
  ULONGLONG Reserved64;
} DSM_COUNTERS, *PDSM_COUNTERS;
````


## -struct-fields
<dl>

### -field <b>PathVerifyEnabled</b>

<dd>
<p>An unsigned 32-bitfield that is used as a flag. This field indicates if path verification must be performed by MPIO periodically on all paths that expose devices that are controlled by this particular DSM.</p>
</dd>

### -field <b>PathVerificationPeriod</b>

<dd>
<p>An unsigned 32-bitfield that is used to indicate the periodicity (in seconds) with which MPIO has been requested to perform path verification. This field is only honored if <i>PathVerifyEnabled</i> is <b>TRUE</b>.</p>
</dd>

### -field <b>PDORemovePeriod</b>

<dd>
<p>An unsigned 32-bitfield that controls the amount of time (in seconds) that the pseudo-LUN will continue to remain in system memory, even after losing all its path information.</p>
</dd>

### -field <b>RetryCount</b>

<dd>
<p>An unsigned 32-bitfield that specifies the number of times a failed I/O will be retried.</p>
</dd>

### -field <b>RetryInterval</b>

<dd>
<p>An unsigned 32-bitfield that specifies the interval of time (in seconds) after which a failed request is retried.</p>
</dd>

### -field <b>Reserved32</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>Reserved64</b>

<dd>
<p>Should be zero.</p>
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