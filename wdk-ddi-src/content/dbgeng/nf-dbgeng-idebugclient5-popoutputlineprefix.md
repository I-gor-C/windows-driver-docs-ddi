---
UID: NF:dbgeng.IDebugClient5.PopOutputLinePrefix
title: IDebugClient5::PopOutputLinePrefix method
author: windows-driver-content
description: Restores a previously saved output line prefix.
old-location: debugger\idebugclient5_popoutputlineprefix.htm
old-project: debugger
ms.assetid: 40371218-E948-475E-92E6-0CB02D348008
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IDebugClient5, IDebugClient5 interface [Windows Debugging], PopOutputLinePrefix method, IDebugClient5::PopOutputLinePrefix, PopOutputLinePrefix method [Windows Debugging], PopOutputLinePrefix method [Windows Debugging], IDebugClient5 interface, PopOutputLinePrefix,IDebugClient5.PopOutputLinePrefix, dbgeng/IDebugClient5::PopOutputLinePrefix, debugger.idebugclient5_popoutputlineprefix
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
-	dbgeng.h
api_name:
-	IDebugClient5.PopOutputLinePrefix
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# PopOutputLinePrefix method
Restores a previously saved output line prefix.

## Syntax

````
HRESULT PopOutputLinePrefix(
  [in] ULONG64 Handle
);
````

## Parameters

`Handle`

The handle of a previously pushed prefix.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>