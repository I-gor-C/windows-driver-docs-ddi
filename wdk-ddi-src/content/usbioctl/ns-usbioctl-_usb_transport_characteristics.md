---
UID : NS:usbioctl._USB_TRANSPORT_CHARACTERISTICS
title : _USB_TRANSPORT_CHARACTERISTICS
author : windows-driver-content
description : Stores the transport characteristics at relevant points in time. This structure is used in the IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS request.
old-location : buses\usb_transport_characteristics.htm
old-project : usbref
ms.assetid : 56394A88-7231-4693-8DD1-C5C7586E490C
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _USB_TRANSPORT_CHARACTERISTICS, *PUSB_TRANSPORT_CHARACTERISTICS, USB_TRANSPORT_CHARACTERISTICS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : usbioctl.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : USB_TRANSPORT_CHARACTERISTICS
req.alt-loc : Usbioctl.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <=DISPATCH_LEVEL
req.typenames : "*PUSB_TRANSPORT_CHARACTERISTICS, USB_TRANSPORT_CHARACTERISTICS"
req.product : Windows 10 or later.
---

# _USB_TRANSPORT_CHARACTERISTICS structure
Stores the transport characteristics at relevant points in time. This structure is used in the  <a href="..\usbioctl\ni-usbioctl-ioctl_usb_get_transport_characteristics.md">IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS</a> request.

## Syntax
````
typedef struct _USB_TRANSPORT_CHARACTERISTICS {
  ULONG                       Version;
  ULONG                       TransportCharacteristicsFlags;
  ULONG64                     CurrentRoundtripLatencyInMilliSeconds;
  ULONG64                     MaxPotentialBandwidth;
} USB_TRANSPORT_CHARACTERISTICS, *PUSB_TRANSPORT_CHARACTERISTICS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | usbioctl.h |

    ## See Also

        <dl>
<dt>
<a href="..\usbioctl\ni-usbioctl-ioctl_usb_get_transport_characteristics.md">IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_TRANSPORT_CHARACTERISTICS structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>