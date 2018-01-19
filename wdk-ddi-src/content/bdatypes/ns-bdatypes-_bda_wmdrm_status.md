---
UID : NS:bdatypes._BDA_WMDRM_STATUS
title : _BDA_WMDRM_STATUS
author : windows-driver-content
description : .
old-location : stream\bda_wmdrm_status.htm
old-project : stream
ms.assetid : FEE7B3B2-2433-4772-8E79-C325ECC343FF
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _BDA_WMDRM_STATUS, BDA_WMDRM_STATUS, *PBDA_WMDRM_STATUS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bdatypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : BDA_WMDRM_STATUS
req.alt-loc : Bdatypes.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : BDA_WMDRM_STATUS, *PBDA_WMDRM_STATUS
---

# _BDA_WMDRM_STATUS structure


## Syntax
````
typedef struct _BDA_WMDRM_STATUS {
  PBDARESULT lResult;
  ULONG      ulMaxCaptureTokenSize;
  ULONG      uMaxStreamingPid;
  ULONG      ulMaxLicense;
  ULONG      ulMinSecurityLevel;
  ULONG      ulRevInfoSequenceNumber;
  ULONGLONG  ulRevInfoIssuedTime;
  ULONG      ulRevListVersion;
  ULONG      ulRevInfoTTL;
  ULONG      ulState;
} BDA_WMDRM_STATUS, *PBDA_WMDRM_STATUS;
````

## Members

        
            `lResult`

            
        
            `ulMaxCaptureTokenSize`

            
        
            `ulMaxLicense`

            
        
            `ulMinSecurityLevel`

            
        
            `ulRevInfoIssuedTime`

            
        
            `ulRevInfoSequenceNumber`

            
        
            `ulRevInfoTTL`

            
        
            `ulRevListVersion`

            
        
            `ulState`

            
        
            `uMaxStreamingPid`

            


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bdatypes.h |