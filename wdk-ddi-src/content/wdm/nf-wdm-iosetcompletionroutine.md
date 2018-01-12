---
UID: NF:wdm.IoSetCompletionRoutine
title: IoSetCompletionRoutine function
author: windows-driver-content
description: The IoSetCompletionRoutine routine registers an IoCompletion routine, which will be called when the next-lower-level driver has completed the requested operation for the given IRP.
old-location: kernel\iosetcompletionroutine.htm
old-project: kernel
ms.assetid: 09c645d0-4d46-46c0-9256-8d2ddd3670b9
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: IoSetCompletionRoutine
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetCompletionRoutine
req.alt-loc: Wdm.h
req.ddi-compliance: CompleteRequest, CompleteRequestStatusCheck, CompletionRoutineRegistered, IoAllocateForward, IoAllocateIrpSignalEventInCompletion, IoAllocateIrpSignalEventInCompletion2, IoAllocateIrpSignalEventInCompletion3, IoAllocateIrpSignalEventInCompletionTimeout, IoBuildFsdForward, IoBuildFsdIrpSignalEventInCompletion, IoBuildFsdIrpSignalEventInCompletion2, IoBuildFsdIrpSignalEventInCompletion3, IoBuildFsdIrpSignalEventInCompletionTimeout, IoSetCompletionRoutineNonPnpDriver, LowerDriverReturn, MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, PendedCompletedRequest, SignalEventInCompletion, SignalEventInCompletion2, SignalEventInCompletion3, StartDeviceWait, StartDeviceWait3, SetCompletionRoutineFromDispatch, IoFreeIrp
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---

# IoSetCompletionRoutine function



## -description
The <b>IoSetCompletionRoutine</b> routine registers an <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine, which will be called when the next-lower-level driver has completed the requested operation for the given IRP. 



## -syntax

````
VOID IoSetCompletionRoutine(
  _In_     PIRP                   Irp,
  _In_opt_ PIO_COMPLETION_ROUTINE CompletionRoutine,
  _In_opt_ PVOID                  Context,
  _In_     BOOLEAN                InvokeOnSuccess,
  _In_     BOOLEAN                InvokeOnError,
  _In_     BOOLEAN                InvokeOnCancel
);
````


## -parameters

### -param Irp [in]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> that the driver is processing. 


### -param CompletionRoutine [in, optional]

Specifies the entry point for the driver-supplied <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine, which is called when the next-lower driver completes the packet.


### -param Context [in, optional]

Pointer to a driver-determined context to pass to the <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine. Context information must be stored in nonpaged memory, because the <i>IoCompletion</i> routine is called at IRQL &lt;= DISPATCH_LEVEL. 


### -param InvokeOnSuccess [in]

Specifies whether the completion routine is called if the IRP is completed with a success status value in the IRP's <a href="..\wdm\ns-wdm-_io_status_block.md">IO_STATUS_BLOCK</a> structure, based on results of the <b>NT_SUCCESS</b> macro (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS values</a>). 


### -param InvokeOnError [in]

Specifies whether the completion routine is called if the IRP is completed with a nonsuccess status value in the IRP's <b>IO_STATUS_BLOCK</b> structure.


### -param InvokeOnCancel [in]

Specifies whether the completion routine is called if a driver or the kernel has called <a href="..\wdm\nf-wdm-iocancelirp.md">IoCancelIrp</a> to cancel the IRP.


## -returns
None


## -remarks
This routine sets the transfer address of the <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine in the given IRP. The lowest-level driver in a chain of layered drivers cannot call this routine.

<b>IoSetCompletionRoutine</b> registers the specified routine to be called when the next-lower-level driver has completed the requested operation in any or all of the following ways:

With a success status value

With a nonsuccess status value

By canceling the IRP

Usually, the I/O status block is set by the underlying device driver. It is read but not altered by any higher-level drivers' <i>IoCompletion</i> routines.

Higher-level drivers that allocate IRP's with <a href="..\wdm\nf-wdm-ioallocateirp.md">IoAllocateIrp</a> or <a href="..\wdm\nf-wdm-iobuildasynchronousfsdrequest.md">IoBuildAsynchronousFsdRequest</a> must call this routine with all <i>InvokeOn</i>Xxx parameters set to <b>TRUE</b> before passing the driver-allocated IRP to <a href="..\wdm\nf-wdm-iocalldriver.md">IoCallDriver</a>. When the <i>IoCompletion</i> routine is called with such an IRP, it must free the driver-allocated IRP and any other resources that the driver set up for the request, such as MDLs with <a href="..\wdm\nf-wdm-iobuildpartialmdl.md">IoBuildPartialMdl</a>. Such a driver should return STATUS_MORE_PROCESSING_REQUIRED when it calls <a href="..\wdm\nf-wdm-iofreeirp.md">IoFreeIrp</a> to forestall the I/O manager's completion processing for the driver-allocated IRP.

Non-PnP drivers that might be unloaded before their <i>IoCompletion</i> routines run should use <a href="..\wdm\nf-wdm-iosetcompletionroutineex.md">IoSetCompletionRoutineEx</a> instead.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975143">CompleteRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975144">CompleteRequestStatusCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543504">CompletionRoutineRegistered</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975153">IoAllocateForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975155">IoAllocateIrpSignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975156">IoAllocateIrpSignalEventInCompletion2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975157">IoAllocateIrpSignalEventInCompletion3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975158">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975165">IoBuildFsdForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975167">IoBuildFsdIrpSignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975168">IoBuildFsdIrpSignalEventInCompletion2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975169">IoBuildFsdIrpSignalEventInCompletion3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975170">IoBuildFsdIrpSignalEventInCompletionTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975181">IoSetCompletionRoutineNonPnpDriver</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548273">LowerDriverReturn</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975188">MarkPower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975189">MarkPowerDown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975190">MarkQueryRelations</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975191">MarkStartDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550374">PendedCompletedRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975249">SignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975250">SignalEventInCompletion2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975251">SignalEventInCompletion3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975252">StartDeviceWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975254">StartDeviceWait3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975097">SetCompletionRoutineFromDispatch</a>, <a href="..\wdm\nf-wdm-iofreeirp.md">IoFreeIrp</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm-_io_stack_location.md">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioallocateirp.md">IoAllocateIrp</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iobuildasynchronousfsdrequest.md">IoBuildAsynchronousFsdRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iobuildpartialmdl.md">IoBuildPartialMdl</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iofreeirp.md">IoFreeIrp</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iosetcompletionroutineex.md">IoSetCompletionRoutineEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSetCompletionRoutine routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

