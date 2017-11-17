---
UID: NF.ntddk.IoPropagateActivityIdToThread
title: IoPropagateActivityIdToThread
author: windows-driver-content
description: The IoPropagateActivityIdToThread routine associates the activity ID from an IRP with the current thread.
old-location: kernel\iopropagateactivityidtothread.htm
ms.assetid: 8E824793-53DF-4573-81B0-6FE925CCB4C4
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoPropagateActivityIdToThread
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
ms.keywords: IoPropagateActivityIdToThread
req.iface: 
---

# IoPropagateActivityIdToThread function



## -description
<p>The <b>IoPropagateActivityIdToThread</b> routine associates the activity ID from an IRP with the current thread.</p>


## -syntax

````
NTSTATUS IoPropagateActivityIdToThread(
  _In_  PIRP    Irp,
  _Out_ LPGUID  PropagatedId,
  _Out_ LPCGUID *OriginalId
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>The IRP whose ID will be propagated to the thread.</p>
</dd>

### -param <i>PropagatedId</i> [out]

<dd>
<p>A pointer to memory allocated by the caller to store the ID in the thread.</p>
</dd>

### -param <i>*OriginalId</i> [out]

<dd>
<p>Upon successfully returning from the call, holds the ID that was previously set on the thread. The driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439297">IoClearActivityIdThread</a> with this pointer when tracing is completed within the same thread context.</p>
</dd>
</dl>

## -returns
<p><b>IoPropagateActivityIdToThread</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The IRP does not have an ID associated with it.</p>

<p> </p>

## -remarks
<p>This routine should be used by drivers that are tracing aware and are issuing I/O on a worker thread. Note that such drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439297">IoClearActivityIdThread</a> with the <i>OriginalId</i> before they return control from the thread, if the call was successful.</p>

<p>Drivers that use I/O work items do not need to call this routine because the I/O subsystem takes care of propagating activity IDs to threads in that case.</p>

<p>This routine should be used by drivers that are tracing aware and are issuing I/O on a worker thread. Note that such drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439297">IoClearActivityIdThread</a> with the <i>OriginalId</i> before they return control from the thread, if the call was successful.</p>

<p>Drivers that use I/O work items do not need to call this routine because the I/O subsystem takes care of propagating activity IDs to threads in that case.</p>

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