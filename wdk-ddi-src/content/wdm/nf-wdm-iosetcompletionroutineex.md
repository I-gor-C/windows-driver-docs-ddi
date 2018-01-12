---
UID: NF:wdm.IoSetCompletionRoutineEx
title: IoSetCompletionRoutineEx function
author: windows-driver-content
description: The IoSetCompletionRoutineEx routine registers an IoCompletion routine, which is called when the next-lower-level driver has completed the requested operation for the given IRP.
old-location: kernel\iosetcompletionroutineex.htm
old-project: kernel
ms.assetid: fe84e542-c8b2-4631-9ffb-dde471311871
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: IoSetCompletionRoutineEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetCompletionRoutineEx
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CompleteRequest, CompleteRequestStatusCheck, CompletionRoutineRegistered, IoAllocateForward, IoAllocateIrpSignalEventInCompletion, IoAllocateIrpSignalEventInCompletion2, IoAllocateIrpSignalEventInCompletion3, IoAllocateIrpSignalEventInCompletionTimeout, IoBuildFsdForward, IoBuildFsdIrpSignalEventInCompletion, IoBuildFsdIrpSignalEventInCompletion2, IoBuildFsdIrpSignalEventInCompletion3, IoBuildFsdIrpSignalEventInCompletionTimeout, IoSetCompletionExCompleteIrp, IoSetCompletionRoutineExCheck, IoSetCompletionRoutineExCheckDeviceObject, LowerDriverReturn, MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, PendedCompletedRequestEx, SignalEventInCompletion, SignalEventInCompletion2, SignalEventInCompletion3, StartDeviceWait2, StartDeviceWait4, SetCompletionRoutineFromDispatch, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---

# IoSetCompletionRoutineEx function



## -description
The <b>IoSetCompletionRoutineEx</b> routine registers an <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine, which is called when the next-lower-level driver has completed the requested operation for the given IRP.



## -syntax

````
NTSTATUS IoSetCompletionRoutineEx(
  _In_     PDEVICE_OBJECT         DeviceObject,
  _In_     PIRP                   Irp,
  _In_     PIO_COMPLETION_ROUTINE CompletionRoutine,
  _In_opt_ PVOID                  Context,
  _In_     BOOLEAN                InvokeOnSuccess,
  _In_     BOOLEAN                InvokeOnError,
  _In_     BOOLEAN                InvokeOnCancel
);
````


## -parameters

### -param DeviceObject [in]

Pointer to the driver's device object.


### -param Irp [in]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> that the driver is processing.


### -param CompletionRoutine [in]

Specifies the entry point for the driver-supplied <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine, which is called when the next-lower driver completes the packet.


### -param Context [in, optional]

Pointer to a driver-determined context to pass to the <i>IoCompletion</i> routine. Context information must be stored in nonpaged memory, because the <i>IoCompletion</i> routine is called at IRQL &lt;= DISPATCH_LEVEL.


### -param InvokeOnSuccess [in]

Specifies whether the completion routine is called if the IRP is completed with a success status value in the IRP's <a href="..\wdm\ns-wdm-_io_status_block.md">IO_STATUS_BLOCK</a> structure, based on results of the NT_SUCCESS macro (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS values</a>).


### -param InvokeOnError [in]

Specifies whether the completion routine is called if the IRP is completed with a nonsuccess status value in the IRP's <b>IO_STATUS_BLOCK</b> structure.


### -param InvokeOnCancel [in]

Specifies whether the completion routine is called if a driver or the kernel has called <a href="..\wdm\nf-wdm-iocancelirp.md">IoCancelIrp</a> to cancel the IRP.


## -returns
This routine returns STATUS_SUCCESS on success, or STATUS_INSUFFICIENT_RESOURCES if insufficient memory is available for the operation.


## -remarks
The <i>IoCompletion</i> routine must belong to the driver that owns the device object pointed to by <i>DeviceObject</i>. This requirement prevents the <i>IoCompletion</i> routine from being unloaded before it returns.

The behavior of <b>IoSetCompletionRoutineEx</b> is the same as the <a href="..\wdm\nf-wdm-iosetcompletionroutine.md">IoSetCompletionRoutine</a> routine, except that:

<b>IoSetCompletionRoutineEx</b> guarantees that a non-Plug and Play driver is not unloaded before the <i>IoCompletion</i> routine runs.

<b>IoSetCompletionRoutineEx</b> is a routine that returns an NTSTATUS value.


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
Available starting with Windows XP.

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
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975143">CompleteRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975144">CompleteRequestStatusCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543504">CompletionRoutineRegistered</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975153">IoAllocateForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975155">IoAllocateIrpSignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975156">IoAllocateIrpSignalEventInCompletion2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975157">IoAllocateIrpSignalEventInCompletion3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975158">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975165">IoBuildFsdForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975167">IoBuildFsdIrpSignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975168">IoBuildFsdIrpSignalEventInCompletion2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975169">IoBuildFsdIrpSignalEventInCompletion3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975170">IoBuildFsdIrpSignalEventInCompletionTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975178">IoSetCompletionExCompleteIrp</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975179">IoSetCompletionRoutineExCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975180">IoSetCompletionRoutineExCheckDeviceObject</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548273">LowerDriverReturn</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975188">MarkPower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975189">MarkPowerDown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975190">MarkQueryRelations</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975191">MarkStartDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975200">PendedCompletedRequestEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975249">SignalEventInCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975250">SignalEventInCompletion2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975251">SignalEventInCompletion3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975253">StartDeviceWait2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975255">StartDeviceWait4</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975097">SetCompletionRoutineFromDispatch</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm-_io_stack_location.md">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a>
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
<a href="..\wdm\nf-wdm-iosetcompletionroutine.md">IoSetCompletionRoutine</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSetCompletionRoutineEx routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

