---
UID: NE:rilapitypes.RILREMOTEPARTYINFOVALUE
title: RILREMOTEPARTYINFOVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilremotepartyinfovalue_2.htm
old-project: netvista
ms.assetid: bdea158f-6ee5-4e59-be50-efd8027a8645
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RILREMOTEPARTYINFOVALUE enumeration [Network Drivers Starting with Windows Vista], RIL_REMOTEPARTYINFO_WITHHELD, rilapitypes/RIL_REMOTEPARTYINFO_MAX, RIL_REMOTEPARTYINFO_MAX, rilapitypes/RIL_REMOTEPARTYINFO_UNAVAILABLE, rilapitypes/RIL_REMOTEPARTYINFO_WITHHELD, RIL_REMOTEPARTYINFO_UNAVAILABLE, netvista.rilremotepartyinfovalue_2, rilapitypes/RILREMOTEPARTYINFOVALUE, RILREMOTEPARTYINFOVALUE
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
-	RILREMOTEPARTYINFOVALUE
product: Windows
targetos: Windows
req.typenames: RILREMOTEPARTYINFOVALUE
req.product: Windows 10 or later.
---

# RILREMOTEPARTYINFOVALUE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILREMOTEPARTYINFOVALUE { 
  RIL_REMOTEPARTYINFO_WITHHELD,
  RIL_REMOTEPARTYINFO_UNAVAILABLE,
  RIL_REMOTEPARTYINFO_MAX
} RILREMOTEPARTYINFOVALUE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_REMOTEPARTYINFO_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REMOTEPARTYINFO_UNAVAILABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REMOTEPARTYINFO_VALID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_REMOTEPARTYINFO_WITHHELD</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |