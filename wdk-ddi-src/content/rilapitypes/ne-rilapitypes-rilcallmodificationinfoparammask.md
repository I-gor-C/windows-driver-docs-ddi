---
UID: NE:rilapitypes.RILCALLMODIFICATIONINFOPARAMMASK
title: RILCALLMODIFICATIONINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationinfoparammask.htm
old-project: netvista
ms.assetid: 1282f158-9e41-4789-abe9-181f367ea235
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILCALLMODIFICATIONINFOPARAMMASK, RILCALLMODIFICATIONINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_CMI_ADDRESS, RIL_PARAM_CMI_ALL, RIL_PARAM_CMI_ALPHAIDENTIFIER, RIL_PARAM_CMI_ID, RIL_PARAM_CMI_MODIFICATIONTYPE, RIL_PARAM_CMI_NEWCALLTYPE, RIL_PARAM_CMI_OLDCALLTYPE, netvista.rilcallmodificationinfoparammask, ntddrilapitypes/RILCALLMODIFICATIONINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_CMI_ADDRESS, ntddrilapitypes/RIL_PARAM_CMI_ALL, ntddrilapitypes/RIL_PARAM_CMI_ALPHAIDENTIFIER, ntddrilapitypes/RIL_PARAM_CMI_ID, ntddrilapitypes/RIL_PARAM_CMI_MODIFICATIONTYPE, ntddrilapitypes/RIL_PARAM_CMI_NEWCALLTYPE, ntddrilapitypes/RIL_PARAM_CMI_OLDCALLTYPE
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
-	RILCALLMODIFICATIONINFOPARAMMASK
product:
- Windows
targetos: Windows
req.typenames: RILCALLMODIFICATIONINFOPARAMMASK
req.product: Windows 10 or later.
---

# RILCALLMODIFICATIONINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILCALLMODIFICATIONINFOPARAMMASK {
  RIL_PARAM_CMI_EXECUTOR          ,
  RIL_PARAM_CMI_ID                ,
  RIL_PARAM_CMI_MODIFICATIONTYPE  ,
  RIL_PARAM_CMI_OLDCALLTYPE       ,
  RIL_PARAM_CMI_NEWCALLTYPE       ,
  RIL_PARAM_CMI_ADDRESS           ,
  RIL_PARAM_CMI_ALPHAIDENTIFIER   ,
  RIL_PARAM_CMI_ALL
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_CMI_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_ID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_MODIFICATIONTYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_OLDCALLTYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_NEWCALLTYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_ALPHAIDENTIFIER</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |