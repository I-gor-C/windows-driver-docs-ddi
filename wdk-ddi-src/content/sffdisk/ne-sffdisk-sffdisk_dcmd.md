---
UID: NE:sffdisk.SFFDISK_DCMD
title: SFFDISK_DCMD
author: windows-driver-content
description: The SFFDISK_DCMD enumeration identifies the type of Secure Digital (SD) card operation.
old-location: sd\sffdisk_dcmd.htm
old-project: SD
ms.assetid: 145e460e-6988-4e61-bb33-6f1b1df54629
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: SD.sffdisk_dcmd, SFFDISK_DCMD, SFFDISK_DCMD enumeration [Buses], SFFDISK_DC_DEVICE_COMMAND, SFFDISK_DC_GET_VERSION, SFFDISK_DC_LOCK_CHANNEL, SFFDISK_DC_UNLOCK_CHANNEL, sd-structs_440acb4f-89ba-4ea0-9f8b-c7fd241dfe85.xml, sffdisk/SFFDISK_DCMD, sffdisk/SFFDISK_DC_DEVICE_COMMAND, sffdisk/SFFDISK_DC_GET_VERSION, sffdisk/SFFDISK_DC_LOCK_CHANNEL, sffdisk/SFFDISK_DC_UNLOCK_CHANNEL
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sffdisk.h
req.include-header: Sffdisk.h
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
req.irql: Any IRQL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	sffdisk.h
api_name:
-	SFFDISK_DCMD
product:
- Windows
targetos: Windows
req.typenames: SFFDISK_DCMD
req.product: Windows 10 or later.
---

# SFFDISK_DCMD Enumeration
The SFFDISK_DCMD enumeration identifies the type of Secure Digital (SD) card operation.

## Syntax
```
typedef enum SFFDISK_DCMD {
  SFFDISK_DC_GET_VERSION     ,
  SFFDISK_DC_LOCK_CHANNEL    ,
  SFFDISK_DC_UNLOCK_CHANNEL  ,
  SFFDISK_DC_DEVICE_COMMAND
} ;
```

## Constants

<table>
            
                <tr>
                    <td>SFFDISK_DC_GET_VERSION</td>
                    <td>The operations retrieves the version of the card.</td>
                </tr>
            
                <tr>
                    <td>SFFDISK_DC_LOCK_CHANNEL</td>
                    <td>The operation locks the interface channel.</td>
                </tr>
            
                <tr>
                    <td>SFFDISK_DC_UNLOCK_CHANNEL</td>
                    <td>The operation unlocks the interface channel.</td>
                </tr>
            
                <tr>
                    <td>SFFDISK_DC_DEVICE_COMMAND</td>
                    <td>The operation executes a device command.</td>
                </tr>
</table>

## Remarks

Applications that submit IOCTL_SFFDISK_DEVICE_COMMAND requests to the SD stack use this enumeration to specify the type of operation. The application must assign one of the values of this enumeration to the <b>Command</b> member of the <a href="https://msdn.microsoft.com/68205c17-5ff6-45a3-83c7-e106b314f9a5">SFFDISK_DEVICE_COMMAND_DATA</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | sffdisk.h (include Sffdisk.h) |

## See Also

<a href="https://msdn.microsoft.com/68205c17-5ff6-45a3-83c7-e106b314f9a5">SFFDISK_DEVICE_COMMAND_DATA</a>