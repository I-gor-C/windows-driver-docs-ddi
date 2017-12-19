---
UID: NF.wdm.IoCallDriver
title: IoCallDriver macro
author: windows-driver-content
description: The IoCallDriver routine sends an IRP to the driver associated with a specified device object.
old-location: kernel\iocalldriver.htm
old-project: kernel
ms.assetid: 5d1fff23-f1e8-41a5-9cd6-a20bd4a7883e
ms.author: windowsdriverdev
ms.date: 12/15/2017
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

Pointer to the <a href="kernel.irp">IRP</a>. 


## -remarks
Before calling <b>IoCallDriver</b>, the calling driver must set up the I/O stack location in the IRP for the target driver. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558781">Passing IRPs Down the Driver Stack</a>.

<b>IoCallDriver</b> assigns the <i>DeviceObject</i> input parameter to the <i>DeviceObject</i> member of the <a href="kernel.io_stack_location">IO_STACK_LOCATION</a> structure for the driver being called.

An IRP passed in a call to <b>IoCallDriver</b> becomes inaccessible to the higher-level driver, unless the higher-level driver has called <a href="kernel.iosetcompletionroutine">IoSetCompletionRoutine</a> to set up an <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine for the IRP. If it has, the IRP input to the <i>IoCompletion</i> routine has its I/O status block set by the lower drivers, and all lower-level drivers' I/O stack locations are filled with zeros.

Drivers for Windows Server 2003, Windows XP, and Windows 2000 must use <a href="kernel.pocalldriver">PoCallDriver</a> rather than <b>IoCallDriver</b> to pass power IRPs (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a>). For more information, see <a href="https://msdn.microsoft.com/a47e2310-e89b-4552-bbe3-d4984ae8b564">Calling IoCallDriver vs. Calling PoCallDriver</a>. 


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
<a href="devtest.wdm_completerequeststatuscheck">CompleteRequestStatusCheck</a>, <a href="devtest.wdm_completionroutineregistered">CompletionRoutineRegistered</a>, <a href="devtest.wdm_deletedevice">DeleteDevice</a>, <a href="devtest.wdm_forwardedatbadirql">ForwardedAtBadIrql</a>, <a href="devtest.wdm_forwardedatbadirqlallocate">ForwardedAtBadIrqlAllocate</a>, <a href="devtest.wdm_forwardedatbadirqlfsdasync">ForwardedAtBadIrqlFsdAsync</a>, <a href="devtest.wdm_forwardedatbadirqlfsdsync">ForwardedAtBadIrqlFsdSync</a>, <a href="devtest.wdm_ioallocateforward">IoAllocateForward</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletiontimeout">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="devtest.wdm_iobuilddevicecontrolwait">IoBuildDeviceControlWait</a>, <a href="devtest.wdm_iobuilddevicecontrolwaittimeout">IoBuildDeviceControlWaitTimeout</a>, <a href="devtest.wdm_iobuildfsdforward">IoBuildFsdForward</a>, <a href="devtest.wdm_iobuildsynchronousfsdrequestwait">IoBuildSynchronousFsdRequestWait</a>, <a href="devtest.wdm_iobuildsynchronousfsdrequestwaittimeout">IoBuildSynchronousFsdRequestWaitTimeout</a>, <a href="devtest.wdm_iosetcompletionroutineexcheck">IoSetCompletionRoutineExCheck</a>, <a href="devtest.wdm_irpprocessingcomplete">IrpProcessingComplete</a>, <a href="devtest.wdm_lowerdriverreturn">LowerDriverReturn</a>, <a href="devtest.wdm_markdevicepower">MarkDevicePower</a>, <a href="devtest.wdm_markingqueuedirps">MarkingQueuedIrps</a>, <a href="devtest.wdm_markirppending">MarkIrpPending</a>, <a href="devtest.wdm_markirppending2">MarkIrpPending2</a>, <a href="devtest.wdm_markpower">MarkPower</a>, <a href="devtest.wdm_markpowerdown">MarkPowerDown</a>, <a href="devtest.wdm_markqueryrelations">MarkQueryRelations</a>, <a href="devtest.wdm_markstartdevice">MarkStartDevice</a>, <a href="devtest.wdm_pendedcompletedrequest">PendedCompletedRequest</a>, <a href="devtest.wdm_pendedcompletedrequest2">PendedCompletedRequest2</a>, <a href="devtest.wdm_pendedcompletedrequest3">PendedCompletedRequest3</a>, <a href="devtest.wdm_pendedcompletedrequestex">PendedCompletedRequestEx</a>, <a href="devtest.wdm_pnpirpcompletion">PnpIrpCompletion</a>, <a href="devtest.wdm_powerdownfail">PowerDownFail</a>, <a href="devtest.wdm_powerupfail">PowerUpFail</a>, <a href="devtest.wdm_removelockforward">RemoveLockForward</a>, <a href="devtest.wdm_removelockforward2">RemoveLockForward2</a>, <a href="devtest.wdm_removelockforwarddevicecontrol">RemoveLockForwardDeviceControl</a>, <a href="devtest.wdm_removelockforwarddevicecontrol2">RemoveLockForwardDeviceControl2</a>, <a href="devtest.wdm_removelockforwarddevicecontrolinternal">RemoveLockForwardDeviceControlInternal</a>, <a href="devtest.wdm_removelockforwarddevicecontrolinternal2">RemoveLockForwardDeviceControlInternal2</a>, <a href="devtest.wdm_removelockforwardread">RemoveLockForwardRead</a>, <a href="devtest.wdm_removelockforwardread2">RemoveLockForwardRead2</a>, <a href="devtest.wdm_removelockforwardwrite">RemoveLockForwardWrite</a>, <a href="devtest.wdm_removelockforwardwrite2">RemoveLockForwardWrite2</a>, <a href="devtest.wdm_removelockmnremove2">RemoveLockMnRemove2</a>, <a href="devtest.wdm_removelockmnsurpriseremove">RemoveLockMnSurpriseRemove</a>, <a href="devtest.wdm_removelockquerymnremove">RemoveLockQueryMnRemove</a>, <a href="devtest.wdm_targetrelationneedsref">TargetRelationNeedsRef</a>, <a href="devtest.wdm_wmiforward">WmiForward</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioallocateirp">IoAllocateIrp</a>
</dt>
<dt>
<a href="kernel.iobuildasynchronousfsdrequest">IoBuildAsynchronousFsdRequest</a>
</dt>
<dt>
<a href="kernel.iobuilddeviceiocontrolrequest">IoBuildDeviceIoControlRequest</a>
</dt>
<dt>
<a href="kernel.iobuildsynchronousfsdrequest">IoBuildSynchronousFsdRequest</a>
</dt>
<dt>
<a href="kernel.iosetcompletionroutine">IoSetCompletionRoutine</a>
</dt>
<dt>
<a href="kernel.pocalldriver">PoCallDriver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoCallDriver routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

