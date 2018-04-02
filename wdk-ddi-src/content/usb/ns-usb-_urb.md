---
UID: NS:usb._URB
title: "_URB"
author: windows-driver-content
description: The URB structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The URB structure defines a format for all possible commands that can be sent to a USB device.
old-location: buses\urb.htm
old-project: usbref
ms.assetid: f28b2c97-61ee-4843-b3c5-b3a55f172c50
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PURB, PURB structure pointer [Buses], URB, URB structure [Buses], _URB, buses.urb, usb/PURB, usb/URB, usbstrct_20441a98-258d-44d2-b414-67b336a44fac.xml
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	usb.h
api_name:
-	URB
product:
- Windows
targetos: Windows
req.typenames: URB, PURB
req.product: Windows 10 or later.
---

# _URB structure
The <b>URB</b> structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The <b>URB</b> structure defines a format for all possible commands that can be sent to a USB device.

## Syntax
```
typedef struct _URB {
  union {
    _URB_BULK_OR_INTERRUPT_TRANSFER          UrbBulkOrInterruptTransfer;
    _URB_CONTROL_DESCRIPTOR_REQUEST          UrbControlDescriptorRequest;
    _URB_CONTROL_FEATURE_REQUEST             UrbControlFeatureRequest;
    _URB_CONTROL_GET_CONFIGURATION_REQUEST   UrbControlGetConfigurationRequest;
    _URB_CONTROL_GET_INTERFACE_REQUEST       UrbControlGetInterfaceRequest;
    _URB_CONTROL_GET_STATUS_REQUEST          UrbControlGetStatusRequest;
    _URB_CONTROL_TRANSFER                    UrbControlTransfer;
    _URB_CONTROL_TRANSFER_EX                 UrbControlTransferEx;
    _URB_CONTROL_VENDOR_OR_CLASS_REQUEST     UrbControlVendorClassRequest;
    _URB_FRAME_LENGTH_CONTROL                UrbFrameLengthControl;
    _URB_GET_CURRENT_FRAME_NUMBER            UrbGetCurrentFrameNumber;
    _URB_GET_FRAME_LENGTH                    UrbGetFrameLength;
    _URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS UrbGetIsochPipeTransferPathDelays;
    _URB_HEADER                              UrbHeader;
    _URB_ISOCH_TRANSFER                      UrbIsochronousTransfer;
    _URB_OPEN_STATIC_STREAMS                 UrbOpenStaticStreams;
    _URB_OS_FEATURE_DESCRIPTOR_REQUEST       UrbOSFeatureDescriptorRequest;
    _URB_PIPE_REQUEST                        UrbPipeRequest;
    _URB_SELECT_CONFIGURATION                UrbSelectConfiguration;
    _URB_SELECT_INTERFACE                    UrbSelectInterface;
    _URB_SET_FRAME_LENGTH                    UrbSetFrameLength;
    struct {
          } _URB_HEADER;
    struct {
          } _URB_SELECT_INTERFACE;
    struct {
          } _URB_SELECT_CONFIGURATION;
    struct {
          } _URB_PIPE_REQUEST;
    struct {
          } _URB_FRAME_LENGTH_CONTROL;
    struct {
          } _URB_GET_FRAME_LENGTH;
    struct {
          } _URB_SET_FRAME_LENGTH;
    struct {
          } _URB_GET_CURRENT_FRAME_NUMBER;
    struct {
          } _URB_CONTROL_TRANSFER;
    struct {
          } _URB_CONTROL_TRANSFER_EX;
    struct {
          } _URB_BULK_OR_INTERRUPT_TRANSFER;
    struct {
          } _URB_ISOCH_TRANSFER;
    struct {
          } _URB_CONTROL_DESCRIPTOR_REQUEST;
    struct {
          } _URB_CONTROL_GET_STATUS_REQUEST;
    struct {
          } _URB_CONTROL_FEATURE_REQUEST;
    struct {
          } _URB_CONTROL_VENDOR_OR_CLASS_REQUEST;
    struct {
          } _URB_CONTROL_GET_INTERFACE_REQUEST;
    struct {
          } _URB_CONTROL_GET_CONFIGURATION_REQUEST;
    struct {
          } _URB_OS_FEATURE_DESCRIPTOR_REQUEST;
    struct {
          } _URB_OPEN_STATIC_STREAMS;
    struct {
          } _URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS;
  };
} URB, PURB;
```

## Members


## Remarks
For information about the function codes to set in each structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540409">_URB_HEADER</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usb.h (include Usb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537271">IOCTL_INTERNAL_USB_SUBMIT_URB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>