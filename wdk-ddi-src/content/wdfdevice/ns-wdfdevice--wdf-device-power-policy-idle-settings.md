---
UID: NS.wdfdevice._WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS
title: WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS
author: windows-driver-content
description: The WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure contains driver-supplied information that the framework uses when a device is idle and the system is in the system working state (S0).
old-location: wdf\wdf_device_power_policy_idle_settings.htm
old-project: wdf
ms.assetid: 8d5acd3a-3ec3-4190-98d4-e7ce9ea8d3e8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS, WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS, *PWDF_DEVICE_POWER_POLICY_IDLE_SETTINGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS
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

# WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</b> structure contains driver-supplied information that the framework uses when a device is idle and the system is in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0).</p>


## -syntax

````
typedef struct _WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS {
  ULONG                                 Size;
  WDF_POWER_POLICY_S0_IDLE_CAPABILITIES IdleCaps;
  DEVICE_POWER_STATE                    DxState;
  ULONG                                 IdleTimeout;
  WDF_POWER_POLICY_S0_IDLE_USER_CONTROL UserControlOfIdleSettings;
  WDF_TRI_STATE                         Enabled;
  WDF_TRI_STATE                         PowerUpIdleDeviceOnSystemWake;
  WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE    IdleTimeoutType;
  WDF_TRI_STATE                         ExcludeD3Cold;
} WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS, *PWDF_DEVICE_POWER_POLICY_IDLE_SETTINGS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>IdleCaps</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552429">WDF_POWER_POLICY_S0_IDLE_CAPABILITIES</a>-typed enumerator that identifies the device's ability to wake itself up after being set to a low-power state, while the system remains in its working (S0) state.</p>
</dd>

### -field <b>DxState</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a>-typed enumerator that identifies the low <a href="https://msdn.microsoft.com/2229f34c-9b88-4e3e-802e-f7be2c7ef168">device power state</a> that the device will enter after the idle timeout period ends. <b>DEVICE_POWER_STATE</b> values are defined in <i>wdm.h</i>.</p>
</dd>

### -field <b>IdleTimeout</b>

<dd>
<p>The amount of time, in milliseconds, that the device will remain idle before the framework places it in the <b>DxState</b>-supplied low-power state. To use the framework's default idle timeout value, specify <b>IdleTimeoutDefaultValue</b>. For more information on when the framework considers the device to be idle, see <a href="wdf.supporting_idle_power_down#idle_conditions#idle_conditions">Supporting Idle Power-Down</a>.</p>
</dd>

### -field <b>UserControlOfIdleSettings</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552432">WDF_POWER_POLICY_S0_IDLE_USER_CONTROL</a>-typed enumerator that indicates whether users have the ability to modify the device's idle settings.</p>
</dd>

### -field <b>Enabled</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed enumerator that indicates whether the device will be powered down if it remains idle and while the system power is at S0. This member can have one of the following values:</p>
<dl>
<dd>
<p><b>WdfTrue</b> - Powering down is enabled.</p>
</dd>
<dd>
<p><b>WdfFalse</b> - Powering down is disabled.</p>
</dd>
<dd>
<p><b>WdfUseDefault</b> - Powering down is initially enabled by default; but if the <b>UserControlOfIdleSettings</b> member is set to <b>IdleAllowUserControl</b>, the <a href="wdf.user_control_of_device_idle_and_wake_behavior">user's setting or driver's INF file</a> overrides the initial value.</p>
</dd>
</dl>
<p>If powering down is enabled, the device has a wake-up capability, and the idle timeout value expires, the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-s0.md">EvtDeviceArmWakeFromS0</a> callback function before the device enters a low-power state.</p>
</dd>

