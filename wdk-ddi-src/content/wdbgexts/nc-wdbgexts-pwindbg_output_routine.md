---
UID : NC:wdbgexts.PWINDBG_OUTPUT_ROUTINE
title : PWINDBG_OUTPUT_ROUTINE
author : windows-driver-content
description : The callback function implements the functionality to print a formatted string to the Debugger Command window.
old-location : debugger\dprintf.htm
old-project : debugger
ms.assetid : 33bcf4d4-1a79-4950-858e-10543faa9432
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _VPCI_WRITE_BLOCK_INPUT, VPCI_WRITE_BLOCK_INPUT, *PVPCI_WRITE_BLOCK_INPUT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wdbgexts.h
req.include-header : Wdbgexts.h, Dbgeng.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : dprintf
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
req.typenames : VPCI_WRITE_BLOCK_INPUT, *PVPCI_WRITE_BLOCK_INPUT
req.product : Windows 10 or later.
---


# PWINDBG_OUTPUT_ROUTINE callback function
The callback function implements the functionality to print a formatted string to the Debugger Command window. 

The wdbgexts.h header declares a macro, <b>dprintf</b> that  prints the formatted string. It works like the C-language routine <b>printf</b>.

## Syntax

```
PWINDBG_OUTPUT_ROUTINE PwindbgOutputRoutine;

void PwindbgOutputRoutine(
  PCSTR lpFormat,
   ...
)
{...}
```

## Parameters

`lpFormat`



`...`




## Return Value

This callback function does not return a value.

## Remarks

When generating very large output strings, it is possible the limits of the debugger engine or operating system may be reached.  For example, some versions of the debugger engine have a 16K character limit for a single piece of output.  If you find that very large output is getting truncated, you may need to split your output into multiple requests.</p>

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