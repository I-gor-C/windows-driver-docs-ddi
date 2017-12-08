---
UID: NC.ntddk.SILO_MONITOR_TERMINATE_CALLBACK
title: SILO_MONITOR_TERMINATE_CALLBACK
author: windows-driver-content
description: This callback is invoked when a silo is terminated.
old-location: kernel\silo_monitor_terminate_callback.htm
old-project: kernel
ms.assetid: 1F87D6AC-3603-4A34-BAAB-8B43ADF9E595
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: TerminateCallback
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

# SILO_MONITOR_TERMINATE_CALLBACK callback



## -description
<p>This callback is invoked when a silo is terminated.</p>


## -prototype

````
SILO_MONITOR_TERMINATE_CALLBACK TerminateCallback;

void TerminateCallback(
  _In_ PESILO Silo
)
{ ... }
````


## -parameters
<dl>

### -param Silo [in]

<dd>
<p>The silo to be terminated.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The expected behavior is that the component will drop any outstanding silo references.  A driver may no longer operate within the namespace of a silo (via <a href="..\ntddk\nf-ntddk-psattachsilotocurrentthread.md">PsAttachSiloToCurrentThread</a>) once it has returned from this function. </p>

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