---
UID : NS:rilapitypes.RILREMOTEPARTYINFO
title : RILREMOTEPARTYINFO
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilremotepartyinfo_2.htm
old-project : netvista
ms.assetid : 0ca17e70-1e50-4b62-89ec-0e92ad6e846b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILREMOTEPARTYINFO, *LPRILREMOTEPARTYINFO, rilapitypes/RILREMOTEPARTYINFO, RILREMOTEPARTYINFO structure [Network Drivers Starting with Windows Vista], netvista.rilremotepartyinfo_2
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
req.typenames : RILREMOTEPARTYINFO, *LPRILREMOTEPARTYINFO
req.product : Windows 10 or later.
---

# RILREMOTEPARTYINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILREMOTEPARTYINFO {
  DWORD                         cbSize;
  DWORD                         dwParams;
  DWORD                         dwExecutor;
  RILADDRESS                    raAddress;
  RILSUBADDRESS                 rsaSubAddress;
  WCHAR [MAXLENGTH_DESCRIPTION] wszDescription;
  RILREMOTEPARTYINFOVALUE       dwNumberPresentationIndicator;
  RILREMOTEPARTYINFOVALUE       dwNamePresentationIndicator;
  DWORD                         dwID;
} RILREMOTEPARTYINFO, RILREMOTEPARTYINFO;
````

## Members


`cbSize`



`dwExecutor`



`dwID`



`dwNamePresentationIndicator`



`dwNumberPresentationIndicator`



`dwParams`



`raAddress`



`rsaSubAddress`



`wszDescription`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |