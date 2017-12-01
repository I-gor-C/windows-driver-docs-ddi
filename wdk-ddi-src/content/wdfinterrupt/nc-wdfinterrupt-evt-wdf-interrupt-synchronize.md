---
UID: NC.wdfinterrupt.EVT_WDF_INTERRUPT_SYNCHRONIZE
title: EVT_WDF_INTERRUPT_SYNCHRONIZE
author: windows-driver-content
description: A driver's EvtInterruptSynchronize event callback function performs operations that must be synchronized with an EvtInterruptIsr callback function.
old-location: wdf\evtinterruptsynchronize.htm
old-project: wdf
ms.assetid: ac73b23d-7742-43a4-8950-b301bd0ba330
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_COINSTALLER_INSTALL_OPTIONS, WDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtInterruptSynchronize
req.alt-loc: Wdfinterrupt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: (See Remarks section.)
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_INTERRUPT_SYNCHRONIZE callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtInterruptSynchronize</i> event callback function performs operations that must be synchronized with an <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function.</p>


## -prototype

````
EVT_WDF_INTERRUPT_SYNCHRONIZE EvtInterruptSynchronize;

BOOLEAN EvtInterruptSynchronize(
  _In_ WDFINTERRUPT Interrupt,
  _In_ WDFCONTEXT   Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>Interrupt</i> [in]

<dd>
<p>A handle to a framework interrupt object.</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Driver-supplied information that the driver specifies when it calls <a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsynchronize.md">WdfInterruptSynchronize</a>.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtInterruptSynchronize</i> callback function must return <b>TRUE</b> if the operation succeeds. Otherwise, this function must return <b>FALSE</b>. </p>

## -remarks
<p>To execute an <i>EvtInterruptSynchronize</i> callback function, the driver must call <a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsynchronize.md">WdfInterruptSynchronize</a>. </p>

<p>If the driver has configured the interrupt object for handling at the device's IRQL (DIRQL), then before calling the <i>EvtInterruptSynchronize</i> callback function, the framework raises the processor's interrupt request level to DIRQL and acquires the spin lock that the driver specified in the interrupt object's <a href="..\wdfinterrupt\ns-wdfinterrupt--wdf-interrupt-config.md">WDF_INTERRUPT_CONFIG</a> structure. </p>

<p>As a result, while an <i>EvtInterruptSynchronize</i> callback function is executing, the interrupt object's <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback function (and any other code that executes at DIRQL while holding the spin lock) cannot execute. </p>

<p><i>EvtInterruptSynchronize</i> callback functions must be designed so that they execute for only a short period of time. They are typically used to access interrupt data that is also accessed by an interrupt object's other <i>EvtInterruptSynchronize</i> or <a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a> callback functions. </p>

<p>Beginning with version 1.11 of KMDF, your driver can provide <a href="wdf.supporting_passive_level_interrupts">passive-level interrupt handling</a>. If the driver has requested passive-level interrupt handling, then before calling the <i>EvtInterruptSynchronize</i> function at IRQL = PASSIVE_LEVEL, the framework acquires the passive-level interrupt lock that the driver configured in the interrupt object's <a href="..\wdfinterrupt\ns-wdfinterrupt--wdf-interrupt-config.md">WDF_INTERRUPT_CONFIG</a> structure.</p>

<p>For more information about the <i>EvtInterruptSynchronize</i> callback function, see <a href="wdf.synchronizing_interrupt_code">Synchronizing Interrupt Code</a>.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>To define an <i>EvtInterruptSynchronize</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtInterruptSynchronize</i> callback function that is named <i>MyInterruptSynchronize</i>, use the <b>EVT_WDF_INTERRUPT_SYNCHRONIZE</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows.</p>

<p>The <b>EVT_WDF_INTERRUPT_SYNCHRONIZE</b> function type is defined in the Wdfinterrupt.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_INTERRUPT_SYNCHRONIZE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>(See Remarks section.)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsynchronize.md">WdfInterruptSynchronize</a>
</dt>
<dt>
<a href="..\wdfinterrupt\ns-wdfinterrupt--wdf-interrupt-config.md">WDF_INTERRUPT_CONFIG</a>
</dt>
<dt>
<a href="..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md">EvtInterruptIsr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_INTERRUPT_SYNCHRONIZE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
