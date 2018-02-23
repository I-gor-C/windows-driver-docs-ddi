---
UID: NE:ntddrilapitypes.RILCALLMODIFICATIONINFOPARAMMASK
title: RILCALLMODIFICATIONINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationinfoparammask.htm
old-project: netvista
ms.assetid: 1282f158-9e41-4789-abe9-181f367ea235
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RIL_PARAM_CMI_NEWCALLTYPE, netvista.rilcallmodificationinfoparammask, ntddrilapitypes/RIL_PARAM_CMI_ALPHAIDENTIFIER, ntddrilapitypes/RIL_PARAM_CMI_NEWCALLTYPE, RILCALLMODIFICATIONINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_CMI_MODIFICATIONTYPE, RIL_PARAM_CMI_ALL, ntddrilapitypes/RIL_PARAM_CMI_ADDRESS, RIL_PARAM_CMI_ID, RIL_PARAM_CMI_ADDRESS, RILCALLMODIFICATIONINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_CMI_ID, ntddrilapitypes/RIL_PARAM_CMI_MODIFICATIONTYPE, RIL_PARAM_CMI_OLDCALLTYPE, RIL_PARAM_CMI_ALPHAIDENTIFIER, ntddrilapitypes/RIL_PARAM_CMI_OLDCALLTYPE, ntddrilapitypes/RIL_PARAM_CMI_ALL, ntddrilapitypes/RILCALLMODIFICATIONINFOPARAMMASK
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
-	RILCALLMODIFICATIONINFOPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILCALLMODIFICATIONINFOPARAMMASK
---

# RILCALLMODIFICATIONINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLMODIFICATIONINFOPARAMMASK { 
  RIL_PARAM_CMI_ID,
  RIL_PARAM_CMI_MODIFICATIONTYPE,
  RIL_PARAM_CMI_OLDCALLTYPE,
  RIL_PARAM_CMI_NEWCALLTYPE,
  RIL_PARAM_CMI_ADDRESS,
  RIL_PARAM_CMI_ALPHAIDENTIFIER,
  RIL_PARAM_CMI_ALL
} RILCALLMODIFICATIONINFOPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_CMI_ADDRESS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_ALPHAIDENTIFIER</td>
                    <td></td>
                </tr>
            
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
                    <td>RIL_PARAM_CMI_NEWCALLTYPE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CMI_OLDCALLTYPE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |