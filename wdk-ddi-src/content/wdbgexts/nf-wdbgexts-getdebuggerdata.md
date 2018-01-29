---
UID : NF:wdbgexts.GetDebuggerData
title : GetDebuggerData macro
author : windows-driver-content
description : The GetDebuggerData function retrieves information stored in a data block.
old-location : debugger\getdebuggerdata.htm
old-project : debugger
ms.assetid : a07afa2e-1f7d-4685-9ede-8b7805dd6583
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : GetDebuggerData function [Windows Debugging], WdbgExts_Ref_a9b54b49-d8ac-4bee-a837-3986a250403a.xml, GetDebuggerData, debugger.getdebuggerdata, wdbgexts/GetDebuggerData
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wdbgexts.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
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

TBD

`BUF`

TBD

`SIZE`

TBD


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