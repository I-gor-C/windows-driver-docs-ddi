---
UID: NC.wdfdevice.EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON
title: EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON
author: windows-driver-content
description: A driver's EvtDeviceArmWakeFromSxWithReason event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state.
old-location: wdf\evtdevicearmwakefromsxwithreason.htm
old-project: wdf
ms.assetid: 8966ea8f-9760-4a09-b9d3-8fd1ac278b12
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
req.kmdf-ver: 1.7
req.umdf-ver: 2.0
req.alt-api: EvtDeviceArmWakeFromSxWithReason
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

# EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtDeviceArmWakeFromSxWithReason</i> event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. The wake signal causes the device to enter its working state (D0) and causes the system to enter its working state (S0). </p>


## -prototype

````
EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON EvtDeviceArmWakeFromSxWithReason;

NTSTATUS EvtDeviceArmWakeFromSxWithReason(
  _In_ WDFDEVICE Device,
  _In_ BOOLEAN   DeviceWakeEnabled,
  _In_ BOOLEAN   ChildrenArmedForWake
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>DeviceWakeEnabled</i> [in]

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the device's ability to wake the system is enabled. </p>
</dd>

### -param <i>ChildrenArmedForWake</i> [in]

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the ability of one or more child devices to wake the system is enabled.</p>
</dd>
</dl>

## -returns
<p>If the <i>EvtDeviceArmWakeFromSxWithReason</i> callback function encounters no error, it must return STATUS_SUCCESS or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>TRUE</b>. Otherwise it must return a status value for which NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>.</p>

<p>If NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>, the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-disarm-wake-from-sx.md">EvtDeviceDisarmWakeFromSx</a> callback function. (The framework does not report a device failure to the PnP manager.) </p>

## -remarks
<p>Version 1.7 and later versions of KMDF support the <i>EvtDeviceArmWakeFromSxWithReason</i> callback function in addition to the <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-sx.md">EvtDeviceArmWakeFromSx</a> callback function.</p>

<p>To register an <i>EvtDeviceArmWakeFromSxWithReason</i> callback function, a driver must call <a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks.md">WdfDeviceInitSetPowerPolicyEventCallbacks</a>. Drivers can register either an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-sx.md">EvtDeviceArmWakeFromSx</a> callback function or an <i>EvtDeviceArmWakeFromSxWithReason</i> callback function, but not both.</p>

<p>The <i>EvtDeviceArmWakeFromSxWithReason</i> callback function provides two parameters that enable the driver to determine why the framework has called it:</p>

<p>The framework sets the <i>DeviceWakeEnabled</i> parameter to <b>TRUE</b> if the <b>Enabled</b> member of the <a href="..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-wake-settings.md">WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS</a> structure indicates that the device can wake the system.</p>

<p>The framework sets the <i>ChildrenArmedForWake</i> parameter to <b>TRUE</b> if one or more of the device's child devices can wake the system and the <b>ArmForWakeIfChildrenAreArmedForWake</b> member of WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS is set to <b>TRUE</b>.</p>

<p>Either one or both of these parameters can be <b>TRUE</b>, because of the following scenarios:</p>

<p>The driver's device is enabled to wake the system.</p>

<p>One or more of the device's child devices are enabled to wake the system.</p>

<p>Both the device and one or more of its child devices are enabled to wake the system.</p>

<p>For more information about the <i>EvtDeviceArmWakeFromSxWithReason</i> callback function, see the Remarks section of <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-sx.md">EvtDeviceArmWakeFromSx</a>.</p>

<p>To define an <i>EvtDeviceArmWakeFromSxWithReason</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceArmWakeFromSxWithReason</i> callback function that is named <i>MyDeviceArmWakeFromSxWithReason</i>, use the <b>EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>1.7</p>
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
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-s0.md">EvtDeviceArmWakeFromS0</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-sx.md">EvtDeviceArmWakeFromSx</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-disarm-wake-from-sx.md">EvtDeviceDisarmWakeFromSx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
