---
UID : NS:ntddrilapitypes.RILMSGMWIDETAIL
title : RILMSGMWIDETAIL
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgmwidetail.htm
old-project : netvista
ms.assetid : 69371414-9f4a-46a6-8622-5750db7a0c5b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilmsgmwidetail, RILMSGMWIDETAIL, *LPRILMSGMWIDETAIL, RILMSGMWIDETAIL structure [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILMSGMWIDETAIL
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
req.typenames : "*LPRILMSGMWIDETAIL, RILMSGMWIDETAIL"
---

# RILMSGMWIDETAIL structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILMSGMWIDETAIL {
  RILMSGMWITYPE      dwMwiType;
  RILMSGMWIPRIORITY  dwMwiPriority;
  RILADDRESS         raToAddress;
  RILADDRESS         raFromAddress;
  RILSYSTEMTIME      stDateSent;
  WCHAR [256]        wszSubject;
  WCHAR [256]        wszMessageId;
} RILMSGMWIDETAIL, RILMSGMWIDETAIL;
````

## Members


`dwMwiPriority`



`dwMwiType`



`raFromAddress`



`raToAddress`



`stDateSent`



`wszMessageId`



`wszSubject`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |