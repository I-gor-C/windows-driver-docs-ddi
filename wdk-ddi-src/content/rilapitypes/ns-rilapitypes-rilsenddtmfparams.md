---
UID : NS:rilapitypes.RILSENDDTMFPARAMS
title : RILSENDDTMFPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsenddtmfparams_2.htm
old-project : netvista
ms.assetid : 0e8c8fa7-35e8-429c-b6e5-c01aba3c6746
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilsenddtmfparams_2, rilapitypes/RILSENDDTMFPARAMS, *LPRILSENDDTMFPARAMS, RILSENDDTMFPARAMS, RILSENDDTMFPARAMS structure [Network Drivers Starting with Windows Vista]
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
req.typenames : RILSENDDTMFPARAMS, *LPRILSENDDTMFPARAMS
req.product : Windows 10 or later.
---

# RILSENDDTMFPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILSENDDTMFPARAMS {
  DWORD                 dwExecutor;
  char [MAXLENGTH_DTMF] szDTMF;
  DWORD                 dwDigitOnTimeMs;
  DWORD                 dwDigitOffTimeMs;
} RILSENDDTMFPARAMS, RILSENDDTMFPARAMS;
````

## Members


`dwDigitOffTimeMs`



`dwDigitOnTimeMs`



`dwExecutor`



`szDTMF`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |