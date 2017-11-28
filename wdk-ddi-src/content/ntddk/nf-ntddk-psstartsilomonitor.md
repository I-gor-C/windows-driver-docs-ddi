---
UID: NF.ntddk.PsStartSiloMonitor
title: PsStartSiloMonitor
author: windows-driver-content
description: This routine tries to start the server silo monitor.
old-location: kernel\psstartsilomonitor.htm
old-project: kernel
ms.assetid: 65828926-FDA7-4F65-AD55-B7E03639FA27
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PsStartSiloMonitor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsStartSiloMonitor
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
req.iface: 
---

# PsStartSiloMonitor function



## -description
<p>This routine tries to start the server silo monitor.</p>


## -syntax

````
NTSTATUS PsStartSiloMonitor(
  _In_ PSILO_MONITOR Monitor
);
````


## -parameters
<dl>

### -param <i>Monitor</i> [in]

<dd>
<p>A pointer to the silo monitor.</p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_REQUEST_ABORTED</b></dt>
</dl><p>The monitor was not able to start.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The monitor does not allow existing silos and one was found in the system.</p><dl>
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