### -field <b>PowerUpIdleDeviceOnSystemWake</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed enumerator that indicates whether the device will return to its working (D0) state when the system returns to its working (S0) state. This member is valid only if the driver sets the <b>IdleCaps</b> member to <a href="..\wudfddi_types\ne-wudfddi-types--wdf-power-policy-s0-idle-capabilities.md">IdleCannotWakeFromS0</a>. The <b>PowerUpIdleDeviceOnSystemWake</b> member can have one of the following values:</p>
<dl>
<dd>
<p><b>WdfTrue</b> - If both the device and the system are in a low-power state, the device returns to its working state when the system returns to its working state.</p>
</dd>
<dd>
<p><b>WdfFalse</b> - If both the device and the system are in a low-power state, the device remains in the low-power state when the system returns to its working state.</p>
</dd>
<dd>
<p><b>WdfUseDefault</b> - The default value that the framework uses if the driver does not set a different value. This value has the same meaning as <b>WdfFalse</b>. </p>
</dd>
</dl>
<p>If the <b>PowerUpIdleDeviceOnSystemWake</b> member is set to <b>WdfFalse</b> or <b>WdfUseDefault</b>, the device returns to its working state only when software accesses the device, such as when an application sends an I/O request to the device. For more information, see <a href="wdf.a_device_returns_to_its_working_state">A Device Returns to Its Working State</a>.</p>
<p>The <b>PowerUpIdleDeviceOnSystemWake</b> member is available in version 1.9 and later versions of KMDF, and starting in version 2.0 of UMDF.</p>
</dd>

### -field <b>IdleTimeoutType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh706247">WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE</a>-typed enumerator  that indicates how the <b>IdleTimeout</b> member is used.</p>
<p>The <b>IdleTimeoutType</b> member is available in version 1.11 and later versions of KMDF, and starting in version 2.0 of UMDF. See additional information in Remarks.</p>
</dd>

### -field <b>ExcludeD3Cold</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed enumerator that indicates whether the D3cold power state should be an allowable choice for the low-power state that the device will enter when the idle timeout period expires. The <b>ExcludeD3Cold</b> member can have one of the following values:</p>
<dl>
<dd>
<p><b>WdfTrue</b> - The framework will move a device to a low-power D-state when the idle timeout period expires.  If that D-state is D3, the device will be moved to D3hot.  If <b>ExcludeD3Cold</b> is set to <b>WdfTrue</b>, then no further transition from D3hot to D3cold will be allowed.</p>
</dd>
<dd>
<p><b>WdfFalse</b> - The device may enter the D3cold power state when the idle timeout period expires, if all of the following criteria are met:</p>
<ul>
<li>The <b>DxState</b> member of this structure specifies <b>PowerDeviceD3</b> or <b>PowerDeviceMaximum</b>.</li>
<li>The ACPI firmware indicates that the device supports the D3cold power state.</li>
<li>If the driver specified <b>IdleCanWakeFromS0</b> or <b>IdleUsbSelectiveSuspend</b> in the <b>IdleCaps</b> member of this structure, the device can respond to an external wake-up event while in the D3cold power state. Otherwise, this requirement does not apply.</li>
</ul>
</dd>
<dd>
<p><b>WdfUseDefault</b> - The framework examines the <i>DDInstall</i><b>.HW</b> section of the driver's INF file. If the following lines are present, this value has the same meaning as <b>WdfFalse</b>:<pre class="syntax" xml:space="preserve"><code>Include = machine.inf
Needs = PciD3ColdSupported
</code></pre> Otherwise, this value has the same meaning as <b>WdfTrue</b>.</p>
</dd>
</dl>
<p>The <b>ExcludeD3Cold</b> member is available starting in KMDF version 1.11, as well as starting in version 2.0 of UMDF, and is ignored in operating systems earlier than Windows 8. See additional information in Remarks.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</b> structure is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a>. </p>

<p>The first time a driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a>, the following actions occur:</p>

<p>The framework stores the values of all <b>WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</b> structure members. </p>

<p>If the <b>UserControlOfIdleSettings</b> member is set to <b>IdleAllowUserControl</b> and if the <b>Enabled</b> member is set to <b>WdfUseDefault</b>, the framework reads the registry to find out if the user has enabled powering down the device when it is idle.</p>

<p>During subsequent calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a>, the framework only stores the values of the <b>DxState</b>, <b>IdleTimeout</b>, and <b>Enabled</b> members. Also, in KMDF 1.9 and earlier, the framework stores the value of the <b>IdleCaps</b> member <i>unless</i> the value is <b>IdleUsbSelectiveSuspend</b>. Therefore, the driver must use the following rules:</p>

