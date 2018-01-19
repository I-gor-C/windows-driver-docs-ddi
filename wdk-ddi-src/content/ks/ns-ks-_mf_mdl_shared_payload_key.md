---
UID : NS:ks._MF_MDL_SHARED_PAYLOAD_KEY
title : _MF_MDL_SHARED_PAYLOAD_KEY
author : windows-driver-content
description : This union is used internally by the operating system.
old-location : stream\mf_mdl_shared_payload_key.htm
old-project : stream
ms.assetid : 3EA093AB-1D23-4744-997E-8C7072934628
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _MF_MDL_SHARED_PAYLOAD_KEY, *PMF_MDL_SHARED_PAYLOAD_KEY, MF_MDL_SHARED_PAYLOAD_KEY
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MF_MDL_SHARED_PAYLOAD_KEY
req.alt-loc : ks.h
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
req.typenames : "*PMF_MDL_SHARED_PAYLOAD_KEY, MF_MDL_SHARED_PAYLOAD_KEY"
---

# _MF_MDL_SHARED_PAYLOAD_KEY structure
This union is used internally by the operating system.

## Syntax
````
typedef union _MF_MDL_SHARED_PAYLOAD_KEY {
  struct {
    ULONG   pHandle;
    ULONG   fHandle;
    ULONG64 uPayload;
  } combined;
  GUID   GMDLHandle;
} MF_MDL_SHARED_PAYLOAD_KEY, PMF_MDL_SHARED_PAYLOAD_KEY;
````

## Members

        
            `combined`

            This member is used internally by the operating system.
        
            `GMDLHandle`

            This structure is used internally by the operating system.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |