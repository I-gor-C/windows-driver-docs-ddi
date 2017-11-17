---
UID: NS.wdbgexts._WINDBG_OLDKD_EXTENSION_APIS
title: WINDBG_OLDKD_EXTENSION_APIS
author: windows-driver-content
description: 
ms.assetid: 14e608ed-1568-4755-8467-72b92439c685
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: WINDBG_OLDKD_EXTENSION_APIS, WINDBG_OLDKD_EXTENSION_APIS, *PWINDBG_OLDKD_EXTENSION_APIS
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

# WINDBG_OLDKD_EXTENSION_APIS structure

## -description



## -struct-fields

### -field ULONG nSize			
 	
### -field PWINDBG_OUTPUT_ROUTINE lpOutputRoutine			
 	
### -field PWINDBG_GET_EXPRESSION32 lpGetExpressionRoutine			
 	
### -field PWINDBG_GET_SYMBOL32 lpGetSymbolRoutine			
 	
### -field PWINDBG_DISASM32 lpDisasmRoutine			
 	
### -field PWINDBG_CHECK_CONTROL_C lpCheckControlCRoutine			
 	
### -field PWINDBG_READ_PROCESS_MEMORY_ROUTINE32 lpReadVirtualMemRoutine			
 	
### -field PWINDBG_WRITE_PROCESS_MEMORY_ROUTINE32 lpWriteVirtualMemRoutine			
 	
### -field PWINDBG_OLDKD_READ_PHYSICAL_MEMORY lpReadPhysicalMemRoutine			
 	
### -field PWINDBG_OLDKD_WRITE_PHYSICAL_MEMORY lpWritePhysicalMemRoutine			
 	
## -remarks

## -see-also