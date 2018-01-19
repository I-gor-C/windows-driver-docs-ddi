---
UID : NS:ntddrilapitypes.RILUICCLOCKCREDENTIAL
title : RILUICCLOCKCREDENTIAL
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluicclockcredential.htm
old-project : netvista
ms.assetid : 4ca8411e-2492-4832-881c-5fdb974485fc
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILUICCLOCKCREDENTIAL, *LPRILUICCLOCKCREDENTIAL, RILUICCLOCKCREDENTIAL
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
req.alt-api : RILUICCLOCKCREDENTIAL
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
req.typenames : "*LPRILUICCLOCKCREDENTIAL, RILUICCLOCKCREDENTIAL"
---

# RILUICCLOCKCREDENTIAL structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILUICCLOCKCREDENTIAL {
  RILUICCLOCK  rilUiccLock;
  char [256]   szPassword;
} RILUICCLOCKCREDENTIAL, RILUICCLOCKCREDENTIAL;
````

## Members

        
            `rilUiccLock`

            
        
            `szPassword`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |