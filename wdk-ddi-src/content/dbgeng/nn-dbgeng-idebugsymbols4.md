---
UID: NN:dbgeng.IDebugSymbols4
title: IDebugSymbols4
author: windows-driver-content
description: This interface supports determination of the symbol of an inline frame.
old-location: debugger\idebugsymbols4.htm
old-project: debugger
ms.assetid: BE2734B5-1E67-4E38-B4DF-0C353BFB1F0B
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugSymbols4, IDebugSymbols4 interface [Windows Debugging], IDebugSymbols4 interface [Windows Debugging], described, dbgeng/IDebugSymbols4, debugger.idebugsymbols4
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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
-	IDebugSymbols4
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugSymbols4 interface

This interface supports determination of the symbol of an inline frame.

## Methods

<p>The <b>IDebugSymbols4</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugSymbols4::GetFieldOffset](nf-dbgeng-idebugsymbols4-getfieldoffset.md) | The GetFieldOffset function returns the offset of a member from the beginning of a structure. |
| [IDebugSymbols4::GetLineByInlineContext](nf-dbgeng-idebugsymbols4-getlinebyinlinecontext.md) | Gets a line by inline context. |
| [IDebugSymbols4::GetLineByInlineContextWide](nf-dbgeng-idebugsymbols4-getlinebyinlinecontextwide.md) | Gets a line by inline context. |
| [IDebugSymbols4::GetNameByInlineContext](nf-dbgeng-idebugsymbols4-getnamebyinlinecontext.md) | Gets a name by inline context. |
| [IDebugSymbols4::GetNameByInlineContextWide](nf-dbgeng-idebugsymbols4-getnamebyinlinecontextwide.md) | Gets a name by inline context. |
| [IDebugSymbols4::GetScopeEx](nf-dbgeng-idebugsymbols4-getscopeex.md) | Gets the scope as an extended frame structure. |
| [IDebugSymbols4::OutputSymbolByInlineContext](nf-dbgeng-idebugsymbols4-outputsymbolbyinlinecontext.md) | Specifies an output symbol by using an inline context. |
| [IDebugSymbols4::SetScopeEx](nf-dbgeng-idebugsymbols4-setscopeex.md) | Sets the scope as an extended frame structure. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |