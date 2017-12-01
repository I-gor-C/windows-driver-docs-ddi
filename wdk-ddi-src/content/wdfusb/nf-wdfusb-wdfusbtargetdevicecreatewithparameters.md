---
UID: NF.wdfusb.WdfUsbTargetDeviceCreateWithParameters
title: WdfUsbTargetDeviceCreateWithParameters
author: windows-driver-content
description: The WdfUsbTargetDeviceCreateWithParameters method creates a framework USB device object for a specified framework device object and opens the USB device for I/O operations.
old-location: wdf\wdfusbtargetdevicecreatewithparameters.htm
old-project: wdf
ms.assetid: E93A944E-81D5-4059-ADA6-2760A091C30B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfUsbTargetDeviceCreateWithParameters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: WdfUsbTargetDeviceCreateWithParameters
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, RequestForUrbXrb, UsbDeviceCreate, UsbDeviceCreateFail, UsbDeviceCreateTarget
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceCreateWithParameters function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>
   
  The <b>WdfUsbTargetDeviceCreateWithParameters</b>  method creates a framework USB device object for a specified framework device object and opens the USB device for I/O operations.
The method also specifies configuration information for the framework USB device object.</p>


## -syntax

````
NTSTATUS WdfUsbTargetDeviceCreateWithParameters(
  _In_     WDFDEVICE                     Device,
  _In_     PWDF_USB_DEVICE_CREATE_CONFIG Config,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES        Attributes,
  _Out_    WDFUSBDEVICE                  *UsbDevice
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>Config</i> [in]

<dd>
<p>A pointer to a <a href="..\wdfusb\ns-wdfusb--wdf-usb-device-create-config.md">WDF_USB_DEVICE_CREATE_CONFIG</a> structure that contains configuration information for the framework USB device object.</p>
</dd>

### -param <i>Attributes</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that contains attributes for the new framework USB device object. (The structure's <b>ParentObject</b> member must be NULL.) This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>UsbDevice</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the new framework USB device object.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetDeviceCreateWithParameters</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The <i>Config</i> parameter is not the correct size.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There was insufficient memory to create a new framework USB device object.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.  See the Remarks section for more information.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>An attempt to get USB configuration information failed.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfUsbTargetDeviceCreateWithParameters</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Windows 8 includes a new USB driver stack to support USB 3.0 devices.</p>

<p>Before a framework-based client driver can use the new capabilities of the USB driver stack for Windows 8, the driver must register itself with the underlying USB driver stack that is loaded by Windows for the device. To register the client driver, call <b>WdfUsbTargetDeviceCreateWithParameters</b> and specify a contract version in the <a href="..\wdfusb\ns-wdfusb--wdf-usb-device-create-config.md">WDF_USB_DEVICE_CREATE_CONFIG</a> structure.</p>

<p> If the client driver is intended to build, run, and use the improvements and the new capabilities on Windows 8, the client contract version is USBD_CLIENT_CONTRACT_VERSION_602.</p>

<p>Typically, drivers call <b>WdfUsbTargetDeviceCreateWithParameters</b> from within an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function. Drivers can also call <b>WdfUsbTargetDeviceCreateWithParameters</b> from within an <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback function.</p>

<p>For information about how WDM USB client drivers interact with the USB 3.0 driver stack, see  <a href="buses.usb_client_driver_contract_in_windows_8">Best Practices: Using URBs</a>.</p>

<p>If the driver calls <b>WdfUsbTargetDeviceCreateWithParameters</b> to create a framework USB device object, the driver must create URBs only by calling <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreateurb.md">WdfUsbTargetDeviceCreateUrb</a> or <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreateisochurb.md">WdfUsbTargetDeviceCreateIsochUrb</a>.</p>

<p>If you call this method from a UMDF driver, you must specify the <b>UmdfDispatcher</b> directive in the driver's INF file.  Otherwise, this method may return <b>STATUS_INVALID_PARAMETER</b>.   For more information about this directive, see <a href="https://docs.microsoft.com/windows-hardware/drivers/wdf/specifying-wdf-directives-in-inf-files">Specifying WDF Directives in INF Files</a>.</p>

<p>The following code example is part of an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> callback function that calls <b>WdfUsbTargetDeviceCreateWithParameters</b>. The example stores the handle to the framework USB device object in driver-defined context space. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_requestforurbxrb">RequestForUrbXrb</a>, <a href="devtest.kmdf_usbdevicecreate">UsbDeviceCreate</a>, <a href="devtest.kmdf_usbdevicecreatefail">UsbDeviceCreateFail</a>, <a href="devtest.kmdf_usbdevicecreatetarget">UsbDeviceCreateTarget</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbdlib\nf-usbdlib-usbd-createhandle.md">USBD_CreateHandle</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreate.md">WdfUsbTargetDeviceCreate</a>
</dt>
<dt>
<a href="..\wdfusb\ns-wdfusb--wdf-usb-device-create-config.md">WDF_USB_DEVICE_CREATE_CONFIG</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-device-create-config-init.md">WDF_USB_DEVICE_CREATE_CONFIG_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceCreateWithParameters method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
