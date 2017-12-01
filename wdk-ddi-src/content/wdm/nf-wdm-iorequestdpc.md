---
UID: NF.wdm.IoRequestDpc
title: IoRequestDpc
author: windows-driver-content
description: The IoRequestDpc routine queues a driver-supplied DpcForIsr routine to complete interrupt-driven I/O processing at a lower IRQL.
old-location: kernel\iorequestdpc.htm
old-project: kernel
ms.assetid: 196555c8-74a6-4dae-ac4d-52654015ffeb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoRequestDpc
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
req.alt-api: IoRequestDpc
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DIRQL
req.iface: 
req.product: Windows 10 or later.
---

# IoRequestDpc function



## -description
<p>The <b>IoRequestDpc</b> routine queues a driver-supplied <a href="kernel.dpcforisr">DpcForIsr</a> routine to complete interrupt-driven I/O processing at a lower IRQL.</p>


## -syntax

````
VOID IoRequestDpc(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp,
  _In_ PVOID          Context
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object for which the request that caused the interrupt is being processed.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the current IRP for the specified device.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to a driver-determined context to be passed to the DPC routine.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Callers of <b>IoRequestDpc</b> must be running at DIRQL.</p>

<p>Drivers call  <b>IoRequestDpc</b> from an <a href="kernel.interruptservice">InterruptService</a> routine. Because of this, <b>IoRequestDpc</b> runs at the DIRQL value that was specified by <i>SynchronizeIrql</i> when the driver called <a href="..\wdm\nf-wdm-ioconnectinterrupt.md">IoConnectInterrupt</a>. However, it is also possible to queue a DPC at any IRQL &gt;= DISPATCH_LEVEL by using the <b>Ke<i>Xxx</i>Dpc</b> routines. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565664">Which Type of DPC Should You Use?</a>
</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>DIRQL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioinitializedpcrequest.md">IoInitializeDpcRequest</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinitializedpc.md">KeInitializeDpc</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinsertqueuedpc.md">KeInsertQueueDpc</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRequestDpc routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
