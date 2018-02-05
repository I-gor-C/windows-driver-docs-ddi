---
UID : NS:rilapitypes.RILMSGMWISUMMARYLIST
title : RILMSGMWISUMMARYLIST
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgmwisummarylist_2.htm
old-project : netvista
ms.assetid : 85f07ef4-6306-4995-9c95-9bbae775af1c
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RILMSGMWISUMMARYLIST, RILMSGMWISUMMARYLIST, *LPRILMSGMWISUMMARYLIST, netvista.rilmsgmwisummarylist_2, RILMSGMWISUMMARYLIST structure [Network Drivers Starting with Windows Vista]
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
req.typenames : "*LPRILMSGMWISUMMARYLIST, RILMSGMWISUMMARYLIST"
req.product : Windows 10 or later.
---

# RILMSGMWISUMMARYLIST structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILMSGMWISUMMARYLIST {
  DWORD                cbSize;
  DWORD                dwParams;
  DWORD                dwExecutor;
  DWORD                dwReferenceNumber;
  RILADDRESS           stAccountAddress;
  DWORD                dwTotalNumberOfDetailItems;
  DWORD                dwNumberOfSummaryItems;
  RILMSGMWISUMMARY [1] stMwiSummary;
} RILMSGMWISUMMARYLIST, RILMSGMWISUMMARYLIST;
````

## Members


`cbSize`



`dwExecutor`



`dwNumberOfSummaryItems`



`dwParams`



`dwReferenceNumber`



`dwTotalNumberOfDetailItems`



`stAccountAddress`



`stMwiSummary`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |