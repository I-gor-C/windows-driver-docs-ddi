---
UID: NC.wdfdriver.EVT_WDF_DRIVER_DEVICE_ADD
title: EVT_WDF_DRIVER_DEVICE_ADD
author: windows-driver-content
description: A driver's EvtDriverDeviceAdd event callback function performs device initialization operations when the Plug and Play (PnP) manager reports the existence of a device.
old-location: wdf\evtdriverdeviceadd.htm
ms.assetid: b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtDriverDeviceAdd
req.alt-loc: Wdfdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WDF_DPC_CONFIG, WDF_DPC_CONFIG, *PWDF_DPC_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_DRIVER_DEVICE_ADD callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtDriverDeviceAdd</i> event callback function performs device initialization operations when the Plug and Play (PnP) manager reports the existence of a device.</p>


## -prototype

````
EVT_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd;

NTSTATUS EvtDriverDeviceAdd(
  _In_    WDFDRIVER       Driver,
  _Inout_ PWDFDEVICE_INIT DeviceInit
)
{ ... }
````


## -parameters
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>A handle to a framework driver object that represents the driver.</p>
</dd>

### -param <i>DeviceInit</i> [in, out]

<dd>
<p>A pointer to a framework-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure. </p>
</dd>
</dl>

## -returns
<p>The<i>EvtDriverDeviceAdd</i> callback function must return STATUS_SUCCESS if the operation succeeds. Otherwise, this callback function must return one of the error status values that are defined in <i>Ntstatus.h</i>. For more information, see the following Remarks section.</p>

## -remarks
<p>Each framework-based driver that supports PnP devices must provide the <i>EvtDriverDeviceAdd</i> callback function. The driver must place the callback function's address in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551300">WDF_DRIVER_CONFIG</a> structure before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>.</p>

<p>The framework calls your driver's <i>EvtDriverDeviceAdd</i> callback function after a bus driver detects a device that has a hardware identifier (ID) that matches a hardware ID that your driver supports. You specify the hardware IDs that your driver supports by providing an INF file, which the operating system uses to install drivers the first time that one of your devices is connected to the computer. For more information about how the system uses INF files and hardware IDs, see <a href="devinst.how_setup_selects_drivers">How Setup Selects Drivers</a>.</p>

<p>A driver's <i>EvtDriverDeviceAdd</i> callback function typically performs at least some of the following initialization operations:</p>

<p>
<a href="wdf.creating_a_framework_device_object">Create a framework device object</a> to represent the device.</p>

<p>
<a href="wdf.creating_i_o_queues">Create I/O queues</a> so the driver can receive I/O requests.</p>

<p>
<a href="wdf.using_device_interfaces">Create device interfaces</a> that applications use to communicate with the device.</p>

<p>
<a href="wdf.using_driver_defined_interfaces">Create driver-defined interfaces</a> that other drivers can use.</p>

<p>Initialize <a href="wdf.supporting_wmi_in_kmdf_drivers">Windows Management Instrumentation (WMI)</a> support.</p>

<p>
<a href="wdf.creating_an_interrupt_object">Create interrupt objects</a>, if the driver handles device interrupts.</p>

<p>
<a href="wdf.enabling_dma_transactions">Enable direct memory access (DMA) transactions</a>, if the driver handles DMA operations.</p>

<p>Some drivers, especially filter drivers, might not create device objects for some devices. If an <i>EvtDriverDeviceAdd</i> callback function does not create a device object, it must still return STATUS_SUCCESS unless an error was encountered.</p>

<p>If a driver's <i>EvtDriverDeviceAdd</i> callback function creates a device object but does not return STATUS_SUCCESS, the framework deletes the device object and its child devices.</p>

<p>If a function driver's <i>EvtDriverDeviceAdd</i> callback function does not return STATUS_SUCCESS, the I/O manager does not build a device stack for the device.</p>

<p>If a filter driver's <i>EvtDriverDeviceAdd</i> callback function does not return STATUS_SUCCESS, the framework converts the return value to STATUS_SUCCESS, and the I/O manager builds the device stack without the filter driver.</p>

<p>To define an <i>EvtDriverDeviceAdd</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDriverDeviceAdd</i> callback function that is named <i>MyDriverDeviceAdd</i>, use the <b>EVT_WDF_DRIVER_DEVICE_ADD</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DRIVER_DEVICE_ADD</b> function type is defined in the WdfDriver.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DRIVER_DEVICE_ADD</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>Each framework-based driver that supports PnP devices must provide the <i>EvtDriverDeviceAdd</i> callback function. The driver must place the callback function's address in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551300">WDF_DRIVER_CONFIG</a> structure before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>.</p>

<p>The framework calls your driver's <i>EvtDriverDeviceAdd</i> callback function after a bus driver detects a device that has a hardware identifier (ID) that matches a hardware ID that your driver supports. You specify the hardware IDs that your driver supports by providing an INF file, which the operating system uses to install drivers the first time that one of your devices is connected to the computer. For more information about how the system uses INF files and hardware IDs, see <a href="devinst.how_setup_selects_drivers">How Setup Selects Drivers</a>.</p>

<p>A driver's <i>EvtDriverDeviceAdd</i> callback function typically performs at least some of the following initialization operations:</p>

<p>
<a href="wdf.creating_a_framework_device_object">Create a framework device object</a> to represent the device.</p>

<p>
<a href="wdf.creating_i_o_queues">Create I/O queues</a> so the driver can receive I/O requests.</p>

<p>
<a href="wdf.using_device_interfaces">Create device interfaces</a> that applications use to communicate with the device.</p>

<p>
<a href="wdf.using_driver_defined_interfaces">Create driver-defined interfaces</a> that other drivers can use.</p>

<p>Initialize <a href="wdf.supporting_wmi_in_kmdf_drivers">Windows Management Instrumentation (WMI)</a> support.</p>

<p>
<a href="wdf.creating_an_interrupt_object">Create interrupt objects</a>, if the driver handles device interrupts.</p>

<p>
<a href="wdf.enabling_dma_transactions">Enable direct memory access (DMA) transactions</a>, if the driver handles DMA operations.</p>

<p>Some drivers, especially filter drivers, might not create device objects for some devices. If an <i>EvtDriverDeviceAdd</i> callback function does not create a device object, it must still return STATUS_SUCCESS unless an error was encountered.</p>

<p>If a driver's <i>EvtDriverDeviceAdd</i> callback function creates a device object but does not return STATUS_SUCCESS, the framework deletes the device object and its child devices.</p>

<p>If a function driver's <i>EvtDriverDeviceAdd</i> callback function does not return STATUS_SUCCESS, the I/O manager does not build a device stack for the device.</p>

<p>If a filter driver's <i>EvtDriverDeviceAdd</i> callback function does not return STATUS_SUCCESS, the framework converts the return value to STATUS_SUCCESS, and the I/O manager builds the device stack without the filter driver.</p>

<p>To define an <i>EvtDriverDeviceAdd</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDriverDeviceAdd</i> callback function that is named <i>MyDriverDeviceAdd</i>, use the <b>EVT_WDF_DRIVER_DEVICE_ADD</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DRIVER_DEVICE_ADD</b> function type is defined in the WdfDriver.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DRIVER_DEVICE_ADD</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>Wdfdriver.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551300">WDF_DRIVER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_DRIVER_DEVICE_ADD callback function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
