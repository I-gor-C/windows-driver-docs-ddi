---
UID: NE:wdfusb._WDF_USB_DEVICE_TRAITS
title: "_WDF_USB_DEVICE_TRAITS"
author: windows-driver-content
description: The WDF_USB_DEVICE_TRAITS enumeration identifies USB device traits.
old-location: wdf\wdf_usb_device_traits.htm
old-project: wdf
ms.assetid: 5ba625f5-5bc0-4e2b-a7a9-5014746086c8
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFUsbRef_504c0bd9-3ba7-47cc-a99d-ab54d46cbdc4.xml, WDF_USB_DEVICE_TRAITS, WDF_USB_DEVICE_TRAITS enumeration, WDF_USB_DEVICE_TRAIT_AT_HIGH_SPEED, WDF_USB_DEVICE_TRAIT_REMOTE_WAKE_CAPABLE, WDF_USB_DEVICE_TRAIT_SELF_POWERED, _WDF_USB_DEVICE_TRAITS, kmdf.wdf_usb_device_traits, wdf.wdf_usb_device_traits, wdfusb/WDF_USB_DEVICE_TRAITS, wdfusb/WDF_USB_DEVICE_TRAIT_AT_HIGH_SPEED, wdfusb/WDF_USB_DEVICE_TRAIT_REMOTE_WAKE_CAPABLE, wdfusb/WDF_USB_DEVICE_TRAIT_SELF_POWERED
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
-	WDF_USB_DEVICE_TRAITS
product: Windows
targetos: Windows
req.typenames: WDF_USB_DEVICE_TRAITS
req.product: Windows 10 or later.
---

# _WDF_USB_DEVICE_TRAITS Enumeration
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_DEVICE_TRAITS</b> enumeration identifies USB device traits.

## Syntax
```
typedef enum _WDF_USB_DEVICE_TRAITS {
  WDF_USB_DEVICE_TRAIT_SELF_POWERED         ,
  WDF_USB_DEVICE_TRAIT_REMOTE_WAKE_CAPABLE  ,
  WDF_USB_DEVICE_TRAIT_AT_HIGH_SPEED
} WDF_USB_DEVICE_TRAITS;
```

## Constants

<table>
            
                <tr>
                    <td>WDF_USB_DEVICE_TRAIT_SELF_POWERED</td>
                    <td>The device is self-powered.</td>
                </tr>
            
                <tr>
                    <td>WDF_USB_DEVICE_TRAIT_REMOTE_WAKE_CAPABLE</td>
                    <td>The device has a remote wakeup capability.</td>
                </tr>
            
                <tr>
                    <td>WDF_USB_DEVICE_TRAIT_AT_HIGH_SPEED</td>
                    <td>The device is operating at high speed or SuperSpeed.</td>
                </tr>
</table>

## Remarks

The <b>WDF_USB_DEVICE_TRAITS</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552592">WDF_USB_DEVICE_INFORMATION</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552592">WDF_USB_DEVICE_INFORMATION</a>