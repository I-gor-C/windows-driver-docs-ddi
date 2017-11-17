---
UID: NS.wdbgexts._WINDBG_EXTENSION_APIS
title: WINDBG_EXTENSION_APIS
author: windows-driver-content
description: 
ms.assetid: 4efa352c-f208-43bf-a7f0-37d02479a5b4
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WINDBG_EXTENSION_APIS, WINDBG_EXTENSION_APIS, *PWINDBG_EXTENSION_APIS
req.header: wdbgexts.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# WINDBG_EXTENSION_APIS structure

## -description



## -struct-fields

### -field ULONG nSize			
 	
### -field PWINDBG_OUTPUT_ROUTINE lpOutputRoutine			
 	
### -field PWINDBG_GET_EXPRESSION lpGetExpressionRoutine			
 	
### -field PWINDBG_GET_SYMBOL lpGetSymbolRoutine			
 	
### -field PWINDBG_DISASM lpDisasmRoutine			
 	
### -field PWINDBG_CHECK_CONTROL_C lpCheckControlCRoutine			
 	
### -field PWINDBG_READ_PROCESS_MEMORY_ROUTINE lpReadProcessMemoryRoutine			
 	
### -field PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE lpWriteProcessMemoryRoutine			
 	
### -field PWINDBG_GET_THREAD_CONTEXT_ROUTINE lpGetThreadContextRoutine			
 	
### -field PWINDBG_SET_THREAD_CONTEXT_ROUTINE lpSetThreadContextRoutine			
 	
### -field PWINDBG_IOCTL_ROUTINE lpIoctlRoutine			
 	
### -field PWINDBG_STACKTRACE_ROUTINE lpStackTraceRoutine			
 	
## -remarks

## -see-also