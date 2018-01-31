---
UID : NS:rilapitypes.RILEXCHANGEUICCAPDURESPONSE
title : RILEXCHANGEUICCAPDURESPONSE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilexchangeuiccapduresponse_2.htm
old-project : netvista
ms.assetid : c9e3a4b3-2ce2-4f90-8be2-01d9870cc982
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILEXCHANGEUICCAPDURESPONSE, *LPRILEXCHANGEUICCAPDURESPONSE, rilapitypes/RILEXCHANGEUICCAPDURESPONSE, RILEXCHANGEUICCAPDURESPONSE structure [Network Drivers Starting with Windows Vista], netvista.rilexchangeuiccapduresponse_2
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
req.typenames : RILEXCHANGEUICCAPDURESPONSE, *LPRILEXCHANGEUICCAPDURESPONSE
req.product : Windows 10 or later.
---

# RILEXCHANGEUICCAPDURESPONSE structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILEXCHANGEUICCAPDURESPONSE {
  DWORD    cbSize;
  DWORD    dwParams;
  DWORD    dwResponseAPDULength;
  BYTE [1] bResponseAPDU;
} RILEXCHANGEUICCAPDURESPONSE, RILEXCHANGEUICCAPDURESPONSE;
````

## Members


`bResponseAPDU`



`cbSize`



`dwParams`



`dwResponseAPDULength`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |