---
UID: NS.wdfdevice._WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA
title: WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA
author: windows-driver-content
description: The WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA structure describes a state change within a device's power policy state machine.
old-location: wdf\wdf_device_power_policy_notification_data.htm
old-project: wdf
ms.assetid: aa91ea9b-3d92-4f33-8bbd-dd64a76a0a86
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA, WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA</b> structure describes a state change within a device's power policy state machine.</p>


## -syntax

````
typedef struct _WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA {
  WDF_STATE_NOTIFICATION_TYPE Type;
  union {
    struct {
      WDF_DEVICE_POWER_POLICY_STATE CurrentState;
      WDF_DEVICE_POWER_POLICY_STATE NewState;
    } EnterState;
    struct {
      WDF_DEVICE_POWER_POLICY_STATE CurrentState;
    } PostProcessState;
    struct {
      WDF_DEVICE_POWER_POLICY_STATE CurrentState;
      WDF_DEVICE_POWER_POLICY_STATE NewState;
    } LeaveState;
  } Data;
} WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>A <a href="..\wdfdevice\ne-wdfdevice--wdf-state-notification-type.md">WDF_STATE_NOTIFICATION_TYPE</a>-typed enumerator that identifies the type of state change that is being reported.</p>
</dd>

### -field <b>Data</b>

<dd>
<dl>

### -field <b>EnterState</b>

<dd>
<dl>

### -field <b>CurrentState</b>

<dd>
<p>If <b>Type</b> is <b>StateNotificationEnterState</b>, this <a href="..\wdfdevice\ne-wdfdevice--wdf-device-power-policy-state.md">WDF_DEVICE_POWER_POLICY_STATE</a>-typed enumerator identifies the state machine's current state.</p>
</dd>

### -field <b>NewState</b>

<dd>
<p>If <b>Type</b> is <b>StateNotificationEnterState</b>, this <a href="..\wdfdevice\ne-wdfdevice--wdf-device-power-policy-state.md">WDF_DEVICE_POWER_POLICY_STATE</a>-typed enumerator identifies the state machine's next state.</p>
</dd>
</dl>
</dd>

### -field <b>PostProcessState</b>

<dd>
<dl>

### -field <b>CurrentState</b>

<dd>
<p>If <b>Type</b> is <b>StateNotificationEnterState</b>, this <a href="..\wdfdevice\ne-wdfdevice--wdf-device-power-policy-state.md">WDF_DEVICE_POWER_POLICY_STATE</a>-typed enumerator identifies the state machine's current state.</p>
</dd>
</dl>
</dd>

### -field <b>LeaveState</b>

<dd>
<dl>

### -field <b>CurrentState</b>

<dd>
<p>If <b>Type</b> is <b>StateNotificationEnterState</b>, this <a href="..\wdfdevice\ne-wdfdevice--wdf-device-power-policy-state.md">WDF_DEVICE_POWER_POLICY_STATE</a>-typed enumerator identifies the state machine's current state.</p>
</dd>

### -field <b>NewState</b>

<dd>
<p>If <b>Type</b> is <b>StateNotificationEnterState</b>, this <a href="..\wdfdevice\ne-wdfdevice--wdf-device-power-policy-state.md">WDF_DEVICE_POWER_POLICY_STATE</a>-typed enumerator identifies the state machine's next state.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA</b> structure is an input argument to a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-power-policy-state-change-notification.md">EvtDevicePowerPolicyStateChange</a> callback function.</p>

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
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceinitregisterpowerpolicystatechangecallback.md">WdfDeviceInitRegisterPowerPolicyStateChangeCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
