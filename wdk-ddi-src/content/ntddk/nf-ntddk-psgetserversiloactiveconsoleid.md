---
UID: NF.ntddk.PsGetServerSiloActiveConsoleId
title: PsGetServerSiloActiveConsoleId
author: windows-driver-content
description: Gets the active console for the current server silo context for the supplied thread.
old-location: kernel\psgetserversiloactiveconsoleid.htm
old-project: kernel
ms.assetid: 66b3c35d-681c-464a-86fa-972825bf3e97
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsGetServerSiloActiveConsoleId
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsGetServerSiloActiveConsoleId
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PsGetServerSiloActiveConsoleId function



## -description
<p>Gets the active console for the current server silo context
    for the supplied thread.
			
            </p>


## -syntax

````
ULONG  PsGetServerSiloActiveConsoleId(
   PESILO Silo
);
````


## -parameters
<dl>

### -param Silo 

<dd>
<p>A pointer to the silo of the job. </p>
</dd>
</dl>

## -returns
<p>Returns the session id for the active console session.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<dt>NtosKrnl.exe (kernel mode)</dt>
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