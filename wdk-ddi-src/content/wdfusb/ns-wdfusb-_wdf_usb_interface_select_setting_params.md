---
UID: NS:wdfusb._WDF_USB_INTERFACE_SELECT_SETTING_PARAMS
title: "_WDF_USB_INTERFACE_SELECT_SETTING_PARAMS"
author: windows-driver-content
description: The WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure contains selection information for a USB interface.
old-location: wdf\wdf_usb_interface_select_setting_params.htm
old-project: wdf
ms.assetid: fad8a205-8427-48c5-b4b5-b125aa9fe85c
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS, DFUsbRef_a32b6d83-abf8-4cc6-9ce3-3d03551164a4.xml, PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS, PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure pointer, WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure, _WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, kmdf.wdf_usb_interface_select_setting_params, wdf.wdf_usb_interface_select_setting_params, wdfusb/PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS, wdfusb/WDF_USB_INTERFACE_SELECT_SETTING_PARAMS"
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
-	WDF_USB_INTERFACE_SELECT_SETTING_PARAMS
product:
- Windows
targetos: Windows
req.typenames: WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, *PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS
req.product: Windows 10 or later.
---

# _WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</b> structure contains selection information for a USB interface.

## Syntax
```
typedef struct _WDF_USB_INTERFACE_SELECT_SETTING_PARAMS {
  ULONG                               Size;
  WdfUsbTargetDeviceSelectSettingType Type;
  union {
    struct {
      PUSB_INTERFACE_DESCRIPTOR InterfaceDescriptor;
    } Descriptor;
    struct {
      UCHAR SettingIndex;
    } Interface;
    struct {
      PURB Urb;
    } Urb;
  } Types;
} WDF_USB_INTERFACE_SELECT_SETTING_PARAMS, *PWDF_USB_INTERFACE_SELECT_SETTING_PARAMS;
```

## Members


`Size`

The size, in bytes, of this structure.

`Type`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff550103">WdfUsbTargetDeviceSelectSettingType</a>-typed value that identifies a technique for specifying a device interface.

`Types`



## Remarks
The <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550073">WdfUsbInterfaceSelectSetting</a> method. 

To initialize a <b>WDF_USB_INTERFACE_SELECT_SETTING_PARAMS</b> structure, your driver must call one of the following functions:

<ul>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553008">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_DESCRIPTOR</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553011">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553016">WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_URB</a>


</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550073">WdfUsbInterfaceSelectSetting</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550103">WdfUsbTargetDeviceSelectSettingType</a>