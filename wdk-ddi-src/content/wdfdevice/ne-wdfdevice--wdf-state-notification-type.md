---
UID: NE.wdfdevice._WDF_STATE_NOTIFICATION_TYPE
title: WDF_STATE_NOTIFICATION_TYPE
author: windows-driver-content
description: The WDF_STATE_NOTIFICATION_TYPE enumeration identifies the type of Plug and Play, power, or power policy notification that a framework-based driver will receive.
old-location: wdf\wdf_state_notification_type.htm
old-project: wdf
ms.assetid: fc44c970-482c-4fbf-a149-e6b732f6c9d8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_STATE_NOTIFICATION_TYPE
req.alt-loc: wdfdevice.h
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

# WDF_STATE_NOTIFICATION_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_STATE_NOTIFICATION_TYPE</b> enumeration identifies the type of Plug and Play, power, or power policy notification that a framework-based driver will receive.</p>


## -syntax

````
typedef enum _WDF_STATE_NOTIFICATION_TYPE { 
  StateNotificationInvalid           = 0x0000,
  StateNotificationEnterState        = 0x0001,
  StateNotificationPostProcessState  = 0x0002,
  StateNotificationLeaveState        = 0x0004,
  StateNotificationAllStates         = StateNotificationEnterState | StateNotificationPostProcessState | StateNotificationLeaveState
} WDF_STATE_NOTIFICATION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="StateNotificationInvalid"></a><a id="statenotificationinvalid"></a><a id="STATENOTIFICATIONINVALID"></a><b>StateNotificationInvalid</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="StateNotificationEnterState"></a><a id="statenotificationenterstate"></a><a id="STATENOTIFICATIONENTERSTATE"></a><b>StateNotificationEnterState</b>

<dd>
<p>The driver is notified immediately before a device's Plug and Play, power, or power policy state machine enters a specified state.</p>
</dd>

### -field <a id="StateNotificationPostProcessState"></a><a id="statenotificationpostprocessstate"></a><a id="STATENOTIFICATIONPOSTPROCESSSTATE"></a><b>StateNotificationPostProcessState</b>

<dd>
<p>The driver is notified immediately after a device's Plug and Play, power, or power policy state machine enters a specified state.</p>
</dd>

### -field <a id="StateNotificationLeaveState"></a><a id="statenotificationleavestate"></a><a id="STATENOTIFICATIONLEAVESTATE"></a><b>StateNotificationLeaveState</b>

<dd>
<p>The driver is notified immediately before a device's Plug and Play, power, or power policy state machine leaves a specified state.</p>
</dd>

### -field <a id="StateNotificationAllStates"></a><a id="statenotificationallstates"></a><a id="STATENOTIFICATIONALLSTATES"></a><b>StateNotificationAllStates</b>

<dd>
<p>The driver receives enter-state, postprocess-state, and leave-state notifications.</p>
</dd>
</dl>

## -remarks
<p>When the framework's state machine for a driver's device changes from state <i>a</i> to state <i>b</i>, the framework notifies the driver (if the driver registered an appropriate event callback function), in the following sequence:</p>

<p>Calls state <i>a</i>'s leave-state notification callback function.</p>

<p>Calls state <i>b</i>'s enter-state notification callback function.</p>

<p>Changes the device's state from <i>a</i> to <i>b</i>.</p>

<p>Calls state <i>b</i>'s postprocess-state notification callback function.</p>

<p>To register for notification of a change in state, the driver can call the following methods:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546057">WdfDeviceInitRegisterPnpStateChangeCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546071">WdfDeviceInitRegisterPowerStateChangeCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546066">WdfDeviceInitRegisterPowerPolicyStateChangeCallback</a>
</p>

<p>When the framework's state machine for a driver's device changes from state <i>a</i> to state <i>b</i>, the framework notifies the driver (if the driver registered an appropriate event callback function), in the following sequence:</p>

<p>Calls state <i>a</i>'s leave-state notification callback function.</p>

<p>Calls state <i>b</i>'s enter-state notification callback function.</p>

<p>Changes the device's state from <i>a</i> to <i>b</i>.</p>

<p>Calls state <i>b</i>'s postprocess-state notification callback function.</p>

<p>To register for notification of a change in state, the driver can call the following methods:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546057">WdfDeviceInitRegisterPnpStateChangeCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546071">WdfDeviceInitRegisterPowerStateChangeCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546066">WdfDeviceInitRegisterPowerPolicyStateChangeCallback</a>
</p>

<p>When the framework's state machine for a driver's device changes from state <i>a</i> to state <i>b</i>, the framework notifies the driver (if the driver registered an appropriate event callback function), in the following sequence:</p>

<p>Calls state <i>a</i>'s leave-state notification callback function.</p>

<p>Calls state <i>b</i>'s enter-state notification callback function.</p>

<p>Changes the device's state from <i>a</i> to <i>b</i>.</p>

<p>Calls state <i>b</i>'s postprocess-state notification callback function.</p>

<p>To register for notification of a change in state, the driver can call the following methods:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546057">WdfDeviceInitRegisterPnpStateChangeCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546071">WdfDeviceInitRegisterPowerStateChangeCallback</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546066">WdfDeviceInitRegisterPowerPolicyStateChangeCallback</a>
</p>

## -requirements
<table>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551260">WDF_DEVICE_PNP_NOTIFICATION_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551268">WDF_DEVICE_POWER_NOTIFICATION_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551273">WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_STATE_NOTIFICATION_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
