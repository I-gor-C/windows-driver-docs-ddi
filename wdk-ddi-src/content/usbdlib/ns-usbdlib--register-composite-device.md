---
UID: NS.usbdlib._REGISTER_COMPOSITE_DEVICE
title: REGISTER_COMPOSITE_DEVICE
author: windows-driver-content
description: The REGISTER_COMPOSITE_DEVICE structure is used with the IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE I/O control request to register a parent driver of a Universal Serial Bus (USB) multi-function device (composite driver) with the USB driver stack.
old-location: buses\register_composite_driver.htm
old-project: usbref
ms.assetid: BBE92635-5230-454E-A6CA-80198B5B2C57
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: REGISTER_COMPOSITE_DEVICE, REGISTER_COMPOSITE_DEVICE, *PREGISTER_COMPOSITE_DEVICE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbdlib.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REGISTER_COMPOSITE_DEVICE
req.alt-loc: usbdlib.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# REGISTER_COMPOSITE_DEVICE structure



## -description
<p>The <b>REGISTER_COMPOSITE_DEVICE</b> structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450854">IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE</a> I/O control request to register a  parent driver of a Universal Serial Bus (USB) multi-function device (composite driver)  with the USB driver stack. </p>
<p>To initialize the <b>REGISTER_COMPOSITE_DEVICE</b> structure, the composite driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406229">USBD_BuildRegisterCompositeDevice</a> routine.</p>


## -syntax

````
typedef struct _REGISTER_COMPOSITE_DEVICE {
  USHORT                        Version;
  USHORT                        Size;
  USBDI_HANDLE                  Reserved;
  COMPOSITE_DEVICE_CAPABILITIES CapabilityFlags;
  ULONG                         FunctionCount;
} REGISTER_COMPOSITE_DEVICE, *PREGISTER_COMPOSITE_DEVICE;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. <a href="https://msdn.microsoft.com/library/windows/hardware/hh406229">USBD_BuildRegisterCompositeDevice</a> sets this  member.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure. <a href="https://msdn.microsoft.com/library/windows/hardware/hh406229">USBD_BuildRegisterCompositeDevice</a> sets this  member.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. <a href="https://msdn.microsoft.com/library/windows/hardware/hh406229">USBD_BuildRegisterCompositeDevice</a> sets this  member.</p>
</dd>

### -field <b>CapabilityFlags</b>

<dd>
<p>The capabilities that are supported by the composite driver.
To specify that function suspend is supported by the composite driver, first initialize the <a href="..\usbdlib\ns-usbdlib--composite-device-capabilities.md">COMPOSITE_DEVICE_CAPABILITIES</a> structure by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450803">COMPOSITE_DEVICE_CAPABILITIES_INIT</a> macro. Then, set the <b>CompositeDeviceCapabilityFunctionSuspend</b>
member of <b>COMPOSITE_DEVICE_CAPABILITIES</b> to 1. Finally, call <a href="https://msdn.microsoft.com/library/windows/hardware/hh406229">USBD_BuildRegisterCompositeDevice</a> and pass the initialized structure in the  <i>CapabilityFlags</i> parameter.</p>
</dd>

### -field <b>FunctionCount</b>

<dd>
<p>The number of functions supported by the composite device. The <b>FunctionCount</b> value must not exceed 255.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 8</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450854">IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406229">USBD_BuildRegisterCompositeDevice</a>
</dt>
<dt>
<a href="..\usbdlib\ns-usbdlib--composite-device-capabilities.md">COMPOSITE_DEVICE_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450803">COMPOSITE_DEVICE_CAPABILITIES_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20REGISTER_COMPOSITE_DEVICE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
