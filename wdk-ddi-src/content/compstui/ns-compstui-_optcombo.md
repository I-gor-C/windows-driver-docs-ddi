---
UID : NS:compstui._OPTCOMBO
title : "_OPTCOMBO"
author : windows-driver-content
description : "."
old-location : print\optcombo.htm
old-project : print
ms.assetid : B1F5A79A-8F64-4B7B-ADB4-BDD8EC17F22E
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : POPTCOMBO, compstui/POPTCOMBO, compstui/OPTCOMBO, OPTCOMBO, _OPTCOMBO, POPTCOMBO structure pointer [Print Devices], OPTCOMBO structure [Print Devices], *POPTCOMBO, print.optcombo
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : compstui.h
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
req.typenames : "*POPTCOMBO, OPTCOMBO"
---

# _OPTCOMBO structure


## Syntax
````
typedef struct _OPTCOMBO {
  WORD      cbSize;
  BYTE      Flags;
  WORD      cListItem;
  POPTPARAM pListItem;
  LONG      Sel;
  LONG      dwReserved[3];
} OPTCOMBO, *POPTCOMBO;
````

## Members


`cbSize`



`cListItem`



`dwReserved`



`Flags`



`pListItem`



`Sel`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | compstui.h |