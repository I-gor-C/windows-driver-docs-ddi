---
UID: NC.ntddk.SILO_MONITOR_CREATE_CALLBACK
title: SILO_MONITOR_CREATE_CALLBACK
author: windows-driver-content
description: This is callback is invoked when a new silo is created.
old-location: kernel\silo_monitor_create_callback.htm
old-project: kernel
ms.assetid: C26C5162-4BB0-401E-9AF5-AF1D2D8715F9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CreateCallback
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

# SILO_MONITOR_CREATE_CALLBACK callback



## -description
<p>This is callback is invoked when a new silo is created.</p>


## -prototype

````
SILO_MONITOR_CREATE_CALLBACK CreateCallback;

NTSTATUS CreateCallback(
  _In_ PESILO Silo
)
{ ... }
````


## -parameters
<dl>

### -param <i>Silo</i> [in]

<dd>
<p>The silo that was created.</p>
</dd>
</dl>

## -returns
<p>The NT code returned by the operation.</p>

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