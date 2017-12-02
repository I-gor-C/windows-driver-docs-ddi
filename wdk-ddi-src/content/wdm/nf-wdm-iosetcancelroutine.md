---
UID: NF.wdm.IoSetCancelRoutine
title: IoSetCancelRoutine
author: windows-driver-content
description: The IoSetCancelRoutine routine sets up a driver-supplied Cancel routine to be called if a given IRP is canceled.
old-location: kernel\iosetcancelroutine.htm
old-project: kernel
ms.assetid: 5bc81897-6463-4588-9348-78a1954216bd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoSetCancelRoutine
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
req.alt-api: IoSetCancelRoutine
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrpCancelField, StartIoCancel
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: DISPATCH_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# IoSetCancelRoutine function



## -description
<p>The <b>IoSetCancelRoutine</b> routine sets up a driver-supplied <a href="kernel.cancel">Cancel</a> routine to be called if a given IRP is canceled. </p>


## -syntax

````
PDRIVER_CANCEL IoSetCancelRoutine(
  _In_ PIRP           Irp,
  _In_ PDRIVER_CANCEL CancelRoutine
);
````


## -parameters
<dl>

### -param Irp [in]

<dd>
<p>Pointer to the IRP being put into or removed from a cancelable state.</p>
</dd>

### -param CancelRoutine [in]

<dd>
<p>Specifies the entry point of the caller-supplied <a href="kernel.cancel">Cancel</a> routine to be called if the specified IRP is canceled or is <b>NULL</b> if the given IRP is being removed from the cancelable state. This routine is declared as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>VOID
(*PDRIVER_CANCEL)(
    IN PDEVICE_OBJECT DeviceObject,
    IN PIRP Irp
    );</pre>
</td>
</tr>
</table></span></div>
</dd>
</dl>

## -returns
<p><b>IoSetCancelRoutine</b> returns the previous value of <i>Irp</i>-&gt;<b>CancelRoutine</b>. If no <i>Cancel</i> routine was previously set, or if IRP cancellation is already in progress, <b>IoSetCancelRoutine</b> returns <b>NULL</b>.</p>

## -remarks
<p>This routine can disable the <i>Cancel</i> routine currently set in an IRP.</p>

<p>A driver must hold the system cancel spin lock when calling this routine if the driver uses the I/O manager-supplied device queue in the device object. The driver runs at IRQL = DISPATCH_LEVEL after calling <a href="kernel.ioacquirecancelspinlock">IoAcquireCancelSpinLock</a> until it releases the cancel spin lock with <a href="kernel.ioreleasecancelspinlock">IoReleaseCancelSpinLock</a>.</p>

<p>If the driver manages its own queues of IRPs, then the driver need not hold the cancel spin lock when calling this routine. <b>IoSetCancelRoutine</b> uses an interlocked exchange intrinsic to set the address of the <i>Cancel</i> routine as an atomic operation. Reduced usage of the cancel spin lock can improve driver performance and overall system performance.</p>

<p>Driver <i>Cancel</i> routines are called at IRQL = DISPATCH_LEVEL with the cancel spin lock held. The <i>Cancel</i> routine must release the cancel spin lock before it returns control.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<p>DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irpcancelfield">IrpCancelField</a>, <a href="devtest.wdm_startiocancel">StartIoCancel</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioacquirecancelspinlock">IoAcquireCancelSpinLock</a>
</dt>
<dt>
<a href="kernel.ioreleasecancelspinlock">IoReleaseCancelSpinLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoSetCancelRoutine routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
