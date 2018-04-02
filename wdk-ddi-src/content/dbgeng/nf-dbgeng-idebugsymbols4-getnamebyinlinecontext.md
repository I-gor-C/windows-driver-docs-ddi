---
UID: NF:dbgeng.IDebugSymbols4.GetNameByInlineContext
title: IDebugSymbols4::GetNameByInlineContext method
author: windows-driver-content
description: Gets a name by inline context.
old-location: debugger\idebugsymbols4_getnamebyinlinecontext.htm
old-project: debugger
ms.assetid: C87E70ED-FCB0-47B6-B6A3-A8EBC8E84058
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: GetNameByInlineContext method [Windows Debugging], GetNameByInlineContext method [Windows Debugging], IDebugSymbols4 interface, GetNameByInlineContext,IDebugSymbols4.GetNameByInlineContext, IDebugSymbols4, IDebugSymbols4 interface [Windows Debugging], GetNameByInlineContext method, IDebugSymbols4::GetNameByInlineContext, dbgeng/IDebugSymbols4::GetNameByInlineContext, debugger.idebugsymbols4_getnamebyinlinecontext
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
-	IDebugSymbols4.GetNameByInlineContext
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugSymbols4::GetNameByInlineContext method
Gets a name by inline context.

## Syntax

```
HRESULT GetNameByInlineContext(
  ULONG64  Offset,
  ULONG    InlineContext,
  PSTR     NameBuffer,
  ULONG    NameBufferSize,
  PULONG   NameSize,
  PULONG64 Displacement
);
```

## Parameters

`Offset`

An offset for the name.

`InlineContext`

The inline context.

`NameBuffer`

A pointer an output buffer.

`NameBufferSize`

The size of the name buffer.

`NameSize`

A pointer to the length of the name.

`Displacement`

A pointer to the displacement value of the name.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/BE2734B5-1E67-4E38-B4DF-0C353BFB1F0B">IDebugSymbols4</a>