---
UID: NE:ucxcontroller._UCX_CONTROLLER_PARENT_BUS_TYPE
title: "_UCX_CONTROLLER_PARENT_BUS_TYPE"
author: windows-driver-content
description: The UCX_CONTROLLER_PARENT_BUS_TYPE enumeration defines the parent bus type.
old-location: buses\ucx_controller_parent_bus_type.htm
old-project: usbref
ms.assetid: FD78074D-E128-4085-A178-0133C9256E42
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: UCX_CONTROLLER_PARENT_BUS_TYPE, UCX_CONTROLLER_PARENT_BUS_TYPE enumeration [Buses], UcxControllerParentBusTypeAcpi, UcxControllerParentBusTypeCustom, UcxControllerParentBusTypePci, _UCX_CONTROLLER_PARENT_BUS_TYPE, buses.ucx_controller_parent_bus_type, ucxcontroller/UCX_CONTROLLER_PARENT_BUS_TYPE, ucxcontroller/UcxControllerParentBusTypeAcpi, ucxcontroller/UcxControllerParentBusTypeCustom, ucxcontroller/UcxControllerParentBusTypePci
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucxcontroller.h
req.include-header: Ucxclass.h
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
-	Ucxcontroller.h
api_name:
-	UCX_CONTROLLER_PARENT_BUS_TYPE
product: Windows
targetos: Windows
req.typenames: UCX_CONTROLLER_PARENT_BUS_TYPE
req.product: Windows 10 or later.
---

# _UCX_CONTROLLER_PARENT_BUS_TYPE Enumeration
The <b>UCX_CONTROLLER_PARENT_BUS_TYPE</b> enumeration defines the parent bus type.

## Syntax
````
typedef enum _UCX_CONTROLLER_PARENT_BUS_TYPE { 
  UcxControllerParentBusTypeCustom,
  UcxControllerParentBusTypePci,
  UcxControllerParentBusTypeAcpi
} UCX_CONTROLLER_PARENT_BUS_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>UcxControllerParentBusTypeCustom</td>
                    <td>Custom bus type.</td>
                </tr>
            
                <tr>
                    <td>UcxControllerParentBusTypePci</td>
                    <td>Parent bus is PCI.</td>
                </tr>
            
                <tr>
                    <td>UcxControllerParentBusTypeAcpi</td>
                    <td>Parent is ACPI.</td>
                </tr>
            
                <tr>
                    <td>UcxControllerParentBusTypeMaUsb</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ucxcontroller.h (include Ucxclass.h) |

## See Also

<a href="..\ucxcontroller\ns-ucxcontroller-_ucx_controller_config.md">UCX_CONTROLLER_CONFIG</a>