---
UID: NF.wudfddi.IWDFDevice2.AssignSxWakeSettings
title: IWDFDevice2::AssignSxWakeSettings
author: windows-driver-content
description: The AssignSxWakeSettings method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.
old-location: wdf\iwdfdevice2_assignsxwakesettings.htm
ms.assetid: 32d3b680-298b-443e-a2c4-db8fc057bf75
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDevice2.AssignSxWakeSettings
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFDevice2, AssignSxWakeSettings, IWDFDevice2::AssignSxWakeSettings
req.iface: IWDFDevice2
req.product: Windows 10 or later.
---

# IWDFDevice2::AssignSxWakeSettings method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>AssignSxWakeSettings</b> method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.</p>


## -syntax

````
HRESULT AssignSxWakeSettings(
  [in] DEVICE_POWER_STATE                    DxState,
  [in] WDF_POWER_POLICY_SX_WAKE_USER_CONTROL UserControlOfWakeSettings,
  [in] WDF_TRI_STATE                         Enabled
);
````


## -parameters
<dl>

### -param <i>DxState</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff554628">DEVICE_POWER_STATE</a>-typed enumerator that identifies the low <a href="https://msdn.microsoft.com/2229f34c-9b88-4e3e-802e-f7be2c7ef168">device power state</a> that the device will enter when the system power state drops to a wakeable low-power state. The value of <i>DxState</i> cannot be <b>PowerDeviceD0</b>. DEVICE_POWER_STATE values are defined in wdm.h.</p>
</dd>

### -param <i>UserControlOfWakeSettings</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552436">WDF_POWER_POLICY_SX_WAKE_USER_CONTROL</a>-typed enumerator that indicates whether users have the ability to modify the device's wake settings.</p>
</dd>

### -param <i>Enabled</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed enumerator that indicates whether the device can wake the system (that is, restore the system to S0) when the system is in a low-power state. This member can have one of the following values:</p>
<dl>
<dd>
<p><b>WdfTrue</b> - Waking the system is enabled.</p>
</dd>
<dd>
<p><b>WdfFalse</b> - Waking the system is disabled.</p>
</dd>
<dd>
<p><b>WdfUseDefault</b> - Waking the system is initially enabled by default; but if the <b>UserControlOfWakeSettings</b> member is set to <b>WakeAllowUserControl</b>, the <a href="wdf.user_control_of_device_idle_and_wake_behavior">user's setting or driver's INF file</a> overrides the initial value.</p>
</dd>
</dl>
<p>If waking the system is enabled and the system is about to enter a low-power state, the framework calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556826">IPowerPolicyCallbackWakeFromSx::OnArmWakeFromSx</a> callback function before the device enters a low-power state.</p>
</dd>
</dl>

## -returns
<p><b>AssignSxWakeSettings</b> returns S_OK if the operation succeeds. Otherwise, the method might return one of the following values:</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The caller specified an invalid value for an input parameter.</p><dl>
<dt><b>HRESULT_FROM_NT(STATUS_INVALID_DEVICE_REQUEST)</b></dt>
</dl><p>The calling driver is not the device's <a href="wdf.power_policy_ownership_in_umdf">power policy owner</a>.</p><dl>
<dt><b>HRESULT_FROM_NT(STATUS_POWER_STATE_INVALID)</b></dt>
</dl><p>The <i>DxState</i> parameter specifies an invalid device power state, or the bus driver indicates that the device cannot trigger a wake signal,</p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.</p>

## -remarks
<p>The first time a driver calls <b>AssignSxWakeSettings</b>, the following actions occur:</p>

<p>The framework stores the parameter values. </p>

<p>If the <i>UserControlOfWakeSettings</i> parameter is set to <b>WakeAllowUserControl</b> and if the <i>Enabled</i> parameter is set to <b>WdfUseDefault</b>, the framework reads the registry to find out if the user has enabled waking the system. </p>

