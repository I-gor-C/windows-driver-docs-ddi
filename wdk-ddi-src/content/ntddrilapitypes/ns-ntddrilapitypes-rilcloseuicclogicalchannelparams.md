---
UID : NS:ntddrilapitypes.RILCLOSEUICCLOGICALCHANNELPARAMS
title : RILCLOSEUICCLOGICALCHANNELPARAMS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcloseuicclogicalchannelparams.htm
old-project : netvista
ms.assetid : 0c06bcd7-d475-40b8-b997-fe65047db331
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCLOSEUICCLOGICALCHANNELPARAMS, *LPRILCLOSEUICCLOGICALCHANNELPARAMS, RILCLOSEUICCLOGICALCHANNELPARAMS
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
req.alt-api : RILCLOSEUICCLOGICALCHANNELPARAMS
req.alt-loc : ntddrilapitypes.h
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
req.typenames : "*LPRILCLOSEUICCLOGICALCHANNELPARAMS, RILCLOSEUICCLOGICALCHANNELPARAMS"
---

# RILCLOSEUICCLOGICALCHANNELPARAMS structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef struct _RILCLOSEUICCLOGICALCHANNELPARAMS {
  DWORD  dwSlotIndex;
  DWORD  dwChannelId;
} RILCLOSEUICCLOGICALCHANNELPARAMS, RILCLOSEUICCLOGICALCHANNELPARAMS;
````

## Members

        
            `dwChannelId`

            
        
            `dwSlotIndex`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |