---
UID: NS:usbfnbase._USBFN_CLASS_INFORMATION_PACKET
title: "_USBFN_CLASS_INFORMATION_PACKET"
author: windows-driver-content
description: Describes device interface class information associated with a USB interface. This structure can only hold information about a single function interface.
old-location: buses\usbfn_class_information_packet.htm
old-project: usbref
ms.assetid: 18A07670-B610-4D09-8BF0-3C55E781A68B
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSBFN_CLASS_INFORMATION_PACKET, PUSBFN_CLASS_INFORMATION_PACKET, PUSBFN_CLASS_INFORMATION_PACKET structure pointer [Buses], USBFN_CLASS_INFORMATION_PACKET, USBFN_CLASS_INFORMATION_PACKET structure [Buses], _USBFN_CLASS_INFORMATION_PACKET, buses.usbfn_class_information_packet, usbfnbase/PUSBFN_CLASS_INFORMATION_PACKET, usbfnbase/USBFN_CLASS_INFORMATION_PACKET"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	usbfnbase.h
api_name:
-	USBFN_CLASS_INFORMATION_PACKET
product: Windows
targetos: Windows
req.typenames: USBFN_CLASS_INFORMATION_PACKET, *PUSBFN_CLASS_INFORMATION_PACKET
req.product: Windows 10 or later.
---

# _USBFN_CLASS_INFORMATION_PACKET structure
Describes device interface class information associated with a USB interface. This structure can only hold information about a single function interface.

## Syntax
```
typedef struct _USBFN_CLASS_INFORMATION_PACKET {
  USBFN_CLASS_INTERFACE FullSpeedClassInterface;
  USBFN_CLASS_INTERFACE HighSpeedClassInterface;
  WCHAR                 InterfaceName[MAX_INTERFACE_NAME_LENGTH];
  WCHAR                 InterfaceGuid[MAX_INTERFACE_GUID_LENGTH];
  BOOLEAN               HasInterfaceGuid;
  USBFN_CLASS_INTERFACE SuperSpeedClassInterface;
} USBFN_CLASS_INFORMATION_PACKET, *PUSBFN_CLASS_INFORMATION_PACKET;
```

## Members


`FullSpeedClassInterface`

A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a> structure that describes an interface for full speed device.

`HighSpeedClassInterface`

A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a> structure that describes an interface for high speed device.

`InterfaceName`



`InterfaceGuid`



`HasInterfaceGuid`

Determines whether the driver has published a device interface is GUID.

`SuperSpeedClassInterface`

A <a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a> structure that describes an interface for SuperSpeed device.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbfnbase.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187990">USBFN_CLASS_INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545939">WdfDeviceCreateSymbolicLink</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff546878">WdfDeviceSetDeviceInterfaceState</a>