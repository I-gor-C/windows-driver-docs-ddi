---
UID: NE.ks.KSEVENTS_LOCKTYPE
title: KSEVENTS_LOCKTYPE
author: windows-driver-content
description: The KSEVENTS_LOCKTYPE enumeration identifies the type of exclusion lock. The types are used with EventFlags in several event-set helper functions.
old-location: stream\ksevents_locktype.htm
old-project: stream
ms.assetid: 775d08ad-40c2-44b7-af02-6c182301e46f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENTS_LOCKTYPE
req.alt-loc: ks.h
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

# KSEVENTS_LOCKTYPE enumeration



## -description
<p>The KSEVENTS_LOCKTYPE enumeration identifies the type of exclusion lock. The types are used with <i>EventFlags</i> in several event-set helper functions.</p>


## -syntax

````
typedef enum  { 
  KSEVENTS_NONE          = 0,
  KSEVENTS_SPINLOCK      = 1,
  KSEVENTS_MUTEX         = 2,
  KSEVENTS_FMUTEX        = 3,
  KSEVENTS_FMUTEXUNSAFE  = 4,
  KSEVENTS_INTERRUPT     = 5,
  KSEVENTS_ERESOURCE     = 6
} KSEVENTS_LOCKTYPE;
````


## -enum-fields
<dl>

### -field KSEVENTS_NONE

<dd>
<p>No lock.</p>
</dd>

### -field KSEVENTS_SPINLOCK

<dd>
<p>Lock is assumed to be a KSPIN_LOCK.</p>
</dd>

### -field KSEVENTS_MUTEX

<dd>
<p>Lock is assumed to be a KMUTEX.</p>
</dd>

### -field KSEVENTS_FMUTEX

<dd>
<p>Lock is assumed to be a FAST_MUTEX and is acquired by raising IRQL to APC_LEVEL.</p>
</dd>

### -field KSEVENTS_FMUTEXUNSAFE

<dd>
<p>Lock is assumed to be a FAST_MUTEX and is acquired without raising IRQL to APC_LEVEL.</p>
</dd>

### -field KSEVENTS_INTERRUPT

<dd>
<p>Lock is assumed to be an interrupt synchronization spin lock.</p>
</dd>

### -field KSEVENTS_ERESOURCE

<dd>
<p>Lock is assumed to be an ERESOURCE.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>