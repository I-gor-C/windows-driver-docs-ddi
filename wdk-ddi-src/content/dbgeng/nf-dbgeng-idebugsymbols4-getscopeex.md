---
UID: NF:dbgeng.IDebugSymbols4.GetScopeEx
title: IDebugSymbols4::GetScopeEx method
author: windows-driver-content
description: Gets the scope as an extended frame structure.
old-location: debugger\idebugsymbols4_getscopeex.htm
old-project: debugger
ms.assetid: B91EF786-51F7-406E-BCC2-C917E6881886
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: GetScopeEx method [Windows Debugging], GetScopeEx method [Windows Debugging], IDebugSymbols4 interface, GetScopeEx,IDebugSymbols4.GetScopeEx, IDebugSymbols4, IDebugSymbols4 interface [Windows Debugging], GetScopeEx method, IDebugSymbols4::GetScopeEx, dbgeng/IDebugSymbols4::GetScopeEx, debugger.idebugsymbols4_getscopeex
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
-	IDebugSymbols4.GetScopeEx
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugSymbols4::GetScopeEx method
Gets the scope as an extended frame structure.

## Syntax

```
HRESULT GetScopeEx(
  PULONG64              InstructionOffset,
  PDEBUG_STACK_FRAME_EX ScopeFrame,
  PVOID                 ScopeContext,
  ULONG                 ScopeContextSize
);
```

## Parameters

`InstructionOffset`

The offset of the instruction for the scope.

`ScopeFrame`

The scope frame returned as a <a href="https://msdn.microsoft.com/library/windows/hardware/dn818561">DEBUG_STACK_FRAME_EX</a> structure.

`ScopeContext`

A pointer to the scope context returned.

`ScopeContextSize`

The size of the scope context.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn818561">DEBUG_STACK_FRAME_EX</a>



<a href="https://msdn.microsoft.com/BE2734B5-1E67-4E38-B4DF-0C353BFB1F0B">IDebugSymbols4</a>