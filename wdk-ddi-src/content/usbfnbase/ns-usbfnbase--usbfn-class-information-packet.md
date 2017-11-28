---
UID: NS.usbfnbase._USBFN_CLASS_INFORMATION_PACKET
title: USBFN_CLASS_INFORMATION_PACKET
author: windows-driver-content
description: Describes device interface class information associated with a USB interface. This structure can only hold information about a single function interface.
old-location: buses\usbfn_class_information_packet.htm
old-project: usbref
ms.assetid: 18A07670-B610-4D09-8BF0-3C55E781A68B
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_CLASS_INFORMATION_PACKET, USBFN_CLASS_INFORMATION_PACKET, *PUSBFN_CLASS_INFORMATION_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbfnbase.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_CLASS_INFORMATION_PACKET
req.alt-loc: usbfnbase.h
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

# USBFN_CLASS_INFORMATION_PACKET structure



## -description
<p>Describes device interface class information associated with a USB interface. This structure can only hold information about a single function interface.</p>


## -syntax

````
typedef struct _USBFN_CLASS_INFORMATION_PACKET {
  USBFN_CLASS_INTERFACE FullSpeedClassInterface;
  USBFN_CLASS_INTERFACE HighSpeedClassInterface;
  WCHAR                 InterfaceName[MAX_INTERFACE_NAME_LENGTH];
  WCHAR                 InterfaceGuid[MAX_INTERFACE_GUID_LENGTH];
  BOOLEAN               HasInterfaceGuid;
  USBFN_CLASS_INTERFACE SuperSpeedClassInterface;
} USBFN_CLASS_INFORMATION_PACKET, *PUSBFN_CLASS_INFORMATION_PACKET;
````


## -struct-fields
<dl>

### -field <b>FullSpeedClassInterface</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a> structure that describes an interface for full speed device.</p>
</dd>

### -field <b>HighSpeedClassInterface</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a> structure that describes an interface for high speed device.</p>
</dd>

### -field <b>InterfaceName[MAX_INTERFACE_NAME_LENGTH]</b>

<dd>
<p>A string that contains the interface name.</p>
</dd>

### -field <b>InterfaceGuid[MAX_INTERFACE_GUID_LENGTH]</b>

<dd>
<p>A string from which the driver can derive the device interface GUID.</p>
</dd>

### -field <b>HasInterfaceGuid</b>

<dd>
<p>Determines whether the driver has published a device interface is GUID. </p>
</dd>

### -field <b>SuperSpeedClassInterface</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a> structure that describes an interface for SuperSpeed device.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbfnbase.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545939">WdfDeviceCreateSymbolicLink</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546878">WdfDeviceSetDeviceInterfaceState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_CLASS_INFORMATION_PACKET structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
