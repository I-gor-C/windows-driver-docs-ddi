---
UID: NF.wdfinterrupt.WdfInterruptQueueDpcForIsr
title: WdfInterruptQueueDpcForIsr
author: windows-driver-content
description: The WdfInterruptQueueDpcForIsr method queues a framework interrupt object's EvtInterruptDpc callback function for execution.
old-location: wdf\wdfinterruptqueuedpcforisr.htm
old-project: wdf
ms.assetid: ba9a292d-12c8-41b5-bddb-7c8ebf4fdc48
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfInterruptQueueDpcForIsr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfInterruptQueueDpcForIsr
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DIRQL
req.iface: 
req.product: Windows 10 or later.
---

# WdfInterruptQueueDpcForIsr function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfInterruptQueueDpcForIsr</b> method queues a framework interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a> callback function for execution.</p>


## -syntax

````
BOOLEAN WdfInterruptQueueDpcForIsr(
  _In_ WDFINTERRUPT Interrupt
);
````


## -parameters
<dl>

### -param <i>Interrupt</i> [in]

<dd>
<p>A handle to a framework interrupt object.</p>
</dd>
</dl>

## -returns
<p><b>WdfInterruptQueueDpcForIsr</b> returns <b>TRUE</b> if it successfully queues the interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a> callback function. The method returns <b>FALSE</b> if the callback function was previously queued and has not executed.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Drivers typically call <b>WdfInterruptQueueDpcForIsr</b> from within an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function.</p>

<p>An interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a> callback function can be queued only once before it executes. Therefore, if a call to <b>WdfInterruptQueueDpcForIsr</b> succeeds, subsequent calls will return <b>FALSE</b> until the framework dequeues and executes the <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>In KMDF 1.11 and later, a driver can call <b>WdfInterruptQueueDpcForIsr</b> from a passive-level ISR.  Note that a driver can register a work item or a DPC but not both.</p>

<p>The following code example shows how an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function should queue an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a> callback function.</p>

<p>Drivers typically call <b>WdfInterruptQueueDpcForIsr</b> from within an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function.</p>

<p>An interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a> callback function can be queued only once before it executes. Therefore, if a call to <b>WdfInterruptQueueDpcForIsr</b> succeeds, subsequent calls will return <b>FALSE</b> until the framework dequeues and executes the <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>In KMDF 1.11 and later, a driver can call <b>WdfInterruptQueueDpcForIsr</b> from a passive-level ISR.  Note that a driver can register a work item or a DPC but not both.</p>

<p>The following code example shows how an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function should queue an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a> callback function.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfinterrupt.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DIRQL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md">EvtInterruptDpc</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptQueueDpcForIsr method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
