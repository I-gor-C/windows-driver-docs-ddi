---
UID : NS:usbioctl._USB_DESCRIPTOR_REQUEST
title : "_USB_DESCRIPTOR_REQUEST"
author : windows-driver-content
description : The USB_DESCRIPTOR_REQUEST structure is used with the IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION I/O control request to retrieve one or more descriptors for the device that is associated with the indicated connection index.
old-location : buses\usb_descriptor_request.htm
old-project : usbref
ms.assetid : d4d51366-4d04-47fe-8c44-09c9c6ccf35f
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : usbioctl/USB_DESCRIPTOR_REQUEST, USB_DESCRIPTOR_REQUEST, USB_DESCRIPTOR_REQUEST structure [Buses], usbstrct_b5a96c38-53d8-4d08-849b-d6c8c4b69c72.xml, usbioctl/PUSB_DESCRIPTOR_REQUEST, PUSB_DESCRIPTOR_REQUEST structure pointer [Buses], *PUSB_DESCRIPTOR_REQUEST, PUSB_DESCRIPTOR_REQUEST, buses.usb_descriptor_request, _USB_DESCRIPTOR_REQUEST
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : usbioctl.h
req.include-header : Usbioctl.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<=DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PUSB_DESCRIPTOR_REQUEST, USB_DESCRIPTOR_REQUEST"
req.product : Windows 10 or later.
---

# _USB_DESCRIPTOR_REQUEST structure
The <b>USB_DESCRIPTOR_REQUEST</b> structure is used with the <a href="..\usbioctl\ni-usbioctl-ioctl_usb_get_descriptor_from_node_connection.md">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a> I/O control request to retrieve one or more descriptors for the device that is associated with the indicated connection index.

## Syntax
````
typedef struct _USB_DESCRIPTOR_REQUEST {
  ULONG  ConnectionIndex;
  struct {
    UCHAR  bmRequest;
    UCHAR  bRequest;
    USHORT wValue;
    USHORT wIndex;
    USHORT wLength;
  } SetupPacket;
  UCHAR  Data[];
} USB_DESCRIPTOR_REQUEST, *PUSB_DESCRIPTOR_REQUEST;
````

## Members


`ConnectionIndex`

The port whose descriptors are retrieved.

`Data`

On output from the <a href="..\usbioctl\ni-usbioctl-ioctl_usb_get_descriptor_from_node_connection.md">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a> I/O control request, this member contains the retrieved descriptors.

`SetupPacket`

The members of the <b>SetupPacket</b> structure are as follows:

## Remarks
If the caller specifies a value of USB_CONFIGURATION_DESCRIPTOR_TYPE in the <b>wValue</b> member, the output buffer must be large enough to hold all of the descriptors that are associated with the current configuration, or the request will fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | usbioctl.h (include Usbioctl.h) |

## See Also

<a href="..\usbioctl\ni-usbioctl-ioctl_usb_get_descriptor_from_node_connection.md">IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_DESCRIPTOR_REQUEST structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>