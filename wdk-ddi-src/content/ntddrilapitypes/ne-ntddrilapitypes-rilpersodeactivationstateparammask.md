---
UID: NE:ntddrilapitypes.RILPERSODEACTIVATIONSTATEPARAMMASK
title: RILPERSODEACTIVATIONSTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersodeactivationstateparammask.htm
old-project: netvista
ms.assetid: 11c4388b-5c0d-4133-9c68-059d1af5c2ca
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RILPERSODEACTIVATIONSTATEPARAMMASK, ntddrilapitypes/RILPERSODEACTIVATIONSTATEPARAMMASK, ntddrilapitypes/RIL_PARAM_PDS_ALL, ntddrilapitypes/RIL_PARAM_PDS_CK_ATTEMPTS, netvista.rilpersodeactivationstateparammask, ntddrilapitypes/RIL_PARAM_PDS_PUK_ATTEMPTS, RIL_PARAM_PDS_ALL, RIL_PARAM_PDS_CK_ATTEMPTS, RIL_PARAM_PDS_PUK_ATTEMPTS, RILPERSODEACTIVATIONSTATEPARAMMASK enumeration [Network Drivers Starting with Windows Vista]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
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
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddrilapitypes.h
apiname:
-	RILPERSODEACTIVATIONSTATEPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILPERSODEACTIVATIONSTATEPARAMMASK
---

# RILPERSODEACTIVATIONSTATEPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPERSODEACTIVATIONSTATEPARAMMASK { 
  RIL_PARAM_PDS_CK_ATTEMPTS,
  RIL_PARAM_PDS_PUK_ATTEMPTS,
  RIL_PARAM_PDS_ALL
} RILPERSODEACTIVATIONSTATEPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_PDS_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PDS_CK_ATTEMPTS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PDS_PUK_ATTEMPTS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_PDS_STATE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |