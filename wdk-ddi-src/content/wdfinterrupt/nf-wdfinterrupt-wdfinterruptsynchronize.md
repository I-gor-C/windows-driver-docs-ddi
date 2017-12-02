---
UID: NF.wdfinterrupt.WdfInterruptSynchronize
title: WdfInterruptSynchronize
author: windows-driver-content
description: The WdfInterruptSynchronize method executes a specified callback function at the device's DIRQL while holding an interrupt object's spin lock.
old-location: wdf\wdfinterruptsynchronize.htm
old-project: wdf
ms.assetid: b41fc37a-d41f-49ca-848f-844e049dd987
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfInterruptSynchronize
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
req.alt-api: WdfInterruptSynchronize
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfInterruptSynchronize function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfInterruptSynchronize</b> method executes a specified callback function at the device's DIRQL while holding an interrupt object's spin lock.</p>
<p>For passive level interrupt objects, this method executes a specified callback function at passive level while holding an interrupt object's passive-level interrupt lock.</p>


## -syntax

````
BOOLEAN WdfInterruptSynchronize(
  _In_ WDFINTERRUPT                  Interrupt,
  _In_ PFN_WDF_INTERRUPT_SYNCHRONIZE Callback,
  _In_ WDFCONTEXT                    Context
);
````


## -parameters
<dl>

### -param Interrupt [in]

<dd>
<p>A handle to a framework interrupt object.</p>
</dd>

### -param Callback [in]

<dd>
<p>A pointer to an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a> callback function.</p>
</dd>

### -param Context [in]

<dd>
<p>An untyped pointer to driver-supplied information that the framework passes to the <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a> callback function.</p>
</dd>
</dl>

## -returns
<p><b>WdfInterruptSynchronize</b> returns the Boolean status value that the <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a> callback function returns.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>If you want your driver to execute code that must run without being preempted and with servicing of device interrupts effectively disabled, you should place that code in an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a> callback function. To schedule execution of the callback function, your driver must call <b>WdfInterruptSynchronize</b>.</p>

<p>The <b>WdfInterruptSynchronize</b> method returns after the <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a> callback function has finished executing.</p>

<p>Instead of calling <b>WdfInterruptSynchronize</b>, your driver can call <a href="wdf.wdfinterruptacquirelock">WdfInterruptAcquireLock</a> and <a href="wdf.wdfinterruptreleaselock">WdfInterruptReleaseLock</a>.</p>

<p>For more information about the <b>WdfInterruptSynchronize</b> method, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>For passive level interrupts, the driver must call <b>WdfInterruptSynchronize</b> at IRQL = PASSIVE_LEVEL.</p>

<p>Do not call <b>WdfInterruptSynchronize</b> from an arbitrary thread context,  such as a <a href="wdf.request_handlers">request handler</a>.</p>

<p>The following code example shows how to call <b>WdfInterruptSynchronize</b> to schedule execution of an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a>  callback function.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfinterruptacquirelock">WdfInterruptAcquireLock</a>
</dt>
<dt>
<a href="wdf.wdfinterruptreleaselock">WdfInterruptReleaseLock</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md">EvtInterruptSynchronize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfInterruptSynchronize method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
