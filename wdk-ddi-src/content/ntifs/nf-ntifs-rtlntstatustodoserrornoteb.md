---
UID: NF.ntifs.RtlNtStatusToDosErrorNoTeb
title: RtlNtStatusToDosErrorNoTeb
author: windows-driver-content
description: Reserved for system use.
old-location: ifsk\rtlntstatustodoserrornoteb.htm
old-project: ifsk
ms.assetid: be22fb7f-408a-44ee-ae83-0f1dadcec87f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlNtStatusToDosErrorNoTeb
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: The RtlNtStatusToDosErrorNoTeb routine is available on Microsoft Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlNtStatusToDosError
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
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# RtlNtStatusToDosErrorNoTeb function



## -description
<p>The <b>RtlNtStatusToDosErrorNoTeb</b>  routine converts the specified NTSTATUS code to its equivalent system error code. Reserved for system use.</p>


## -syntax

````
ULONG RtlNtStatusToDosError(
  _In_ NTSTATUS Status
);
````


## -parameters
<dl>

### -param <i>Status</i> [in]

<dd>
<p>The NTSTATUS code to be converted.</p>
</dd>
</dl>

## -returns
<p><b>RtlNtStatusToDosErrorNoTeb</b> returns the corresponding system error code. Error codes are defined in <i>Winerror.h</i>.</p>

## -remarks
<p>There is no function that provides the inverse functionality of <b>RtlNtStatusToDosErrorNoTeb</b>, converting a system error code to its corresponding NTSTATUS code. </p>

<p>There is no function that provides the inverse functionality of <b>RtlNtStatusToDosErrorNoTeb</b>, converting a system error code to its corresponding NTSTATUS code. </p>

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
<p>The RtlNtStatusToDosErrorNoTeb routine is available on Microsoft Windows 2000 and later versions of Windows. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>