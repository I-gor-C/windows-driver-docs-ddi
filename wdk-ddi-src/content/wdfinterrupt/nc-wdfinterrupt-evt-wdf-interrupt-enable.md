---
UID: NC.wdfinterrupt.EVT_WDF_INTERRUPT_ENABLE
title: EVT_WDF_INTERRUPT_ENABLE
author: windows-driver-content
description: A driver's EvtInterruptEnable event callback function enables a specified hardware interrupt.
old-location: wdf\evtinterruptenable.htm
ms.assetid: 981195e6-6f62-4a6f-9c84-d98f6cd7bab3
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtInterruptEnable
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
ms.keywords: WDF_COINSTALLER_INSTALL_OPTIONS, WDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_INTERRUPT_ENABLE callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtInterruptEnable</i> event callback function enables a specified hardware interrupt.</p>


## -prototype

````
EVT_WDF_INTERRUPT_ENABLE EvtInterruptEnable;

NTSTATUS EvtInterruptEnable(
  _In_ WDFINTERRUPT Interrupt,
  _In_ WDFDEVICE    AssociatedDevice
)
{ ... }
````


## -parameters
<dl>

### -param <i>Interrupt</i> [in]

<dd>
<p>A handle to a framework interrupt object.</p>
</dd>

### -param <i>AssociatedDevice</i> [in]

<dd>
<p>A handle to the framework device object that the driver passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtInterruptEnable</i> callback function must return STATUS_SUCCESS or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>TRUE</b> if the function encounters no errors. Otherwise, this function must return a status value for which NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>. </p>

## -remarks
<p>To register an <i>EvtInterruptEnable</i> callback function, your driver must place the callback function's address in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552347">WDF_INTERRUPT_CONFIG</a> structure before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>.</p>

<p>The framework calls the driver's <i>EvtInterruptEnable</i> callback function each time the device enters its working (D0) state. Additionally, a driver can cause the framework to call the <i>EvtInterruptEnable</i> callback function by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547354">WdfInterruptEnable</a>.  Note that most framework-based drivers should not call <b>WdfInterruptEnable</b>, because the framework calls the driver's <i>EvtInterruptEnable</i> callback function each time the device enters its working (D0) state.</p>

<p>Before calling the <i>EvtInterruptEnable</i> callback function, the framework raises the processor's IRQL to the device's DIRQL and acquires the spin lock that the driver specified in the interrupt object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552347">WDF_INTERRUPT_CONFIG</a> structure. </p>

<p>Beginning with version 1.11 of KMDF, your driver can provide <a href="wdf.supporting_passive_level_interrupts">passive-level interrupt handling</a>. If the driver has requested passive-level interrupt handling, then before calling the <i>EvtInterruptEnable</i> function at IRQL = PASSIVE_LEVEL, the framework acquires the passive-level interrupt lock that the driver configured in the interrupt object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552347">WDF_INTERRUPT_CONFIG</a> structure.</p>

<p>After the <i>EvtInterruptEnable</i> callback function returns, the framework calls the driver's <a href="https://msdn.microsoft.com/38d74ce1-9d9d-4da5-a2b3-579048850b28">EvtDeviceD0EntryPostInterruptsEnabled</a> event callback function at IRQL = PASSIVE_LEVEL.</p>

<p>You must not assume that a device will use the same interrupt resources each time the framework calls your driver's <i>EvtInterruptEnable</i> callback function. Sometimes the PnP manager <a href="wdf.the_pnp_manager_redistributes_system_resources">redistributes system resources</a>, and it might assign new interrupt resources to your device. The driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff547367">WdfInterruptGetInfo</a> to determine a device's interrupt resources.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>To define an <i>EvtInterruptEnable</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtInterruptEnable</i> callback function that is named <i>MyInterruptEnable</i>, use the <b>EVT_WDF_INTERRUPT_ENABLE</b> type as shown in this code example:</p>

<p>Then, implement your callback function:</p>

<p>The <b>EVT_WDF_INTERRUPT_ENABLE</b> function type is defined in the Wdfinterrupt.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_INTERRUPT_ENABLE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>To register an <i>EvtInterruptEnable</i> callback function, your driver must place the callback function's address in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552347">WDF_INTERRUPT_CONFIG</a> structure before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>.</p>

<p>The framework calls the driver's <i>EvtInterruptEnable</i> callback function each time the device enters its working (D0) state. Additionally, a driver can cause the framework to call the <i>EvtInterruptEnable</i> callback function by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547354">WdfInterruptEnable</a>.  Note that most framework-based drivers should not call <b>WdfInterruptEnable</b>, because the framework calls the driver's <i>EvtInterruptEnable</i> callback function each time the device enters its working (D0) state.</p>

<p>Before calling the <i>EvtInterruptEnable</i> callback function, the framework raises the processor's IRQL to the device's DIRQL and acquires the spin lock that the driver specified in the interrupt object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552347">WDF_INTERRUPT_CONFIG</a> structure. </p>

<p>Beginning with version 1.11 of KMDF, your driver can provide <a href="wdf.supporting_passive_level_interrupts">passive-level interrupt handling</a>. If the driver has requested passive-level interrupt handling, then before calling the <i>EvtInterruptEnable</i> function at IRQL = PASSIVE_LEVEL, the framework acquires the passive-level interrupt lock that the driver configured in the interrupt object's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552347">WDF_INTERRUPT_CONFIG</a> structure.</p>

<p>After the <i>EvtInterruptEnable</i> callback function returns, the framework calls the driver's <a href="https://msdn.microsoft.com/38d74ce1-9d9d-4da5-a2b3-579048850b28">EvtDeviceD0EntryPostInterruptsEnabled</a> event callback function at IRQL = PASSIVE_LEVEL.</p>

<p>You must not assume that a device will use the same interrupt resources each time the framework calls your driver's <i>EvtInterruptEnable</i> callback function. Sometimes the PnP manager <a href="wdf.the_pnp_manager_redistributes_system_resources">redistributes system resources</a>, and it might assign new interrupt resources to your device. The driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff547367">WdfInterruptGetInfo</a> to determine a device's interrupt resources.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="wdf.handling_hardware_interrupts">Handling Hardware Interrupts</a>.</p>

<p>To define an <i>EvtInterruptEnable</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtInterruptEnable</i> callback function that is named <i>MyInterruptEnable</i>, use the <b>EVT_WDF_INTERRUPT_ENABLE</b> type as shown in this code example:</p>

<p>Then, implement your callback function:</p>

<p>The <b>EVT_WDF_INTERRUPT_ENABLE</b> function type is defined in the Wdfinterrupt.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_INTERRUPT_ENABLE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547345">WdfInterruptCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547354">WdfInterruptEnable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547367">WdfInterruptGetInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552347">WDF_INTERRUPT_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/38d74ce1-9d9d-4da5-a2b3-579048850b28">EvtDeviceD0EntryPostInterruptsEnabled</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a9d5e3cd-2e95-4ad6-9380-64fe4df9e27f">EvtInterruptDisable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_INTERRUPT_ENABLE callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
