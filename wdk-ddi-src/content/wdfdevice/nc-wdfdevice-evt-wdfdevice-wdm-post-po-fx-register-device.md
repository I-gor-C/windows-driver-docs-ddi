---
UID: NC.wdfdevice.EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE
title: EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE
author: windows-driver-content
description: The EvtDeviceWdmPostPoFxRegisterDevice callback function performs device-specific operations after the framework has registered with the power framework.
old-location: wdf\evtdevicewdmpostpofxregisterdevice.htm
old-project: wdf
ms.assetid: 4CE227F5-9ED4-4484-AFBF-44D1260EB99D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: EvtDeviceWdmPostPoFxRegisterDevice
req.alt-loc: Wdfdevice.h
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
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The 
  <i>EvtDeviceWdmPostPoFxRegisterDevice</i> callback function performs device-specific operations after the framework has registered with the power framework.</p>


## -prototype

````
EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE EvtDeviceWdmPostPoFxRegisterDevice;

NTSTATUS EvtDeviceWdmPostPoFxRegisterDevice(
  _In_ WDFDEVICE Device,
  _In_ POHANDLE  PoHandle
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>PoHandle</i> [in]

<dd>
<p>A handle that represents the device’s registration with the power framework.</p>
</dd>
</dl>

## -returns
<p>An NTSTATUS value indicating success or failure of the operations performed in this callback. If failure is returned, the framework in turn  will fail <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a>.</p>

## -remarks
<p>If you are writing a KMDF driver for a single-component device that defines multiple functional power states, you can register an <i>EvtDeviceWdmPostPoFxRegisterDevice</i> callback function to receive notification after the framework registers with the power management framework (PoFx).</p>

<p>To register <i>EvtDeviceWdmPostPoFxRegisterDevice</i>, a driver must call <a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings.md">WdfDeviceWdmAssignPowerFrameworkSettings</a>.</p>

<p>The POHANDLE received in <i>EvtDeviceWdmPostPoFxRegisterDevice</i> remains valid until the driver returns from <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-pre-po-fx-unregister-device.md">EvtDeviceWdmPrePoFxUnregisterDevice</a>.</p>

<p>Your driver can use the POHANDLE to call <a href="..\wdm\nf-wdm-pofxsetcomponentlatency.md">PoFxSetComponentLatency</a>, <a href="..\wdm\nf-wdm-pofxsetcomponentresidency.md">PoFxSetComponentResidency</a>, and <a href="..\wdm\nf-wdm-pofxsetcomponentwake.md">PoFxSetComponentWake</a> to specify latency, residency, and wake hints to the power framework.</p>

<p> 

Your driver can also use the POHANDLE to call <a href="..\wdm\nf-wdm-pofxpowercontrol.md">PoFxPowerControl</a> to send a power control request to PoFx.</p>

<p>A KMDF driver for a multiple component device does not provide <i>EvtDeviceWdmPostPoFxRegisterDevice</i>. Instead, such a driver receives the POHANDLE when it calls <i>PoFxRegisterDevice</i>.  For more information, see <a href="wdf.supporting_multiple_functional_power_states_for_multiple-component_devices">Supporting Multiple Functional Power States for Multiple-Component Devices</a>.</p>

<p>To define an <i>EvtDeviceWdmPostPoFxRegisterDevice</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceWdmPostPoFxRegisterDevice</i> callback function that is named <i>MyDeviceWdmPostPoFxRegisterDevice</i>, use the <b>EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows.</p>

<p>The <b>EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
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
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings.md">WdfDeviceWdmAssignPowerFrameworkSettings</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-pre-po-fx-unregister-device.md">EvtDeviceWdmPrePoFxUnregisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
