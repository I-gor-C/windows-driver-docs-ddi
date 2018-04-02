---
UID: NE:rilapitypes.RILCALLTYPE
title: RILCALLTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcalltype.htm
old-project: netvista
ms.assetid: bd6b9e57-f50b-4743-9c51-066940aad200
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILCALLTYPE, RILCALLTYPE enumeration [Network Drivers Starting with Windows Vista], RIL_CALLTYPE_DATA, RIL_CALLTYPE_FAX, RIL_CALLTYPE_IMS, RIL_CALLTYPE_MAX, RIL_CALLTYPE_PTT, RIL_CALLTYPE_SUPSVC, RIL_CALLTYPE_USSD, RIL_CALLTYPE_VOICE, RIL_CALLTYPE_VT, netvista.rilcalltype, ntddrilapitypes/RILCALLTYPE, ntddrilapitypes/RIL_CALLTYPE_DATA, ntddrilapitypes/RIL_CALLTYPE_FAX, ntddrilapitypes/RIL_CALLTYPE_IMS, ntddrilapitypes/RIL_CALLTYPE_MAX, ntddrilapitypes/RIL_CALLTYPE_PTT, ntddrilapitypes/RIL_CALLTYPE_SUPSVC, ntddrilapitypes/RIL_CALLTYPE_USSD, ntddrilapitypes/RIL_CALLTYPE_VOICE, ntddrilapitypes/RIL_CALLTYPE_VT
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
-	RILCALLTYPE
product: Windows
targetos: Windows
req.typenames: RILCALLTYPE
req.product: Windows 10 or later.
---

# RILCALLTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILCALLTYPE {
  RIL_CALLTYPE_UNKNOWN  ,
  RIL_CALLTYPE_VOICE    ,
  RIL_CALLTYPE_DATA     ,
  RIL_CALLTYPE_FAX      ,
  RIL_CALLTYPE_PTT      ,
  RIL_CALLTYPE_VT       ,
  RIL_CALLTYPE_USSD     ,
  RIL_CALLTYPE_SUPSVC   ,
  RIL_CALLTYPE_IMS      ,
  RIL_CALLTYPE_MAX
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_CALLTYPE_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_VOICE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_FAX</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_PTT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_VT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_USSD</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_SUPSVC</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_IMS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_CALLTYPE_MAX</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |