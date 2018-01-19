---
UID : NN:dbgeng.IDebugClient6
title : IDebugClient6
author : windows-driver-content
description : This interface supports event context callbacks.
old-location : debugger\idebugclient6.htm
old-project : debugger
ms.assetid : 9F8DFF33-DE07-4061-9A9E-3C8172F75EB5
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
req.alt-api : IDebugClient6
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

# IDebugClient6 interface

This interface supports event context callbacks.

## Methods

<p>The <b>IDebugClient6</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugClient6.SetEventContextCallbacks](nf-dbgeng-idebugclient6-seteventcontextcallbacks.md) | Registers an event callbacks object with this client. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **DLL** |  |