---
UID: NE:nfccx._NFC_CX_POLL_MODE_CONFIG
title: "_NFC_CX_POLL_MODE_CONFIG"
author: windows-driver-content
description: The NFC_CX_POLL_MODE_CONFIG enumeration specifies poll mode.
old-location: nfpdrivers\nfc_cx_poll_mode_config.htm
old-project: nfpdrivers
ms.assetid: A073D570-DF55-424E-8E86-49DE6A31E6FB
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PNFC_CX_POLL_MODE_CONFIG, NFC_CX_POLL_DEFAULT, NFC_CX_POLL_MODE_CONFIG, NFC_CX_POLL_MODE_CONFIG enumeration [Near-Field Proximity Drivers], NFC_CX_POLL_MODE_CONFIG, *PNFC_CX_POLL_MODE_CONFIG, NFC_CX_POLL_MODE_CONFIG, *PNFC_CX_POLL_MODE_CONFIG enumeration [Near-Field Proximity Drivers], NFC_CX_POLL_NFC_15693, NFC_CX_POLL_NFC_A, NFC_CX_POLL_NFC_ACTIVE, NFC_CX_POLL_NFC_B, NFC_CX_POLL_NFC_F_212, NFC_CX_POLL_NFC_F_424, PNFC_CX_POLL_MODE_CONFIG, _NFC_CX_POLL_MODE_CONFIG, nfccx/NFC_CX_POLL_DEFAULT, nfccx/NFC_CX_POLL_MODE_CONFIG, nfccx/NFC_CX_POLL_NFC_15693, nfccx/NFC_CX_POLL_NFC_A, nfccx/NFC_CX_POLL_NFC_ACTIVE, nfccx/NFC_CX_POLL_NFC_B, nfccx/NFC_CX_POLL_NFC_F_212, nfccx/NFC_CX_POLL_NFC_F_424, nfpdrivers.nfc_cx_poll_mode_config"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: nfccx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
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
req.irql: Requires same
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	nfccx.h
api_name:
-	NFC_CX_POLL_MODE_CONFIG, *PNFC_CX_POLL_MODE_CONFIG
product: Windows
targetos: Windows
req.typenames: NFC_CX_POLL_MODE_CONFIG, *PNFC_CX_POLL_MODE_CONFIG
---

# _NFC_CX_POLL_MODE_CONFIG Enumeration
The NFC_CX_POLL_MODE_CONFIG enumeration specifies poll mode.

## Syntax
```
typedef enum _NFC_CX_POLL_MODE_CONFIG {
  NFC_CX_POLL_NFC_A        ,
  NFC_CX_POLL_NFC_B        ,
  NFC_CX_POLL_NFC_F_212    ,
  NFC_CX_POLL_NFC_F_424    ,
  NFC_CX_POLL_NFC_15693    ,
  NFC_CX_POLL_NFC_ACTIVE   ,
  NFC_CX_POLL_NFC_A_KOVIO  ,
  NFC_CX_POLL_DEFAULT
} *PNFC_CX_POLL_MODE_CONFIG, NFC_CX_POLL_MODE_CONFIG;
```

## Constants

<table>
            
                <tr>
                    <td>NFC_CX_POLL_NFC_A</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NFC_CX_POLL_NFC_B</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NFC_CX_POLL_NFC_F_212</td>
                    <td>NFC-F poll mode (212 kbps)</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_POLL_NFC_F_424</td>
                    <td>NFC-F poll mode (424 kbps)</td>
                </tr>
            
                <tr>
                    <td>NFC_CX_POLL_NFC_15693</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NFC_CX_POLL_NFC_ACTIVE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NFC_CX_POLL_NFC_A_KOVIO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>NFC_CX_POLL_DEFAULT</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | nfccx.h |

## See Also

<a href="https://msdn.microsoft.com/windows/hardware/drivers/nfc/nfc-class-extension-">NFC class extension design guide</a>



<a href="http://go.microsoft.com/fwlink/p/?LinkID=785320">Near field communication (NFC) design guide</a>