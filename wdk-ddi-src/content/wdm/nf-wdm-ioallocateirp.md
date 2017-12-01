---
UID: NF.wdm.IoAllocateIrp
title: IoAllocateIrp
author: windows-driver-content
description: The IoAllocateIrp routine allocates an IRP, given the number of I/O stack locations for each driver layered under the caller, and, optionally, for the caller.
old-location: kernel\ioallocateirp.htm
old-project: kernel
ms.assetid: 40abbdf8-3712-4724-8aef-16c247780c86
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoAllocateIrp
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
req.alt-api: IoAllocateIrp
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: ForwardedAtBadIrqlAllocate, IoAllocateComplete, IoAllocateForward, IoAllocateFree, IoAllocateIrpSignalEventInCompletion, IoAllocateIrpSignalEventInCompletion2, IoAllocateIrpSignalEventInCompletion3, IoAllocateIrpSignalEventInCompletionTimeout, IoReuseIrp, MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, HwStorPortProhibitedDDIs, IoFreeIrp, SpNoWait, StorPortStartIo
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

# IoAllocateIrp function



## -description
<p>The <b>IoAllocateIrp</b> routine allocates an IRP, given the number of I/O stack locations for each driver layered under the caller, and, optionally, for the caller.</p>


## -syntax

````
PIRP IoAllocateIrp(
  _In_ CCHAR   StackSize,
  _In_ BOOLEAN ChargeQuota
);
````


## -parameters
<dl>

### -param <i>StackSize</i> [in]

<dd>
<p>Specifies the number of I/O stack locations to be allocated for the IRP. This value must be at least equal to the <b>StackSize</b> of the next-lower driver's device object, but can be one greater than this value. The calling driver need not allocate a stack location in the IRP for itself.</p>
</dd>

### -param <i>ChargeQuota</i> [in]

<dd>
<p>Setting this to <b>TRUE</b> causes the memory allocated for the IRP to be charged against the quota for the current process. Should be set to <b>FALSE</b> by intermediate drivers. This can be set to <b>TRUE</b> only by highest-level drivers that are called in the context of the thread that originates the I/O request for which the driver is allocating another IRP.</p>
</dd>
</dl>

## -returns
<p><b>IoAllocateIrp</b> returns a pointer to an IRP, which was allocated from nonpaged system space, or <b>NULL</b> if an IRP could not be allocated.</p>

## -remarks
<p>The <b>IoAllocateIrp</b> routine does not associate the IRP with a thread. The allocating driver must free the IRP instead of completing it back to the I/O manager.</p>

<p>An intermediate or highest-level driver can call <b>IoAllocateIrp</b> to create IRPs for requests it sends to lower-level drivers. Such a driver must initialize the IRP and must set its <a href="..\wdm\nc-wdm-io-completion-routine.md">IoCompletion</a> routine in the IRP it creates so the caller can dispose of the IRP when lower-level drivers have completed processing of the request.</p>

<p><b>IoAllocateIrp</b> automatically initializes the IRP's members. Do not use <b>IoInitializeIrp</b> to initialize the IRP before its first use. (You can use <b>IoInitializeIrp</b> to reuse an IRP that you have already used under certain special circumstances. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561107">Reusing IRPs</a> for details.)</p>

<p>An intermediate or highest-level driver also can call <a href="..\wdm\nf-wdm-iobuilddeviceiocontrolrequest.md">IoBuildDeviceIoControlRequest</a>, <a href="..\wdm\nf-wdm-iobuildasynchronousfsdrequest.md">IoBuildAsynchronousFsdRequest</a> or <a href="..\wdm\nf-wdm-iobuildsynchronousfsdrequest.md">IoBuildSynchronousFsdRequest</a> to set up requests it sends to lower-level drivers. Only a highest-level driver can call <a href="..\ntddk\nf-ntddk-iomakeassociatedirp.md">IoMakeAssociatedIrp</a>. </p>

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
<a href="devtest.wdm_forwardedatbadirqlallocate">ForwardedAtBadIrqlAllocate</a>, <a href="devtest.wdm_ioallocatecomplete">IoAllocateComplete</a>, <a href="devtest.wdm_ioallocateforward">IoAllocateForward</a>, <a href="devtest.wdm_ioallocatefree">IoAllocateFree</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletion">IoAllocateIrpSignalEventInCompletion</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletion2">IoAllocateIrpSignalEventInCompletion2</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletion3">IoAllocateIrpSignalEventInCompletion3</a>, <a href="devtest.wdm_ioallocateirpsignaleventincompletiontimeout">IoAllocateIrpSignalEventInCompletionTimeout</a>, <a href="..\wdm\nf-wdm-ioreuseirp.md">IoReuseIrp</a>, <a href="devtest.wdm_markpower">MarkPower</a>, <a href="devtest.wdm_markpowerdown">MarkPowerDown</a>, <a href="devtest.wdm_markqueryrelations">MarkQueryRelations</a>, <a href="devtest.wdm_markstartdevice">MarkStartDevice</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="..\wdm\nf-wdm-iofreeirp.md">IoFreeIrp</a>, <a href="devtest.storport_spnowait">SpNoWait</a>, <a href="devtest.storport_storportstartio">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--io-stack-location.md">IO_STACK_LOCATION</a>
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
<a href="..\wdm\nf-wdm-iofreeirp.md">IoFreeIrp</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iomakeassociatedirp.md">IoMakeAssociatedIrp</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioreuseirp.md">IoReuseIrp</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iosetcompletionroutine.md">IoSetCompletionRoutine</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--irp.md">IRP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoAllocateIrp routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
