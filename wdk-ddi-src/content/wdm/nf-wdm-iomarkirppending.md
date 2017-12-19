---
UID: NF.wdm.IoMarkIrpPending
title: IoMarkIrpPending function
author: windows-driver-content
description: The IoMarkIrpPending routine marks the specified IRP, indicating that a driver's dispatch routine subsequently returned STATUS_PENDING because further processing is required by other driver routines.
old-location: kernel\iomarkirppending.htm
old-project: kernel
ms.assetid: 424d5ebd-c871-40d8-b5b7-3a4a04fe60fa
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IoMarkIrpPending
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
req.alt-api: IoMarkIrpPending
req.alt-loc: Wdm.h
req.ddi-compliance: CompleteRequestStatusCheck, CompletionEventChecking, IrpCancelField, LowerDriverReturn, MarkDevicePower, MarkingInterlockedQueuedIrps, MarkingQueuedIrps, MarkIrpPending, MarkIrpPending2, MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, PendedCompletedRequest3
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.product: Windows 10 or later.
---

# IoMarkIrpPending function



## -description
The <b>IoMarkIrpPending</b> routine marks the specified IRP, indicating that a driver's dispatch routine subsequently returned STATUS_PENDING because further processing is required by other driver routines.



## -syntax

````
VOID IoMarkIrpPending(
  _Inout_ PIRP Irp
);
````


## -parameters

### -param Irp [in, out]

Pointer to the IRP to be marked as pending.


## -returns
None


## -remarks
Unless the driver's dispatch routine completes the IRP (by calling <a href="kernel.iocompleterequest">IoCompleteRequest</a>) or passes the IRP on to lower drivers, it must call <b>IoMarkIrpPending</b> with the IRP. Otherwise, the I/O manager attempts to complete the IRP as soon as the dispatch routine returns control.

After calling <b>IoMarkIrpPending</b>, the dispatch routine must return STATUS_PENDING, even if some routine completes the IRP (by calling <a href="kernel.iocompleterequest">IoCompleteRequest</a>) before the dispatch routine that called <b>IoMarkIrpPending</b> returns.

If a driver queues incoming IRPs, it should call <b>IoMarkIrpPending</b> before it queues each IRP. Otherwise, an IRP could be dequeued, completed by another driver routine, and freed by the system before the call to <b>IoMarkIrpPending</b> occurs, thereby causing a crash.

If a driver sets an <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine for an IRP and then passes the IRP down to a lower driver, the <i>IoCompletion</i> routine should check the <b>IRP-&gt;PendingReturned</b> flag. If the flag is set, the <i>IoCompletion</i> routine must call <b>IoMarkIrpPending</b> with the IRP. (<i>IoCompletion</i> routines do not return STATUS_PENDING, however. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff547084">Implementing an IoCompletion Routine</a>.) 

A driver that passes down the IRP and then waits on an event should not mark the IRP pending. Instead, its <i>IoCompletion</i> routine should signal the event and return STATUS_MORE_PROCESSING_REQUIRED.

If your driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a>, be careful not to modify the <a href="kernel.io_stack_location">IO_STACK_LOCATION</a> structure in a way that could unintentionally affect the lower driver or the system's behavior with respect to that driver. In particular, your driver should not modify the <b>IO_STACK_LOCATION</b> structure's <b>Parameters</b> union, and should not call <b>IoMarkIrpPending</b>.


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
Any level

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_completerequeststatuscheck">CompleteRequestStatusCheck</a>, <a href="devtest.wdm_completioneventchecking">CompletionEventChecking</a>, <a href="devtest.wdm_irpcancelfield">IrpCancelField</a>, <a href="devtest.wdm_lowerdriverreturn">LowerDriverReturn</a>, <a href="devtest.wdm_markdevicepower">MarkDevicePower</a>, <a href="devtest.wdm_markinginterlockedqueuedirps">MarkingInterlockedQueuedIrps</a>, <a href="devtest.wdm_markingqueuedirps">MarkingQueuedIrps</a>, <a href="devtest.wdm_markirppending">MarkIrpPending</a>, <a href="devtest.wdm_markirppending2">MarkIrpPending2</a>, <a href="devtest.wdm_markpower">MarkPower</a>, <a href="devtest.wdm_markpowerdown">MarkPowerDown</a>, <a href="devtest.wdm_markqueryrelations">MarkQueryRelations</a>, <a href="devtest.wdm_markstartdevice">MarkStartDevice</a>, <a href="devtest.wdm_pendedcompletedrequest3">PendedCompletedRequest3</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.iocompleterequest">IoCompleteRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550355">IoSkipCurrentIrpStackLocation</a>
</dt>
<dt>
<a href="kernel.io_stack_location">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="kernel.iostartpacket">IoStartPacket</a>
</dt>
<dt>
<a href="kernel.irp">IRP</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoMarkIrpPending routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

