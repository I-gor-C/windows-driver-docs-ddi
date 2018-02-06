---
UID: NE:ntddrilapitypes.RILEQUIPMENTSTATE
title: RILEQUIPMENTSTATE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilequipmentstate.htm
old-project: netvista
ms.assetid: aa00ebc4-c8de-4a73-ad43-77f4e173e617
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RILEQUIPMENTSTATE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILEQUIPMENTSTATE, ntddrilapitypes/RIL_EQSTATE_FULL, RIL_EQSTATE_SHUTDOWN, RIL_EQSTATE_FULL, netvista.rilequipmentstate, ntddrilapitypes/RIL_EQSTATE_SHUTDOWN, RIL_EQSTATE_MAX, ntddrilapitypes/RIL_EQSTATE_MAX, RILEQUIPMENTSTATE
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
-	RILEQUIPMENTSTATE
product: Windows
targetos: Windows
req.typenames: RILEQUIPMENTSTATE
---

# RILEQUIPMENTSTATE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILEQUIPMENTSTATE { 
  RIL_EQSTATE_FULL,
  RIL_EQSTATE_SHUTDOWN,
  RIL_EQSTATE_MAX
} RILEQUIPMENTSTATE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_EQSTATE_FULL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EQSTATE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EQSTATE_MINIMUM</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_EQSTATE_SHUTDOWN</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |