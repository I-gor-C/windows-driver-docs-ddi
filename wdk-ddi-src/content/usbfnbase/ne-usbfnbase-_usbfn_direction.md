---
UID: NE:usbfnbase._USBFN_DIRECTION
title: "_USBFN_DIRECTION"
author: windows-driver-content
description: Defines the USB data transfer direction types.
old-location: buses\usbfn_direction.htm
old-project: usbref
ms.assetid: C6E1FA5A-993C-4212-9428-0B759C09F5DE
ms.author: windowsdriverdev
ms.date: 2/8/2018
ms.keywords: UsbfnDirectionOut, usbfnbase/USBFN_DIRECTION, USBFN_DIRECTION enumeration [Buses], usbfnbase/UsbfnDirectionIn, usbfnbase/UsbfnDirectionTx, UsbfnDirectionMinimum, usbfnbase/UsbfnDirectionMinimum, *PUSBFN_DIRECTION, USBFN_DIRECTION, usbfnbase/UsbfnDirectionRx, UsbfnDirectionTx, UsbfnDirectionIn, UsbfnDirectionMaximum, buses.usbfn_direction, usbfnbase/UsbfnDirectionMaximum, usbfnbase/UsbfnDirectionOut, _USBFN_DIRECTION, UsbfnDirectionRx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	usbfnbase.h
apiname:
-	USBFN_DIRECTION
product: Windows
targetos: Windows
req.typenames: USBFN_DIRECTION, *PUSBFN_DIRECTION
req.product: Windows 10 or later.
---

# _USBFN_DIRECTION Enumeration
Defines the USB data transfer direction types.

## Syntax
````
typedef enum _USBFN_DIRECTION { 
  UsbfnDirectionMinimum  = 0x0,
  UsbfnDirectionIn,
  UsbfnDirectionOut,
  UsbfnDirectionTx       = UsbfnDirectionIn,
  UsbfnDirectionRx       = UsbfnDirectionOut,
  UsbfnDirectionMaximum
} USBFN_DIRECTION;
````

## Constants

<table>
            
                <tr>
                    <td>UsbfnDirectionIn</td>
                    <td>The transfer is to the host from an endpoint.</td>
                </tr>
            
                <tr>
                    <td>UsbfnDirectionMaximum</td>
                    <td>The maximum value in this enumeration.</td>
                </tr>
            
                <tr>
                    <td>UsbfnDirectionMinimum</td>
                    <td>The minimum value in this enumeration.</td>
                </tr>
            
                <tr>
                    <td>UsbfnDirectionOut</td>
                    <td>The transfer is from the host to the endpoint.</td>
                </tr>
            
                <tr>
                    <td>UsbfnDirectionRx</td>
                    <td>The bus transfer is from the host to the device.</td>
                </tr>
            
                <tr>
                    <td>UsbfnDirectionTx</td>
                    <td>The bus transfer to the host from the device.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbfnbase.h |