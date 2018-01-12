---
UID: NF:wdm.IoCallDriver
title: IoCallDriver macro
author: windows-driver-content
description: The IoCallDriver routine sends an IRP to the driver associated with a specified device object.
old-location: kernel\iocalldriver.htm
old-project: kernel
ms.assetid: 5d1fff23-f1e8-41a5-9cd6-a20bd4a7883e
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: IoCallDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoCallDriver
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: CompleteRequestStatusCheck, CompletionRoutineRegistered, DeleteDevice, ForwardedAtBadIrql, ForwardedAtBadIrqlAllocate, ForwardedAtBadIrqlFsdAsync, ForwardedAtBadIrqlFsdSync, IoAllocateForward, IoAllocateIrpSignalEventInCompletionTimeout, IoBuildDeviceControlWait, IoBuildDeviceControlWaitTimeout, IoBuildFsdForward, IoBuildSynchronousFsdRequestWait, IoBuildSynchronousFsdRequestWaitTimeout, IoSetCompletionRoutineExCheck, IrpProcessingComplete, LowerDriverReturn, MarkDevicePower, MarkingQueuedIrps, MarkIrpPending, MarkIrpPending2, MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, PendedCompletedRequest, PendedCompletedRequest2, PendedCompletedRequest3, PendedCompletedRequestEx, PnpIrpCompletion, PowerDownFail, PowerUpFail, RemoveLockForward, RemoveLockForward2, RemoveLockForwardDeviceControl, RemoveLockForwardDeviceControl2, RemoveLockForwardDeviceControlInternal, RemoveLockForwardDeviceControlInternal2, RemoveLockForwardRead, RemoveLockForwardRead2, RemoveLockForwardWrite, RemoveLockForwardWrite2, RemoveLockMnRemove2, RemoveLockMnSurpriseRemove, RemoveLockQueryMnRemove, TargetRelationNeedsRef, WmiForward, HwStorPortProhibitedDDIs
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

# IoCallDriver macro



## -description
The <b>IoCallDriver</b> routine sends an IRP to the driver associated with a specified device object.



## -syntax

````
NTSTATUS IoCallDriver(
  _In_    PDEVICE_OBJECT DeviceObject,
  _Inout_ PIRP           Irp
);
````


## -parameters

### -param DeviceObject [in]

Pointer to a <a href="wdkgloss.d#wdkgloss.device_object#wdkgloss.device_object"><i>device object</i></a>, representing the target device for the requested I/O operation.


### -param Irp [in, out]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>. 


## -remarks
Before calling <b>IoCallDriver</b>, the calling driver must set up the I/O stack location in the IRP for the target driver. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558781">Passing IRPs Down the Driver Stack</a>.

<b>IoCallDriver</b> assigns the <i>DeviceObject</i> input parameter to the <i>DeviceObject</i> member of the <a href="..\wdm\ns-wdm-_io_stack_location.md">IO_STACK_LOCATION</a> structure for the driver being called.

An IRP passed in a call to <b>IoCallDriver</b> becomes inaccessible to the higher-level driver, unless the higher-level driver has called <a href="..\wdm\nf-wdm-iosetcompletionroutine.md">IoSetCompletionRoutine</a> to set up an <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine for the IRP. If it has, the IRP input to the <i>IoCompletion</i> routine has its I/O status block set by the lower drivers, and all lower-level drivers' I/O stack locations are filled with zeros.

Drivers for Windows Server 2003, Windows XP, and Windows 2000 must use <a href="..\wdm\nf-wdm-pocalldriver.md">PoCallDriver</a> rather than <b>IoCallDriver</b> to pass power IRPs (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a>). For more information, see <a href="https://msdn.microsoft.com/a47e2310-e89b-4552-bbe3-d4984ae8b564">Calling IoCallDriver vs. Calling PoCallDriver</a>. 


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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975144">CompleteRequestStatusCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543504">CompletionRoutineRegistered</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975146">DeleteDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546166">ForwardedAtBadIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975147">ForwardedAtBadIrqlAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975148">ForwardedAtBadIrqlFsdAsync</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975149">ForwardedAtBadIrqlFsdSync</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975153">IoAllocateForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975158">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975161">IoBuildDeviceControlWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975162">IoBuildDeviceControlWaitTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975165">IoBuildFsdForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975173">IoBuildSynchronousFsdRequestWait</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975174">IoBuildSynchronousFsdRequestWaitTimeout</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975179">IoSetCompletionRoutineExCheck</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547325">IrpProcessingComplete</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548273">LowerDriverReturn</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975187">MarkDevicePower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549016">MarkingQueuedIrps</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549018">MarkIrpPending</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549021">MarkIrpPending2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975188">MarkPower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975189">MarkPowerDown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975190">MarkQueryRelations</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975191">MarkStartDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550374">PendedCompletedRequest</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975198">PendedCompletedRequest2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975199">PendedCompletedRequest3</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975200">PendedCompletedRequestEx</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550407">PnpIrpCompletion</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975203">PowerDownFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975205">PowerUpFail</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975208">RemoveLockForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975209">RemoveLockForward2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975210">RemoveLockForwardDeviceControl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975211">RemoveLockForwardDeviceControl2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975212">RemoveLockForwardDeviceControlInternal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975213">RemoveLockForwardDeviceControlInternal2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975214">RemoveLockForwardRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975215">RemoveLockForwardRead2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975216">RemoveLockForwardWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975217">RemoveLockForwardWrite2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975233">RemoveLockMnRemove2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975234">RemoveLockMnSurpriseRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975235">RemoveLockQueryMnRemove</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552918">TargetRelationNeedsRef</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556175">WmiForward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioallocateirp.md">IoAllocateIrp</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iobuildasynchronousfsdrequest.md">IoBuildAsynchronousFsdRequest</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iobuilddeviceiocontrolrequest.md">IoBuildDeviceIoControlRequest</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iobuildsynchronousfsdrequest.md">IoBuildSynchronousFsdRequest</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iosetcompletionroutine.md">IoSetCompletionRoutine</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-pocalldriver.md">PoCallDriver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoCallDriver routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

