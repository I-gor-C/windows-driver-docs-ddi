---
UID: NF.ursdevice.UrsSetPoHandle
title: UrsSetPoHandle
author: windows-driver-content
description: Registers and deletes the client driver's registration with the power management framework (PoFx).
old-location: buses\urssetpohandle.htm
old-project: usbref
ms.assetid: 87B34452-DC2C-4FD4-B0F8-51EFAF2D4AA6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UrsSetPoHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ursdevice.h
req.include-header: Urscx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: UrsSetPoHandle
req.alt-loc: Urscxstub.lib,Urscxstub.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Urscxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# UrsSetPoHandle function



## -description
<p>Registers and deletes the client driver's registration with the power management framework (PoFx).</p>


## -syntax

````
FORCEINLINE void UrsSetPoHandle(
  _In_ WDFDEVICE Device,
  _In_ POHANDLE  PoHandle
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to the framework device object that the client driver retrieved in the previous call to <a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md">WdfDeviceCreate</a>.</p>
</dd>

### -param <i>PoHandle</i> [in]

<dd>
<p>A handle that represents the registration of the device with PoFx. The client driver receives this handle from WDF in  <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-post-po-fx-register-device.md">EvtDeviceWdmPostPoFxRegisterDevice</a>  and <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-pre-po-fx-unregister-device.md">EvtDeviceWdmPrePoFxUnregisterDevice</a> callback functions.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The client driver for the dual-role controller must be the power policy owner. The driver can receive notifications from the power management framework (PoFx). To do so, after calling <a href="buses.ursdeviceinitialize">UrsDeviceInitialize</a>, the driver must register PoFx callback functions. The client driver registers the device with the power framework directly or obtains a POHANDLE from WDF in <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-post-po-fx-register-device.md">EvtDeviceWdmPostPoFxRegisterDevice</a>. After registration is successful, the driver provides that handle to the USB dual-role class extension.</p>

<p>In the client driver's implementation of the <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-post-po-fx-register-device.md">EvtDeviceWdmPostPoFxRegisterDevice</a> callback function, the driver is expected to call <b>UrsSetPoHandle</b> by passing the received handle. On some platforms, the class extension might use the POHANDLE to power-manage the controller. Conversely, before the class extension deletes the registration with the power framework, it invokes the client driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-pre-po-fx-unregister-device.md">EvtDeviceWdmPrePoFxUnregisterDevice</a> implementation. The driver is expected to call  <b>UrsSetPoHandle</b> by passing NULL as the PoHandle value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ursdevice.h (include Urscx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Urscxstub.lib</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-post-po-fx-register-device.md">EvtDeviceWdmPostPoFxRegisterDevice</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-pre-po-fx-unregister-device.md">EvtDeviceWdmPrePoFxUnregisterDevice</a>
</dt>
<dt><i>EvtDeviceWdmPrePoFxUnregisterDevice</i></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20UrsSetPoHandle function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
