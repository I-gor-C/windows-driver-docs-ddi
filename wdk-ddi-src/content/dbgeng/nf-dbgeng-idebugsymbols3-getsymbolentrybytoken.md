---
UID : NF:dbgeng.IDebugSymbols3.GetSymbolEntryByToken
title : IDebugSymbols3::GetSymbolEntryByToken method
author : windows-driver-content
description : Looks up a symbol by using a managed metadata token.
old-location : debugger\idebugsymbols3_getsymbolentrybytoken.htm
old-project : debugger
ms.assetid : C5BAED6C-223F-4D1B-A9A4-323C93DD5AD9
ms.author : windowsdriverdev
ms.date : 1/19/2018
ms.keywords : GetSymbolEntryByToken method [Windows Debugging], GetSymbolEntryByToken method [Windows Debugging], IDebugSymbols3 interface, debugger.idebugsymbols3_getsymbolentrybytoken, dbgeng/IDebugSymbols3::GetSymbolEntryByToken, GetSymbolEntryByToken, IDebugSymbols3, IDebugSymbols3 interface [Windows Debugging], GetSymbolEntryByToken method, IDebugSymbols3::GetSymbolEntryByToken
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : dbgeng.h
req.include-header : Dbgeng.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : dbgeng.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PDOT4_ACTIVITY, DOT4_ACTIVITY"
---


# GetSymbolEntryByToken method
Looks up a symbol by using a managed metadata token.

## Syntax

````
HRESULT GetSymbolEntryByToken(
  [in]  ULONG64              ModuleBase,
  [in]  ULONG                Token,
  [out] PDEBUG_MODULE_AND_ID Id
);
````

## Parameters

`ModuleBase`

The base of the module.

`Token`

The token to use to look up the symbol.

`Id`

A pointer to the module as a <a href="..\dbgeng\ns-dbgeng-_debug_module_and_id.md">DEBUG_MODULE_AND_ID</a> structure.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dbgeng.h (include Dbgeng.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\dbgeng\ns-dbgeng-_debug_module_and_id.md">DEBUG_MODULE_AND_ID</a>

<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSymbolEntryByToken method%20 RELEASE:%20(1/19/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>