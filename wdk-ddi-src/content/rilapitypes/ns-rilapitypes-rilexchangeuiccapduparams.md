---
UID : NS:rilapitypes.RILEXCHANGEUICCAPDUPARAMS
title : RILEXCHANGEUICCAPDUPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilexchangeuiccapduparams_2.htm
old-project : netvista
ms.assetid : 0bbdfb04-70a9-4ded-9947-6f082940cfa0
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILEXCHANGEUICCAPDUPARAMS structure [Network Drivers Starting with Windows Vista], netvista.rilexchangeuiccapduparams_2, *LPRILEXCHANGEUICCAPDUPARAMS, rilapitypes/RILEXCHANGEUICCAPDUPARAMS, RILEXCHANGEUICCAPDUPARAMS
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILEXCHANGEUICCAPDUPARAMS, *LPRILEXCHANGEUICCAPDUPARAMS
req.product : Windows 10 or later.
---

# RILEXCHANGEUICCAPDUPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILEXCHANGEUICCAPDUPARAMS {
  DWORD    dwSlotIndex;
  DWORD    dwChannelId;
  DWORD    dwAPDULength;
  BYTE [1] bAPDU;
} RILEXCHANGEUICCAPDUPARAMS, RILEXCHANGEUICCAPDUPARAMS;
````

## Members


`bAPDU`



`dwAPDULength`



`dwChannelId`



`dwSlotIndex`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |