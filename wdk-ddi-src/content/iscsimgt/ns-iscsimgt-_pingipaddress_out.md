---
UID : NS:iscsimgt._PingIPAddress_OUT
title : _PingIPAddress_OUT
author : windows-driver-content
description : The PingIPAddress_OUT structure holds the output data for the PingIPAddress method.
old-location : storage\pingipaddress_out.htm
old-project : storage
ms.assetid : 26512dc5-9d3d-4dd5-bce3-37feb64dded8
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _PingIPAddress_OUT, PingIPAddress_OUT, *PPingIPAddress_OUT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : iscsimgt.h
req.include-header : Iscsimgt.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PingIPAddress_OUT
req.alt-loc : iscsimgt.h
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
req.typenames : PingIPAddress_OUT, *PPingIPAddress_OUT
---

# _PingIPAddress_OUT structure
The PingIPAddress_OUT structure holds the output data for the PingIPAddress method.

## Syntax
````
typedef struct _PingIPAddress_OUT {
  ULONG Status;
  ULONG ResponsesReceived;
} PingIPAddress_OUT, *PPingIPAddress_OUT;
````

## Members

        
            `ResponsesReceived`

            The number of responses that were received.
        
            `Status`

            A status of type ISDSC_ERROR.

    ## Remarks
        We recommend that you implement this class.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | iscsimgt.h (include Iscsimgt.h) |