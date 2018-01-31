---
UID : NS:dbgeng._DEBUG_CACHED_SYMBOL_INFO
title : "_DEBUG_CACHED_SYMBOL_INFO"
author : windows-driver-content
description : Defines information about cached symbols.
old-location : debugger\debug_cached_symbol_info.htm
old-project : debugger
ms.assetid : CC7914B6-DCE1-45D1-84D3-5FF1449AD565
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : PDEBUG_CACHED_SYMBOL_INFO structure pointer [Windows Debugging], _DEBUG_CACHED_SYMBOL_INFO, DEBUG_CACHED_SYMBOL_INFO structure [Windows Debugging], dbgeng/DEBUG_CACHED_SYMBOL_INFO, DEBUG_CACHED_SYMBOL_INFO, PDEBUG_CACHED_SYMBOL_INFO, *PDEBUG_CACHED_SYMBOL_INFO, debugger.debug_cached_symbol_info, dbgeng/PDEBUG_CACHED_SYMBOL_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : dbgeng.h
req.include-header : DbgEng.h
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
req.typenames : "*PDEBUG_CACHED_SYMBOL_INFO, DEBUG_CACHED_SYMBOL_INFO"
---

# _DEBUG_CACHED_SYMBOL_INFO structure
Defines information about cached symbols.

## Syntax
````
typedef struct _DEBUG_CACHED_SYMBOL_INFO {
  ULONG64 ModBase;
  ULONG64 Arg1;
  ULONG64 Arg2;
  ULONG   Id;
  ULONG   Arg3;
} DEBUG_CACHED_SYMBOL_INFO, *PDEBUG_CACHED_SYMBOL_INFO;
````

## Members


`Arg1`

An argument value.

`Arg2`

An argument value.

`Arg3`

An argument value.

`Id`

An ID.

`ModBase`

A module base.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include DbgEng.h) |