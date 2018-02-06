---
UID: NE:rilapitypes.RILIMSSSTATUSPARAMMASK
title: RILIMSSSTATUSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssstatusparammask_2.htm
old-project: netvista
ms.assetid: 0d5896e8-b85e-407c-8b3e-cc8ad95c2ab1
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: RIL_PARAM_IMSSTATUS_SERVINGDOMAIN, RIL_PARAM_IMSSTATUS_AVAILABLESERVICES, RILIMSSSTATUSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARAM_IMSSTATUS_HUICCAPP, rilapitypes/RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT, rilapitypes/RIL_PARAM_IMSSTATUS_SERVINGDOMAIN, RIL_PARAM_IMSSTATUS_ALL, netvista.rilimssstatusparammask_2, rilapitypes/RIL_PARAM_IMSSTATUS_ALL, rilapitypes/RIL_PARAM_IMSSTATUS_SYSTEMTYPE, RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT, rilapitypes/RILIMSSSTATUSPARAMMASK, RIL_PARAM_IMSSTATUS_SYSTEMTYPE, RIL_PARAM_IMSSTATUS_HUICCAPP, RILIMSSSTATUSPARAMMASK, rilapitypes/RIL_PARAM_IMSSTATUS_AVAILABLESERVICES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
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
req.lib: NtosKrnl.exe
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	rilapitypes.h
apiname:
-	RILIMSSSTATUSPARAMMASK
product: Windows
targetos: Windows
req.typenames: RILIMSSSTATUSPARAMMASK
req.product: Windows 10 or later.
---

# RILIMSSSTATUSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSSSTATUSPARAMMASK { 
  RIL_PARAM_IMSSTATUS_HUICCAPP,
  RIL_PARAM_IMSSTATUS_AVAILABLESERVICES,
  RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT,
  RIL_PARAM_IMSSTATUS_SERVINGDOMAIN,
  RIL_PARAM_IMSSTATUS_SYSTEMTYPE,
  RIL_PARAM_IMSSTATUS_ALL
} RILIMSSSTATUSPARAMMASK;
````

## Constants

<table>
            
                <tr>
                    <td>RIL_PARAM_IMSSTATUS_ALL</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_IMSSTATUS_AVAILABLESERVICES</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_IMSSTATUS_EXECUTOR</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_IMSSTATUS_HUICCAPP</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_IMSSTATUS_SERVINGDOMAIN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_IMSSTATUS_SMSSUPPORTEDFORMAT</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>RIL_PARAM_IMSSTATUS_SYSTEMTYPE</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |