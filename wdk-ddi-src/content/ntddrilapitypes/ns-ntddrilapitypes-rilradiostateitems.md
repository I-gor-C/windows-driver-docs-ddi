---
UID : NS:ntddrilapitypes.RILRADIOSTATEITEMS
title : RILRADIOSTATEITEMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilradiostateitems.htm
old-project : netvista
ms.assetid : 26b2521c-7008-437d-aed3-3ed2be5d5959
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILRADIOSTATEITEMS, ntddrilapitypes/RILRADIOSTATEITEMS, RILRADIOSTATEITEMS structure [Network Drivers Starting with Windows Vista], netvista.rilradiostateitems, *LPRILRADIOSTATEITEMS
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
req.typenames : RILRADIOSTATEITEMS, *LPRILRADIOSTATEITEMS
---

# RILRADIOSTATEITEMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILRADIOSTATEITEMS {
  DWORD                 dwGroupId;
  DWORD                 dwCntItems;
  RILRADIOSTATEITEM [1] rilItems;
} RILRADIOSTATEITEMS, RILRADIOSTATEITEMS;
````

## Members


`dwCntItems`



`dwGroupId`



`rilItems`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |