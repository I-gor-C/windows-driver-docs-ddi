---
UID: NE:ntddrilapitypes.RILCALLINFOMULTIPARTY
title: RILCALLINFOMULTIPARTY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfomultiparty.htm
old-project: netvista
ms.assetid: 4a343e55-9150-4411-bf37-f410b94ca0aa
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILCALLINFOMULTIPARTY, RILCALLINFOMULTIPARTY enumeration [Network Drivers Starting with Windows Vista], RIL_CALL_MAX, RIL_CALL_MULTIPARTY, netvista.rilcallinfomultiparty, ntddrilapitypes/RILCALLINFOMULTIPARTY, ntddrilapitypes/RIL_CALL_MAX, ntddrilapitypes/RIL_CALL_MULTIPARTY
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
-	RILCALLINFOMULTIPARTY
product: Windows
targetos: Windows
req.typenames: RILCALLINFOMULTIPARTY
---

# RILCALLINFOMULTIPARTY Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILCALLINFOMULTIPARTY {
  RIL_CALL_SINGLEPARTY  ,
  RIL_CALL_MULTIPARTY   ,
  RIL_CALL_MAX
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_CALL_SINGLEPARTY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALL_MULTIPARTY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALL_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |