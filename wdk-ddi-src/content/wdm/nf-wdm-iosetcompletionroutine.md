---
UID: NF.wdm.IoSetCompletionRoutine
title: IoSetCompletionRoutine function
author: windows-driver-content
description: The IoSetCompletionRoutine routine registers an IoCompletion routine, which will be called when the next-lower-level driver has completed the requested operation for the given IRP.
old-location: kernel\iosetcompletionroutine.htm
old-project: kernel
ms.assetid: 09c645d0-4d46-46c0-9256-8d2ddd3670b9
ms.author: windowsdriverdev
ms.date: 12/15/2017
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

Pointer to the <a href="kernel.irp">IRP</a> that the driver is processing. 


### -param CompletionRoutine [in, optional]

Specifies the entry point for the driver-supplied <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine, which is called when the next-lower driver completes the packet.


### -param Context [in, optional]

Pointer to a driver-determined context to pass to the <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine. Context information must be stored in nonpaged memory, because the <i>IoCompletion</i> routine is called at IRQL &lt;= DISPATCH_LEVEL. 


### -param InvokeOnSuccess [in]

Specifies whether the completion routine is called if the IRP is completed with a success status value in the IRP's <a href="kernel.io_status_block">IO_STATUS_BLOCK</a> structure, based on results of the <b>NT_SUCCESS</b> macro (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS values</a>). 


### -param InvokeOnError [in]

Specifies whether the completion routine is called if the IRP is completed with a nonsuccess status value in the IRP's <b>IO_STATUS_BLOCK</b> structure.


### -param InvokeOnCancel [in]

Specifies whether the completion routine is called if a driver or the kernel has called <a href="kernel.iocancelirp">IoCancelIrp</a> to cancel the IRP.


## -returns
None


## -remarks
This routine sets the transfer address of the <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine in the given IRP. The lowest-level driver in a chain of layered drivers cannot call this routine.

<b>IoSetCompletionRoutine</b> registers the specified routine to be called when the next-lower-level driver has completed the requested operation in any or all of the following ways:

With a success status value

With a nonsuccess status value

By canceling the IRP

Usually, the I/O status block is set by the underlying device driver. It is read but not altered by any higher-level drivers' <i>IoCompletion</i> routines.

Higher-level drivers that allocate IRP's with <a href="kernel.ioallocateirp">IoAllocateIrp</a> or <a href="kernel.iobuildasynchronousfsdrequest">IoBuildAsynchronousFsdRequest</a> must call this routine with all <i>InvokeOn</i>Xxx parameters set to <b>TRUE</b> before passing the driver-allocated IRP to <a href="kernel.iocalldriver">IoCallDriver</a>. When the <i>IoCompletion</i> routine is called with such an IRP, it must free the driver-allocated IRP and any other resources that the driver set up for the request, such as MDLs with <a href="kernel.iobuildpartialmdl">IoBuildPartialMdl</a>. Such a driver should return STATUS_MORE_PROCESSING_REQUIRED when it calls <a href="kernel.iofreeirp">IoFreeIrp</a> to forestall the I/O manager's completion processing for the driver-allocated IRP.

Non-PnP drivers that might be unloaded before their <i>IoCompletion</i> routines run should use <a href="kernel.iosetcompletionroutineex">IoSetCompletionRoutineEx</a> instead.


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
<a href="devtest.wdm_completerequest">CompleteRequest</a>, <a href="devtest.wdm_completerequeststatuscheck">CompleteRequestStatusCheck</a>, <a href="devtest.wdm_completionroutineregistered">CompletionRoutineRegistered</a>, <a href="devtest.wdm_ioallocateforward">IoAllocateForward</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletion">IoAllocateIrpSignalEventInCompletion</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletion2">IoAllocateIrpSignalEventInCompletion2</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletion3">IoAllocateIrpSignalEventInCompletion3</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletiontimeout">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="devtest.wdm_iobuildfsdforward">IoBuildFsdForward</a>, <a href="devtest.wdm_iobuildfsdirpsignaleventincompletion">IoBuildFsdIrpSignalEventInCompletion</a>, <a href="devtest.wdm_iobuildfsdirpsignaleventincompletion2">IoBuildFsdIrpSignalEventInCompletion2</a>, <a href="devtest.wdm_iobuildfsdirpsignaleventincompletion3">IoBuildFsdIrpSignalEventInCompletion3</a>, <a href="devtest.wdm_iobuildfsdirpsignaleventincompletiontimeout">IoBuildFsdIrpSignalEventInCompletionTimeout</a>, <a href="devtest.wdm_iosetcompletionroutinenonpnpdriver">IoSetCompletionRoutineNonPnpDriver</a>, <a href="devtest.wdm_lowerdriverreturn">LowerDriverReturn</a>, <a href="devtest.wdm_markpower">MarkPower</a>, <a href="devtest.wdm_markpowerdown">MarkPowerDown</a>, <a href="devtest.wdm_markqueryrelations">MarkQueryRelations</a>, <a href="devtest.wdm_markstartdevice">MarkStartDevice</a>, <a href="devtest.wdm_pendedcompletedrequest">PendedCompletedRequest</a>, <a href="devtest.wdm_signaleventincompletion">SignalEventInCompletion</a>, <a href="devtest.wdm_signaleventincompletion2">SignalEventInCompletion2</a>, <a href="devtest.wdm_signaleventincompletion3">SignalEventInCompletion3</a>, <a href="devtest.wdm_startdevicewait">StartDeviceWait</a>, <a href="devtest.wdm_startdevicewait3">StartDeviceWait3</a>, <a href="devtest.kmdf_setcompletionroutinefromdispatch">SetCompletionRoutineFromDispatch</a>, <a href="devtest.storport_iofreeirp">IoFreeIrp</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.io_stack_location">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="kernel.ioallocateirp">IoAllocateIrp</a>
</dt>
<dt>
<a href="kernel.iobuildasynchronousfsdrequest">IoBuildAsynchronousFsdRequest</a>
</dt>
<dt>
<a href="kernel.irp">IRP</a>
</dt>
<dt>
<a href="kernel.iobuildpartialmdl">IoBuildPartialMdl</a>
</dt>
<dt>
<a href="kernel.iofreeirp">IoFreeIrp</a>
</dt>
<dt>
<a href="kernel.iosetcompletionroutineex">IoSetCompletionRoutineEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSetCompletionRoutine routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

