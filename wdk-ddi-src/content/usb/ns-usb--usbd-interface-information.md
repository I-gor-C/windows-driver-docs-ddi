---
UID: NS.usb._USBD_INTERFACE_INFORMATION
title: USBD_INTERFACE_INFORMATION
author: windows-driver-content
description: The USBD_INTERFACE_INFORMATION structure holds information about an interface for a configuration on a USB device.
old-location: buses\usbd_interface_information.htm
ms.assetid: dde09937-14fb-423b-8905-8a398a9c5902
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_INTERFACE_INFORMATION
req.alt-loc: usb.h
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
ms.keywords: USBD_INTERFACE_INFORMATION, USBD_INTERFACE_INFORMATION, *PUSBD_INTERFACE_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# USBD_INTERFACE_INFORMATION structure



## -description
<p>The <b>USBD_INTERFACE_INFORMATION</b> structure holds information about an interface for a configuration on a USB device.</p>


## -syntax

````
typedef struct _USBD_INTERFACE_INFORMATION {
  USHORT                Length;
  UCHAR                 InterfaceNumber;
  UCHAR                 AlternateSetting;
  UCHAR                 Class;
  UCHAR                 SubClass;
  UCHAR                 Protocol;
  UCHAR                 Reserved;
  USBD_INTERFACE_HANDLE InterfaceHandle;
  ULONG                 NumberOfPipes;
  USBD_PIPE_INFORMATION Pipes[1];
} USBD_INTERFACE_INFORMATION, *PUSBD_INTERFACE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>Specifies the length, in bytes, of this structure.</p>
</dd>

### -field <b>InterfaceNumber</b>

<dd>
<p>Specifies the device-defined index identifier for this interface.</p>
</dd>

### -field <b>AlternateSetting</b>

<dd>
<p>Specifies a device-defined index identifier that indicates which alternate setting this interface is using, should use, or describes.</p>
</dd>

### -field <b>Class</b>

<dd>
<p>Contains a USB-assigned identifier that specifies a USB-defined class that this interface conforms to.</p>
</dd>

### -field <b>SubClass</b>

<dd>
<p>Contains a USB-assigned identifier that specifies a USB-defined subclass that this interface conforms to. This code is specific to the code in <b>Class</b>.</p>
</dd>

### -field <b>Protocol</b>

<dd>
<p>Contains a USB-assigned identifier that specifies a USB-defined protocol that this interface conforms to. This code is specific to the codes in <b>Class</b> and <b>SubClass</b>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>InterfaceHandle</b>

<dd>
<p>Contains a host controller driver-defined handle that is used to access this interface. This member should be treated as opaque.</p>
</dd>

### -field <b>NumberOfPipes</b>

<dd>
<p>Specifies the number of pipes (endpoints) in this interface.</p>
</dd>

### -field <b>Pipes</b>

<dd>
<p>Pointer to the first element in the array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff539114">USBD_PIPE_INFORMATION</a> structures. The length of the array depends on the number of endpoints in the interface descriptor.</p>
</dd>
</dl>

## -remarks
<p>Members that are part of this structure, but not described here, should be treated as opaque and considered to be reserved for system use.</p>

<p>The reserved members of this structure must be treated as opaque and are reserved for system use.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usb.h (include Usb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539114">USBD_PIPE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_INTERFACE_INFORMATION structure%20 RELEASE:%20(11/3/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
