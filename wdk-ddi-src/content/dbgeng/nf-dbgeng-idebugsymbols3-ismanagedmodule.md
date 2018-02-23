---
UID: NF:dbgeng.IDebugSymbols3.IsManagedModule
title: IDebugSymbols3::IsManagedModule method
author: windows-driver-content
description: Checks whether the engine is using managed debugging support when it retrieves information for a module.
old-location: debugger\idebugsymbols3_ismanagedmodule.htm
old-project: Debugger
ms.assetid: AECBA6E8-B030-4418-A561-9E48B4880D15
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: IDebugSymbols3 interface [Windows Debugging], IsManagedModule method, IsManagedModule, debugger.idebugsymbols3_ismanagedmodule, dbgeng/IDebugSymbols3::IsManagedModule, IDebugSymbols3::IsManagedModule, IDebugSymbols3, IsManagedModule method [Windows Debugging], IsManagedModule method [Windows Debugging], IDebugSymbols3 interface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
-	Dbgeng.h
apiname:
-	IDebugSymbols3.IsManagedModule
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---


# IsManagedModule method
Checks whether the engine is using managed
    debugging support when it retrieves information
    for a module.

## Syntax

````
HRESULT IsManagedModule(
  [in] ULONG   Index,
  [in] ULONG64 Base
);
````

## Parameters

`Index`

The index of a module.

`Base`

The base of the module.


## Return Value

<b>IDebugSymbols3::IsManagedModule</b> returns a value of <b>S_OK</b> if the engine is using managed
    debugging support when it retrieves information
    for a module.

## Remarks

It can be expensive to run this check.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** | dbgeng.h |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugSymbols3::IsManagedModule method%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>