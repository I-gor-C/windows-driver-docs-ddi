---
UID : NS:dbgeng._DEBUG_GET_TEXT_COMPLETIONS_OUT
title : _DEBUG_GET_TEXT_COMPLETIONS_OUT
author : windows-driver-content
description : Defines information about text completions to get.
old-location : debugger\debug_get_text_completions_out.htm
old-project : debugger
ms.assetid : 09F3A720-C039-4C8D-84A4-8AF071E1FFB0
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _DEBUG_GET_TEXT_COMPLETIONS_OUT, *PDEBUG_GET_TEXT_COMPLETIONS_OUT, DEBUG_GET_TEXT_COMPLETIONS_OUT
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
req.alt-api : DEBUG_GET_TEXT_COMPLETIONS_OUT
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
req.typenames : "*PDEBUG_GET_TEXT_COMPLETIONS_OUT, DEBUG_GET_TEXT_COMPLETIONS_OUT"
---

# _DEBUG_GET_TEXT_COMPLETIONS_OUT structure
Defines information about text completions to get.

## Syntax
````
typedef struct _DEBUG_GET_TEXT_COMPLETIONS_OUT {
  ULONG   Flags;
  ULONG   ReplaceIndex;
  ULONG   MatchCount;
  ULONG   Reserved1;
  ULONG64 Reserved2[2];
} DEBUG_GET_TEXT_COMPLETIONS_OUT, *PDEBUG_GET_TEXT_COMPLETIONS_OUT;
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
        
            `MatchCount`

            Count value of matches.
        
            `ReplaceIndex`

            The index of the replace location.
        
            `Reserved1`

            Reserved.
        
            `Reserved2`

            Reserved.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include DbgEng.h) |