---
UID: NF.wdfdevice.WdfDeviceAssignS0IdleSettings
title: WdfDeviceAssignS0IdleSettings
author: windows-driver-content
description: The WdfDeviceAssignS0IdleSettings method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.
old-location: wdf\wdfdeviceassigns0idlesettings.htm
ms.assetid: 78bb5b51-b5b2-4177-8965-e54c04881dd3
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceAssignS0IdleSettings
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, FDOPowerPolicyOwnerAPI, KmdfIrql, KmdfIrql2, NonFDONotPowerPolicyOwnerAPI
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: WdfDeviceAssignS0IdleSettings
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceAssignS0IdleSettings function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceAssignS0IdleSettings</b> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.</p>


## -syntax

````
NTSTATUS WdfDeviceAssignS0IdleSettings(
  _In_ WDFDEVICE                              Device,
  _In_ PWDF_DEVICE_POWER_POLICY_IDLE_SETTINGS Settings
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>Settings</i> [in]

<dd>
<p>A pointer to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure. </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfDeviceAssignS0IdleSettings</b> returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The calling driver is not the device's power policy owner.
</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid <i>Settings</i> value is detected.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure is incorrect. </p><dl>
<dt><b>STATUS_POWER_STATE_INVALID</b></dt>
</dl><p>This value is returned if one of the following occurs:</p>

<p>Starting in KMDF version 1.11 running on Windows 8, the framework checks if the system's firmware can handle a wake signal while the system is in its fully on (S0) power state. If the machine fails this check, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545903">WdfDeviceAssignS0IdleSettings</a> returns <b>STATUS_POWER_STATE_INVALID</b>, and the device remains in its fully on (D0) power state as long as the system remains in S0.</p>

<p>In this case, the driver should not return an error status value from <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> or any other runtime callback.  At most, the driver might log an error indicating that the device will consume more power than it normally would.</p>

<p> </p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>If the driver sets the <b>IdleTimeoutType</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> to <b>SystemManagedIdleTimeout</b> or <b>SystemManagedIdleTimeoutWithHint</b>, it must call <b>WdfDeviceAssignS0IdleSettings</b> before returning from <a href="https://msdn.microsoft.com/0cfabb0f-2d5e-4445-8683-d2916de5b549">EvtDeviceD0Entry</a>. Typically, a driver first calls <b>WdfDeviceAssignS0IdleSettings</b> from <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>.</p>

<p> Additional calls to <b>WdfDeviceAssignS0IdleSettings</b> can be made at any time. However, after the driver  sets the value of the <b>IdleTimeoutType</b> member in its first call to <b>WdfDeviceAssignS0IdleSettings</b>, it must not change this value in later calls to this method.</p>

<p>If the driver registers for asynchronous notifications in <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> (for example by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559727">PoRegisterPowerSettingCallback</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549526">IoRegisterPlugPlayNotification</a>), the driver must not subsequently call <b>WdfDeviceAssignS0IdleSettings</b> from within the driver callback routine that it registered.</p>

<p>For more information, see <a href="wdf.supporting_idle_power_down">Supporting Idle Power-Down</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure, sets an idle time-out value of 10 seconds, and calls <b>WdfDeviceAssignS0IdleSettings</b>.</p>

<p>If the driver sets the <b>IdleTimeoutType</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> to <b>SystemManagedIdleTimeout</b> or <b>SystemManagedIdleTimeoutWithHint</b>, it must call <b>WdfDeviceAssignS0IdleSettings</b> before returning from <a href="https://msdn.microsoft.com/0cfabb0f-2d5e-4445-8683-d2916de5b549">EvtDeviceD0Entry</a>. Typically, a driver first calls <b>WdfDeviceAssignS0IdleSettings</b> from <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>.</p>

<p> Additional calls to <b>WdfDeviceAssignS0IdleSettings</b> can be made at any time. However, after the driver  sets the value of the <b>IdleTimeoutType</b> member in its first call to <b>WdfDeviceAssignS0IdleSettings</b>, it must not change this value in later calls to this method.</p>

<p>If the driver registers for asynchronous notifications in <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> (for example by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff559727">PoRegisterPowerSettingCallback</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549526">IoRegisterPlugPlayNotification</a>), the driver must not subsequently call <b>WdfDeviceAssignS0IdleSettings</b> from within the driver callback routine that it registered.</p>

<p>For more information, see <a href="wdf.supporting_idle_power_down">Supporting Idle Power-Down</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a> structure, sets an idle time-out value of 10 seconds, and calls <b>WdfDeviceAssignS0IdleSettings</b>.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546047">FDOPowerPolicyOwnerAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549345">NonFDONotPowerPolicyOwnerAPI</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545909">WdfDeviceAssignSxWakeSettings</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551270">WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceAssignS0IdleSettings method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
