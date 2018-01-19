---
UID : NS:rilapitypes.RILGETCALLFORWARDINGPARAMS
title : RILGETCALLFORWARDINGPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgetcallforwardingparams_2.htm
old-project : netvista
ms.assetid : f7ebe2a7-b29e-411e-bdfa-744c95645095
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILGETCALLFORWARDINGPARAMS, *LPRILGETCALLFORWARDINGPARAMS, RILGETCALLFORWARDINGPARAMS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILGETCALLFORWARDINGPARAMS
req.alt-loc : rilapitypes.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*LPRILGETCALLFORWARDINGPARAMS, RILGETCALLFORWARDINGPARAMS"
req.product : Windows 10 or later.
---

# RILGETCALLFORWARDINGPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILGETCALLFORWARDINGPARAMS {
  DWORD                            dwExecutor;
  RILCALLFORWARDINGSETTINGSREASON  dwReason;
  BOOL                             fAllClasses;
  DWORD                            dwInfoClasses;
} RILGETCALLFORWARDINGPARAMS, RILGETCALLFORWARDINGPARAMS;
````

## Members

        
            `dwExecutor`

            
        
            `dwInfoClasses`

            
        
            `dwReason`

            
        
            `fAllClasses`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |