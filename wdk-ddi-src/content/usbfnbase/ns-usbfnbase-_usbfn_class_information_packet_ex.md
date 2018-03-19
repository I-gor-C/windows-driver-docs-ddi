---
UID: NS:usbfnbase._USBFN_CLASS_INFORMATION_PACKET_EX
title: "_USBFN_CLASS_INFORMATION_PACKET_EX"
author: windows-driver-content
description: Describes device interface class information associated with a USB interface. This structure can be used to describe single and multi-interface functions.
old-location: buses\usbfn_class_information_packet_ex.htm
old-project: usbref
ms.assetid: 373D7CA9-AF1B-46E8-AE6A-F693A9214527
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: "*PUSBFN_CLASS_INFORMATION_PACKET_EX, PUSBFN_CLASS_INFORMATION_PACKET_EX, PUSBFN_CLASS_INFORMATION_PACKET_EX structure pointer [Buses], USBFN_CLASS_INFORMATION_PACKET_EX, USBFN_CLASS_INFORMATION_PACKET_EX structure [Buses], _USBFN_CLASS_INFORMATION_PACKET_EX, buses.usbfn_class_information_packet_ex, usbfnbase/PUSBFN_CLASS_INFORMATION_PACKET_EX, usbfnbase/USBFN_CLASS_INFORMATION_PACKET_EX"
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
-	USBFN_CLASS_INFORMATION_PACKET_EX
product: Windows
targetos: Windows
req.typenames: USBFN_CLASS_INFORMATION_PACKET_EX, *PUSBFN_CLASS_INFORMATION_PACKET_EX
req.product: Windows 10 or later.
---

# _USBFN_CLASS_INFORMATION_PACKET_EX structure
Describes device interface class information associated with a USB interface. This structure can be used to describe single and multi-interface functions.

## Syntax
````
typedef struct _USBFN_CLASS_INFORMATION_PACKET_EX {
  USBFN_CLASS_INTERFACE_EX FullSpeedClassInterface;
  USBFN_CLASS_INTERFACE_EX HighSpeedClassInterface;
  USBFN_CLASS_INTERFACE    SuperSpeedClassInterface;
  WCHAR                    InterfaceName[MAX_INTERFACE_NAME_LENGTH];
  WCHAR                    InterfaceGuid[MAX_INTERFACE_GUID_LENGTH];
  BOOLEAN                  HasInterfaceGuid;
} USBFN_CLASS_INFORMATION_PACKET_EX, *PUSBFN_CLASS_INFORMATION_PACKET_EX;
````

## Members


`FullSpeedClassInterfaceEx`



`HighSpeedClassInterfaceEx`



`SuperSpeedClassInterfaceEx`



`InterfaceName`



`InterfaceGuid`



`HasInterfaceGuid`

Determines whether the driver has published a device interface is GUID.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbfnbase.h |

## See Also

<a href="..\wdfdevice\nf-wdfdevice-wdfdevicesetdeviceinterfacestate.md">WdfDeviceSetDeviceInterfaceState</a>



<a href="..\wdfdevice\nf-wdfdevice-wdfdevicecreatesymboliclink.md">WdfDeviceCreateSymbolicLink</a>



<a href="..\usbfnbase\ns-usbfnbase-_usbfn_class_interface.md">USBFN_CLASS_INTERFACE</a>