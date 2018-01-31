---
UID : NS:rilapitypes.RILMANAGECALLSPARAMS_V3
title : RILMANAGECALLSPARAMS_V3
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmanagecallsparams_v3_2.htm
old-project : netvista
ms.assetid : 2e7b862f-2c0b-48fa-ae3f-b4832c17b2ee
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilmanagecallsparams_v3_2, RILMANAGECALLSPARAMS_V3 structure [Network Drivers Starting with Windows Vista], RILMANAGECALLSPARAMS_V3, *LPRILMANAGECALLSPARAMS_V3, rilapitypes/RILMANAGECALLSPARAMS_V3
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
req.typenames : "*LPRILMANAGECALLSPARAMS_V3, RILMANAGECALLSPARAMS_V3"
req.product : Windows 10 or later.
---

# RILMANAGECALLSPARAMS_V3 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILMANAGECALLSPARAMS_V3 {
  DWORD                       dwExecutor;
  RILMANAGECALLPARAMSCOMMAND  dwCommand;
  DWORD                       dwID;
  BOOL                        fHasOfferAnswer;
  RILCALLMEDIAOFFERANSWERSET  rcmOfferAnswer;
  RILADDRESS                  raAddress;
} RILMANAGECALLSPARAMS_V3, RILMANAGECALLSPARAMS_V3;
````

## Members


`dwCommand`



`dwExecutor`



`dwID`



`fHasOfferAnswer`



`raAddress`



`rcmOfferAnswer`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |