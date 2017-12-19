---
UID: NF.ntddk.IoClearActivityIdThread
title: IoClearActivityIdThread function
author: windows-driver-content
description: The IoClearActivityIdThread routine clears the activity ID of the current thread.
old-location: kernel\ioclearactivityidthread.htm
old-project: kernel
ms.assetid: 2F69FC2F-C336-4B51-8EFC-0A9AA22121B9
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
---

# IoClearActivityIdThread function



## -description
The IoClearActivityIdThread routine clears the activity ID of the current thread.



## -syntax

````
void IoClearActivityIdThread(
  _In_ LPCGUID OriginalId
);
````


## -parameters

### -param OriginalId [in]

The activity ID that was previously set on the thread.


## -returns
None.


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
Version

</th>
<td width="70%">
Available starting with  Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>