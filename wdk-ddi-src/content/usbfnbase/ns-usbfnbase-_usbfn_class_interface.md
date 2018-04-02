---
UID: NS:usbfnbase._USBFN_CLASS_INTERFACE
title: "_USBFN_CLASS_INTERFACE"
author: windows-driver-content
description: Describes an interface and its endpoints.
old-location: buses\usbfn_class_interface.htm
old-project: usbref
ms.assetid: D7173157-D532-4E71-A4E5-55A3B9626DB8
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PUSBFN_CLASS_INTERFACE, PUSBFN_CLASS_INTERFACE, PUSBFN_CLASS_INTERFACE structure pointer [Buses], USBFN_CLASS_INTERFACE, USBFN_CLASS_INTERFACE structure [Buses], _USBFN_CLASS_INTERFACE, buses.usbfn_class_interface, usbfnbase/PUSBFN_CLASS_INTERFACE, usbfnbase/USBFN_CLASS_INTERFACE"
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
-	USBFN_CLASS_INTERFACE
product: Windows
targetos: Windows
req.typenames: USBFN_CLASS_INTERFACE, *PUSBFN_CLASS_INTERFACE
req.product: Windows 10 or later.
---

# _USBFN_CLASS_INTERFACE structure
Describes an interface and its endpoints.

## Syntax
```
typedef struct _USBFN_CLASS_INTERFACE {
  UINT8                  InterfaceNumber;
  UINT8                  PipeCount;
  USBFN_PIPE_INFORMATION PipeArr[MAX_NUM_USBFN_PIPES];
} USBFN_CLASS_INTERFACE, *PUSBFN_CLASS_INTERFACE;
```

## Members


`InterfaceNumber`

The index number of the interface.

`PipeCount`

The number of endpoints contained in  the interface.

`PipeArr`

An array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt188003">USBFN_PIPE_INFORMATION</a> structures that describes the endpoints in the interface.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbfnbase.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt188003">USBFN_PIPE_INFORMATION</a>