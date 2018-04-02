---
UID: NS:ucxusbdevice._UCX_USBDEVICE_CHARACTERISTIC
title: "_UCX_USBDEVICE_CHARACTERISTIC"
author: windows-driver-content
description: Stores the characteristics of an device.
old-location: buses\ucx_usbdevice_characteristic.htm
old-project: usbref
ms.assetid: 31BF5607-51EA-4FBF-A754-872FBD45915D
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUCX_USBDEVICE_CHARACTERISTIC, PUCX_USBDEVICE_CHARACTERISTIC, PUCX_USBDEVICE_CHARACTERISTIC structure pointer [Buses], UCX_USBDEVICE_CHARACTERISTIC, UCX_USBDEVICE_CHARACTERISTIC structure [Buses], _UCX_USBDEVICE_CHARACTERISTIC, buses.ucx_usbdevice_characteristic, ucxusbdevice/PUCX_USBDEVICE_CHARACTERISTIC, ucxusbdevice/UCX_USBDEVICE_CHARACTERISTIC"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ucxusbdevice.h
api_name:
-	UCX_USBDEVICE_CHARACTERISTIC
product: Windows
targetos: Windows
req.typenames: UCX_USBDEVICE_CHARACTERISTIC, *PUCX_USBDEVICE_CHARACTERISTIC
req.product: Windows 10 or later.
---

# _UCX_USBDEVICE_CHARACTERISTIC structure
Stores the characteristics of an device.

## Syntax
```
typedef struct _UCX_USBDEVICE_CHARACTERISTIC {
  ULONG                             Size;
  UCX_USBDEVICE_CHARACTERISTIC_TYPE CharacteristicType;
  union {
    UCX_USBDEVICE_CHARACTERISTIC_PATH_DELAY PathDelay;
  };
} *PUCX_USBDEVICE_CHARACTERISTIC, UCX_USBDEVICE_CHARACTERISTIC;
```

## Members


`Size`

Size of this structure.

`CharacteristicType`

A <a href="https://msdn.microsoft.com/86FA72CC-C23F-40B9-9FDD-80C3B0D5EA73">UCX_USBDEVICE_CHARACTERISTIC_TYPE</a>-type value that indicates the type of device characteristic.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | ucxusbdevice.h (include Ucxclass.h) |

## See Also

<a href="https://msdn.microsoft.com/EE8568F6-3D88-477E-9F0D-044D014EBCF3">EVT_UCX_USBDEVICE_GET_CHARACTERISTIC</a>