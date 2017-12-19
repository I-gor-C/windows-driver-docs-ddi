---
UID: NF.wdfusb.WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS
title: WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function
author: windows-driver-content
description: The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function initializes a WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure so that a driver can specify a configuration by using USB descriptors.
old-location: wdf\wdf_usb_device_select_config_params_init_interfaces_descriptors.htm
old-project: wdf
ms.assetid: 45f024d2-f500-49aa-9a9d-3ec16ff7e99b
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS
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
req.alt-api: WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS
req.alt-loc: wdfusb.h
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
req.product: Windows 10 or later.
---

# WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</b> function initializes a <a href="wdf.wdf_usb_device_select_config_params">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure so that a driver can specify a configuration by using USB descriptors. 



## -syntax

````
VOID WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS(
  _Out_ PWDF_USB_DEVICE_SELECT_CONFIG_PARAMS Params,
  _In_  PUSB_CONFIGURATION_DESCRIPTOR        ConfigDescriptor,
  _In_  PUSB_INTERFACE_DESCRIPTOR            *InterfaceDescriptors,
  _In_  ULONG                                NumInterfaceDescriptors
);
````


## -parameters

### -param Params [out]

A pointer to a driver-allocated <a href="wdf.wdf_usb_device_select_config_params">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure.


### -param ConfigDescriptor [in]

A pointer to a <a href="buses.usb_configuration_descriptor">USB_CONFIGURATION_DESCRIPTOR</a> structure.


### -param InterfaceDescriptors [in]

A pointer to an array of <a href="buses.usb_interface_descriptor">USB_INTERFACE_DESCRIPTOR</a> structures.


### -param NumInterfaceDescriptors [in]

The number of elements that is in the <i>InterfaceDescriptors</i> array.


## -returns
Non


## -remarks
The <b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</b> function zeros the <a href="wdf.wdf_usb_device_select_config_params">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure and sets the <b>Size</b> member to the size of the structure. It also sets the <b>Type</b> member to <b>WdfUsbTargetDeviceSelectConfigTypeInterfacesDescriptor</b>.

This function uses the <i>ConfigDescriptor</i>, <i>InterfaceDescriptors</i>, and <i>NumInterfaceDescriptors</i> parameters to set the structure's <b>Types.Descriptor</b> union members.

To initialize a <a href="wdf.wdf_usb_device_select_config_params">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a> structure, the driver must call one of the following functions:


<a href="wdf.wdf_usb_device_select_config_params_init_deconfig">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_DECONFIG</a>



<a href="wdf.wdf_usb_device_select_config_params_init_single_interface">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE</a>



<a href="wdf.wdf_usb_device_select_config_params_init_multiple_interfaces">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES</a>


<b>WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</b>


<a href="wdf.wdf_usb_device_select_config_params_init_urb">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB</a>



## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_configuration_descriptor">USB_CONFIGURATION_DESCRIPTOR</a>
</dt>
<dt>
<a href="buses.usb_interface_descriptor">USB_INTERFACE_DESCRIPTOR</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_select_config_params">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_select_config_params_init_deconfig">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_DECONFIG</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_select_config_params_init_interfaces_descriptors">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_select_config_params_init_multiple_interfaces">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_select_config_params_init_single_interface">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE</a>
</dt>
<dt>
<a href="wdf.wdf_usb_device_select_config_params_init_urb">WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

