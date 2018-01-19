---
UID : NN:dbgeng.IDebugInputCallbacks
title : IDebugInputCallbacks
author : windows-driver-content
description : IDebugInputCallbacks interface
old-location : debugger\idebuginputcallbacks.htm
old-project : debugger
ms.assetid : 2122d970-1d1c-4ef0-b8f7-92ef6e4f0731
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : IDebugSystemObjects4, IDebugSystemObjects4::SetImplicitThreadDataOffset, SetImplicitThreadDataOffset
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IDebugInputCallbacks
req.alt-loc : dbgeng.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---

# IDebugInputCallbacks interface



## Methods

<p>The <b>IDebugInputCallbacks</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugInputCallbacks.EndInput](nf-dbgeng-idebuginputcallbacks-endinput.md) | The EndInput callback method is called by the engine to indicate that it is no longer waiting for input. |
| [dbgeng.IDebugInputCallbacks.StartInput](nf-dbgeng-idebuginputcallbacks-startinput.md) | The StartInput callback method is called by the engine to indicate that it is waiting for a line of input. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **DLL** |  |