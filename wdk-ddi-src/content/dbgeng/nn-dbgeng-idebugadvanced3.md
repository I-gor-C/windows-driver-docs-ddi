---
UID: NN:dbgeng.IDebugAdvanced3
title: IDebugAdvanced3
author: windows-driver-content
description: IDebugAdvanced3 interface
old-location: debugger\idebugadvanced3.htm
old-project: debugger
ms.assetid: f0226d35-f7a9-4220-be91-afb6d0debd36
ms.author: windowsdriverdev
ms.date: 1/19/2018
ms.keywords: debugger.idebugadvanced3, IDebugAdvanced3 interface [Windows Debugging], IDebugAdvanced3 interface [Windows Debugging], described, IDebugAdvanced3, dbgeng/IDebugAdvanced3
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
req.lib: dbgeng.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	dbgeng.h
apiname:
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
| [dbgeng.IDebugAdvanced3.FindSourceFileAndToken](nf-dbgeng-idebugadvanced3-findsourcefileandtoken.md) | The FindSourceFileAndToken method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [dbgeng.IDebugAdvanced3.FindSourceFileAndTokenWide](nf-dbgeng-idebugadvanced3-findsourcefileandtokenwide.md) | The FindSourceFileAndTokenWide method returns the filename of a source file on the source path or return the value of a variable associated with a file token. |
| [dbgeng.IDebugAdvanced3.GetSourceFileInformation](nf-dbgeng-idebugadvanced3-getsourcefileinformation.md) | The GetSourceFileInformation method returns specified information about a source file. |
| [dbgeng.IDebugAdvanced3.GetSourceFileInformationWide](nf-dbgeng-idebugadvanced3-getsourcefileinformationwide.md) | The GetSourceFileInformationWide method returns specified information about a source file. |
| [dbgeng.IDebugAdvanced3.GetSymbolInformation](nf-dbgeng-idebugadvanced3-getsymbolinformation.md) | The GetSymbolInformation method returns specified information about a symbol. |
| [dbgeng.IDebugAdvanced3.GetSymbolInformationWide](nf-dbgeng-idebugadvanced3-getsymbolinformationwide.md) | The SetSymbolInformationWide method returns specified information about a symbol. |
| [dbgeng.IDebugAdvanced3.GetSystemObjectInformation](nf-dbgeng-idebugadvanced3-getsystemobjectinformation.md) | The GetSystemObjectInformation method returns information about operating system objects on the target. |
| [dbgeng.IDebugAdvanced3.GetThreadContext](nf-dbgeng-idebugadvanced3-getthreadcontext.md) | The GetThreadContext method returns the current thread context. |
| [dbgeng.IDebugAdvanced3.Request](nf-dbgeng-idebugadvanced3-request.md) | The Request method performs a variety of different operations. |
| [dbgeng.IDebugAdvanced3.SetThreadContext](nf-dbgeng-idebugadvanced3-setthreadcontext.md) | The SetThreadContext method sets the current thread context. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugadvanced2.md">IDebugAdvanced2</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugAdvanced3 interface%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>