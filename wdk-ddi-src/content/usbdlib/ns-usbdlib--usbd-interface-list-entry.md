---
UID: NS.usbdlib._USBD_INTERFACE_LIST_ENTRY
title: USBD_INTERFACE_LIST_ENTRY
author: windows-driver-content
description: The USBD_INTERFACE_LIST_ENTRY structure is used by USB client drivers to create an array of interfaces to be inserted into a configuration request.
old-location: buses\usbd_interface_list_entry.htm
old-project: usbref
ms.assetid: 9b729c52-b03b-4b53-ae1a-9a025585ba7b
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_INTERFACE_LIST_ENTRY, USBD_INTERFACE_LIST_ENTRY, *PUSBD_INTERFACE_LIST_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbdlib.h
req.include-header: Usbdlib.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_INTERFACE_LIST_ENTRY
req.alt-loc: usbdlib.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USBD_INTERFACE_LIST_ENTRY structure



## -description
<p>The <b>USBD_INTERFACE_LIST_ENTRY</b> structure is used by USB client drivers to create an array of interfaces to be inserted into a configuration request.</p>


## -syntax

````
typedef struct _USBD_INTERFACE_LIST_ENTRY {
  PUSB_INTERFACE_DESCRIPTOR   InterfaceDescriptor;
  PUSBD_INTERFACE_INFORMATION Interface;
} USBD_INTERFACE_LIST_ENTRY, *PUSBD_INTERFACE_LIST_ENTRY;
````


## -struct-fields
<dl>

### -field <b>InterfaceDescriptor</b>

<dd>
<p>Pointer to a <a href="..\usbspec\ns-usbspec--usb-interface-descriptor.md">USB_INTERFACE_DESCRIPTOR</a> structure that describes the interface to be added to the configuration request.</p>
</dd>

### -field <b>Interface</b>

<dd>
<p>Pointer to a <a href="..\usb\ns-usb--usbd-interface-information.md">USBD_INTERFACE_INFORMATION</a> structure that describes the properties and settings of the interface pointed to by <i>InterfaceDescriptor</i>.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by USB clients with the routine <a href="..\usbdlib\nf-usbdlib-usbd-createconfigurationrequestex.md">USBD_CreateConfigurationRequestEx</a>. Clients allocate an array of these structures, one for each interface to be configured. Clients must also allocate a <b>NULL</b> entry in the array to be used as a terminator before calling <b>USBD_CreateConfigurationRequestEx</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h (include Usbdlib.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbdlib\nf-usbdlib-usbd-createconfigurationrequestex.md">USBD_CreateConfigurationRequestEx</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_INTERFACE_LIST_ENTRY structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
