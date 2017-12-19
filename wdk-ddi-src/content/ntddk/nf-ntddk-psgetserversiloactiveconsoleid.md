---
UID: NF.ntddk.PsGetServerSiloActiveConsoleId
title: PsGetServerSiloActiveConsoleId function
author: windows-driver-content
description: Gets the active console for the current server silo context for the supplied thread.
old-location: kernel\psgetserversiloactiveconsoleid.htm
old-project: kernel
ms.assetid: 66b3c35d-681c-464a-86fa-972825bf3e97
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
---

# PsGetServerSiloActiveConsoleId function



## -description
Gets the active console for the current server silo context
    for the supplied thread.
			
            



## -syntax

````
ULONG  PsGetServerSiloActiveConsoleId(
   PESILO Silo
);
````


## -parameters

### -param Silo 

A pointer to the silo of the job. 


## -returns
Returns the session id for the active console session.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10, version 1709

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe (kernel mode)</dt>
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