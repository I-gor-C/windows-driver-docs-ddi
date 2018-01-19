---
UID : NS:dbgeng._DEBUG_GET_TEXT_COMPLETIONS_IN
title : _DEBUG_GET_TEXT_COMPLETIONS_IN
author : windows-driver-content
description : Defines information about text completions to get.
old-location : debugger\debug_get_text_completions_in.htm
old-project : debugger
ms.assetid : 1B8B0B7D-346D-41FC-B718-60B04F10702C
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _DEBUG_GET_TEXT_COMPLETIONS_IN, *PDEBUG_GET_TEXT_COMPLETIONS_IN, DEBUG_GET_TEXT_COMPLETIONS_IN
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
req.alt-api : DEBUG_GET_TEXT_COMPLETIONS_IN
req.alt-loc : DbgEng.h
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
req.typenames : "*PDEBUG_GET_TEXT_COMPLETIONS_IN, DEBUG_GET_TEXT_COMPLETIONS_IN"
---

# _DEBUG_GET_TEXT_COMPLETIONS_IN structure
Defines information about text completions to get.

## Syntax
````
typedef struct _DEBUG_GET_TEXT_COMPLETIONS_IN {
  ULONG   Flags;
  ULONG   MatchCountLimit;
  ULONG64 Reserved[3];
} DEBUG_GET_TEXT_COMPLETIONS_IN, *PDEBUG_GET_TEXT_COMPLETIONS_IN;
````

## Members

        
            `Flags`

            Flags. Valid flag values include the following:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `MatchCountLimit`

            The limit of matches.
        
            `Reserved`

            Reserved.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include DbgEng.h) |