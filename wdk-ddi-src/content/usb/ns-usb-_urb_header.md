---
UID : NS:usb._URB_HEADER
title : _URB_HEADER
author : windows-driver-content
description : The _URB_HEADER structure is used by USB client drivers to provide basic information about the request being sent to the host controller driver.
old-location : buses\_urb_header.htm
old-project : usbref
ms.assetid : d23b9332-1e9d-4592-9674-3e5d8fc1d11e
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : URB_FUNCTION_BULK_OR_INTERRUPT_TRANSFER, URB_FUNCTION_GET_STATUS_FROM_INTERFACE, URB_FUNCTION_CLEAR_FEATURE_TO_INTERFACE, URB_FUNCTION_CLASS_DEVICE, URB_FUNCTION_GET_CURRENT_FRAME_NUMBER, URB_FUNCTION_OPEN_STATIC_STREAMS, URB_FUNCTION_GET_FRAME_LENGTH, URB_FUNCTION_CLOSE_STATIC_STREAMS, URB_FUNCTION_CLASS_ENDPOINT, URB_FUNCTION_CLEAR_FEATURE_TO_DEVICE, URB_FUNCTION_SET_FEATURE_TO_DEVICE, URB_FUNCTION_GET_DESCRIPTOR_FROM_ENDPOINT, URB_FUNCTION_SYNC_RESET_PIPE_AND_CLEAR_STALL, buses._urb_header, URB_FUNCTION_SET_DESCRIPTOR_TO_ENDPOINT, URB_FUNCTION_SELECT_INTERFACE, URB_FUNCTION_GET_INTERFACE, URB_FUNCTION_GET_MS_FEATURE_DESCRIPTOR, URB_FUNCTION_CLASS_OTHER, URB_FUNCTION_RELEASE_FRAME_LENGTH_CONTROL, usb/_URB_HEADER, URB_FUNCTION_SET_DESCRIPTOR_TO_INTERFACE, URB_FUNCTION_ISOCH_TRANSFER_USING_CHAINED_MDL, URB_FUNCTION_SET_FRAME_LENGTH, URB_FUNCTION_VENDOR_OTHER, URB_FUNCTION_RESET_PIPE, URB_FUNCTION_BULK_OR_INTERRUPT_TRANSFER_USING_CHAINED_MDL, URB_FUNCTION_CONTROL_TRANSFER, URB_FUNCTION_SET_DESCRIPTOR_TO_DEVICE, URB_FUNCTION_CLEAR_FEATURE_TO_OTHER, URB_FUNCTION_GET_STATUS_FROM_OTHER, _URB_HEADER structure [Buses], URB_FUNCTION_VENDOR_INTERFACE, URB_FUNCTION_CLASS_INTERFACE, URB_FUNCTION_ABORT_PIPE, URB_FUNCTION_SET_FEATURE_TO_ENDPOINT, URB_FUNCTION_SET_FEATURE_TO_OTHER, URB_FUNCTION_SELECT_CONFIGURATION, URB_FUNCTION_VENDOR_DEVICE, URB_FUNCTION_CONTROL_TRANSFER_EX, URB_FUNCTION_SYNC_RESET_PIPE, URB_FUNCTION_SYNC_CLEAR_STALL, URB_FUNCTION_SET_FEATURE_TO_INTERFACE, URB_FUNCTION_GET_CONFIGURATION, URB_FUNCTION_CLEAR_FEATURE_TO_ENDPOINT, URB_FUNCTION_GET_DESCRIPTOR_FROM_INTERFACE, usbstrct_588f903a-8690-4295-94b0-8b9162ff190e.xml, URB_FUNCTION_GET_DESCRIPTOR_FROM_DEVICE, URB_FUNCTION_GET_STATUS_FROM_DEVICE, URB_FUNCTION_ISOCH_TRANSFER, URB_FUNCTION_TAKE_FRAME_LENGTH_CONTROL, URB_FUNCTION_GET_STATUS_FROM_ENDPOINT, _URB_HEADER, URB_FUNCTION_VENDOR_ENDPOINT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : usb.h
req.include-header : Usb.h
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
req.product : Windows 10 or later.
---

# _URB_HEADER structure
The <b>_URB_HEADER</b> structure is used by USB client drivers to provide basic information about the request being sent to the host controller driver.

## Syntax
````
struct _URB_HEADER {
  USHORT      Length;
  USHORT      Function;
  USBD_STATUS Status;
  PVOID       UsbdDeviceHandle;
  ULONG       UsbdFlags;
};
````

## Members


`Function`

Specifies a numeric code indicating the requested operation for this URB. One of the following values must be set:

`Length`

Specifies the length, in bytes, of the URB. For URB requests that use data structures other than <b>_URB_HEADER</b>, this member must be set to the length of the entire URB request structure, not the _URB_HEADER size.

`Status`

Contains a USBD_STATUS_<i>XXX</i> code on return from the host controller driver.

`UsbdDeviceHandle`

Reserved. Do not use.

`UsbdFlags`

Reserved. Do not use.

## Remarks
The <b>_URB_HEADER</b> structure is a member of all USB requests that are part of the URB structure. The <b>_URB_HEADER</b> structure is used to provide common information about each request to the host controller driver.

The reserved members of this structure must be treated as opaque and are reserved for system use.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | usb.h (include Usb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540160">USB Structures</a>

<a href="..\usb\ns-usb-_urb_select_interface.md">_URB_SELECT_INTERFACE</a>

<a href="..\usb\ns-usb-_urb_os_feature_descriptor_request.md">_URB_OS_FEATURE_DESCRIPTOR_REQUEST</a>

<a href="..\usb\ns-usb-_urb_control_get_configuration_request.md">_URB_CONTROL_GET_CONFIGURATION_REQUEST</a>

<a href="..\usb\ns-usb-_urb_control_get_status_request.md">_URB_CONTROL_GET_STATUS_REQUEST</a>

<a href="..\usb\ns-usb-_urb_control_descriptor_request.md">_URB_CONTROL_DESCRIPTOR_REQUEST</a>

<a href="..\usb\ns-usb-_urb_control_feature_request.md">_URB_CONTROL_FEATURE_REQUEST</a>

<a href="..\usb\ns-usb-_urb_control_transfer.md">_URB_CONTROL_TRANSFER</a>

<a href="..\usb\ns-usb-_urb_pipe_request.md">_URB_PIPE_REQUEST</a>

<a href="..\usb\ns-usb-_urb_bulk_or_interrupt_transfer.md">_URB_BULK_OR_INTERRUPT_TRANSFER</a>

<a href="..\usb\ns-usb-_urb_control_get_interface_request.md">_URB_CONTROL_GET_INTERFACE_REQUEST</a>

<a href="..\usb\ns-usb-_urb_get_current_frame_number.md">_URB_GET_CURRENT_FRAME_NUMBER</a>

<a href="..\usb\ns-usb-_urb_select_configuration.md">_URB_SELECT_CONFIGURATION</a>

<a href="..\usb\ns-usb-_urb.md">URB</a>

<a href="..\usb\ns-usb-_urb_control_vendor_or_class_request.md">_URB_CONTROL_VENDOR_OR_CLASS_REQUEST</a>

<a href="..\usb\ns-usb-_urb_isoch_transfer.md">_URB_ISOCH_TRANSFER</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20_URB_HEADER structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>