---
UID: NF.wdfusb.WdfUsbInterfaceGetConfiguredPipe
title: WdfUsbInterfaceGetConfiguredPipe
author: windows-driver-content
description: The WdfUsbInterfaceGetConfiguredPipe method returns a handle to the framework pipe object that is associated with a specified USB device interface and pipe index. Optionally, the method also returns information about the pipe.
old-location: wdf\wdfusbinterfacegetconfiguredpipe.htm
old-project: wdf
ms.assetid: 0836a969-e484-485f-9b65-202c177b4f43
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfUsbInterfaceGetConfiguredPipe
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
req.alt-api: WdfUsbInterfaceGetConfiguredPipe
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbInterfaceGetConfiguredPipe function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbInterfaceGetConfiguredPipe</b> method returns a handle to the framework pipe object that is associated with a specified USB device interface and pipe index. Optionally, the method also returns information about the pipe.</p>


## -syntax

````
WDFUSBPIPE WdfUsbInterfaceGetConfiguredPipe(
  _In_      WDFUSBINTERFACE           UsbInterface,
  _In_      UCHAR                     PipeIndex,
  _Out_opt_ PWDF_USB_PIPE_INFORMATION PipeInfo
);
````


## -parameters
<dl>

### -param <i>UsbInterface</i> [in]

<dd>
<p>A handle to a USB interface object that was obtained by calling <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicegetinterface.md">WdfUsbTargetDeviceGetInterface</a>. </p>
</dd>

### -param <i>PipeIndex</i> [in]

<dd>
<p>A zero-based index into the set of framework pipe objects that are associated with the specified interface object.</p>
</dd>

### -param <i>PipeInfo</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfusb\ns-wdfusb--wdf-usb-pipe-information.md">WDF_USB_PIPE_INFORMATION</a> structure that the framework fills in. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, <b>WdfUsbInterfaceGetConfiguredPipe</b> returns a handle to the framework pipe object that is associated with the specified interface object and pipe index. The method returns <b>NULL</b> if the <a href="..\wdfusb\ns-wdfusb--wdf-usb-pipe-information.md">WDF_USB_PIPE_INFORMATION</a> structure's size is incorrect or if the pipe index value is too large.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Your driver can call <b>WdfUsbInterfaceGetConfiguredPipe</b> after it has called <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdeviceselectconfig.md">WdfUsbTargetDeviceSelectConfig</a>.</p>

<p>For more information about the <b>WdfUsbInterfaceGetConfiguredPipe</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example sends a USB abort request to each configured pipe of a specified USB interface.</p>

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
<a href="..\wdfusb\ns-wdfusb--wdf-usb-pipe-information.md">WDF_USB_PIPE_INFORMATION</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbInterfaceGetConfiguredPipe method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