<p>During subsequent calls to <b>AssignSxWakeSettings</b>, the framework does not store the value of the <i>UserControlOfWakeSettings</i> parameter. In other words, the framework performs the following steps the first time the driver calls <b>AssignSxWakeSettings</b> but not during later calls:</p>

<p>Stores the value of the <i>UserControlOfWakeSettings</i> parameter.</p>

<p>Looks for a user setting in the registry, if the value of the <i>Enabled</i> parameter is <b>WdfUseDefault</b>.</p>

<p>The following rules apply to the value that you specify for the <i>DxState</i> parameter:</p>

<p>The value cannot be <b>PowerDeviceD0</b>. </p>

<p>If you specify <b>DevicePowerMaximum</b>, the framework uses the value that the kernel-mode driver for the device's bus supplied in the <b>DeviceWake</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551264">WDF_DEVICE_POWER_CAPABILITIES</a> structure.</p>

<p>You cannot specify a device power state that is lower than the device power state in the <b>DeviceWake</b> member of the kernel-mode bus driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551264">WDF_DEVICE_POWER_CAPABILITIES</a> structure. (In other words, if the bus driver's <b>DeviceWake</b> value is <b>PowerDeviceD2</b>, your function driver's <i>DxState</i> value cannot be <b>PowerDeviceD3</b>.) </p>

<p>For information about registry entries that control a device's wake capabilities, see <a href="wdf.user_control_of_device_idle_and_wake_behavior_in_umdf">User Control of Device Idle and Wake Behavior in UMDF</a>. </p>

<p>For more information about supporting a device's wake capabilities, see <a href="wdf.supporting_system_wake_up_in_umdf_drivers">Supporting System Wake-Up in UMDF-based Drivers</a>.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a> interface and then calls <b>AssignSxWakeSettings</b>.</p>

<p>The first time a driver calls <b>AssignSxWakeSettings</b>, the following actions occur:</p>

<p>The framework stores the parameter values. </p>

<p>If the <i>UserControlOfWakeSettings</i> parameter is set to <b>WakeAllowUserControl</b> and if the <i>Enabled</i> parameter is set to <b>WdfUseDefault</b>, the framework reads the registry to find out if the user has enabled waking the system. </p>

<p>During subsequent calls to <b>AssignSxWakeSettings</b>, the framework does not store the value of the <i>UserControlOfWakeSettings</i> parameter. In other words, the framework performs the following steps the first time the driver calls <b>AssignSxWakeSettings</b> but not during later calls:</p>

<p>Stores the value of the <i>UserControlOfWakeSettings</i> parameter.</p>

<p>Looks for a user setting in the registry, if the value of the <i>Enabled</i> parameter is <b>WdfUseDefault</b>.</p>

<p>The following rules apply to the value that you specify for the <i>DxState</i> parameter:</p>

<p>The value cannot be <b>PowerDeviceD0</b>. </p>

<p>If you specify <b>DevicePowerMaximum</b>, the framework uses the value that the kernel-mode driver for the device's bus supplied in the <b>DeviceWake</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff551264">WDF_DEVICE_POWER_CAPABILITIES</a> structure.</p>

<p>You cannot specify a device power state that is lower than the device power state in the <b>DeviceWake</b> member of the kernel-mode bus driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551264">WDF_DEVICE_POWER_CAPABILITIES</a> structure. (In other words, if the bus driver's <b>DeviceWake</b> value is <b>PowerDeviceD2</b>, your function driver's <i>DxState</i> value cannot be <b>PowerDeviceD3</b>.) </p>

<p>For information about registry entries that control a device's wake capabilities, see <a href="wdf.user_control_of_device_idle_and_wake_behavior_in_umdf">User Control of Device Idle and Wake Behavior in UMDF</a>. </p>

<p>For more information about supporting a device's wake capabilities, see <a href="wdf.supporting_system_wake_up_in_umdf_drivers">Supporting System Wake-Up in UMDF-based Drivers</a>.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a> interface and then calls <b>AssignSxWakeSettings</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556918">IWDFDevice2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556920">IWDFDevice2::AssignS0IdleSettings</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice2::AssignSxWakeSettings method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
