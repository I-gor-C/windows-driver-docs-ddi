---
UID: NS.USBBUSIF._USBC_DEVICE_CONFIGURATION_INTERFACE_V1
title: _USBC_DEVICE_CONFIGURATION_INTERFACE_V1
author: windows-driver-content
description: The USBC_DEVICE_CONFIGURATION_INTERFACE_V1 structure is exposed by the vendor-supplied filter drivers to assist the USB generic parent driver in defining interface collections.
old-location: buses\usbc_device_configuration_interface_v1.htm
old-project: usbref
ms.assetid: 86e8946f-f87f-40d4-bd02-6e4befe847e0
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _USBC_DEVICE_CONFIGURATION_INTERFACE_V1, USBC_DEVICE_CONFIGURATION_INTERFACE_V1, *PUSBC_DEVICE_CONFIGURATION_INTERFACE_V1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbbusif.h
req.include-header: Usbbusif.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBC_DEVICE_CONFIGURATION_INTERFACE_V1
req.alt-loc: usbbusif.h
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

# _USBC_DEVICE_CONFIGURATION_INTERFACE_V1 structure



## -description
The <b>USBC_DEVICE_CONFIGURATION_INTERFACE_V1</b> structure is exposed by the vendor-supplied filter drivers to assist the USB generic parent driver in defining interface collections.



## -syntax

````
typedef struct _USBC_DEVICE_CONFIGURATION_INTERFACE_V1 {
  USHORT                     Size;
  USHORT                     Version;
  PVOID                      Context;
  PINTERFACE_REFERENCE       InterfaceReference;
  PINTERFACE_DEREFERENCE     InterfaceDereference;
  USBC_START_DEVICE_CALLBACK StartDeviceCallback;
  USBC_PDO_ENABLE_CALLBACK   PdoEnableCallback;
  PVOID                      Reserved[8];
} USBC_DEVICE_CONFIGURATION_INTERFACE_V1, *PUSBC_DEVICE_CONFIGURATION_INTERFACE_V1;
````


## -struct-fields

### -field Size

The size, in bytes, of this structure.


### -field Version

The version of the interface.


### -field Context

The USB generic parent driver does not use this member. It is populated by the vendor supplied filter driver and may be used to track instance information for the bus interface. It is passed as a parameter to <a href="kernel.interfacereference">InterfaceReference</a> and <a href="kernel.interfacedereference">InterfaceDereference</a>. 


### -field InterfaceReference

Pointer to a routine that increments the number of references to this interface. For more information about this routine, see <a href="kernel.interfacereference">InterfaceReference</a>. 


### -field InterfaceDereference

Pointer to a routine that decrements the number of references to this interface. For more information about this routine, see <a href="kernel.interfacedereference">InterfaceDereference</a>. 


### -field StartDeviceCallback

Pointer to the callback routine that the filter driver furnishes to the USB generic parent driver to assist in defining interface collections on a device. For more information, see <a href="..\usbbusif\nc-usbbusif-usbc_start_device_callback.md">USBC_START_DEVICE_CALLBACK</a>.


### -field PdoEnableCallback

Reserved.


### -field Reserved

Reserved.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Usbbusif.h (include Usbbusif.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.custom_enumeration_of_interface_collections_by_vendor_supplied_callbac">Customizing Enumeration of Interface Collections for Composite Devices</a>
</dt>
<dt>
<a href="..\usbbusif\nc-usbbusif-usbc_start_device_callback.md">USBC_START_DEVICE_CALLBACK</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB structures</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBC_DEVICE_CONFIGURATION_INTERFACE_V1 structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

