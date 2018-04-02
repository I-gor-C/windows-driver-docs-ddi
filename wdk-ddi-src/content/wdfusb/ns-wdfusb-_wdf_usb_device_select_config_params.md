---
UID: NS:wdfusb._WDF_USB_DEVICE_SELECT_CONFIG_PARAMS
title: "_WDF_USB_DEVICE_SELECT_CONFIG_PARAMS"
author: windows-driver-content
description: The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure specifies USB device configuration parameters.
old-location: wdf\wdf_usb_device_select_config_params.htm
old-project: wdf
ms.assetid: d48484eb-a7bf-4ca7-9d18-4c4c166db90c
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS, DFUsbRef_1f6335f1-ec4c-413e-b176-46b1bdf70d46.xml, PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS, PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure pointer, WDF_USB_DEVICE_SELECT_CONFIG_PARAMS, WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure, _WDF_USB_DEVICE_SELECT_CONFIG_PARAMS, kmdf.wdf_usb_device_select_config_params, wdf.wdf_usb_device_select_config_params, wdfusb/PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS, wdfusb/WDF_USB_DEVICE_SELECT_CONFIG_PARAMS"
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
-	WDF_USB_DEVICE_SELECT_CONFIG_PARAMS
product: Windows
targetos: Windows
req.typenames: WDF_USB_DEVICE_SELECT_CONFIG_PARAMS, *PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS
req.product: Windows 10 or later.
---

# _WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</b> structure specifies USB device configuration parameters.

## Syntax
```
typedef struct _WDF_USB_DEVICE_SELECT_CONFIG_PARAMS {
  ULONG                              Size;
  WdfUsbTargetDeviceSelectConfigType Type;
  union {
    struct {
      PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor;
      PUSB_INTERFACE_DESCRIPTOR     *InterfaceDescriptors;
      ULONG                         NumInterfaceDescriptors;
    } Descriptor;
    struct {
      PURB Urb;
    } Urb;
    struct {
      UCHAR           NumberConfiguredPipes;
      WDFUSBINTERFACE ConfiguredUsbInterface;
    } SingleInterface;
    struct {
      UCHAR                           NumberInterfaces;
      PWDF_USB_INTERFACE_SETTING_PAIR Pairs;
      UCHAR                           NumberOfConfiguredInterfaces;
    } MultiInterface;
  } Types;
} WDF_USB_DEVICE_SELECT_CONFIG_PARAMS, *PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS;
```

## Members


`Size`

The size, in bytes, of this structure.

`Type`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff550102">WdfUsbTargetDeviceSelectConfigType</a>-typed value that either specifies the type of configuration that is being selected or indicates that the current configuration is being deconfigured.

`Types`



## Remarks
The <b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</b> structure is used as input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a>.

To initialize a <b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</b> structure, use one of the following functions:


<a href="https://msdn.microsoft.com/library/windows/hardware/ff552982">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_DECONFIG</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552995">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552992">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552986">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552997">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB</a>


If the driver sets the <b>Type</b> member to <b>WdfUsbTargetDeviceSelectConfigTypeInterfacesDescriptor</b>, it can change the USB device configuration. All other values use the current USB device configuration.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553023">WDF_USB_INTERFACE_SETTING_PAIR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550102">WdfUsbTargetDeviceSelectConfigType</a>