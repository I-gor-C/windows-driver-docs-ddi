---
UID : NS:1394._IRB_REQ_CONTROL
title : _IRB_REQ_CONTROL
author : windows-driver-content
description : This structure contains the fields necessary for the 1394 bus driver to carry out a control request.
old-location : ieee\irb_req_control.htm
old-project : IEEE
ms.assetid : F0ABD318-AC63-40D5-B94E-BD6FEA1A57AC
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _IRB_REQ_CONTROL, IRB_REQ_CONTROL
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : 1394.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IRB_REQ_CONTROL
req.alt-loc : 1394.h
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
req.typenames : IRB_REQ_CONTROL
---

# _IRB_REQ_CONTROL structure
This structure contains the fields necessary for the 1394 bus driver to carry out a control request.

## Syntax
````
typedef struct _IRB_REQ_CONTROL {
  ULONG ulIoControlCode;
  PMDL  pInBuffer;
  ULONG ulInBufferLength;
  PMDL  pOutBuffer;
  ULONG ulOutBufferLength;
  ULONG BytesReturned;
} IRB_REQ_CONTROL;
````

## Members

        
            `BytesReturned`

            Specifies the number of bytes returned.
        
            `pInBuffer`

            Points to an MDL that describes the input buffer. The input buffer contains user-defined information.
        
            `pOutBuffer`

            Points to an MDL that describes the output buffer. The output buffer contains user-defined information.
        
            `ulInBufferLength`

            Specifies the length of the input buffer.
        
            `ulIoControlCode`

            Specifies the control code used in this request. Vendors should make these control codes unique, so that they do not overlap.
        
            `ulOutBufferLength`

            Specifies the length of the output buffer.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | 1394.h |