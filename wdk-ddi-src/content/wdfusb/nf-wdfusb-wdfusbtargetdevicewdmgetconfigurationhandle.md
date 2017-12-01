---
UID: NF.wdfusb.WdfUsbTargetDeviceWdmGetConfigurationHandle
title: WdfUsbTargetDeviceWdmGetConfigurationHandle
author: windows-driver-content
description: The WdfUsbTargetDeviceWdmGetConfigurationHandle method returns the USBD_CONFIGURATION_HANDLE-typed handle that is associated with the current configuration of a specified USB device.
old-location: wdf\wdfusbtargetdevicewdmgetconfigurationhandle.htm
old-project: wdf
ms.assetid: 7f501e5c-13dd-418d-9b9f-f984aed45cc0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfUsbTargetDeviceWdmGetConfigurationHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfUsbTargetDeviceWdmGetConfigurationHandle
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceWdmGetConfigurationHandle function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfUsbTargetDeviceWdmGetConfigurationHandle</b> method returns the USBD_CONFIGURATION_HANDLE-typed handle that is associated with the current configuration of a specified USB device.</p>


## -syntax

````
USBD_CONFIGURATION_HANDLE WdfUsbTargetDeviceWdmGetConfigurationHandle(
  _In_ WDFUSBDEVICE UsbDevice
);
````


## -parameters
<dl>

### -param <i>UsbDevice</i> [in]

<dd>
<p>A handle to a USB device object that was obtained from a previous call to <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreatewithparameters.md">WdfUsbTargetDeviceCreateWithParameters</a>.</p>
</dd>
</dl>

## -returns
<p>If the driver has selected a configuration for the device, <b>WdfUsbTargetDeviceWdmGetConfigurationHandle</b> returns the device's USBD_CONFIGURATION_HANDLE-typed handle. Otherwise, the method returns <b>NULL</b>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>A framework-based driver needs to obtain a USBD_CONFIGURATION_HANDLE-typed handle only if it creates a <a href="..\usb\ns-usb--urb.md">URB</a> that contains a <a href="buses._urb_select_interface">_URB_SELECT_INTERFACE</a> structure.</p>

<p>The driver can call <b>WdfUsbTargetDeviceWdmGetConfigurationHandle</b> after it has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceselectconfig.md">WdfUsbTargetDeviceSelectConfig</a>. The USBD_CONFIGURATION_HANDLE-typed handle that <b>WdfUsbTargetDeviceWdmGetConfigurationHandle</b> returns is valid until the driver calls <b>WdfUsbTargetDeviceSelectConfig</b> again or the USB device object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md">EvtCleanupCallback</a> function for the USB device object, and if the object is deleted before the driver calls <b>WdfUsbTargetDeviceSelectConfig</b> again, the handle is valid until the object's <i>EvtCleanupCallback</i> function returns.</p>

<p>For more information about the <b>WdfUsbTargetDeviceWdmGetConfigurationHandle</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example obtains a handle to the current configuration of a specified USB device.</p>

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
<dt>Wdfusb.h (include Wdfusb.h)</dt>
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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_usbkmdfirql">UsbKmdfIrql</a>, <a href="devtest.kmdf_usbkmdfirql2">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._urb_select_interface">_URB_SELECT_INTERFACE</a>
</dt>
<dt>
<a href="..\usb\ns-usb--urb.md">URB</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceselectconfig.md">WdfUsbTargetDeviceSelectConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceWdmGetConfigurationHandle method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
