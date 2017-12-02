---
UID: NS.ksi.PKSIDEFAULTCLOCK
title: PKSIDEFAULTCLOCK
author: windows-driver-content
description: .
old-location: stream\ksidefaultclock.htm
old-project: stream
ms.assetid: 08509C28-DDD4-4060-A16A-857A6BF6F6E1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSIDEFAULTCLOCK
req.alt-loc: Ksi.h
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

# PKSIDEFAULTCLOCK structure



## -description
<p></p>


## -syntax

````
typedef struct {
  LONGLONG                  Frequency;
  LONGLONG                  LastDueTime;
  LONGLONG                  RunningTimeDelta;
  LONGLONG                  LastRunningTime;
  KSPIN_LOCK                TimeAccessLock;
  LIST_ENTRY                EventQueue;
  KSPIN_LOCK                EventQueueLock;
  KTIMER                    QueueTimer;
  KDPC                      QueueDpc;
  LONG                      ReferenceCount;
  KSSTATE                   State;
  LONGLONG                  SuspendDelta;
  LONGLONG                  SuspendTime;
  PFNKSSETTIMER             SetTimer;
  PFNKSCANCELTIMER          CancelTimer;
  PFNKSCLOCK_CORRELATEDTIME CorrelatedTime;
  PVOID                     Context;
  KSRESOLUTION              Resolution;
  KEVENT                    FreeEvent;
  LONG                      ExternalTimeReferenceCount;
  BOOLEAN                   ExternalTimeValid;
  LONGLONG                  LastStreamTime;
} KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK;
````


## -struct-fields
<dl>

### -field Frequency

<dd></dd>

### -field LastDueTime

<dd></dd>

### -field RunningTimeDelta

<dd></dd>

### -field LastRunningTime

<dd></dd>

### -field TimeAccessLock

<dd></dd>

### -field EventQueue

<dd></dd>

### -field EventQueueLock

<dd></dd>

### -field QueueTimer

<dd></dd>

### -field QueueDpc

<dd></dd>

### -field ReferenceCount

<dd></dd>

### -field State

<dd></dd>

### -field SuspendDelta

<dd></dd>

### -field SuspendTime

<dd></dd>

### -field SetTimer

<dd></dd>

### -field CancelTimer

<dd></dd>

### -field CorrelatedTime

<dd></dd>

### -field Context

<dd></dd>

### -field Resolution

<dd></dd>

### -field FreeEvent

<dd></dd>

### -field ExternalTimeReferenceCount

<dd></dd>

### -field ExternalTimeValid

<dd></dd>

### -field LastStreamTime

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
<dt>Ksi.h</dt>
</dl>
</td>
</tr>
</table>