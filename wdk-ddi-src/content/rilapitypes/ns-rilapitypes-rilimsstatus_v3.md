---
UID : NS:rilapitypes.RILIMSSTATUS_V3
title : RILIMSSTATUS_V3
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilimsstatus_v3_2.htm
old-project : netvista
ms.assetid : 7ae2e97d-d055-412f-a219-258780319797
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.rilimsstatus_v3_2, RILIMSSTATUS_V3 structure [Network Drivers Starting with Windows Vista], RILIMSSTATUS, *LPRILIMSSTATUS_V3, *LPRILIMSSTATUS, rilapitypes/RILIMSSTATUS_V3, RILIMSSTATUS_V3
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
req.typenames : RILIMSSTATUS, *LPRILIMSSTATUS_V3, RILIMSSTATUS_V3, *LPRILIMSSTATUS
req.product : Windows 10 or later.
---

# RILIMSSTATUS_V3 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILIMSSTATUS_V3 {
  DWORD                     cbSize;
  DWORD                     dwParams;
  DWORD                     dwExecutor;
  HUICCAPP                  hUiccApp;
  DWORD                     dwAvailableServices;
  RILSMSFORMAT              dwSMSSupportedFormat;
  WCHAR [MAXLENGTH_ADDRESS] wszServingDomain;
  RILIMSSYSTEMTYPE          dwIMSSystemType;
} RILIMSSTATUS_V3, RILIMSSTATUS_V3;
````

## Members


`cbSize`



`dwAvailableServices`



`dwExecutor`



`dwIMSSystemType`



`dwParams`



`dwSMSSupportedFormat`



`hUiccApp`



`wszServingDomain`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |