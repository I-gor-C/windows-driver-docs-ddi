---
UID: NN:dbgeng.IDebugSymbolGroup2
title: IDebugSymbolGroup2
author: windows-driver-content
description: IDebugSymbolGroup2 interface
old-location: debugger\idebugsymbolgroup2.htm
old-project: debugger
ms.assetid: d702fe69-966c-4b9a-aa0e-b8376288cb79
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IDebugSymbolGroup2, IDebugSymbolGroup2 interface [Windows Debugging], IDebugSymbolGroup2 interface [Windows Debugging], described, dbgeng/IDebugSymbolGroup2, debugger.idebugsymbolgroup2
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
-	IDebugSymbolGroup2
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugSymbolGroup2 interface



## Methods

<p>The <b>IDebugSymbolGroup2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDebugSymbolGroup2::AddSymbol](nf-dbgeng-idebugsymbolgroup2-addsymbol.md) | The AddSymbol method adds a symbol to a symbol group. |
| [IDebugSymbolGroup2::AddSymbolWide](nf-dbgeng-idebugsymbolgroup2-addsymbolwide.md) | The AddSymbolWide method adds a symbol to a symbol group. |
| [IDebugSymbolGroup2::ExpandSymbol](nf-dbgeng-idebugsymbolgroup2-expandsymbol.md) | The ExpandSymbol method adds or removes the children of a symbol from a symbol group. |
| [IDebugSymbolGroup2::GetNumberSymbols](nf-dbgeng-idebugsymbolgroup2-getnumbersymbols.md) | The GetNumberSymbols method returns the number of symbols that are contained in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolEntryInformation](nf-dbgeng-idebugsymbolgroup2-getsymbolentryinformation.md) | The GetSymbolEntryInformation method returns information about a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolName](nf-dbgeng-idebugsymbolgroup2-getsymbolname.md) | The GetSymbolName method returns the name of a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolNameWide](nf-dbgeng-idebugsymbolgroup2-getsymbolnamewide.md) | The GetSymbolNameWide method returns the name of a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolOffset](nf-dbgeng-idebugsymbolgroup2-getsymboloffset.md) | The GetSymbolOffset method retrieves the location in the process's virtual address space of a symbol in a symbol group, if the symbol has an absolute address. |
| [IDebugSymbolGroup2::GetSymbolParameters](nf-dbgeng-idebugsymbolgroup2-getsymbolparameters.md) | The GetSymbolParameters method returns the symbol parameters that describe the specified symbols in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolRegister](nf-dbgeng-idebugsymbolgroup2-getsymbolregister.md) | The GetSymbolRegister method returns the register that contains the value or a pointer to the value of a symbol in a symbol group. |
| [IDebugSymbolGroup2::GetSymbolSize](nf-dbgeng-idebugsymbolgroup2-getsymbolsize.md) | The GetSymbolSize method returns the size of a symbol's value. |
| [IDebugSymbolGroup2::GetSymbolTypeName](nf-dbgeng-idebugsymbolgroup2-getsymboltypename.md) | The GetSymbolTypeName methods return the name of the specified symbol's type. |
| [IDebugSymbolGroup2::GetSymbolTypeNameWide](nf-dbgeng-idebugsymbolgroup2-getsymboltypenamewide.md) | The GetSymbolTypeNameWide method returns the name of the specified symbol's type. |
| [IDebugSymbolGroup2::GetSymbolValueText](nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetext.md) | The GetSymbolValueText method returns a string that represents the value of a symbol. |
| [IDebugSymbolGroup2::GetSymbolValueTextWide](nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetextwide.md) | The GetSymbolValueTextWide method returns a string that represents the value of a symbol. |
| [IDebugSymbolGroup2::OutputAsType](nf-dbgeng-idebugsymbolgroup2-outputastype.md) | The OutputAsType method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [IDebugSymbolGroup2::OutputAsTypeWide](nf-dbgeng-idebugsymbolgroup2-outputastypewide.md) | The OutputAsTypeWide method changes the type of a symbol in a symbol group. The symbol's entry is updated to represent the new type. |
| [IDebugSymbolGroup2::OutputSymbols](nf-dbgeng-idebugsymbolgroup2-outputsymbols.md) | The OutputSymbols method prints the specified symbols to the debugger console. |
| [IDebugSymbolGroup2::RemoveSymbolByIndex](nf-dbgeng-idebugsymbolgroup2-removesymbolbyindex.md) | The RemoveSymbolByIndex method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup2::RemoveSymbolByName](nf-dbgeng-idebugsymbolgroup2-removesymbolbyname.md) | The RemoveSymbolByName method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup2::RemoveSymbolByNameWide](nf-dbgeng-idebugsymbolgroup2-removesymbolbynamewide.md) | The RemoveSymbolByNameWide method removes the specified symbol from a symbol group. |
| [IDebugSymbolGroup2::WriteSymbol](nf-dbgeng-idebugsymbolgroup2-writesymbol.md) | The WriteSymbol methods set the value of the specified symbol. |
| [IDebugSymbolGroup2::WriteSymbolWide](nf-dbgeng-idebugsymbolgroup2-writesymbolwide.md) | The WriteSymbolWide method sets the value of the specified symbol. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup.md">IDebugSymbolGroup</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup2 interface%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>