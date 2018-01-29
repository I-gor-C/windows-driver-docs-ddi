---
UID : NS:ntddrilapitypes.RILEMERGENCYNUMBER
title : RILEMERGENCYNUMBER
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilemergencynumber.htm
old-project : netvista
ms.assetid : 1725c893-1c36-40d2-99d7-e163020fc4fc
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILEMERGENCYNUMBER, netvista.rilemergencynumber, ntddrilapitypes/RILEMERGENCYNUMBER, RILEMERGENCYNUMBER structure [Network Drivers Starting with Windows Vista], *LPRILEMERGENCYNUMBER
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
req.typenames : "*LPRILEMERGENCYNUMBER, RILEMERGENCYNUMBER"
---

# RILEMERGENCYNUMBER structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILEMERGENCYNUMBER {
  DWORD     cbSize;
  DWORD     dwParams;
  DWORD     dwExecutor;
  HUICCAPP  hUiccApp;
  DWORD     dwCategory;
  WCHAR [8] wszEmergencyNumber;
} RILEMERGENCYNUMBER, RILEMERGENCYNUMBER;
````

## Members


`cbSize`



`dwCategory`



`dwExecutor`



`dwParams`



`hUiccApp`



`wszEmergencyNumber`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |