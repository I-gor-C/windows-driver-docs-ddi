---
UID: NF.ntddk.PsGetSiloMonitorContextSlot
title: PsGetSiloMonitorContextSlot
author: windows-driver-content
description: This routine returns the silo context slot that was allocated by the monitor during the registration.
old-location: kernel\psgetsilomonitorcontextslot.htm
ms.assetid: 0871EA8C-4F59-451E-89FB-8A0D44219456
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
req.alt-api: PsGetSiloMonitorContextSlot
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
ms.keywords: PsGetSiloMonitorContextSlot
req.iface: 
---

# PsGetSiloMonitorContextSlot function



## -description
<p>This routine returns the silo context slot that was allocated by the monitor during the registration.</p>


## -syntax

````
ULONG PsGetSiloMonitorContextSlot(
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
<p>A valid silo context slot.</p>

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