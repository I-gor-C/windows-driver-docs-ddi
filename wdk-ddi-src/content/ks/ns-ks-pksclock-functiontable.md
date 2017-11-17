---
UID: NS.ks.PKSCLOCK_FUNCTIONTABLE
title: PKSCLOCK_FUNCTIONTABLE
author: windows-driver-content
description: The KSCLOCK_FUNCTIONTABLE structure describes a function table for the master clock.
old-location: stream\ksclock_functiontable.htm
ms.assetid: ed16588e-1c63-411d-b5c8-a8151a218328
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCLOCK_FUNCTIONTABLE
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
ms.keywords: PKSCLOCK_FUNCTIONTABLE, KSCLOCK_FUNCTIONTABLE, *PKSCLOCK_FUNCTIONTABLE
req.iface: 
---

# PKSCLOCK_FUNCTIONTABLE structure



## -description
<p>The KSCLOCK_FUNCTIONTABLE structure describes a function table for the master clock.</p>


## -syntax

````
typedef struct {
  PFNKSCLOCK_GETTIME        GetTime;
  PFNKSCLOCK_GETTIME        GetPhysicalTime;
  PFNKSCLOCK_CORRELATEDTIME GetCorrelatedTime;
  PFNKSCLOCK_CORRELATEDTIME GetCorrelatedPhysicalTime;
} KSCLOCK_FUNCTIONTABLE, *PKSCLOCK_FUNCTIONTABLE;
````


## -struct-fields
<dl>

### -field <b>GetTime</b>

<dd>
<p>Pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff567161">KStrClockGetTime</a> routine.</p>
</dd>

### -field <b>GetPhysicalTime</b>

<dd>
<p>Pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff567160">KStrClockGetPhysicalTime</a> routine.</p>
</dd>

### -field <b>GetCorrelatedTime</b>

<dd>
<p>Pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff567159">KStrClockGetCorrelatedTime</a> routine.</p>
</dd>

### -field <b>GetCorrelatedPhysicalTime</b>

<dd>
<p>Pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff567157">KStrClockGetCorrelatedPhysicalTime</a> routine. </p>
</dd>
</dl>

## -remarks
<p>Supply this structure in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564466">KSPROPERTY_CLOCK_FUNCTIONTABLE</a> request. The property request then returns pointers to the requested routines.</p>

<p>The function pointers returned in this structure are valid until the clock's file object is released.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564466">KSPROPERTY_CLOCK_FUNCTIONTABLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSCLOCK_FUNCTIONTABLE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
