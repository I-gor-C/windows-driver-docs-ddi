---
UID: NN:dbgeng.IDebugSymbolGroup
title: IDebugSymbolGroup
author: windows-driver-content
description: IDebugSymbolGroup interface
old-location: debugger\idebugsymbolgroup.htm
old-project: debugger
ms.assetid: dd629e4a-938e-4db6-b0f3-6dd12a431486
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: ComOther_f174a794-e2c2-4d0a-912e-b3de6327ef19.xml, IDebugSymbolGroup, IDebugSymbolGroup interface [Windows Debugging], IDebugSymbolGroup interface [Windows Debugging], described, dbgeng/IDebugSymbolGroup, debugger.idebugsymbolgroup
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
-	IDebugSymbolGroup
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugSymbolGroup interface



## Methods

<p>The <b>IDebugSymbolGroup</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugSymbolGroup::AddSymbol](nf-dbgeng-idebugsymbolgroup-addsymbol.md) | The AddSymbol method adds a symbol to a symbol group. |
| [IDebugSymbolGroup::ExpandSymbol](nf-dbgeng-idebugsymbolgroup-expandsymbol.md) | The ExpandSymbol method adds or removes the children of a symbol from a symbol group. |
| [IDebugSymbolGroup::GetNumberSymbols](nf-dbgeng-idebugsymbolgroup-getnumbersymbols.md) | The GetNumberSymbols method returns the number of symbols that are contained in a symbol group. |
| [IDebugSymbolGroup::GetSymbolName](nf-dbgeng-idebugsymbolgroup-getsymbolname.md) | The GetSymbolName method returns the name of a symbol in a symbol group. |
| [IDebugSymbolGroup::GetSymbolParameters](nf-dbgeng-idebugsymbolgroup-getsymbolparameters.md) | The GetSymbolParameters method returns the symbol parameters that describe the specified symbols in a symbol group. |
| [IDebugSymbolGroup::OutputAsType](nf-dbgeng-idebugsymbolgroup-outputastype.md) | The OutputAsType method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [IDebugSymbolGroup::OutputSymbols](nf-dbgeng-idebugsymbolgroup-outputsymbols.md) | The OutputSymbols method prints the specified symbols to the debugger console. |
| [IDebugSymbolGroup::RemoveSymbolByIndex](nf-dbgeng-idebugsymbolgroup-removesymbolbyindex.md) | The RemoveSymbolByIndex method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup::RemoveSymbolByName](nf-dbgeng-idebugsymbolgroup-removesymbolbyname.md) | The RemoveSymbolByName method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup::WriteSymbol](nf-dbgeng-idebugsymbolgroup-writesymbol.md) | The WriteSymbol methods set the value of the specified symbol. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup2.md">IDebugSymbolGroup2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup interface%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>