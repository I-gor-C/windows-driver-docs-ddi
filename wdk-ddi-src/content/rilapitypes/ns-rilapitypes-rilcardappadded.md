---
UID : NS:rilapitypes.RILCARDAPPADDED
title : RILCARDAPPADDED
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcardappadded_2.htm
old-project : netvista
ms.assetid : 8e4eed61-bd57-4731-9178-7f8d33fbd240
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILCARDAPPADDED, RILCARDAPPADDED structure [Network Drivers Starting with Windows Vista], *LPRILCARDAPPADDED, netvista.rilcardappadded_2, rilapitypes/RILCARDAPPADDED
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
req.typenames : "*LPRILCARDAPPADDED, RILCARDAPPADDED"
req.product : Windows 10 or later.
---

# RILCARDAPPADDED structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCARDAPPADDED {
  DWORD           cbSize;
  DWORD           dwParams;
  DWORD           dwSlotIndex;
  RILUICCAPPINFO  rilUiccAppInfo;
} RILCARDAPPADDED, RILCARDAPPADDED;
````

## Members


`cbSize`



`dwParams`



`dwSlotIndex`



`rilUiccAppInfo`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |