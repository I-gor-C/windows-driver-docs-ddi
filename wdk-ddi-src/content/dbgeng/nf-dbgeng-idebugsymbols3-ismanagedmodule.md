---
UID: NF:dbgeng.IDebugSymbols3.IsManagedModule
title: IDebugSymbols3::IsManagedModule method
author: windows-driver-content
description: Checks whether the engine is using managed debugging support when it retrieves information for a module.
old-location: debugger\idebugsymbols3_ismanagedmodule.htm
old-project: debugger
ms.assetid: AECBA6E8-B030-4418-A561-9E48B4880D15
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugSymbols3, IDebugSymbols3 interface [Windows Debugging], IsManagedModule method, IDebugSymbols3::IsManagedModule, IsManagedModule method [Windows Debugging], IsManagedModule method [Windows Debugging], IDebugSymbols3 interface, IsManagedModule,IDebugSymbols3.IsManagedModule, dbgeng/IDebugSymbols3::IsManagedModule, debugger.idebugsymbols3_ismanagedmodule
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
-	IDebugSymbols3.IsManagedModule
product:
- Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugSymbols3::IsManagedModule method
Checks whether the engine is using managed
    debugging support when it retrieves information
    for a module.

## Syntax

```
HRESULT IsManagedModule(
  ULONG   Index,
  ULONG64 Base
);
```

## Parameters

`Index`

The index of a module.

`Base`

The base of the module.


## Return Value

<b>IDebugSymbols3::IsManagedModule</b> returns a value of <b>S_OK</b> if the engine is using managed
    debugging support when it retrieves information
    for a module.

## Remarks

It can be expensive to run this check.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>