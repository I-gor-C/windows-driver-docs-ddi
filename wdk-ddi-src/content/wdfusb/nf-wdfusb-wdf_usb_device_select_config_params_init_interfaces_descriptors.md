---
UID: NF:wdfusb.WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS
title: WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function
author: windows-driver-content
description: The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function initializes a WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure so that a driver can specify a configuration by using USB descriptors.
old-location: wdf\wdf_usb_device_select_config_params_init_interfaces_descriptors.htm
old-project: wdf
ms.assetid: 45f024d2-f500-49aa-9a9d-3ec16ff7e99b
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFUsbRef_294960b9-c686-4701-bed5-aff84f9bc990.xml, WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS, WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function, kmdf.wdf_usb_device_select_config_params_init_interfaces_descriptors, wdf.wdf_usb_device_select_config_params_init_interfaces_descriptors, wdfusb/WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
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
-	WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS
product: Windows
targetos: Windows
req.typenames: WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
req.product: Windows 10 or later.
---


# WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure so that a driver can specify a configuration by using USB descriptors.

## Syntax

```
void WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS(
  PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS Params,
  PUSB_CONFIGURATION_DESCRIPTOR        ConfigDescriptor,
  PUSB_INTERFACE_DESCRIPTOR            *InterfaceDescriptors,
  ULONG                                NumInterfaceDescriptors
);
```

## Parameters

`Params`

A pointer to a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure.

`ConfigDescriptor`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a> structure.

`InterfaceDescriptors`

A pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a> structures.

`NumInterfaceDescriptors`

The number of elements that is in the <i>InterfaceDescriptors</i> array.


## Return Value

Non

## Remarks

The <b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</b> function zeros the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure and sets the <b>Size</b> member to the size of the structure. It also sets the <b>Type</b> member to <b>WdfUsbTargetDeviceSelectConfigTypeInterfacesDescriptor</b>.

This function uses the <i>ConfigDescriptor</i>, <i>InterfaceDescriptors</i>, and <i>NumInterfaceDescriptors</i> parameters to set the structure's <b>Types.Descriptor</b> union members.

To initialize a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure, the driver must call one of the following functions:

<ul>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552982">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_DECONFIG</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552995">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE</a>


</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552992">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES</a>


</li>
<li>
<b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</b>

</li>
<li>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552997">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB</a>


</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552600">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552982">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_DECONFIG</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552986">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552992">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552995">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552997">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB</a>