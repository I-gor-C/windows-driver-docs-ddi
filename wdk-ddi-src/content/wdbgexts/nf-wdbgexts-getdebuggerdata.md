---
UID : NF:wdbgexts.GetDebuggerData
title : GetDebuggerData macro
author : windows-driver-content
description : The GetDebuggerData function retrieves information stored in a data block.
old-location : debugger\getdebuggerdata.htm
old-project : debugger
ms.assetid : a07afa2e-1f7d-4685-9ede-8b7805dd6583
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : GetDebuggerData
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
req.header : wdbgexts.h
req.include-header : Wdbgexts.h, Dbgeng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : GetDebuggerData
req.alt-loc : wdbgexts.h
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
req.typenames : EXT_TDOP
req.product : Windows 10 or later.
---


# GetDebuggerData function
The <b>GetDebuggerData</b> function retrieves information stored in a data block.

## Syntax

````
ULONG GetDebuggerData(
   ULONG Tag,
   PVOID Buf,
   ULONG Size
);
````

## Parameters

`TAG`



`BUF`



`SIZE`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdbgexts.h (include Wdbgexts.h, Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |