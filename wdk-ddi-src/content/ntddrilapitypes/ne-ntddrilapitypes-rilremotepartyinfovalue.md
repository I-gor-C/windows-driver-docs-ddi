---
UID: NE:ntddrilapitypes.RILREMOTEPARTYINFOVALUE
title: RILREMOTEPARTYINFOVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilremotepartyinfovalue.htm
old-project: netvista
ms.assetid: 9cc766c4-a2c0-4b84-a4d8-b005cddd9eea
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILREMOTEPARTYINFOVALUE, RILREMOTEPARTYINFOVALUE enumeration [Network Drivers Starting with Windows Vista], RIL_REMOTEPARTYINFO_MAX, RIL_REMOTEPARTYINFO_UNAVAILABLE, RIL_REMOTEPARTYINFO_WITHHELD, netvista.rilremotepartyinfovalue, ntddrilapitypes/RILREMOTEPARTYINFOVALUE, ntddrilapitypes/RIL_REMOTEPARTYINFO_MAX, ntddrilapitypes/RIL_REMOTEPARTYINFO_UNAVAILABLE, ntddrilapitypes/RIL_REMOTEPARTYINFO_WITHHELD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: Rilapitypes.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddrilapitypes.h
api_name:
-	RILREMOTEPARTYINFOVALUE
product: Windows
targetos: Windows
req.typenames: RILREMOTEPARTYINFOVALUE
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
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |