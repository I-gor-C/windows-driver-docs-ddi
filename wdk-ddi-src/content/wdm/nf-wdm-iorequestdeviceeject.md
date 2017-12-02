---
UID: NF.wdm.IoRequestDeviceEject
title: IoRequestDeviceEject
author: windows-driver-content
description: The IoRequestDeviceEject routine notifies the PnP manager that the device eject button was pressed.
old-location: kernel\iorequestdeviceeject.htm
old-project: kernel
ms.assetid: ceaa6793-43ba-4998-827e-8a2c7c892e50
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoRequestDeviceEject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRequestDeviceEject
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# IoRequestDeviceEject function



## -description
<p>The <b>IoRequestDeviceEject</b> routine notifies the PnP manager that the device eject button was pressed. </p>


## -syntax

````
VOID IoRequestDeviceEject(
  _In_ PDEVICE_OBJECT PhysicalDeviceObject
);
````


## -parameters
<dl>

### -param PhysicalDeviceObject [in]

<dd>
<p>Pointer to the PDO for the device. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Note that this routine reports a request for device eject, not media eject.</p>

<p>Typically, a PnP bus driver calls <b>IoRequestDeviceEject</b> to notify the PnP manager that a user pressed the device eject button on one of its child devices. </p>

<p>A driver calls this routine, rather than sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550853">IRP_MN_EJECT</a> request, because this routine allows the PnP manager to coordinate additional actions for the eject besides sending the IRP. For example, the PnP manager notifies user-mode and kernel-mode components that registered for notification of changes on the device. </p>

<p>The PnP manager directs an orderly shutdown of the device. The PnP manager:</p>

<p>Creates a list of other devices that are affected by this device being ejected.</p>

<p>The PnP manager queries for the device's removal relations, ejection relations, and bus relations (child devices). </p>

<p>Determines whether the device and its related devices can be software-removed.</p>

<p>The PnP manager sends <a href="https://msdn.microsoft.com/library/windows/hardware/ff551705">IRP_MN_QUERY_REMOVE_DEVICE</a> IRPs to the drivers for the device and its related devices. The PnP manager also sends notifications to any user-mode and kernel-mode components that registered for device-change notification on the device or any of its related devices. If any of the drivers or user-mode components fail the query-remove, the PnP manager pops up a dialog box to notify the user that the eject failed.</p>

<p>Software-removes the device and its related devices.</p>

<p>If the previous steps are successful, the PnP manager notifies registered drivers and applications that the device and its related devices are being software-removed. Then the PnP manager sends <a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a> IRPs to the drivers for the device and its related devices. Function and filter drivers detach from the device stack and delete their device objects for the device(s). The bus drivers retain the PDO(s) for the device(s), unless a device is physically gone and the bus driver omitted the device in its most recent response to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a>/<b>BusRelations</b> for the device's parent bus.</p>

<p>Directs the bus driver to eject the device (if possible).</p>

<p>The PnP manager takes different steps, depending on the eject capabilities of the device:</p>

<p>Hot eject is supported.</p>

<p>If the <b>EjectSupported</b> capability is set for the device, the device can be ejected when the system is running (is in the <b>PowerSystemWorking</b> state). The PnP manager sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550853">IRP_MN_EJECT</a> request to the bus driver for the device. Any function and filter drivers detached previously from the stack in response to the remove IRP, so the bus driver handles the eject IRP. When the bus driver completes the IRP, the PnP manager expects the device to be physically absent from the system.</p>

<p>Hot eject is <u>not</u> supported.</p>

<p>In this case, the device is <b>Removable</b> but does not support eject. The PnP manager marks the device as not-present/not-working-properly. The PnP manager will not restart the device until a user physically removes it and reinserts it. In this case, the PnP manager does not send an <b>IRP_MN_EJECT</b>.</p>

<p>A device's parent bus driver sets the capabilities for a device, including its eject capabilities, in response to an <a href="kernel.irp_mn_query_capabilities">IRP_MN_QUERY_CAPABILITIES</a> request. A function or filter driver can optionally specify capabilities.</p>

<p>When a device is ejected, its child devices are physically removed from the system along with it.</p>

<p>A user-mode application can initiate a device eject. In that case, no driver calls this routine but the operating system calls the PnP manager to initiate the steps listed above.</p>

<p>Callers of <b>IoRequestDeviceEject</b> must be running at IRQL &lt;= DISPATCH_LEVEL. The PnP manager performs most of its device-eject tasks listed above at IRQL = PASSIVE_LEVEL. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550853">IRP_MN_EJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551705">IRP_MN_QUERY_REMOVE_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551670">IRP_MN_QUERY_DEVICE_RELATIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551738">IRP_MN_REMOVE_DEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRequestDeviceEject routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
