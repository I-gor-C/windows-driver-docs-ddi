---
UID: NN:dbgeng.IDebugAdvanced2
title: IDebugAdvanced2
author: windows-driver-content
description: IDebugAdvanced2 interface
old-location: debugger\idebugadvanced2.htm
old-project: debugger
ms.assetid: 9b5f73db-1fb8-4e07-8053-67cb5020505e
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugAdvanced2, IDebugAdvanced2 interface [Windows Debugging], IDebugAdvanced2 interface [Windows Debugging], described, dbgeng/IDebugAdvanced2, debugger.idebugadvanced2
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
-	IDebugAdvanced2
product:
- Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugAdvanced2 interface



## Methods

<p>The <b>IDebugAdvanced2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugAdvanced2::FindSourceFileAndToken](nf-dbgeng-idebugadvanced2-findsourcefileandtoken.md) | The FindSourceFileAndToken method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [IDebugAdvanced2::GetSourceFileInformation](nf-dbgeng-idebugadvanced2-getsourcefileinformation.md) | The GetSourceFileInformation method returns specified information about a source file. |
| [IDebugAdvanced2::GetSymbolInformation](nf-dbgeng-idebugadvanced2-getsymbolinformation.md) | The GetSymbolInformation method returns specified information about a symbol. |
| [IDebugAdvanced2::GetSystemObjectInformation](nf-dbgeng-idebugadvanced2-getsystemobjectinformation.md) | The GetSystemObjectInformation method returns information about operating system objects on the target. |
| [IDebugAdvanced2::GetThreadContext](nf-dbgeng-idebugadvanced2-getthreadcontext.md) | The GetThreadContext method returns the current thread context. |
| [IDebugAdvanced2::Request](nf-dbgeng-idebugadvanced2-request.md) | The Request method performs a variety of different operations. |
| [IDebugAdvanced2::SetThreadContext](nf-dbgeng-idebugadvanced2-setthreadcontext.md) | The SetThreadContext method sets the current thread context. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549798">IDebugAdvanced</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549807">IDebugAdvanced3</a>