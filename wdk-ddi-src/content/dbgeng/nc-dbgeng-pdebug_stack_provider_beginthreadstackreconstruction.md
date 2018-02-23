---
UID: NC:dbgeng.PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION
title: PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION
author: windows-driver-content
description: The BeginThreadStackReconstruction callback function causes debugger to pass the stream to the dump stack provider prior to thread enumeration.
old-location: debugger\beginthreadstackreconstruction.htm
old-project: Debugger
ms.assetid: 50CBBBED-EF1B-485F-90D3-0056AF8984E7
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: debugger.beginthreadstackreconstruction, BeginThreadStackReconstruction, BeginThreadStackReconstruction callback function [Windows Debugging], BeginThreadStackReconstruction, PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION, PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION, dbgeng/BeginThreadStackReconstruction
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	Dbgeng.h
apiname:
-	BeginThreadStackReconstruction
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION callback function
The <i>BeginThreadStackReconstruction</i> callback function causes debugger to pass the stream to the dump stack provider prior to thread enumeration.
<div class="code"><span codelanguage="ManagedCPlusPlus"><table>
<tr>
<th>C++</th>
</tr>
<tr>
<td>
<pre>CALLBACK* PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION BeginThreadStackReconstruction; </pre>
</td>
</tr>
</table></span></div>

## Syntax

```
PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION PdebugStackProviderBeginthreadstackreconstruction;

HRESULT PdebugStackProviderBeginthreadstackreconstruction(
  ULONG StreamType,
  PVOID MiniDumpStreamBuffer,
  ULONG BufferSize
)
{...}
```

## Parameters

`StreamType`

A stream type.

`MiniDumpStreamBuffer`

A mini-dump stream buffer.

`BufferSize`

The size of the buffer.


## Return Value

If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

<i>BeginThreadStackReconstruction</i> is called <b>PDEBUG_STACK_PROVIDER_BEGINTHREADSTACKRECONSTRUCTION</b> in the Dbgeng.h header file.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |