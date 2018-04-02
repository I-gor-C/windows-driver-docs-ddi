---
UID: NS:wdbgexts._SEARCHMEMORY
title: "_SEARCHMEMORY"
author: windows-driver-content
description: The SearchMemory function searches the target's virtual memory for a specified pattern of bytes.
old-location: debugger\searchmemory.htm
old-project: debugger
ms.assetid: 7e07c47e-803b-44fa-9d0f-aa86475246d2
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PSEARCHMEMORY, SEARCHMEMORY, SearchMemory, SearchMemory function [Windows Debugging], WdbgExts_Ref_4eb909e5-edfd-487c-851c-812b15274c66.xml, _SEARCHMEMORY, debugger.searchmemory, wdbgexts/SearchMemory"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdbgexts.h
api_name:
-	SearchMemory
product:
- Windows
targetos: Windows
req.typenames: SEARCHMEMORY, *PSEARCHMEMORY
---

# _SEARCHMEMORY structure
The <b>SearchMemory</b> function searches the target's virtual memory for a specified pattern of bytes.

## Syntax
```
typedef struct _SEARCHMEMORY {
  ULONG64 SearchAddress;
  ULONG64 SearchLength;
  ULONG64 FoundAddress;
  ULONG   PatternLength;
  PVOID   Pattern;
} SEARCHMEMORY, *PSEARCHMEMORY;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdbgexts.h (include Wdbgexts.h, Dbgeng.h) |