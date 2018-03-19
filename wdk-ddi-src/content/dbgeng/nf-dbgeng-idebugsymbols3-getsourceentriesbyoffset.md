---
UID: NF:dbgeng.IDebugSymbols3.GetSourceEntriesByOffset
title: IDebugSymbols3::GetSourceEntriesByOffset method
author: windows-driver-content
description: Queries symbol information and returns locations in the target's memory by using an offset.
old-location: debugger\idebugsymbols3_getsourceentriesbyoffset.htm
old-project: debugger
ms.assetid: CA84F931-5EB9-49D0-9EA5-288900A8DE46
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: GetSourceEntriesByOffset method [Windows Debugging], GetSourceEntriesByOffset method [Windows Debugging], IDebugSymbols3 interface, GetSourceEntriesByOffset,IDebugSymbols3.GetSourceEntriesByOffset, IDebugSymbols3, IDebugSymbols3 interface [Windows Debugging], GetSourceEntriesByOffset method, IDebugSymbols3::GetSourceEntriesByOffset, dbgeng/IDebugSymbols3::GetSourceEntriesByOffset, debugger.idebugsymbols3_getsourceentriesbyoffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
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
-	COM
api_location:
-	Dbgeng.h
api_name:
-	IDebugSymbols3.GetSourceEntriesByOffset
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# GetSourceEntriesByOffset method
Queries symbol information and returns locations in the target's memory by using an offset.

## Syntax

````
HRESULT GetSourceEntriesByOffset(
  [in]            ULONG64                                               Offset,
  [in]            ULONG                                                 Flags,
  [out]           _writes_opt_(EntriesCount) PDEBUG_SYMBOL_SOURCE_ENTRY Entries,
  [in]            ULONG                                                 EntriesCount,
  [out, optional] PULONG                                                EntriesAvail
);
````

## Parameters

`Offset`

The  offset of the entry.

`Flags`

A bit-set that contains options that affect the behavior of this method.

`Entries`

A pointer to a returned entry as a <a href="..\dbgeng\ns-dbgeng-_debug_symbol_source_entry.md">DEBUG_SYMBOL_SOURCE_ENTRY</a> structure.

`EntriesCount`

The number of entries.

`EntriesAvail`

A pointer to the number of entries available.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

This method can return multiple results for a source lookup. This allows for all possible results to be returned.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\ns-dbgeng-_debug_symbol_source_entry.md">DEBUG_SYMBOL_SOURCE_ENTRY</a>



<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>