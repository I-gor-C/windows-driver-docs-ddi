---
UID : NS:rilapitypes.RILCALLMEDIAOFFERANSWERSET
title : RILCALLMEDIAOFFERANSWERSET
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmediaofferanswerset_2.htm
old-project : netvista
ms.assetid : 272e2bf5-9d84-407d-9126-41bcb4f43d91
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*LPRILCALLMEDIAOFFERANSWERSET, rilapitypes/RILCALLMEDIAOFFERANSWERSET, RILCALLMEDIAOFFERANSWERSET structure [Network Drivers Starting with Windows Vista], RILCALLMEDIAOFFERANSWERSET, netvista.rilcallmediaofferanswerset_2"
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
req.typenames : "*LPRILCALLMEDIAOFFERANSWERSET, RILCALLMEDIAOFFERANSWERSET"
req.product : Windows 10 or later.
---

# RILCALLMEDIAOFFERANSWERSET structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCALLMEDIAOFFERANSWERSET {
  DWORD                                       cbSize;
  RILCALLMEDIAOFFERANSWERTYPE                 dwType;
  DWORD                                       dwNumberOfItems;
  RILCALLMEDIAOFFERANSWER [MAXNUM_CALL_MEDIA] stOfferAnswer;
} RILCALLMEDIAOFFERANSWERSET, RILCALLMEDIAOFFERANSWERSET;
````

## Members


`cbSize`



`dwNumberOfItems`



`dwType`



`stOfferAnswer`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |