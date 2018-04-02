---
UID: NE:rilapitypes.RILCALLHANDOVERSTATEPARAMMASK
title: RILCALLHANDOVERSTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallhandoverstateparammask.htm
old-project: netvista
ms.assetid: 2534a05b-9e7f-4081-af61-721cd1fa82fc
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILCALLHANDOVERSTATEPARAMMASK, RILCALLHANDOVERSTATEPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_HANDOVER_3GPPCAUSE, RIL_PARAM_HANDOVER_ALL, RIL_PARAM_HANDOVER_NEW_TYPE, RIL_PARAM_HANDOVER_OLD_TYPE, netvista.rilcallhandoverstateparammask, ntddrilapitypes/RILCALLHANDOVERSTATEPARAMMASK, ntddrilapitypes/RIL_PARAM_HANDOVER_3GPPCAUSE, ntddrilapitypes/RIL_PARAM_HANDOVER_ALL, ntddrilapitypes/RIL_PARAM_HANDOVER_NEW_TYPE, ntddrilapitypes/RIL_PARAM_HANDOVER_OLD_TYPE
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
-	RILCALLHANDOVERSTATEPARAMMASK
product:
- Windows
targetos: Windows
req.typenames: RILCALLHANDOVERSTATEPARAMMASK
req.product: Windows 10 or later.
---

# RILCALLHANDOVERSTATEPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILCALLHANDOVERSTATEPARAMMASK {
  RIL_PARAM_HANDOVER_PHASE      ,
  RIL_PARAM_HANDOVER_OLD_TYPE   ,
  RIL_PARAM_HANDOVER_NEW_TYPE   ,
  RIL_PARAM_HANDOVER_3GPPCAUSE  ,
  RIL_PARAM_HANDOVER_ALL
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_HANDOVER_PHASE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_HANDOVER_OLD_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_HANDOVER_NEW_TYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_HANDOVER_3GPPCAUSE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_HANDOVER_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |