---
UID: NN:dbgeng.IDebugEventCallbacksWide
title: IDebugEventCallbacksWide
author: windows-driver-content
description: IDebugEventCallbacksWide interface
old-location: debugger\idebugeventcallbackswide.htm
old-project: debugger
ms.assetid: 717fad3a-91b1-41c8-ac71-e9ea52533efd
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IDebugEventCallbacksWide, IDebugEventCallbacksWide interface [Windows Debugging], IDebugEventCallbacksWide interface [Windows Debugging], described, dbgeng/IDebugEventCallbacksWide, debugger.idebugeventcallbackswide
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	dbgeng.h
api_name:
-	IDebugEventCallbacksWide
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugEventCallbacksWide interface



## Methods

<p>The <b>IDebugEventCallbacksWide</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugEventCallbacksWide::Breakpoint](nf-dbgeng-idebugeventcallbackswide-breakpoint.md) | The Breakpoint callback method is called by the engine when the target issues a breakpointexception. |
| [IDebugEventCallbacksWide::ChangeDebuggeeState](nf-dbgeng-idebugeventcallbackswide-changedebuggeestate.md) | The ChangeDebuggeeState callback method is called by the engine when it makes or detects changes to the target. |
| [IDebugEventCallbacksWide::ChangeEngineState](nf-dbgeng-idebugeventcallbackswide-changeenginestate.md) | The ChangeEngineState callback method is called by the engine when its state has changed. |
| [IDebugEventCallbacksWide::ChangeSymbolState](nf-dbgeng-idebugeventcallbackswide-changesymbolstate.md) | The ChangeSymbolState callback method is called by the engine when the symbol state changes. |
| [IDebugEventCallbacksWide::CreateProcess](nf-dbgeng-idebugeventcallbackswide-createprocess.md) | The CreateProcess callback method is called by the engine when a create-processdebugging event occurs in the target. |
| [IDebugEventCallbacksWide::CreateThread](nf-dbgeng-idebugeventcallbackswide-createthread.md) | The CreateThread callback method is called by the engine when a create-threaddebugging event occurs in the target. |
| [IDebugEventCallbacksWide::Exception](nf-dbgeng-idebugeventcallbackswide-exception.md) | The Exception callback method is called by the engine when an exceptiondebugging event occurs in the target. |
| [IDebugEventCallbacksWide::ExitProcess](nf-dbgeng-idebugeventcallbackswide-exitprocess.md) | The ExitProcess callback method is called by the engine when an exit-processdebugging event occurs in the target. |
| [IDebugEventCallbacksWide::ExitThread](nf-dbgeng-idebugeventcallbackswide-exitthread.md) | The ExitThread callback method is called by the engine when an exit-threaddebugging event occurs in the target. |
| [IDebugEventCallbacksWide::GetInterestMask](nf-dbgeng-idebugeventcallbackswide-getinterestmask.md) | The GetInterestMask callback method is called to determine which events the IDebugEventCallbacksWide object is interested in. The engine calls GetInterestMask when the object is registered with a client by using SetEventCallbacks. |
| [IDebugEventCallbacksWide::LoadModule](nf-dbgeng-idebugeventcallbackswide-loadmodule.md) | The LoadModule callback method is called by the engine when a module-load debugging event occurs in the target. |
| [IDebugEventCallbacksWide::SessionStatus](nf-dbgeng-idebugeventcallbackswide-sessionstatus.md) | The SessionStatus callback method is called by the engine when a change occurs in the debugger session. |
| [IDebugEventCallbacksWide::SystemError](nf-dbgeng-idebugeventcallbackswide-systemerror.md) | The SystemError callback method is called by the engine when a system error occurs in the target. |
| [IDebugEventCallbacksWide::UnloadModule](nf-dbgeng-idebugeventcallbackswide-unloadmodule.md) | The UnloadModule callback method is called by the engine when a module-unload debugging event occurs in the target. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |