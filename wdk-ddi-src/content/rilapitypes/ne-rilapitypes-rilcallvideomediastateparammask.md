---
UID: NE:rilapitypes.RILCALLVIDEOMEDIASTATEPARAMMASK
title: RILCALLVIDEOMEDIASTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallvideomediastateparammask.htm
old-project: netvista
ms.assetid: e36617c0-8471-417d-9135-bdd29c586172
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILCALLVIDEOMEDIASTATEPARAMMASK, RILCALLVIDEOMEDIASTATEPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_CALLVIDEO_ALL, RIL_PARAM_CALLVIDEO_CONTEXTID, RIL_PARAM_CALLVIDEO_FLAGS, netvista.rilcallvideomediastateparammask, ntddrilapitypes/RILCALLVIDEOMEDIASTATEPARAMMASK, ntddrilapitypes/RIL_PARAM_CALLVIDEO_ALL, ntddrilapitypes/RIL_PARAM_CALLVIDEO_CONTEXTID, ntddrilapitypes/RIL_PARAM_CALLVIDEO_FLAGS
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
-	RILCALLVIDEOMEDIASTATEPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILCALLVIDEOMEDIASTATEPARAMMASK
req.product: Windows 10 or later.
---

# RILCALLVIDEOMEDIASTATEPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLVIDEOMEDIASTATEPARAMMASK { 
  RIL_PARAM_CALLVIDEO_FLAGS,
  RIL_PARAM_CALLVIDEO_CONTEXTID,
  RIL_PARAM_CALLVIDEO_ALL
} RILCALLVIDEOMEDIASTATEPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_CALLVIDEO_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CALLVIDEO_CONTEXTID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CALLVIDEO_FLAGS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_CALLVIDEO_PEERCAPABILITIES</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |