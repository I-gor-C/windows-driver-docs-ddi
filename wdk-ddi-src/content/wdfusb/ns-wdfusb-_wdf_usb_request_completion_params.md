---
UID: NS:wdfusb._WDF_USB_REQUEST_COMPLETION_PARAMS
title: "_WDF_USB_REQUEST_COMPLETION_PARAMS"
author: windows-driver-content
description: The WDF_USB_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request for a USB device.
old-location: wdf\wdf_usb_request_completion_params.htm
old-project: wdf
ms.assetid: cd29d27c-9da2-477f-898e-13ee480aac9e
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdfusb/WDF_USB_REQUEST_COMPLETION_PARAMS, _WDF_USB_REQUEST_COMPLETION_PARAMS, PWDF_USB_REQUEST_COMPLETION_PARAMS structure pointer, DFUsbRef_14574f86-fd65-41df-be8e-557f6fe09c4f.xml, wdfusb/PWDF_USB_REQUEST_COMPLETION_PARAMS, *PWDF_USB_REQUEST_COMPLETION_PARAMS, PWDF_USB_REQUEST_COMPLETION_PARAMS, WDF_USB_REQUEST_COMPLETION_PARAMS structure, wdf.wdf_usb_request_completion_params, kmdf.wdf_usb_request_completion_params, WDF_USB_REQUEST_COMPLETION_PARAMS
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wdfusb.h
apiname:
-	WDF_USB_REQUEST_COMPLETION_PARAMS
product: Windows
targetos: Windows
req.typenames: "*PWDF_USB_REQUEST_COMPLETION_PARAMS, WDF_USB_REQUEST_COMPLETION_PARAMS"
req.product: Windows 10 or later.
---

# _WDF_USB_REQUEST_COMPLETION_PARAMS structure
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_REQUEST_COMPLETION_PARAMS</b> structure contains parameters that are associated with the completion of an I/O request for a USB device.

## Syntax
````
typedef struct _WDF_USB_REQUEST_COMPLETION_PARAMS {
  USBD_STATUS          UsbdStatus;
  WDF_USB_REQUEST_TYPE Type;
  union {
    struct {
      WDFMEMORY Buffer;
      USHORT    LangID;
      UCHAR     StringIndex;
      UCHAR     RequiredSize;
    } DeviceString;
    struct {
      WDFMEMORY                    Buffer;
      WDF_USB_CONTROL_SETUP_PACKET SetupPacket;
      ULONG                        Length;
    } DeviceControlTransfer;
    struct {
      WDFMEMORY Buffer;
    } DeviceUrb;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } PipeWrite;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } PipeRead;
    struct {
      WDFMEMORY Buffer;
    } PipeUrb;
  } Parameters;
} WDF_USB_REQUEST_COMPLETION_PARAMS, *PWDF_USB_REQUEST_COMPLETION_PARAMS;
````

## Members


`Parameters`



`Type`

A <a href="..\wudfusb\ne-wudfusb-_wdf_usb_request_type.md">WDF_USB_REQUEST_TYPE</a>-typed values that identifies the request type.

`UsbdStatus`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff539136">USBD_STATUS</a>-typed status value that the I/O target returned.

## Remarks
The <b>WDF_USB_REQUEST_COMPLETION_PARAMS</b> structure is a member of the <a href="..\wdfrequest\ns-wdfrequest-_wdf_request_completion_params.md">WDF_REQUEST_COMPLETION_PARAMS</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="..\wdfrequest\nf-wdfrequest-wdfrequestgetcompletionparams.md">WdfRequestGetCompletionParams</a>



<a href="..\wdfrequest\nc-wdfrequest-evt_wdf_request_completion_routine.md">CompletionRoutine</a>



<a href="..\wdfrequest\ns-wdfrequest-_wdf_request_completion_params.md">WDF_REQUEST_COMPLETION_PARAMS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_REQUEST_COMPLETION_PARAMS structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>