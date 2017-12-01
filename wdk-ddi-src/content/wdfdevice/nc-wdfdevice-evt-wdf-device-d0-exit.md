---
UID: NC.wdfdevice.EVT_WDF_DEVICE_D0_EXIT
title: EVT_WDF_DEVICE_D0_EXIT
author: windows-driver-content
description: A driver's EvtDeviceD0Exit event callback function performs operations that are needed when the driver's device leaves the D0 power state.
old-location: wdf\evtdeviced0exit.htm
old-project: wdf
ms.assetid: bc3af732-f9ab-43a4-bc6f-7fa0b4c05a66
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
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: EvtDeviceD0Exit
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

# EVT_WDF_DEVICE_D0_EXIT callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtDeviceD0Exit</i> event callback function performs operations that are needed when the driver's device leaves the D0 power state.</p>


## -prototype

````
EVT_WDF_DEVICE_D0_EXIT EvtDeviceD0Exit;

NTSTATUS EvtDeviceD0Exit(
  _In_ WDFDEVICE              Device,
  _In_ WDF_POWER_DEVICE_STATE TargetState
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>TargetState</i> [in]

<dd>
<p>A <a href="..\wudfddi_types\ne-wudfddi-types--wdf-power-device-state.md">WDF_POWER_DEVICE_STATE</a>-typed enumerator that identifies the device power state that the device is about to enter.</p>
</dd>
</dl>

## -returns
<p>If the <i>EvtDeviceD0Exit</i> callback function encounters no errors, it must return STATUS_SUCCESS or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>TRUE</b>. Otherwise, it must return a status value for which NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>.</p>

## -remarks
<p>To register an <i>EvtDeviceD0Exit</i> callback function, a driver must call <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks.md">WdfDeviceInitSetPnpPowerEventCallbacks</a>. </p>

<p>If the driver has registered an <i>EvtDeviceD0Exit</i> callback function, the framework calls the function each time one of the driver's devices leaves its working (D0) state. A device leaves the D0 state when one of the following occurs:</p>

<p>The system and all of its devices are about to leave their working states and enter a low-power state.</p>

<p>The device is about to enter a low-power state because it is idle, if the device supports low-power idle.</p>

<p>The Plug and Play manager is attempting to redistribute the system's hardware resources.</p>

<p>A user has indicated, typically by means of an application's user interface, that he or she wants to remove the device.</p>

<p>The framework also calls the <i>EvtDeviceD0Exit</i> callback function after a device has been removed unexpectedly (surprise-removed).</p>

<p>For more information about when the framework calls this callback function, see <a href="wdf.pnp_and_power_management_scenarios">PnP and Power Management Scenarios</a>.</p>

<p>Unless the device has been surprise-removed, the framework calls this callback function immediately after it disables the device's interrupts, but before the device's power is reduced from D0. The <i>TargetState</i> parameter identifies the device power state that the device is about to enter. </p>

<p>The <i>EvtDeviceD0Exit</i> callback function must perform any operations that are necessary before the device enters the specified low-power state, such as saving any information that the driver will need later to restore the device to its D0 power state.</p>

<p>If the <i>TargetState</i> parameter is <b>WdfPowerDevicePrepareForHibernation</b>, the driver must not shut off the device, because the system will use the device when saving its hibernation file. </p>

<p>If <i>TargetState</i> is <b>WdfPowerDeviceD3Final</b>, you should assume that the system is being turned off, the device is about to be removed, or a <a href="wdf.the_pnp_manager_redistributes_system_resources">resource rebalance</a> is in progress. If your driver must save information, it should write it to disk or some other permanent storage medium. </p>

<p>For more information about drivers that provide this callback function, see <a href="wdf.supporting_pnp_and_power_management_in_function_drivers">Supporting PnP and Power Management in Function Drivers</a>.</p>

<p>To define an <i>EvtDeviceD0Exit</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceD0Exit</i> callback function that is named <i>MyDeviceD0Exit</i>, use the <b>EVT_WDF_DEVICE_D0_EXIT</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_D0_EXIT</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_D0_EXIT</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_DEVICE_D0_EXIT callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
