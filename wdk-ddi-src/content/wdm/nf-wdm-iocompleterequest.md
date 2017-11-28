---
UID: NF.wdm.IoCompleteRequest
title: IoCompleteRequest
author: windows-driver-content
description: The IoCompleteRequest routine indicates that the caller has completed all processing for a given I/O request and is returning the given IRP to the I/O manager.
old-location: kernel\iocompleterequest.htm
old-project: kernel
ms.assetid: 59252b09-00ee-4a39-9849-5ce840ee16a7
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoCompleteRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoCompleteRequest
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CompleteRequest, CompleteRequestStatusCheck, DoubleCompletion, IoAllocateComplete, IoBuildFsdComplete, IoSetCompletionExCompleteIrp, IrpProcessingComplete, MarkIrpPending, PendedCompletedRequest, PendedCompletedRequest2, PendedCompletedRequest3, PendedCompletedRequestEx, PnpIrpCompletion, SpinLockSafe, WmiComplete, HwStorPortProhibitedDDIs, SpinLockSafe(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoCompleteRequest function



## -description
<p>The <b>IoCompleteRequest</b> routine indicates that the caller has completed all processing for a given I/O request and is returning the given IRP to the I/O manager.</p>


## -syntax

````
VOID IoCompleteRequest(
  _In_ PIRP  Irp,
  _In_ CCHAR PriorityBoost
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the IRP to be completed.</p>
</dd>

### -param <i>PriorityBoost</i> [in]

<dd>
<p>Specifies a system-defined constant by which to increment the run-time priority of the original thread that requested the operation. This value is IO_NO_INCREMENT if the original thread requested an operation the driver could complete quickly (so the requesting thread is not compensated for its assumed wait for I/O to be completed) or if the IRP is completed with an error. Otherwise, the set of <i>PriorityBoost</i> constants are device-type-specific. See Ntddk.h or Wdm.h for these constants.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When a driver has finished all processing for a given IRP, it calls <b>IoCompleteRequest</b>. The I/O manager checks the IRP to determine whether any higher-level drivers have set up an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine for the IRP. If so, each <i>IoCompletion</i> routine is called, in turn, until every layered driver in the chain has completed the IRP.</p>

<p>When all drivers have completed a given IRP, the I/O manager returns status to the original requester of the operation. Note that a higher-level driver that sets up a driver-created IRP must supply an <i>IoCompletion</i> routine to release the IRP it created.</p>

<p>Never call <b>IoCompleteRequest</b> while holding a spin lock. Attempting to complete an IRP while holding a spin lock can cause deadlocks.</p>

<p>When a driver has finished all processing for a given IRP, it calls <b>IoCompleteRequest</b>. The I/O manager checks the IRP to determine whether any higher-level drivers have set up an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine for the IRP. If so, each <i>IoCompletion</i> routine is called, in turn, until every layered driver in the chain has completed the IRP.</p>

<p>When all drivers have completed a given IRP, the I/O manager returns status to the original requester of the operation. Note that a higher-level driver that sets up a driver-created IRP must supply an <i>IoCompletion</i> routine to release the IRP it created.</p>

<p>Never call <b>IoCompleteRequest</b> while holding a spin lock. Attempting to complete an IRP while holding a spin lock can cause deadlocks.</p>

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
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975143">CompleteRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975144">CompleteRequestStatusCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff819059">DoubleCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975152">IoAllocateComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975164">IoBuildFsdComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975178">IoSetCompletionExCompleteIrp</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547325">IrpProcessingComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549018">MarkIrpPending</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550374">PendedCompletedRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975198">PendedCompletedRequest2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975199">PendedCompletedRequest3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975200">PendedCompletedRequestEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550407">PnpIrpCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454252">SpinLockSafe</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556174">WmiComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_spinlocksafe">SpinLockSafe(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549679">IoSetCompletionRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoCompleteRequest routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
