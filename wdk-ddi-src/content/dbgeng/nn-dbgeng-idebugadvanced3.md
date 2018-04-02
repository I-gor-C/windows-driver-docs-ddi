---
UID: NN:dbgeng.IDebugAdvanced3
title: IDebugAdvanced3
author: windows-driver-content
description: IDebugAdvanced3 interface
old-location: debugger\idebugadvanced3.htm
old-project: debugger
ms.assetid: f0226d35-f7a9-4220-be91-afb6d0debd36
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugAdvanced3, IDebugAdvanced3 interface [Windows Debugging], IDebugAdvanced3 interface [Windows Debugging], described, dbgeng/IDebugAdvanced3, debugger.idebugadvanced3
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
-	dbgeng.h
api_name:
-	IDebugAdvanced3
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugAdvanced3 interface



## Methods

<p>The <b>IDebugAdvanced3</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugAdvanced3::FindSourceFileAndToken](nf-dbgeng-idebugadvanced3-findsourcefileandtoken.md) | The FindSourceFileAndToken method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [IDebugAdvanced3::FindSourceFileAndTokenWide](nf-dbgeng-idebugadvanced3-findsourcefileandtokenwide.md) | The FindSourceFileAndTokenWide method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [IDebugAdvanced3::GetSourceFileInformation](nf-dbgeng-idebugadvanced3-getsourcefileinformation.md) | The GetSourceFileInformation method returns specified information about a source file. |
| [IDebugAdvanced3::GetSourceFileInformationWide](nf-dbgeng-idebugadvanced3-getsourcefileinformationwide.md) | The GetSourceFileInformationWide method returns specified information about a source file. |
| [IDebugAdvanced3::GetSymbolInformation](nf-dbgeng-idebugadvanced3-getsymbolinformation.md) | The GetSymbolInformation method returns specified information about a symbol. |
| [IDebugAdvanced3::GetSymbolInformationWide](nf-dbgeng-idebugadvanced3-getsymbolinformationwide.md) | The SetSymbolInformationWide method returns specified information about a symbol. |
| [IDebugAdvanced3::GetSystemObjectInformation](nf-dbgeng-idebugadvanced3-getsystemobjectinformation.md) | The GetSystemObjectInformation method returns information about operating system objects on the target. |
| [IDebugAdvanced3::GetThreadContext](nf-dbgeng-idebugadvanced3-getthreadcontext.md) | The GetThreadContext method returns the current thread context. |
| [IDebugAdvanced3::Request](nf-dbgeng-idebugadvanced3-request.md) | The Request method performs a variety of different operations. |
| [IDebugAdvanced3::SetThreadContext](nf-dbgeng-idebugadvanced3-setthreadcontext.md) | The SetThreadContext method sets the current thread context. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549803">IDebugAdvanced2</a>