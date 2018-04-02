---
UID: NN:dbgeng.IDebugOutputCallbacks2
title: IDebugOutputCallbacks2
author: windows-driver-content
description: The IDebugOutputCallbacks2 interface allows clients to receive full debugger markup language (DML) content for presentation.
old-location: debugger\idebugoutputcallbacks2.htm
old-project: debugger
ms.assetid: D35D8960-AD9F-4493-B6CD-3E3049CC3BBD
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugOutputCallbacks2, IDebugOutputCallbacks2 interface [Windows Debugging], IDebugOutputCallbacks2 interface [Windows Debugging], described, dbgeng/IDebugOutputCallbacks2, debugger.idebugoutputcallbacks2
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
-	IDebugOutputCallbacks2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugOutputCallbacks2 interface

The <b>IDebugOutputCallbacks2</b> interface allows clients to receive full  debugger markup language (DML) content for presentation. 

This interface extends the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a> interface, not the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550804">IDebugOutputCallbacksWide</a> interface. Therefore, it can be passed in to the existing <a href="https://msdn.microsoft.com/library/windows/hardware/ff556751">SetOutputCallbacks</a> method. 

The engine performs a <b>QueryInterface</b> for <b>IDebugOutputCallbacks2</b> to see which interface the incoming output callback object supports. If the object supports <b>IDebugOutputCallbacks2</b>, all output will be sent through the extended <b>IDebugOutputCallbacks2</b> methods.

An output object can register for both text and DML content, if it can handle them both. During output processing of the callback the engine will pick the format that reduces conversions, thus supporting both may reduce conversions in the engine. It is not necessary, though, and supporting only one format is the expected mode of operation.

The basic <a href="https://msdn.microsoft.com/library/windows/hardware/ff550815">IDebugOutputCallbacks::Output</a> method is not used.

## Methods

<p>The <b>IDebugOutputCallbacks2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugOutputCallbacks2::GetInterestMask](nf-dbgeng-idebugoutputcallbacks2-getinterestmask.md) | Allows the callback object to describe which kinds of output notifications it wants to receive. |
| [IDebugOutputCallbacks2::Output](nf-dbgeng-idebugoutputcallbacks2-output.md) | This method is not used. |
| [IDebugOutputCallbacks2::Output2](nf-dbgeng-idebugoutputcallbacks2-output2.md) | Returns notifications for the IDebugOutputCallbacks2 interface. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550801">IDebugOutputCallbacks</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550804">IDebugOutputCallbacksWide</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff556751">SetOutputCallbacks</a>