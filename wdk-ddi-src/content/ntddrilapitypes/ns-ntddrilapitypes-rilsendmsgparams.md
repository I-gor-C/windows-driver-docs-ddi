---
UID : NS:ntddrilapitypes.RILSENDMSGPARAMS
title : RILSENDMSGPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsendmsgparams.htm
old-project : netvista
ms.assetid : de1049a8-e089-4d15-baca-2c760f895894
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILSENDMSGPARAMS, RILSENDMSGPARAMS, *LPRILSENDMSGPARAMS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddrilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILSENDMSGPARAMS
req.alt-loc : ntddrilapitypes.h
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
req.typenames : RILSENDMSGPARAMS, *LPRILSENDMSGPARAMS
---

# RILSENDMSGPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILSENDMSGPARAMS {
  DWORD       dwExecutor;
  HUICCAPP    hUiccApp;
  RILMESSAGE  rmMessage;
  DWORD       dwOptions;
} RILSENDMSGPARAMS, RILSENDMSGPARAMS;
````

## Members

        
            `dwExecutor`

            
        
            `dwOptions`

            
        
            `hUiccApp`

            
        
            `rmMessage`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |