---
UID: NE:ntddrilapitypes.RILIMSSUBSCRIBETYPE
title: RILIMSSUBSCRIBETYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssubscribetype.htm
old-project: netvista
ms.assetid: 347b42c1-7585-471c-af42-44218da48fa3
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: netvista.rilimssubscribetype, RIL_IMSSUBSCRIBETYPE_MWI, RILIMSSUBSCRIBETYPE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_IMSSUBSCRIBETYPE_MAX, RIL_IMSSUBSCRIBETYPE_CONFERENCE, ntddrilapitypes/RIL_IMSSUBSCRIBETYPE_MWI, RILIMSSUBSCRIBETYPE, ntddrilapitypes/RIL_IMSSUBSCRIBETYPE_CONFERENCE, RIL_IMSSUBSCRIBETYPE_MAX, ntddrilapitypes/RILIMSSUBSCRIBETYPE
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
-	RILIMSSUBSCRIBETYPE
product: Windows
targetos: Windows
req.typenames: RILIMSSUBSCRIBETYPE
---

# RILIMSSUBSCRIBETYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSSUBSCRIBETYPE { 
  RIL_IMSSUBSCRIBETYPE_MWI,
  RIL_IMSSUBSCRIBETYPE_CONFERENCE,
  RIL_IMSSUBSCRIBETYPE_MAX
} RILIMSSUBSCRIBETYPE;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_IMSSUBSCRIBETYPE_CONFERENCE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMSSUBSCRIBETYPE_MAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMSSUBSCRIBETYPE_MWI</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_IMSSUBSCRIBETYPE_REG</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |