---
UID: NE:rilapitypes.RILSYSTEMSELECTIONPREFSMODE
title: RILSYSTEMSELECTIONPREFSMODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsystemselectionprefsmode.htm
old-project: netvista
ms.assetid: f2d9bb70-cb0c-4e4b-be7a-11a89df739be
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILSYSTEMSELECTIONPREFSMODE, RILSYSTEMSELECTIONPREFSMODE enumeration [Network Drivers Starting with Windows Vista], RIL_OPSELMODE_MANUAL, RIL_OPSELMODE_MAX, netvista.rilsystemselectionprefsmode, ntddrilapitypes/RILSYSTEMSELECTIONPREFSMODE, ntddrilapitypes/RIL_OPSELMODE_MANUAL, ntddrilapitypes/RIL_OPSELMODE_MAX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
-	RILSYSTEMSELECTIONPREFSMODE
product:
- Windows
targetos: Windows
req.typenames: RILSYSTEMSELECTIONPREFSMODE
req.product: Windows 10 or later.
---

# RILSYSTEMSELECTIONPREFSMODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILSYSTEMSELECTIONPREFSMODE {
  RIL_OPSELMODE_AUTOMATIC  ,
  RIL_OPSELMODE_MANUAL     ,
  RIL_OPSELMODE_MAX
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_OPSELMODE_AUTOMATIC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSELMODE_MANUAL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_OPSELMODE_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |