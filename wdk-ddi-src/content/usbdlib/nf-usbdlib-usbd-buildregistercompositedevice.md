---
UID: NF.usbdlib.USBD_BuildRegisterCompositeDevice
title: USBD_BuildRegisterCompositeDevice
author: windows-driver-content
description: The USBD_BuildRegisterCompositeDevice routine is called by the driver of a USB multi-function device (composite driver) to initialize a REGISTER_COMPOSITE_DEVICE structure with the information required for registering the driver with the USB driver stack.
old-location: buses\usbd_buildregistercompositedriver.htm
old-project: usbref
ms.assetid: 6683C688-CCDD-498B-AA60-81430DC3BCA4
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_BuildRegisterCompositeDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_BuildRegisterCompositeDevice
req.alt-loc: Usbdex.lib,Usbdex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbdex.lib
req.dll: 
req.irql: < = DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USBD_BuildRegisterCompositeDevice function



## -description
<p>The <b>USBD_BuildRegisterCompositeDevice</b> routine is called by the driver of a USB  multi-function device (composite driver) to  initialize a <a href="..\usbdlib\ns-usbdlib--register-composite-device.md">REGISTER_COMPOSITE_DEVICE</a> structure with the information required for registering the driver with the USB driver stack. </p>
<p>The routine is called by a driver that replaces the Microsoft-provided composite driver, Usbccgp.sys.</p>


## -syntax

````
void  USBD_BuildRegisterCompositeDevice(
  _In_  USBD_HANDLE                             USBDHandle,
  _In_  COMPOSITE_DEVICE_CAPABILITIES           CapabilityFlags,
  _In_  ULONG                                   FunctionCount,
  _Out_ bcount(Size) PREGISTER_COMPOSITE_DEVICE RegisterCompositeDevice
);
````


## -parameters
<dl>

### -param USBDHandle [in]

<dd>
<p>A USBD handle that is retrieved in a previous call to the <a href="..\usbdlib\nf-usbdlib-usbd-createhandle.md">USBD_CreateHandle</a> routine.</p>
</dd>

### -param CapabilityFlags [in]

<dd>
<p>A caller-allocated <a href="..\usbdlib\ns-usbdlib--composite-device-capabilities.md">COMPOSITE_DEVICE_CAPABILITIES</a> structure that indicates the capabilities that are supported by the composite driver. For instance, to   indicate that the composite driver supports function suspend, set the <b>CapabilityFunctionSuspend</b> member of <b>COMPOSITE_DEVICE_CAPABILITIES</b> to 1.</p>
</dd>

### -param FunctionCount [in]

<dd>
<p>The number of physical device objects (PDOs) to be created by the parent driver. The <i>FunctionCount</i> value cannot exceed 255.</p>
</dd>

### -param RegisterCompositeDevice [out]

<dd>
<p>A pointer to a caller-allocated <a href="..\usbdlib\ns-usbdlib--register-composite-device.md">REGISTER_COMPOSITE_DEVICE</a> structure. Upon completion, the structure is populated with the specified registration  information. To register the composite driver, send the <a href="..\usbioctl\ni-usbioctl-ioctl-internal-usb-register-composite-device.md">IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE</a> I/O request and pass the populated structure. </p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Usbdex.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt; = DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbdlib\ns-usbdlib--register-composite-device.md">REGISTER_COMPOSITE_DEVICE</a>
</dt>
<dt>
<a href="..\usbioctl\ni-usbioctl-ioctl-internal-usb-register-composite-device.md">IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_BuildRegisterCompositeDevice routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
