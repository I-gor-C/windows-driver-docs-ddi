---
UID: NF.ntddk.PsUnregisterSiloMonitor
title: PsUnregisterSiloMonitor
author: windows-driver-content
description: This routine unregisters a server silo monitor.
old-location: kernel\psunregistersilomonitor.htm
old-project: kernel
ms.assetid: B1B85AD5-F626-4177-8218-428B617A97F6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PsUnregisterSiloMonitor
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
req.alt-api: PsUnregisterSiloMonitor
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

# PsUnregisterSiloMonitor function



## -description
<p>This routine unregisters a server silo monitor.</p>


## -syntax

````
void PsUnregisterSiloMonitor(
  _In_ _Post_invalid_ PSILO_MONITOR Monitor
);
````


## -parameters
<dl>

### -param <i>Monitor</i> [in]

<dd>
<p>The server silo monitor to unregister.</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks
<p>The monitor will not receive further notifications after this routine completes.
    
If the monitor allocated a silo context slot, this routine will not complete until all silo contexts have been removed from slot.</p>

<p>The monitor will not receive further notifications after this routine completes.
    
If the monitor allocated a silo context slot, this routine will not complete until all silo contexts have been removed from slot.</p>

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