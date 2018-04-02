---
UID: NF:dbgeng.IDebugSymbols.GetSymbolPath
title: IDebugSymbols::GetSymbolPath method
author: windows-driver-content
description: The GetSymbolPath method returns the symbol path.
old-location: debugger\getsymbolpath.htm
old-project: debugger
ms.assetid: bee6d7c5-b866-4b48-859e-9acb2219e7c1
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: GetSymbolPath method [Windows Debugging], GetSymbolPath method [Windows Debugging], IDebugSymbols interface, GetSymbolPath method [Windows Debugging], IDebugSymbols2 interface, GetSymbolPath method [Windows Debugging], IDebugSymbols3 interface, GetSymbolPath,IDebugSymbols.GetSymbolPath, IDebugSymbols, IDebugSymbols interface [Windows Debugging], GetSymbolPath method, IDebugSymbols2 interface [Windows Debugging], GetSymbolPath method, IDebugSymbols2::GetSymbolPath, IDebugSymbols3 interface [Windows Debugging], GetSymbolPath method, IDebugSymbols3::GetSymbolPath, IDebugSymbols::GetSymbolPath, IDebugSymbols_b13afb68-0f30-477d-be1b-a2b49ae40081.xml, dbgeng/IDebugSymbols2::GetSymbolPath, dbgeng/IDebugSymbols3::GetSymbolPath, dbgeng/IDebugSymbols::GetSymbolPath, debugger.getsymbolpath
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: dbgeng.h
req.include-header: Dbgeng.h
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
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugSymbols.GetSymbolPath
-	IDebugSymbols2.GetSymbolPath
-	IDebugSymbols3.GetSymbolPath
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IDebugSymbols::GetSymbolPath method
The <b>GetSymbolPath</b>  method returns the symbol path.

## Syntax

```
HRESULT GetSymbolPath(
  PSTR   Buffer,
  ULONG  BufferSize,
  PULONG PathSize
);
```

## Parameters

`Buffer`

Receives the symbol path.  This is a string that contains symbol path elements separated by semicolons (<b>;</b>).  Each symbol path element can specify either a directory or a symbol server.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.

`BufferSize`

Specifies the size, in characters, of the <i>Buffer</i> buffer.

`PathSize`

Receives the size, in characters, of the symbol path.


## Return Value

These methods can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The method was successful.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_FALSE</b></dt>
</dl>
</td>
<td width="60%">
The method was successful. However, the buffer was not large enough to hold the symbol path and the path was truncated.

</td>
</tr>
</table>

## Remarks

For more information about manipulating the symbol path, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560150">Using Symbols</a>.  For an overview of the symbol path and its syntax, see <a href="https://msdn.microsoft.com/705df98f-717f-40ad-a424-101826970691">Symbol Path</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538110">AppendSymbolPath</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550856">IDebugSymbols</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550864">IDebugSymbols2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff556802">SetSymbolPath</a>