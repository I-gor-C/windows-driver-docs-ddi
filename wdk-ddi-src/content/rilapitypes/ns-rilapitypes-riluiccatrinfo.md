---
UID : NS:rilapitypes.RILUICCATRINFO
title : RILUICCATRINFO
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluiccatrinfo_2.htm
old-project : netvista
ms.assetid : d7deda33-b68a-4413-a7fc-2988e97906e1
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.riluiccatrinfo_2, RILUICCATRINFO, *LPRILUICCATRINFO, RILUICCATRINFO structure [Network Drivers Starting with Windows Vista], rilapitypes/RILUICCATRINFO
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
req.typenames : RILUICCATRINFO, *LPRILUICCATRINFO
req.product : Windows 10 or later.
---

# RILUICCATRINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILUICCATRINFO {
  DWORD                dwATRlength;
  BYTE [MAXLENGTH_ATR] bATR;
} RILUICCATRINFO, RILUICCATRINFO;
````

## Members


`bATR`



`dwATRlength`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |