---
UID: NE:ntddrilapitypes.RILMSGCDMAMSGSTATUSTYPE
title: RILMSGCDMAMSGSTATUSTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmamsgstatustype.htm
old-project: netvista
ms.assetid: 60365fd7-3897-4948-a251-098e5a91c959
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RIL_MSGSTATUSTYPE_READACK, RILMSGCDMAMSGSTATUSTYPE, RILMSGCDMAMSGSTATUSTYPE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILMSGCDMAMSGSTATUSTYPE, netvista.rilmsgcdmamsgstatustype, RIL_MSGSTATUSTYPE_MAX, ntddrilapitypes/RIL_MSGSTATUSTYPE_DELIVERYACK, ntddrilapitypes/RIL_MSGSTATUSTYPE_READACK, RIL_MSGSTATUSTYPE_USERACK, ntddrilapitypes/RIL_MSGSTATUSTYPE_USERACK, RIL_MSGSTATUSTYPE_DELIVERYACK, ntddrilapitypes/RIL_MSGSTATUSTYPE_MAX
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
-	RILMSGCDMAMSGSTATUSTYPE
product: Windows
targetos: Windows
req.typenames: RILMSGCDMAMSGSTATUSTYPE
---

# RILMSGCDMAMSGSTATUSTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGCDMAMSGSTATUSTYPE { 
  RIL_MSGSTATUSTYPE_DELIVERYACK,
  RIL_MSGSTATUSTYPE_USERACK,
  RIL_MSGSTATUSTYPE_READACK,
  RIL_MSGSTATUSTYPE_MAX
} RILMSGCDMAMSGSTATUSTYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_MSGSTATUSTYPE_BEARERACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUSTYPE_DELIVERYACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUSTYPE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUSTYPE_READACK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_MSGSTATUSTYPE_USERACK</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |