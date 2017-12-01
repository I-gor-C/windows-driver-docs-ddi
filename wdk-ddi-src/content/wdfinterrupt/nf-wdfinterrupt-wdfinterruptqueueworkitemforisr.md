---
UID: NF.wdfinterrupt.WdfInterruptQueueWorkItemForIsr
title: WdfInterruptQueueWorkItemForIsr
author: windows-driver-content
description: The WdfInterruptQueueWorkItemForIsr method queues a framework interrupt object's EvtInterruptWorkItem callback function for execution.
old-location: wdf\wdfinterruptqueueworkitemforisr.htm
old-project: wdf
ms.assetid: 1E88E9D9-B564-43B4-9A83-F621FF23437F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfInterruptQueueWorkItemForIsr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfInterruptQueueWorkItemForIsr
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DIRQL
req.iface: 
req.product: Windows 10 or later.
---

# WdfInterruptQueueWorkItemForIsr function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfInterruptQueueWorkItemForIsr</b> method queues a framework interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md">EvtInterruptWorkItem</a> callback function for execution.</p>


## -syntax

````
BOOLEAN WdfInterruptQueueWorkItemForIsr(
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
<p>
      If the driver's ISR is running at IRQL = PASSIVE_LEVEL, <b>WdfInterruptQueueWorkItemForIsr</b> returns <b>TRUE</b> if it successfully queues the interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md">EvtInterruptWorkItem</a> callback function. The method returns <b>FALSE</b> if the callback function was previously queued and has not executed.</p>

<p>
      If the driver's ISR is running at IRQL = DIRQL, the framework first queues an internal DPC and then queues a work item from that DPC. In this case, <b>WdfInterruptQueueWorkItemForIsr</b> returns <b>TRUE</b> if the framework successfully queues the internal DPC. The method returns <b>FALSE</b> if the internal DPC was previously queued.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Drivers typically call <b>WdfInterruptQueueWorkItemForIsr</b> from within an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function.</p>

<p>An interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md">EvtInterruptWorkItem</a> callback function can be queued only once before it executes. Therefore, if a call to <b>WdfInterruptQueueWorkItemForIsr</b> succeeds, subsequent calls will not queue additional callbacks.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>  A bug check occurs if drivers call <b>WdfInterruptQueueWorkItemForIsr</b> with an interrupt object that does not specify an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md">EvtInterruptWorkItem</a> callback function.

</p>

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
<p>1.11</p>
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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptqueuedpcforisr.md">WdfInterruptQueueDpcForIsr</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptcreate.md">WdfInterruptCreate</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptQueueWorkItemForIsr method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