<p>
<ul>
<li>
<p>If the driver specifies <b>IdleUsbSelectiveSuspend</b> for the <b>IdleCaps</b> member's value, it must do so the first time that it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a>, and it cannot subsequently change that value.</p>
</li>
<li>
<p>	If the driver specifies <b>IdleCanWakeFromS0</b> or <b>IdleCannotWakeFromS0</b> the first time it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a>, it can subsequently call <b>WdfDeviceAssignS0IdleSettings</b> again to change that value (but it cannot change the value to <b>IdleUsbSelectiveSuspend</b>).
</p>
</li>
</ul>
</p>

<p>If the driver specifies <b>IdleUsbSelectiveSuspend</b> for the <b>IdleCaps</b> member's value, it must do so the first time that it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a>, and it cannot subsequently change that value.</p>

<p>	If the driver specifies <b>IdleCanWakeFromS0</b> or <b>IdleCannotWakeFromS0</b> the first time it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a>, it can subsequently call <b>WdfDeviceAssignS0IdleSettings</b> again to change that value (but it cannot change the value to <b>IdleUsbSelectiveSuspend</b>).
</p>

<p>Starting in KMDF 1.11 and UMDF 2.0, a KMDF driver can switch between <b>IdleUsbSelectiveSuspend</b> and <b>IdleCannotWakeFromS0</b> at any time.</p>

<p>Starting in Windows 8, setting the <b>IdleTimeoutType</b> member to <b>SystemManagedIdleTimeout</b> or <b>SystemManagedIdleTimeoutWithHint</b> causes the framework to register with the power management framework (PoFx).</p>

<p>If the driver is implementing functional power state support for a multiple-component device, the driver must either set <b>IdleTimeoutType</b> to <b>DriverManagedIdleTimeout</b> or not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a> at all.</p>

<p> For more information, see <a href="wdf.supporting_functional_power_states">Supporting Functional Power States</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh406637">Overview of the Power Management Framework</a>.</p>

<p>The following rules apply to the value that you specify for the <b>DxState</b> member:</p>

<p>The value cannot be <b>PowerDeviceD0</b>.</p>

<p>For USB devices, the value cannot be <b>PowerDeviceD0</b> or <b>PowerDeviceD3</b>.</p>

<p>If you specify <b>PowerDeviceMaximum</b>, the framework uses the value that the driver for the device's bus supplied in the <b>DeviceWake</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551264">WDF_DEVICE_POWER_CAPABILITIES</a> structure.</p>

<p>If the value of the <b>IdleCaps</b> member is <b>IdleCanWakeFromS0</b>, you cannot specify a device power state that is lower than the device power state in the <b>DeviceWake</b> member of the bus driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551264">WDF_DEVICE_POWER_CAPABILITIES</a> structure. (In other words, if the bus driver's <b>DeviceWake</b> value is <b>PowerDeviceD2</b>, your function driver's <b>DxState</b> value cannot be <b>PowerDeviceD3</b>.)</p>

<p>In operating systems earlier than Windows 8, the D3 power state signifies that the device is in a low-power state, but that some power to the bus is still maintained. Starting in Windows 8, the former D3 power state is called D3hot, and a new power state (D3cold) is available. A device can enter the D3cold state either while the system is in its working (S0) state or in a low-power state.  When a device is in the D3cold  power state, the bus is inactive and the device must trigger its own wake signal when an external action (for example plugging in a network cable) causes a hardware event.</p>

<p>Starting in KMDF 1.11 and UMDF 2.0, a device that <a href="wdf.supporting_idle_power_down">supports idle power-down</a> can use the <b>ExcludeD3Cold</b> member of this structure to specify whether the D3cold power state should be an allowable choice for the low <a href="https://msdn.microsoft.com/2229f34c-9b88-4e3e-802e-f7be2c7ef168">device power state</a> that the device will enter after the idle timeout period ends.</p>

<p>For information about registry entries that control a device's idle capabilities, see <a href="wdf.user_control_of_device_idle_and_wake_behavior">User Control of Device Idle and Wake Behavior</a>. </p>

<p>To initialize its <b>WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</b> structure, your driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551271">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT</a>.</p>

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
</table>