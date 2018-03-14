---
UID: NE:rilapitypes.RILSUPSERVICEDATAPARAMMASK
title: RILSUPSERVICEDATAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupservicedataparammask.htm
old-project: netvista
ms.assetid: 2b0ff5a7-02b3-4a22-98da-d13825bc2f45
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: RILSUPSERVICEDATAPARAMMASK, RILSUPSERVICEDATAPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_SSDI_ALL, RIL_PARAM_SSDI_CC_ERROR, RIL_PARAM_SSDI_DATA, RIL_PARAM_SSDI_DATASIZE, RIL_PARAM_SSDI_SS_ERROR, RIL_PARAM_SSDI_STATUS, RIL_PARAM_SSDI_VENDOR_ERROR, netvista.rilsupservicedataparammask, ntddrilapitypes/RILSUPSERVICEDATAPARAMMASK, ntddrilapitypes/RIL_PARAM_SSDI_ALL, ntddrilapitypes/RIL_PARAM_SSDI_CC_ERROR, ntddrilapitypes/RIL_PARAM_SSDI_DATA, ntddrilapitypes/RIL_PARAM_SSDI_DATASIZE, ntddrilapitypes/RIL_PARAM_SSDI_SS_ERROR, ntddrilapitypes/RIL_PARAM_SSDI_STATUS, ntddrilapitypes/RIL_PARAM_SSDI_VENDOR_ERROR
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
-	RILSUPSERVICEDATAPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILSUPSERVICEDATAPARAMMASK
req.product: Windows 10 or later.
---

# RILSUPSERVICEDATAPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSUPSERVICEDATAPARAMMASK { 
  RIL_PARAM_SSDI_STATUS,
  RIL_PARAM_SSDI_SS_ERROR,
  RIL_PARAM_SSDI_CC_ERROR,
  RIL_PARAM_SSDI_VENDOR_ERROR,
  RIL_PARAM_SSDI_DATASIZE,
  RIL_PARAM_SSDI_DATA,
  RIL_PARAM_SSDI_ALL
} RILSUPSERVICEDATAPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_SSDI_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SSDI_CC_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SSDI_DATA</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SSDI_DATASIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SSDI_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SSDI_SS_ERROR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SSDI_STATUS</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_SSDI_VENDOR_ERROR</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |