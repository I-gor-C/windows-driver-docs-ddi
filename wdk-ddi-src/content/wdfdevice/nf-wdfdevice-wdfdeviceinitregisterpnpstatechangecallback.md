---
UID: NF.wdfdevice.WdfDeviceInitRegisterPnpStateChangeCallback
title: WdfDeviceInitRegisterPnpStateChangeCallback
author: windows-driver-content
description: The WdfDeviceInitRegisterPnpStateChangeCallback method registers a driver-supplied event callback function that the framework calls when a device's Plug and Play state machine changes state.
old-location: wdf\wdfdeviceinitregisterpnpstatechangecallback.htm
old-project: wdf
ms.assetid: a14b790a-28d7-4fb8-823f-f37f05e7529f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceInitRegisterPnpStateChangeCallback
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
req.alt-api: WdfDeviceInitRegisterPnpStateChangeCallback
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: ChildDeviceInitAPI, DeviceInitAPI, DriverCreate, InitFreeDeviceCallback, InitFreeDeviceCreate, InitFreeNull, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI, PdoInitFreeDeviceCallback, PdoInitFreeDeviceCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceInitRegisterPnpStateChangeCallback function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDeviceInitRegisterPnpStateChangeCallback</b> method registers a driver-supplied event callback function that the framework calls when a device's Plug and Play state machine changes state.</p>


## -syntax

````
NTSTATUS WdfDeviceInitRegisterPnpStateChangeCallback(
  _In_ PWDFDEVICE_INIT                              DeviceInit,
  _In_ WDF_DEVICE_PNP_STATE                         PnpState,
  _In_ PFN_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION EvtDevicePnpStateChange,
  _In_ ULONG                                        CallbackTypes
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> [in]

<dd>
<p>A caller-supplied pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.</p>
</dd>

### -param <i>PnpState</i> [in]

<dd>
<p>A <a href="..\wdfdevice\ne-wdfdevice--wdf-device-pnp-state.md">WDF_DEVICE_PNP_STATE</a> enumerator that identifies the Plug and Play machine state for which the driver is requesting notification.</p>
</dd>

### -param <i>EvtDevicePnpStateChange</i> [in]

<dd>
<p>A caller-supplied pointer to the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-pnp-state-change-notification.md">EvtDevicePnpStateChange</a> event callback function.</p>
</dd>

### -param <i>CallbackTypes</i> [in]

<dd>
<p>An ORed combination of <a href="..\wdfdevice\ne-wdfdevice--wdf-state-notification-type.md">WDF_STATE_NOTIFICATION_TYPE</a>-typed enumerators.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfDeviceInitRegisterPnpStateChangeCallback</b> returns STATUS_SUCCESS. Additional return values include:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There is insufficient memory to complete the operation.</p>

<p> </p>

## -remarks
<p>If your driver calls <b>WdfDeviceInitRegisterPnpStateChangeCallback</b>, it must do so before it calls <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>.</p>

<p>For more information about <b>WdfDeviceInitRegisterPnpStateChangeCallback</b>, see <a href="wdf.state_machines_in_the_framework">State Machines in the Framework</a>.</p>

<p>The following code example registers an event callback function that the framework will call when the device's Plug and Play state machine changes state.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_initfreedevicecallback">InitFreeDeviceCallback</a>, <a href="devtest.kmdf_initfreedevicecreate">InitFreeDeviceCreate</a>, <a href="devtest.kmdf_initfreenull">InitFreeNull</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>, <a href="devtest.kmdf_pdoinitfreedevicecallback">PdoInitFreeDeviceCallback</a>, <a href="devtest.kmdf_pdoinitfreedevicecreate">PdoInitFreeDeviceCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a>
</dt>
<dt>
<a href="..\wdfdevice\ne-wdfdevice--wdf-device-pnp-state.md">WDF_DEVICE_PNP_STATE</a>
</dt>
<dt>
<a href="..\wdfdevice\ne-wdfdevice--wdf-state-notification-type.md">WDF_STATE_NOTIFICATION_TYPE</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-pnp-state-change-notification.md">EvtDevicePnpStateChange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitRegisterPnpStateChangeCallback method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
