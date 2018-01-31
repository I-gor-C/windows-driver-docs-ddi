---
UID : NS:rilapitypes.RILPOSITIONINFO_V1
title : RILPOSITIONINFO_V1
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilpositioninfo_v1_2.htm
old-project : netvista
ms.assetid : ff622111-e4c3-47eb-9509-dbe86d0d5acf
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILPOSITIONINFO_V1 structure [Network Drivers Starting with Windows Vista], netvista.rilpositioninfo_v1_2, *LPRILPOSITIONINFO_V1, RILPOSITIONINFO_V1, rilapitypes/RILPOSITIONINFO_V1
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
req.typenames : RILPOSITIONINFO_V1, *LPRILPOSITIONINFO_V1
req.product : Windows 10 or later.
---

# RILPOSITIONINFO_V1 structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILPOSITIONINFO_V1 {
  DWORD                                   cbSize;
  DWORD                                   dwSystemType;
  RILPOSITIONINFOGSM                      stGSMServingCellInfo;
  RILPOSITIONINFOUMTS                     stUMTSServingCellInfo;
  RILPOSITIONINFOLTE                      stLTEServingCellInfo;
  DWORD                                   dwCntGSMNMR;
  RILGSMNMR [MAX_GSMPOS_COUNT_OF_NMR]     rgNMR;
  DWORD                                   dwCntUMTSMRL;
  RILUMTSMRL [MAX_UMTSPOS_COUNT_OF_MRL]   ruMRL;
  DWORD                                   dwCntEUTRAMRL;
  RILEUTRAMRL [MAX_EUTRAPOS_COUNT_OF_MRL] reMRL;
  DWORD                                   dwCntC2KMRL;
  RILC2KMRL [MAX_C2KPOS_COUNT_OF_MRL]     rc2kMRL;
} RILPOSITIONINFO_V1, RILPOSITIONINFO_V1;
````

## Members


`cbSize`



`dwCntC2KMRL`



`dwCntEUTRAMRL`



`dwCntGSMNMR`



`dwCntUMTSMRL`



`dwSystemType`



`rc2kMRL`



`reMRL`



`rgNMR`



`ruMRL`



`stGSMServingCellInfo`



`stLTEServingCellInfo`



`stUMTSServingCellInfo`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |