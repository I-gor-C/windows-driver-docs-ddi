---
UID: NF:ks.KsCreateClock
title: KsCreateClock function
author: windows-driver-content
description: The KsCreateClock function creates a handle to a clock instance.
old-location: stream\kscreateclock.htm
old-project: stream
ms.assetid: a125161d-c086-45a4-9b66-4c13d9ed5f11
ms.author: windowsdriverdev
ms.date: 1/9/2018
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
req.typenames: 
---

# KsCreateClock function



## -description
The <b>KsCreateClock</b> function creates a handle to a clock instance. 



## -syntax

````
NTSTATUS KsCreateClock(
  _In_  HANDLE          ConnectionHandle,
  _In_  PKSCLOCK_CREATE ClockCreate,
  _Out_ PHANDLE         ClockHandle
);
````


## -parameters

### -param ConnectionHandle [in]

Specifies the handle to the connection on which to create the clock.


### -param ClockCreate [in]

Specifies clock create parameters. This currently consists of a flag that must be set to zero.


### -param ClockHandle [out]

Specifies the new clock handle.


## -returns
The <b>KsCreateClock</b> function returns STATUS_SUCCESS if successful, or it returns an error on clock creation failure.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>