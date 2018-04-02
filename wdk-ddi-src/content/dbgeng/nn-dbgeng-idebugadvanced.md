---
UID: NN:dbgeng.IDebugAdvanced
title: IDebugAdvanced
author: windows-driver-content
description: IDebugAdvanced interface
old-location: debugger\idebugadvanced.htm
old-project: debugger
ms.assetid: 773c93fe-1eec-4951-960e-67164dcb41ce
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: IDebugAdvanced, IDebugAdvanced interface [Windows Debugging], IDebugAdvanced interface [Windows Debugging], described, IDebugAdvanced_73a2f722-f225-466b-aecc-2c7e6999e25f.xml, dbgeng/IDebugAdvanced, debugger.idebugadvanced
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
-	IDebugAdvanced
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugAdvanced interface



## Methods

<p>The <b>IDebugAdvanced</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugAdvanced::GetThreadContext](nf-dbgeng-idebugadvanced-getthreadcontext.md) | The GetThreadContext method returns the current thread context. |
| [IDebugAdvanced::SetThreadContext](nf-dbgeng-idebugadvanced-setthreadcontext.md) | The SetThreadContext method sets the current thread context. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549803">IDebugAdvanced2</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549807">IDebugAdvanced3</a>