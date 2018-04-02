---
UID: NF:dbgeng.IDebugClient5.GetOutputLinePrefixWide
title: IDebugClient5::GetOutputLinePrefixWide method
author: windows-driver-content
description: Gets a Unicode character string prefix for output lines.
old-location: debugger\idebugclient5_getoutputlineprefixwide.htm
old-project: debugger
ms.assetid: 145A478E-826B-4E82-B358-6140D3A4063F
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: GetOutputLinePrefixWide method [Windows Debugging], GetOutputLinePrefixWide method [Windows Debugging], IDebugClient5 interface, GetOutputLinePrefixWide,IDebugClient5.GetOutputLinePrefixWide, IDebugClient5, IDebugClient5 interface [Windows Debugging], GetOutputLinePrefixWide method, IDebugClient5::GetOutputLinePrefixWide, dbgeng/IDebugClient5::GetOutputLinePrefixWide, debugger.idebugclient5_getoutputlineprefixwide
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
-	IDebugClient5.GetOutputLinePrefixWide
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugClient5::GetOutputLinePrefixWide method
Gets a Unicode character string prefix for output lines.

## Syntax

```
HRESULT GetOutputLinePrefixWide(
  PWSTR  Buffer,
  ULONG  BufferSize,
  PULONG PrefixSize
);
```

## Parameters

`Buffer`

The pointer to the buffer of the prefix.

`BufferSize`

The length of the buffer.

`PrefixSize`

A pointer to the length of the prefix.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>