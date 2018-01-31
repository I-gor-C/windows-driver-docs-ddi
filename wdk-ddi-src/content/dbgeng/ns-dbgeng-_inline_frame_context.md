---
UID : NS:dbgeng._INLINE_FRAME_CONTEXT
title : "_INLINE_FRAME_CONTEXT"
author : windows-driver-content
description : Describes inline frame context.
old-location : debugger\inline_frame_context.htm
old-project : debugger
ms.assetid : 6EB52227-8685-4096-882F-64550A84DE4F
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : dbgeng/INLINE_FRAME_CONTEXT, _INLINE_FRAME_CONTEXT, INLINE_FRAME_CONTEXT, debugger.inline_frame_context, INLINE_FRAME_CONTEXT union [Windows Debugging]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : dbgeng.h
req.include-header : Dbgeng.h
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
req.typenames : INLINE_FRAME_CONTEXT
---

# _INLINE_FRAME_CONTEXT structure
Describes inline frame context.

## Syntax
````
typedef union _INLINE_FRAME_CONTEXT {
  DWORD  ContextValue;
  struct  {
        BYTE FrameId;
        BYTE FrameType;
        WORD FrameSignature;
    };
} INLINE_FRAME_CONTEXT;
````

## Members


`ContextValue`

A context value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |