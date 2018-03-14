---
UID: NN:dbgeng.IDebugAdvanced
title: IDebugAdvanced
author: windows-driver-content
description: IDebugAdvanced interface
old-location: debugger\idebugadvanced.htm
old-project: debugger
ms.assetid: 773c93fe-1eec-4951-960e-67164dcb41ce
ms.author: windowsdriverdev
ms.date: 2/27/2018
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

<a href="..\dbgeng\nn-dbgeng-idebugadvanced2.md">IDebugAdvanced2</a>



<a href="..\dbgeng\nn-dbgeng-idebugadvanced3.md">IDebugAdvanced3</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugAdvanced interface%20 RELEASE:%20(2/27/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>