---
UID: NS:wdfusb._WDF_USB_REQUEST_COMPLETION_PARAMS
title: "_WDF_USB_REQUEST_COMPLETION_PARAMS"
author: windows-driver-content
description: The WDF_USB_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request for a USB device.
old-location: wdf\wdf_usb_request_completion_params.htm
old-project: wdf
ms.assetid: cd29d27c-9da2-477f-898e-13ee480aac9e
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_USB_REQUEST_COMPLETION_PARAMS, DFUsbRef_14574f86-fd65-41df-be8e-557f6fe09c4f.xml, PWDF_USB_REQUEST_COMPLETION_PARAMS, PWDF_USB_REQUEST_COMPLETION_PARAMS structure pointer, WDF_USB_REQUEST_COMPLETION_PARAMS, WDF_USB_REQUEST_COMPLETION_PARAMS structure, _WDF_USB_REQUEST_COMPLETION_PARAMS, kmdf.wdf_usb_request_completion_params, wdf.wdf_usb_request_completion_params, wdfusb/PWDF_USB_REQUEST_COMPLETION_PARAMS, wdfusb/WDF_USB_REQUEST_COMPLETION_PARAMS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
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
-	wdfusb.h
api_name:
-	WDF_USB_REQUEST_COMPLETION_PARAMS
product: Windows
targetos: Windows
req.typenames: WDF_USB_REQUEST_COMPLETION_PARAMS, *PWDF_USB_REQUEST_COMPLETION_PARAMS
req.product: Windows 10 or later.
---

# _WDF_USB_REQUEST_COMPLETION_PARAMS structure
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_REQUEST_COMPLETION_PARAMS</b> structure contains parameters that are associated with the completion of an I/O request for a USB device.

## Syntax
```
typedef struct _WDF_USB_REQUEST_COMPLETION_PARAMS {
  USBD_STATUS          UsbdStatus;
  WDF_USB_REQUEST_TYPE Type;
  union {
    struct {
      WDFMEMORY Buffer;
      USHORT    LangID;
      UCHAR     StringIndex;
      UCHAR     RequiredSize;
    } DeviceString;
    struct {
      WDFMEMORY                    Buffer;
      WDF_USB_CONTROL_SETUP_PACKET SetupPacket;
      ULONG                        Length;
    } DeviceControlTransfer;
    struct {
      WDFMEMORY Buffer;
    } DeviceUrb;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } PipeWrite;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } PipeRead;
    struct {
      WDFMEMORY Buffer;
    } PipeUrb;
  } Parameters;
} WDF_USB_REQUEST_COMPLETION_PARAMS, *PWDF_USB_REQUEST_COMPLETION_PARAMS;
```

## Members


`UsbdStatus`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff539136">USBD_STATUS</a>-typed status value that the I/O target returned.

`Type`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff553055">WDF_USB_REQUEST_TYPE</a>-typed values that identifies the request type.

`Parameters`



## Remarks
The <b>WDF_USB_REQUEST_COMPLETION_PARAMS</b> structure is a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a>