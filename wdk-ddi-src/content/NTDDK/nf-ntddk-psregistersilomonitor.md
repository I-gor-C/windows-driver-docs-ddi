---
UID: NF.ntddk.PsRegisterSiloMonitor
title: PsRegisterSiloMonitor
author: windows-driver-content
description: This routine registers a server silo monitor that can receive notifications about server silo events.
old-location: kernel\psregistersilomonitor.htm
ms.assetid: C04F29FF-972C-44CC-8557-28C23827ADF0
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsRegisterSiloMonitor
req.alt-loc: ntddk.h
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
ms.keywords: PsRegisterSiloMonitor
req.iface: 
---

# PsRegisterSiloMonitor function



## -description
<p>This routine registers a server silo monitor that can receive notifications about server silo events.</p>
<p>
<div class="alert"><b>Note</b>  To start receiving notifications, call the <a href="https://msdn.microsoft.com/library/windows/hardware/mt735082">PsStartSiloMonitor</a> routine.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS PsRegisterSiloMonitor(
  _In_  PSILO_MONITOR_REGISTRATION Registration,
  _Out_ PSILO_MONITOR              *ReturnedMonitor
);
````


## -parameters
<dl>

### -param <i>Registration</i> [in]

<dd>
<p>Specifies the server silo monitor to be registered, of type <a href="https://msdn.microsoft.com/library/windows/hardware/mt735088">SILO_MONITOR_REGISTRATION</a>. </p>
</dd>

### -param <i>ReturnedMonitor</i> [out]

<dd>
<p>Receives a pointer to the monitor. This pointer is used to make further monitor-related calls.</p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The version specified in <b>ntddk.h</b> does not match <b>SILO_MONITOR_REGISTRATION_VERSION</b>, the component name is not specified, or the terminate callback is not supplied.</p><dl>
<dt><b>STATUS_PRIVILEDGE_NOT_HELD</b></dt>
</dl><p>The routine is called in a silo.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There is no memory to register a silo monitor or there is no available silo slot.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1607</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>