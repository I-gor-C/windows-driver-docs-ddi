---
UID: NE:rilapitypes.RILREQUESTGEOLOCATIONDATAPARAMMASK
title: RILREQUESTGEOLOCATIONDATAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrequestgeolocationdataparammask.htm
old-project: netvista
ms.assetid: 86b89336-56f9-4665-a0d3-37dc6ec6c377
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: RILREQUESTGEOLOCATIONDATAPARAMMASK, RILREQUESTGEOLOCATIONDATAPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL, RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR, RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK, RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY, RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION, RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE, netvista.rilrequestgeolocationdataparammask, ntddrilapitypes/RILREQUESTGEOLOCATIONDATAPARAMMASK, ntddrilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL, ntddrilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR, ntddrilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK, ntddrilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY, ntddrilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION, ntddrilapitypes/RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE
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
-	RILREQUESTGEOLOCATIONDATAPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILREQUESTGEOLOCATIONDATAPARAMMASK
req.product: Windows 10 or later.
---

# RILREQUESTGEOLOCATIONDATAPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef enum RILREQUESTGEOLOCATIONDATAPARAMMASK {
  RIL_PARAM_REQUESTGEOLOCATIONDATA_NONE                ,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE                ,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR            ,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK                ,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY    ,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION  ,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL
} ;
```

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_REQUESTGEOLOCATIONDATA_NONE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |