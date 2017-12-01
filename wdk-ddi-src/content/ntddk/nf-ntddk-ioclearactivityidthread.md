---
UID: NF.ntddk.IoClearActivityIdThread
title: IoClearActivityIdThread
author: windows-driver-content
description: The IoClearActivityIdThread routine clears the activity ID of the current thread.
old-location: kernel\ioclearactivityidthread.htm
old-project: kernel
ms.assetid: 2F69FC2F-C336-4B51-8EFC-0A9AA22121B9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoClearActivityIdThread
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoClearActivityIdThread
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
req.iface: 
---

# IoClearActivityIdThread function



## -description
<p>The IoClearActivityIdThread routine clears the activity ID of the current thread.</p>


## -syntax

````
void IoClearActivityIdThread(
  _In_ LPCGUID OriginalId
);
````


## -parameters
<dl>

### -param <i>OriginalId</i> [in]

<dd>
<p>The activity ID that was previously set on the thread.</p>
</dd>
</dl>

## -returns
<p>None.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>