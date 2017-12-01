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

### -field <b>Frequency</b>

<dd></dd>

### -field <b>LastDueTime</b>

<dd></dd>

### -field <b>RunningTimeDelta</b>

<dd></dd>

### -field <b>LastRunningTime</b>

<dd></dd>

### -field <b>TimeAccessLock</b>

<dd></dd>

### -field <b>EventQueue</b>

<dd></dd>

### -field <b>EventQueueLock</b>

<dd></dd>

### -field <b>QueueTimer</b>

<dd></dd>

### -field <b>QueueDpc</b>

<dd></dd>

### -field <b>ReferenceCount</b>

<dd></dd>

### -field <b>State</b>

<dd></dd>

### -field <b>SuspendDelta</b>

<dd></dd>

### -field <b>SuspendTime</b>

<dd></dd>

### -field <b>SetTimer</b>

<dd></dd>

### -field <b>CancelTimer</b>

<dd></dd>

### -field <b>CorrelatedTime</b>

<dd></dd>

### -field <b>Context</b>

<dd></dd>

### -field <b>Resolution</b>

<dd></dd>

### -field <b>FreeEvent</b>

<dd></dd>

### -field <b>ExternalTimeReferenceCount</b>

<dd></dd>

### -field <b>ExternalTimeValid</b>

<dd></dd>

### -field <b>LastStreamTime</b>

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