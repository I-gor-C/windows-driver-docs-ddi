---
UID: NF.wdfdevice.WdfDeviceWdmAssignPowerFrameworkSettings
title: WdfDeviceWdmAssignPowerFrameworkSettings
author: windows-driver-content
description: The WdfDeviceWdmAssignPowerFrameworkSettings method registers power management framework (PoFx) settings for single-component devices.
old-location: wdf\wdfdevicewdmassignpowerframeworksettings.htm
ms.assetid: 676A458E-A6E0-4F09-AAF2-21EA122EF74D
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfDeviceWdmAssignPowerFrameworkSettings
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfDeviceWdmAssignPowerFrameworkSettings
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceWdmAssignPowerFrameworkSettings function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> method registers  power management framework (PoFx) settings for single-component devices.</p>


## -syntax

````
NTSTATUS WdfDeviceWdmAssignPowerFrameworkSettings(
  _In_ WDFDEVICE                      Device,
  _In_ PWDF_POWER_FRAMEWORK_SETTINGS PowerFrameworkSettings
);
````


## -parameters
<dl>

### -param <i> Device</i> [in]

<dd>
<p>A handle to the framework device object for which PoFx settings are being specified.</p>
</dd>

### -param <i>PowerFrameworkSettings</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406489">WDF_POWER_FRAMEWORK_SETTINGS</a> structure that describes the client driver’s PoFx settings.</p>
</dd>
</dl>

## -returns
<p>The <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> method returns an NTSTATUS value that indicates success or failure of the operation.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551277">WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS</a> structure is incorrect. </p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The calling driver is not the device's power policy owner.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid <i>Settings</i> value is detected.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>The <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> method applies only to single-component devices.</p>

<p>After calling this method, the client driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a> and set the <b>IdleTimeoutType</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure to <b>SystemManagedIdleTimeout</b> or <b>SystemManagedIdleTimeoutWithHint</b>.</p>

<p>A driver must call <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> before or during the first time a device starts. Because a device can start more than once, for example if resource rebalancing occurs, a driver might call this method from within <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>  or  <a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a>. The framework calls these functions only once, even if the device is started more than once.</p>

<p>Alternatively, the driver could keep track of whether it has already called <b>WdfDeviceWdmAssignPowerFrameworkSettings</b>, and call it from one of the following callback functions: <a href="https://msdn.microsoft.com/a3d4a983-8a75-44be-bd72-8673d89f9f87">EvtDevicePrepareHardware</a>, <a href="https://msdn.microsoft.com/0cfabb0f-2d5e-4445-8683-d2916de5b549">EvtDeviceD0Entry</a>, <a href="https://msdn.microsoft.com/38d74ce1-9d9d-4da5-a2b3-579048850b28">EvtDeviceD0EntryPostInterruptsEnabled</a>, or <a href="https://msdn.microsoft.com/13d7fbc6-6f93-4ef9-abd4-f2adc4e8e23a">EvtDeviceSelfManagedIoRestart</a>.</p>

<p>If your driver calls <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> more than once, the framework generates a verifier error.</p>

<p>The power management framework (PoFx) is available only on Windows 8 and later. When running on an operating system that does not support PoFx, <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> takes no action and returns STATUS_SUCCESS.</p>

<p>For more information, see <a href="wdf.supporting_functional_power_states">Supporting Functional Power States</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh406637">Overview of the Power Management Framework</a>.</p>

<p>In the following code example, the driver initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406489">WDF_POWER_FRAMEWORK_SETTINGS</a> structure by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406492">WDF_POWER_FRAMEWORK_SETTINGS_INIT</a>  function. The driver then manually sets some of the members of the structure, and then calls <b>WdfDeviceWdmAssignPowerFrameworkSettings</b>.</p>

<p>The <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> method applies only to single-component devices.</p>

<p>After calling this method, the client driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a> and set the <b>IdleTimeoutType</b> field of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure to <b>SystemManagedIdleTimeout</b> or <b>SystemManagedIdleTimeoutWithHint</b>.</p>

<p>A driver must call <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> before or during the first time a device starts. Because a device can start more than once, for example if resource rebalancing occurs, a driver might call this method from within <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>  or  <a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a>. The framework calls these functions only once, even if the device is started more than once.</p>

<p>Alternatively, the driver could keep track of whether it has already called <b>WdfDeviceWdmAssignPowerFrameworkSettings</b>, and call it from one of the following callback functions: <a href="https://msdn.microsoft.com/a3d4a983-8a75-44be-bd72-8673d89f9f87">EvtDevicePrepareHardware</a>, <a href="https://msdn.microsoft.com/0cfabb0f-2d5e-4445-8683-d2916de5b549">EvtDeviceD0Entry</a>, <a href="https://msdn.microsoft.com/38d74ce1-9d9d-4da5-a2b3-579048850b28">EvtDeviceD0EntryPostInterruptsEnabled</a>, or <a href="https://msdn.microsoft.com/13d7fbc6-6f93-4ef9-abd4-f2adc4e8e23a">EvtDeviceSelfManagedIoRestart</a>.</p>

<p>If your driver calls <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> more than once, the framework generates a verifier error.</p>

<p>The power management framework (PoFx) is available only on Windows 8 and later. When running on an operating system that does not support PoFx, <b>WdfDeviceWdmAssignPowerFrameworkSettings</b> takes no action and returns STATUS_SUCCESS.</p>

<p>For more information, see <a href="wdf.supporting_functional_power_states">Supporting Functional Power States</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh406637">Overview of the Power Management Framework</a>.</p>

<p>In the following code example, the driver initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406489">WDF_POWER_FRAMEWORK_SETTINGS</a> structure by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406492">WDF_POWER_FRAMEWORK_SETTINGS_INIT</a>  function. The driver then manually sets some of the members of the structure, and then calls <b>WdfDeviceWdmAssignPowerFrameworkSettings</b>.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406489">WDF_POWER_FRAMEWORK_SETTINGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406492">WDF_POWER_FRAMEWORK_SETTINGS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4CE227F5-9ED4-4484-AFBF-44D1260EB99D">EvtDeviceWdmPostPoFxRegisterDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/D663C47D-C59E-4210-84D8-9773A3003990">EvtDeviceWdmPrePoFxUnregisterDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceWdmAssignPowerFrameworkSettings method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
