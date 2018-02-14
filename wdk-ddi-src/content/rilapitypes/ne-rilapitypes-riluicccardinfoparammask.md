---
UID: NE:rilapitypes.RILUICCCARDINFOPARAMMASK
title: RILUICCCARDINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicccardinfoparammask_2.htm
old-project: netvista
ms.assetid: f27c7f54-f939-4e9b-a27c-b0137fbb7cec
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: rilapitypes/RIL_PARAM_CARDINFO_NUMAPPS, RIL_PARAM_CARDINFO_APPINFO, rilapitypes/RIL_PARAM_CARDINFO_ALL, RILUICCCARDINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_CARDINFO_APPINFO, rilapitypes/RIL_PARAM_CARDINFO_ICCID, RIL_PARAM_CARDINFO_ICCID, netvista.riluicccardinfoparammask_2, RIL_PARAM_CARDINFO_ALL, RILUICCCARDINFOPARAMMASK, rilapitypes/RILUICCCARDINFOPARAMMASK, RIL_PARAM_CARDINFO_NUMAPPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rilapitypes.h
apiname:
-	RILUICCCARDINFOPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILUICCCARDINFOPARAMMASK
req.product: Windows 10 or later.
---

# RILUICCCARDINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUICCCARDINFOPARAMMASK { 
  RIL_PARAM_CARDINFO_ICCID,
  RIL_PARAM_CARDINFO_NUMAPPS,
  RIL_PARAM_CARDINFO_APPINFO,
  RIL_PARAM_CARDINFO_ALL
} RILUICCCARDINFOPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_CARDINFO_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CARDINFO_APPINFO</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CARDINFO_ICCID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CARDINFO_ISVIRTUAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CARDINFO_NUMAPPS</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |