---
UID : NE:ks.KSEVENTS_LOCKTYPE
title : KSEVENTS_LOCKTYPE
author : windows-driver-content
description : The KSEVENTS_LOCKTYPE enumeration identifies the type of exclusion lock. The types are used with EventFlags in several event-set helper functions.
old-location : stream\ksevents_locktype.htm
old-project : stream
ms.assetid : 775d08ad-40c2-44b7-af02-6c182301e46f
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSEVENTS_NONE, KSEVENTS_SPINLOCK, KSEVENTS_INTERRUPT, ks/KSEVENTS_ERESOURCE, ks/KSEVENTS_FMUTEXUNSAFE, ks/KSEVENTS_INTERRUPT, KSEVENTS_LOCKTYPE, KSEVENTS_ERESOURCE, KSEVENTS_MUTEX, ks/KSEVENTS_FMUTEX, ks/KSEVENTS_NONE, ks-struct_293dbf13-1dbe-478e-83fb-d38e17e4a697.xml, ks/KSEVENTS_SPINLOCK, ks/KSEVENTS_LOCKTYPE, KSEVENTS_LOCKTYPE enumeration [Streaming Media Devices], KSEVENTS_FMUTEX, KSEVENTS_FMUTEXUNSAFE, ks/KSEVENTS_MUTEX, stream.ksevents_locktype
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : KSEVENTS_LOCKTYPE
---

# KSEVENTS_LOCKTYPE Enumeration
The KSEVENTS_LOCKTYPE enumeration identifies the type of exclusion lock. The types are used with <i>EventFlags</i> in several event-set helper functions.

## Syntax
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

## Constants

<table>

<tr>
<td>KSEVENTS_ERESOURCE</td>
<td>Lock is assumed to be an ERESOURCE.</td>
</tr>

<tr>
<td>KSEVENTS_FMUTEX</td>
<td>Lock is assumed to be a FAST_MUTEX and is acquired by raising IRQL to APC_LEVEL.</td>
</tr>

<tr>
<td>KSEVENTS_FMUTEXUNSAFE</td>
<td>Lock is assumed to be a FAST_MUTEX and is acquired without raising IRQL to APC_LEVEL.</td>
</tr>

<tr>
<td>KSEVENTS_INTERRUPT</td>
<td>Lock is assumed to be an interrupt synchronization spin lock.</td>
</tr>

<tr>
<td>KSEVENTS_MUTEX</td>
<td>Lock is assumed to be a KMUTEX.</td>
</tr>

<tr>
<td>KSEVENTS_NONE</td>
<td>No lock.</td>
</tr>

<tr>
<td>KSEVENTS_SPINLOCK</td>
<td>Lock is assumed to be a KSPIN_LOCK.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |