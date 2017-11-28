---
UID: NF.wdfdevice.WdfDeviceInitSetReleaseHardwareOrderOnFailure
title: WdfDeviceInitSetReleaseHardwareOrderOnFailure
author: windows-driver-content
description: The WdfDeviceInitSetReleaseHardwareOrderOnFailure method specifies whether the framework calls the driver's EvtDeviceReleaseHardware callback function immediately after device failure, or waits until all child devices have been removed.
old-location: wdf\wdfdeviceinitsetreleasehardwareorderonfailure.htm
old-project: wdf
ms.assetid: 5DC3C7C8-E7D1-4874-AF8D-8E6FD48DF046
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDeviceInitSetReleaseHardwareOrderOnFailure
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfDeviceInitSetReleaseHardwareOrderOnFailure
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceInitSetReleaseHardwareOrderOnFailure function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>
   The <b>WdfDeviceInitSetReleaseHardwareOrderOnFailure</b> method specifies whether the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function immediately after device failure, or waits until all child devices have been removed.</p>


## -syntax

````
void WdfDeviceInitSetReleaseHardwareOrderOnFailure(
  _In_ PWDFDEVICE_INIT                       DeviceInit,
  _In_ WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE ReleaseHardwareOrderOnFailure
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a> structure.</p>
</dd>

### -param <i>ReleaseHardwareOrderOnFailure</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh706249">WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE</a>-typed enumerator that specifies when the framework calls the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks
<p>Typically, the framework calls a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function after it has called the <i>EvtDeviceReleaseHardware</i> function for all child devices that the driver enumerates.</p>

<p>In the event of a device power-up or power-down failure, however, the framework might call the  driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> before it has called the <i>EvtDeviceReleaseHardware</i> functions for all child devices.</p>

<p>To override this default behavior, a driver can call <b>WdfDeviceInitSetReleaseHardwareOrderOnFailure</b> to specify that, even in device failure scenarios, the framework should always wait to call its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> function until it has called the <i>EvtDeviceReleaseHardware</i> functions of the child devices.</p>

<p> For example, a bus driver that performs hardware access on behalf of its child devices could use this technique to ensure that its child devices do not request access to hardware after the framework has called the bus driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function.</p>

<p>If a driver calls <b>WdfDeviceInitSetReleaseHardwareOrderOnFailure</b>, it must do so before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example shows how a bus driver can request that the framework wait to call its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function until all of its child devices have been removed.</p>

<p>Typically, the framework calls a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function after it has called the <i>EvtDeviceReleaseHardware</i> function for all child devices that the driver enumerates.</p>

<p>In the event of a device power-up or power-down failure, however, the framework might call the  driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> before it has called the <i>EvtDeviceReleaseHardware</i> functions for all child devices.</p>

<p>To override this default behavior, a driver can call <b>WdfDeviceInitSetReleaseHardwareOrderOnFailure</b> to specify that, even in device failure scenarios, the framework should always wait to call its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> function until it has called the <i>EvtDeviceReleaseHardware</i> functions of the child devices.</p>

<p> For example, a bus driver that performs hardware access on behalf of its child devices could use this technique to ensure that its child devices do not request access to hardware after the framework has called the bus driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function.</p>

<p>If a driver calls <b>WdfDeviceInitSetReleaseHardwareOrderOnFailure</b>, it must do so before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>. For more information about calling <b>WdfDeviceCreate</b>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.</p>

<p>The following code example shows how a bus driver can request that the framework wait to call its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function until all of its child devices have been removed.</p>

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
<p>1.11</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546951">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh706249">WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetReleaseHardwareOrderOnFailure method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
