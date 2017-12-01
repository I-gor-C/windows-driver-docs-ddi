---
UID: NF.wdfusb.WdfUsbInterfaceSelectSetting
title: WdfUsbInterfaceSelectSetting
author: windows-driver-content
description: The WdfUsbInterfaceSelectSetting method selects a specified alternate setting for a specified USB interface.
old-location: wdf\wdfusbinterfaceselectsetting.htm
old-project: wdf
ms.assetid: 398b7649-152e-4fed-b633-16627dadf0f8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfUsbInterfaceSelectSetting
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfUsbInterfaceSelectSetting
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, UsbKmdfIrql, UsbKmdfIrql2
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

# WdfUsbInterfaceSelectSetting function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbInterfaceSelectSetting</b> method selects a specified alternate setting for a specified USB interface.</p>


## -syntax

````
NTSTATUS WdfUsbInterfaceSelectSetting(
  _In_     WDFUSBINTERFACE                          UsbInterface,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES                   PipesAttributes,
  _In_     PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS Params
);
````


## -parameters
<dl>

### -param <i>UsbInterface</i> [in]

<dd>
<p>A handle to a USB interface object that was obtained by calling <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicegetinterface.md">WdfUsbTargetDeviceGetInterface</a>. </p>
</dd>

### -param <i>PipesAttributes</i> [in, optional]

<dd>
<p>A pointer to a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that specifies object attributes for pipe objects that the framework creates for the interface. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>Params</i> [in]

<dd>
<p>A pointer to a caller-supplied <a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a> structure that contains interface selection parameters.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbInterfaceSelectSetting</b> returns the I/O target's completion status value if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There was insufficient memory to create a new pipe object.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfUsbInterfaceSelectSetting</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>After your driver calls <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceselectconfig.md">WdfUsbTargetDeviceSelectConfig</a> to select a configuration, the driver can call <b>WdfUsbInterfaceSelectSetting</b> to select an alternate setting for one of the device's interfaces.</p>

<p>Your driver can select an interface's alternate setting by specifying a USB interface descriptor or a <a href="..\usb\ns-usb--urb.md">URB</a>, or by just providing an alternate setting for the interface. In all cases, the driver must provide a handle to an interface object. </p>

<p>If your driver just provides an alternate setting, the framework uses the interface object to determine the interface to which the setting belongs. </p>

<p>If your driver specifies an interface descriptor or a URB, the framework uses the interface that is specified in the descriptor or URB.</p>

<p>The framework creates a framework USB pipe object for each pipe that is associated with the interface, after deleting any pipe objects that the framework might have previously created for the interface. To obtain information about an interface's pipe objects, your driver can call <a href="..\wdfusb\nf-wdfusb-wdfusbinterfacegetnumconfiguredpipes.md">WdfUsbInterfaceGetNumConfiguredPipes</a> and <a href="..\wdfusb\nf-wdfusb-wdfusbinterfacegetconfiguredpipe.md">WdfUsbInterfaceGetConfiguredPipe</a>.</p>

<p>For more information about the <b>WdfUsbInterfaceSelectSetting</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example initializes a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure with attributes for the pipe objects that the framework will create. Then, the example initializes a <a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a> structure to specify alternate setting 1. Finally, the example calls <b>WdfUsbInterfaceSelectSetting</b> to select the alternate setting and create pipe objects for the interface's pipes.</p>

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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_usbkmdfirql">UsbKmdfIrql</a>, <a href="devtest.kmdf_usbkmdfirql2">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdfobject\nf-wdfobject-wdf-object-attributes-init.md">WDF_OBJECT_ATTRIBUTES_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552405">WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE</a>
</dt>
<dt>
<a href="..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-setting.md">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbinterfacegetconfiguredpipe.md">WdfUsbInterfaceGetConfiguredPipe</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbinterfacegetnumconfiguredpipes.md">WdfUsbInterfaceGetNumConfiguredPipes</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicegetinterface.md">WdfUsbTargetDeviceGetInterface</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceselectconfig.md">WdfUsbTargetDeviceSelectConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbInterfaceSelectSetting method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
