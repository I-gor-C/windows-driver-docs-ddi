---
UID: NF.wdfdevice.WdfDeviceGetDevicePowerState
title: WdfDeviceGetDevicePowerState
author: windows-driver-content
description: The WdfDeviceGetDevicePowerState method returns the current state of the framework's power state machine, for a specified device.
old-location: wdf\wdfdevicegetdevicepowerstate.htm
old-project: wdf
ms.assetid: 7405e0c7-9263-4911-9b1e-52cffa559af3
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceGetDevicePowerState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDeviceGetDevicePowerState
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceGetDevicePowerState function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceGetDevicePowerState</b> method returns the current state of the framework's power state machine, for a specified device.</p>


## -syntax

````
WDF_DEVICE_POWER_STATE WdfDeviceGetDevicePowerState(
  _In_ WDFDEVICE Device
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>
</dl>

## -returns
<p><b>WdfDeviceGetDevicePowerState</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551280">WDF_DEVICE_POWER_STATE</a>-typed enumerator that identifies the current state of the framework's power state machine for the specified device. </p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Most drivers do not need to be aware of the state of the framework's power state machine. For more information about the framework's state machines, see <a href="wdf.state_machines_in_the_framework">State Machines in the Framework</a>.</p>

<p>The <b>WdfDeviceGetDevicePowerState</b> method returns a meaningful value only if it is called from within the following callback functions:</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry-post-interrupts-enabled.md">EvtDeviceD0EntryPostInterruptsEnabled</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit-pre-interrupts-disabled.md">EvtDeviceD0ExitPreInterruptsDisabled</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-init.md">EvtDeviceSelfManagedIoInit</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-suspend.md">EvtDeviceSelfManagedIoSuspend</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-restart.md">EvtDeviceSelfManagedIoRestart</a>
</p>

<p>The following code example obtains the current state of the framework's power state machine for a specified device.</p>

<p>Most drivers do not need to be aware of the state of the framework's power state machine. For more information about the framework's state machines, see <a href="wdf.state_machines_in_the_framework">State Machines in the Framework</a>.</p>

<p>The <b>WdfDeviceGetDevicePowerState</b> method returns a meaningful value only if it is called from within the following callback functions:</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md">EvtDeviceD0Entry</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry-post-interrupts-enabled.md">EvtDeviceD0EntryPostInterruptsEnabled</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md">EvtDeviceD0Exit</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit-pre-interrupts-disabled.md">EvtDeviceD0ExitPreInterruptsDisabled</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-init.md">EvtDeviceSelfManagedIoInit</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-suspend.md">EvtDeviceSelfManagedIoSuspend</a>
</p>

<p>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-restart.md">EvtDeviceSelfManagedIoRestart</a>
</p>

<p>The following code example obtains the current state of the framework's power state machine for a specified device.</p>

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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545969">WdfDeviceGetDevicePnpState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545974">WdfDeviceGetDevicePowerPolicyState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546966">WdfDevStateNormalize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceGetDevicePowerState method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
