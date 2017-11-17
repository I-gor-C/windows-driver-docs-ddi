---
UID: NS.ksi.PKSIDEFAULTCLOCK
title: PKSIDEFAULTCLOCK
author: windows-driver-content
description: TBD.
old-location: stream\ksidefaultclock.htm
ms.assetid: 08509C28-DDD4-4060-A16A-857A6BF6F6E1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSIDEFAULTCLOCK
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
req.irql: 
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
req.iface: 
---

# PKSIDEFAULTCLOCK structure



## -description
<p>TBD</p>


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

### -field <b>Frequency</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>LastDueTime</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>RunningTimeDelta</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>LastRunningTime</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>TimeAccessLock</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>EventQueue</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>EventQueueLock</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>QueueTimer</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>QueueDpc</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ReferenceCount</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>State</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>SuspendDelta</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>SuspendTime</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>SetTimer</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>CancelTimer</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>CorrelatedTime</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Context</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>Resolution</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>FreeEvent</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ExternalTimeReferenceCount</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>ExternalTimeValid</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>LastStreamTime</b>

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
<dt>Ksi.h</dt>
</dl>
</td>
</tr>
</table>