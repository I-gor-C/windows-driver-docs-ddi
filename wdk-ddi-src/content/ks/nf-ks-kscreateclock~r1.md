---
UID: NF.ks.KsCreateClock~r1
title: KsCreateClock
author: windows-driver-content
description: The KsCreateClock function creates a handle to a clock instance.
old-location: stream\kscreateclock.htm
old-project: stream
ms.assetid: a125161d-c086-45a4-9b66-4c13d9ed5f11
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsCreateClock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsCreateClock
req.alt-loc: ks.lib,ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsCreateClock function



## -description
<p>The <b>KsCreateClock</b> function creates a handle to a clock instance. </p>


## -syntax

````
NTSTATUS KsCreateClock(
  _In_  HANDLE          ConnectionHandle,
  _In_  PKSCLOCK_CREATE ClockCreate,
  _Out_ PHANDLE         ClockHandle
);
````


## -parameters
<dl>

### -param ConnectionHandle [in]

<dd>
<p>Specifies the handle to the connection on which to create the clock.</p>
</dd>

### -param ClockCreate [in]

<dd>
<p>Specifies clock create parameters. This currently consists of a flag that must be set to zero.</p>
</dd>

### -param ClockHandle [out]

<dd>
<p>Specifies the new clock handle.</p>
</dd>
</dl>

## -returns
<p>The <b>KsCreateClock</b> function returns STATUS_SUCCESS if successful, or it returns an error on clock creation failure.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>