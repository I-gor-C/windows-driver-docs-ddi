---
UID: NE:nfccx._NFC_CX_TRANSPORT_TYPE
title: "_NFC_CX_TRANSPORT_TYPE"
author: windows-driver-content
description: The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types.
old-location: nfpdrivers\nfc_cx_transport_type.htm
old-project: nfpdrivers
ms.assetid: CC8BEC9A-87F6-4C50-A8FA-ED2A2A5D2934
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PNFC_CX_TRANSPORT_TYPE, NFC_CX_TRANSPORT_CUSTOM, NFC_CX_TRANSPORT_I2C, NFC_CX_TRANSPORT_SPI, NFC_CX_TRANSPORT_TYPE, NFC_CX_TRANSPORT_TYPE enumeration [Near-Field Proximity Drivers], NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE, NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE enumeration [Near-Field Proximity Drivers], NFC_CX_TRANSPORT_UART, _NFC_CX_TRANSPORT_TYPE, nfccx/NFC_CX_TRANSPORT_CUSTOM, nfccx/NFC_CX_TRANSPORT_I2C, nfccx/NFC_CX_TRANSPORT_SPI, nfccx/NFC_CX_TRANSPORT_TYPE, nfccx/NFC_CX_TRANSPORT_UART, nfpdrivers.nfc_cx_transport_type"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfccx.h
req.include-header: Ncidef.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: None supported
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
req.irql: Requires same
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	nfccx.h
api_name:
-	NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE
product:
- Windows
targetos: Windows
req.typenames: NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE
---

# _NFC_CX_TRANSPORT_TYPE Enumeration
The NFC_CX_TRANSPORT_TYPE enumeration specifies transport types.

## Syntax
```
typedef enum _NFC_CX_TRANSPORT_TYPE {
  NFC_CX_TRANSPORT_I2C     ,
  NFC_CX_TRANSPORT_SPI     ,
  NFC_CX_TRANSPORT_UART    ,
  NFC_CX_TRANSPORT_CUSTOM
} NFC_CX_TRANSPORT_TYPE, *PNFC_CX_TRANSPORT_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>NFC_CX_TRANSPORT_I2C</td>
                    <td>Specifies an Inter-Integrated Circuit (I2C) bus.</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_TRANSPORT_SPI</td>
                    <td>Specifies a Serial Peripheral Interface (SPI).</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_TRANSPORT_UART</td>
                    <td>Specifies a Universal Asynchronous Receiver/Transmitter (UART).</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_TRANSPORT_CUSTOM</td>
                    <td>Specifies a custom transport type.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | nfccx.h (include Ncidef.h) |

## See Also

<a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a>



<a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a>