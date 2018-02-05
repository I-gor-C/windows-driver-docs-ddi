---
UID : NS:rilapitypes.RILGETDRIVERVERSIONPARAMS
title : RILGETDRIVERVERSIONPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgetdriverversionparams_2.htm
old-project : netvista
ms.assetid : b396b12e-f8c4-4e5e-b3c4-9822bcd996a4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*LPRILGETDRIVERVERSIONPARAMS, netvista.rilgetdriverversionparams_2, rilapitypes/RILGETDRIVERVERSIONPARAMS, RILGETDRIVERVERSIONPARAMS structure [Network Drivers Starting with Windows Vista], RILGETDRIVERVERSIONPARAMS"
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
req.typenames : "*LPRILGETDRIVERVERSIONPARAMS, RILGETDRIVERVERSIONPARAMS"
req.product : Windows 10 or later.
---

# RILGETDRIVERVERSIONPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILGETDRIVERVERSIONPARAMS {
  DWORD  dwMinVersion;
  DWORD  dwMaxVersion;
} RILGETDRIVERVERSIONPARAMS, RILGETDRIVERVERSIONPARAMS;
````

## Members


`dwMaxVersion`



`dwMinVersion`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |