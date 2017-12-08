---
UID: NS.usbioctl._USB_NODE_CONNECTION_INFORMATION_EX
title: USB_NODE_CONNECTION_INFORMATION_EX
author: windows-driver-content
description: The USB_NODE_CONNECTION_INFORMATION_EX structure is used in conjunction with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about the connection associated with the indicated USB port.
old-location: buses\usb_node_connection_information_ex.htm
old-project: usbref
ms.assetid: d824e279-50a9-46a1-a93a-9ae17928f146
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_NODE_CONNECTION_INFORMATION_EX, USB_NODE_CONNECTION_INFORMATION_EX, *PUSB_NODE_CONNECTION_INFORMATION_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_NODE_CONNECTION_INFORMATION_EX
req.alt-loc: usbioctl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USB_NODE_CONNECTION_INFORMATION_EX structure



## -description
<p>The <b>USB_NODE_CONNECTION_INFORMATION_EX</b> structure is used in conjunction with the <a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-node-connection-information-ex.md">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a> request to obtain information about the connection associated with the indicated USB port.</p>


## -syntax

````
typedef struct _USB_NODE_CONNECTION_INFORMATION_EX {
  ULONG                 ConnectionIndex;
  USB_DEVICE_DESCRIPTOR DeviceDescriptor;
  UCHAR                 CurrentConfigurationValue;
  UCHAR                 Speed;
  BOOLEAN               DeviceIsHub;
  USHORT                DeviceAddress;
  ULONG                 NumberOfOpenPipes;
  USB_CONNECTION_STATUS ConnectionStatus;
  USB_PIPE_INFO         PipeList[];
} USB_NODE_CONNECTION_INFORMATION_EX, *PUSB_NODE_CONNECTION_INFORMATION_EX;
````


## -struct-fields
<dl>

### -field ConnectionIndex

<dd>
<p>Contains a value greater than or equal to 1 that specifies the number of the port.</p>
</dd>

### -field DeviceDescriptor

<dd>
<p>Contains a structure of type <a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a> that reports the USB device descriptor returned by the attached device during enumeration.</p>
</dd>

### -field CurrentConfigurationValue

<dd>
<p>Contains the ID used with the SetConfiguration request to specify that current configuration of the device connected to the indicated port. For an explanation of this value, see the Universal Serial Bus Specification.</p>
</dd>

### -field Speed

<dd>
<p>Contains a value of type <a href="..\usbspec\ne-usbspec--usb-device-speed.md">USB_DEVICE_SPEED</a> that indicates the speed of the device. </p>
</dd>

### -field DeviceIsHub

<dd>
<p>Indicates, when <b>TRUE</b>, that the device attached to the port is a hub.</p>
</dd>

### -field DeviceAddress

<dd>
<p>Contains the USB-assigned, bus-relative address of the device that is attached to the port.</p>
</dd>

### -field NumberOfOpenPipes

<dd>
<p>Indicates the number of open USB pipes associated with the port.</p>
</dd>

### -field ConnectionStatus

<dd>
<p>Contains an enumerator of type <a href="..\usbioctl\ne-usbioctl--usb-connection-status.md">USB_CONNECTION_STATUS</a> that indicates the connection status.</p>
</dd>

### -field PipeList

<dd>
<p>Contains an array of structures of type <a href="..\usbioctl\ns-usbioctl--usb-pipe-info.md">USB_PIPE_INFO</a> that describes the open pipes associated with the port. Pipe descriptions include the schedule offset of the pipe and the associated endpoint descriptor. This information can be used to calculate bandwidth usage.</p>
</dd>
</dl>

## -remarks
<p>If there is no device connected, <a href="..\usbioctl\ni-usbioctl-ioctl-usb-get-node-connection-information-ex.md">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</a> just returns information about the port. If a device is connected to the port <b>IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX</b> returns information about both the port and the connected device.</p>

<p>The <b>USB_NODE_CONNECTION_INFORMATION_EX</b> structure is an extended version of <a href="..\usbioctl\ns-usbioctl--usb-node-connection-information.md">USB_NODE_CONNECTION_INFORMATION</a>. The two structures are identical, except for one member. In the extended structure, the <b>Speed</b> member indicates the device speed.  </p>

<p>The <b>Speed</b> member of the <b>USB_NODE_CONNECTION_INFORMATION_EX</b> structure is a UCHAR and it can specify any of the values of the <a href="..\usbspec\ne-usbspec--usb-device-speed.md">USB_DEVICE_SPEED</a> enumerator.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbioctl\ne-usbioctl--usb-connection-status.md">USB_CONNECTION_STATUS</a>
</dt>
<dt>
<a href="..\usbioctl\ns-usbioctl--usb-pipe-info.md">USB_PIPE_INFO</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_NODE_CONNECTION_INFORMATION_EX structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
