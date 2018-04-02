---
UID: NE:wdfusb._WDF_USB_PIPE_TYPE
title: "_WDF_USB_PIPE_TYPE"
author: windows-driver-content
description: The WDF_USB_PIPE_TYPE enumeration identifies the types of USB pipes.
old-location: wdf\wdf_usb_pipe_type.htm
old-project: wdf
ms.assetid: ae230ff0-4fd9-417b-8ee0-80e3ca5a30ff
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFUsbRef_6a3da4b3-f8ac-4208-bdd2-1136a6417b3a.xml, WDF_USB_PIPE_TYPE, WDF_USB_PIPE_TYPE enumeration, WdfUsbPipeTypeBulk, WdfUsbPipeTypeControl, WdfUsbPipeTypeInterrupt, WdfUsbPipeTypeInvalid, WdfUsbPipeTypeIsochronous, _WDF_USB_PIPE_TYPE, kmdf.wdf_usb_pipe_type, wdf.wdf_usb_pipe_type, wdfusb/WDF_USB_PIPE_TYPE, wdfusb/WdfUsbPipeTypeBulk, wdfusb/WdfUsbPipeTypeControl, wdfusb/WdfUsbPipeTypeInterrupt, wdfusb/WdfUsbPipeTypeInvalid, wdfusb/WdfUsbPipeTypeIsochronous
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
req.irql: "<=DISPATCH_LEVEL  (See Remarks section.)"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfusb.h
api_name:
-	WDF_USB_PIPE_TYPE
product:
- Windows
targetos: Windows
req.typenames: WDF_USB_PIPE_TYPE
req.product: Windows 10 or later.
---

# _WDF_USB_PIPE_TYPE Enumeration
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_PIPE_TYPE</b> enumeration identifies the types of USB pipes.

## Syntax
```
typedef enum _WDF_USB_PIPE_TYPE {
  WdfUsbPipeTypeInvalid      ,
  WdfUsbPipeTypeControl      ,
  WdfUsbPipeTypeIsochronous  ,
  WdfUsbPipeTypeBulk         ,
  WdfUsbPipeTypeInterrupt
} WDF_USB_PIPE_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>WdfUsbPipeTypeInvalid</td>
                    <td>Reserved for internal use.</td>
                </tr>
            
                <tr>
                    <td>WdfUsbPipeTypeControl</td>
                    <td>The pipe is a control pipe.</td>
                </tr>
            
                <tr>
                    <td>WdfUsbPipeTypeIsochronous</td>
                    <td>The pipe is an isochronous pipe.</td>
                </tr>
            
                <tr>
                    <td>WdfUsbPipeTypeBulk</td>
                    <td>The pipe is a bulk pipe.</td>
                </tr>
            
                <tr>
                    <td>WdfUsbPipeTypeInterrupt</td>
                    <td>The pipe is an interrupt pipe.</td>
                </tr>
</table>

## Remarks

The <b>WDF_USB_PIPE_TYPE</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553037">WDF_USB_PIPE_INFORMATION</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553037">WDF_USB_PIPE_INFORMATION</a>