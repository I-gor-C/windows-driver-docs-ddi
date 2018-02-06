---
UID: NS:usb._URB
title: "_URB"
author: windows-driver-content
description: The URB structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The URB structure defines a format for all possible commands that can be sent to a USB device.
old-location: buses\urb.htm
old-project: usbref
ms.assetid: f28b2c97-61ee-4843-b3c5-b3a55f172c50
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: URB, buses.urb, PURB structure pointer [Buses], _URB, usb/URB, URB structure [Buses], PURB, usbstrct_20441a98-258d-44d2-b414-67b336a44fac.xml, usb/PURB
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usb.h
req.include-header: Usb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	usb.h
apiname:
-	URB
product: Windows
targetos: Windows
req.typenames: PURB, URB
req.product: Windows 10 or later.
---

# _URB structure
The <b>URB</b> structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The <b>URB</b> structure defines a format for all possible commands that can be sent to a USB device.

## Syntax
````
typedef struct _URB {
  union {
    struct _URB_HEADER  UrbHeader;
    struct _URB_SELECT_INTERFACE  UrbSelectInterface;
    struct _URB_SELECT_CONFIGURATION  UrbSelectConfiguration;
    struct _URB_PIPE_REQUEST  UrbPipeRequest;
    struct _URB_FRAME_LENGTH_CONTROL  UrbFrameLengthControl;
    struct _URB_GET_FRAME_LENGTH  UrbGetFrameLength;
    struct _URB_SET_FRAME_LENGTH  UrbSetFrameLength;
    struct _URB_GET_CURRENT_FRAME_NUMBER  UrbGetCurrentFrameNumber;
    struct _URB_CONTROL_TRANSFER  UrbControlTransfer;
    struct _URB_CONTROL_TRANSFER_EX  UrbControlTransferEx;
    struct _URB_CONTROL_TRANSFER_EX  UrbControlTransferEx;
    struct _URB_BULK_OR_INTERRUPT_TRANSFER  UrbBulkOrInterruptTransfer;
    struct _URB_ISOCH_TRANSFER  UrbIsochronousTransfer;
    struct _URB_CONTROL_DESCRIPTOR_REQUEST  UrbControlDescriptorRequest;
    struct _URB_CONTROL_GET_STATUS_REQUEST  UrbControlGetStatusRequest;
    struct _URB_CONTROL_FEATURE_REQUEST  UrbControlFeatureRequest;
    struct _URB_CONTROL_VENDOR_OR_CLASS_REQUEST  UrbControlVendorClassRequest;
    struct _URB_CONTROL_GET_INTERFACE_REQUEST  UrbControlGetInterfaceRequest;
    struct _URB_CONTROL_GET_CONFIGURATION_REQUEST  UrbControlGetConfigurationRequest;
    struct _URB_OS_FEATURE_DESCRIPTOR_REQUEST  UrbOSFeatureDescriptorRequest;
    struct _URB_OPEN_STATIC_STREAMS  UrbOpenStaticStreams;
    struct _URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS  UrbGetIsochPipeTransferPathDelays;
  };
} URB, *PURB;
````

## Members


## Remarks
For information about the function codes to set in each structure, see <a href="..\usb\ns-usb-_urb_header.md">_URB_HEADER</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usb.h (include Usb.h) |

## See Also

<a href="..\usbioctl\ni-usbioctl-ioctl_internal_usb_submit_urb.md">IOCTL_INTERNAL_USB_SUBMIT_URB</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20URB structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>