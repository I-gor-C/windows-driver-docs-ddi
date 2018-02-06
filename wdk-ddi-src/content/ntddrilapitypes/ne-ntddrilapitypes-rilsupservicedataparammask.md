---
UID: NE:ntddrilapitypes.RILSUPSERVICEDATAPARAMMASK
title: RILSUPSERVICEDATAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupservicedataparammask.htm
old-project: netvista
ms.assetid: 2b0ff5a7-02b3-4a22-98da-d13825bc2f45
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RIL_PARAM_SSDI_ALL, RILSUPSERVICEDATAPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_SSDI_VENDOR_ERROR, netvista.rilsupservicedataparammask, ntddrilapitypes/RIL_PARAM_SSDI_STATUS, RIL_PARAM_SSDI_DATASIZE, RIL_PARAM_SSDI_STATUS, RIL_PARAM_SSDI_DATA, ntddrilapitypes/RILSUPSERVICEDATAPARAMMASK, ntddrilapitypes/RIL_PARAM_SSDI_SS_ERROR, ntddrilapitypes/RIL_PARAM_SSDI_CC_ERROR, RIL_PARAM_SSDI_CC_ERROR, ntddrilapitypes/RIL_PARAM_SSDI_VENDOR_ERROR, RILSUPSERVICEDATAPARAMMASK, ntddrilapitypes/RIL_PARAM_SSDI_DATA, RIL_PARAM_SSDI_SS_ERROR, ntddrilapitypes/RIL_PARAM_SSDI_ALL, ntddrilapitypes/RIL_PARAM_SSDI_DATASIZE
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
-	RILSUPSERVICEDATAPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILSUPSERVICEDATAPARAMMASK
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
| **Header** | ntddrilapitypes.h |