---
UID: NE:bthddi._CODING_FORMAT
title: "_CODING_FORMAT"
author: windows-driver-content
description: This enumeration is for internal use only.
old-location: bltooth\coding_format.htm
old-project: bltooth
ms.assetid: 3A97BBAF-47B0-4987-B5EC-2B3A40F2B42D
ms.author: windowsdriverdev
ms.date: 12/21/2017
ms.keywords: bthddi/, *PCODING_FORMAT, CODING_FORMAT, CODING_FORMAT enumeration [Bluetooth Devices], _CODING_FORMAT, bthddi/PCODING_FORMAT, PCODING_FORMAT enumeration pointer [Bluetooth Devices], bthddi/CODING_FORMAT, bltooth.coding_format, PCODING_FORMAT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthddi.h
req.include-header: Bthddi.h
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
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	bthddi.h
apiname:
-	CODING_FORMAT
product: Windows
targetos: Windows
req.typenames: "*PCODING_FORMAT, CODING_FORMAT"
---

# _CODING_FORMAT Enumeration
This enumeration is for internal use only.

## Syntax
````
typedef enum _CODING_FORMAT { 
    = 
} CODING_FORMAT, *PCODING_FORMAT;
````

## Constants

<table>
            
                <tr>
                    <td>ScoCodingFormatALaw</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ScoCodingFormatCVSD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ScoCodingFormatLinearPCM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ScoCodingFormatMSBC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ScoCodingFormatTransparent</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ScoCodingFormatULaw</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ScoCodingFormatVendorSpecific</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | bthddi.h (include Bthddi.h) |