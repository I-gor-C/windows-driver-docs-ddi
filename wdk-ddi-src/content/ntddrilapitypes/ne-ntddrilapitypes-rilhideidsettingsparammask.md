---
UID: NE:ntddrilapitypes.RILHIDEIDSETTINGSPARAMMASK
title: RILHIDEIDSETTINGSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilhideidsettingsparammask.htm
old-project: netvista
ms.assetid: 3ac34302-f56f-424d-b627-f977c4aabfba
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RILHIDEIDSETTINGSPARAMMASK, RILHIDEIDSETTINGSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_HIDS_ALL, RIL_PARAM_HIDS_PROVISIONING, RIL_PARAM_HIDS_STATUS, netvista.rilhideidsettingsparammask, ntddrilapitypes/RILHIDEIDSETTINGSPARAMMASK, ntddrilapitypes/RIL_PARAM_HIDS_ALL, ntddrilapitypes/RIL_PARAM_HIDS_PROVISIONING, ntddrilapitypes/RIL_PARAM_HIDS_STATUS
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddrilapitypes.h
api_name:
-	RILHIDEIDSETTINGSPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILHIDEIDSETTINGSPARAMMASK
---

# RILHIDEIDSETTINGSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILHIDEIDSETTINGSPARAMMASK { 
  RIL_PARAM_HIDS_STATUS,
  RIL_PARAM_HIDS_PROVISIONING,
  RIL_PARAM_HIDS_ALL
} RILHIDEIDSETTINGSPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_HIDS_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_HIDS_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_HIDS_PROVISIONING</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_HIDS_STATUS</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |