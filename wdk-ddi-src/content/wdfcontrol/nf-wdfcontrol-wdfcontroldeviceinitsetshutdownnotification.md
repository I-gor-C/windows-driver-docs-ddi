---
UID: NF.wdfcontrol.WdfControlDeviceInitSetShutdownNotification
title: WdfControlDeviceInitSetShutdownNotification function
author: windows-driver-content
description: The WdfControlDeviceInitSetShutdownNotification method sets shutdown notification information for a control device object.
old-location: wdf\wdfcontroldeviceinitsetshutdownnotification.htm
old-project: wdf
ms.assetid: 43a5a017-f5de-4906-acbb-96419b4a3f1c
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfControlDeviceInitSetShutdownNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcontrol.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfControlDeviceInitSetShutdownNotification
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ControlDeviceInitAPI, DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfControlDeviceInitSetShutdownNotification function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfControlDeviceInitSetShutdownNotification</b> method sets shutdown notification information for a control device object.



## -syntax

````
VOID WdfControlDeviceInitSetShutdownNotification(
  _In_ PWDFDEVICE_INIT                      DeviceInit,
  _In_ PFN_WDF_DEVICE_SHUTDOWN_NOTIFICATION Notification,
  _In_ UCHAR                                Flags
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure that the driver obtained by calling <a href="wdf.wdfcontroldeviceinitallocate">WdfControlDeviceInitAllocate</a>.


### -param Notification [in]

A pointer to the driver's <a href="wdf.evtdeviceshutdownnotification">EvtDeviceShutdownNotification</a> event callback function.


### -param Flags [in]

One or more <a href="wdf.wdf_device_shutdown_flags">WDF_DEVICE_SHUTDOWN_FLAGS</a>-typed flags that indicate when the <a href="wdf.evtdeviceshutdownnotification">EvtDeviceShutdownNotification</a> callback function will be called.


## -returns
None


## -remarks
The driver must call <b>WdfControlDeviceInitSetShutdownNotification</b> before calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>. For more information about calling <b>WdfControlDeviceInitSetShutdownNotification</b>, see <a href="wdf.using_control_device_objects">Using Control Device Objects</a>.

For a code example that uses <b>WdfControlDeviceInitSetShutdownNotification</b>, see <a href="wdf.wdfcontroldeviceinitallocate">WdfControlDeviceInitAllocate</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfcontrol.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_controldeviceinitapi">ControlDeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtdeviceshutdownnotification">EvtDeviceShutdownNotification</a>
</dt>
<dt>
<a href="wdf.wdf_device_shutdown_flags">WDF_DEVICE_SHUTDOWN_FLAGS</a>
</dt>
<dt>
<a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfControlDeviceInitSetShutdownNotification method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

