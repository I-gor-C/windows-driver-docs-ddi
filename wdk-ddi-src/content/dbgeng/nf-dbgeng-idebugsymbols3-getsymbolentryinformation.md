---
UID: NF.dbgeng.IDebugSymbols3.GetSymbolEntryInformation
title: IDebugSymbols3::GetSymbolEntryInformation
author: windows-driver-content
description: The GetSymbolEntryInformation method returns the symbol entry information for a symbol.
old-location: debugger\getsymbolentryinformation.htm
old-project: debugger
ms.assetid: 02fe418f-1793-4585-9891-1274a4ddba74
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetSymbolEntryInformation, IDebugSymbols3::GetSymbolEntryInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3.GetSymbolEntryInformation
req.alt-loc: dbgeng.h
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetSymbolEntryInformation method



## -description
<p>The <b>GetSymbolEntryInformation</b> method returns the symbol entry information for a symbol.</p>


## -syntax

````
HRESULT GetSymbolEntryInformation(
  [in]  PDEBUG_MODULE_AND_ID Id,
  [out] PDEBUG_SYMBOL_ENTRY  Info
);
````


## -parameters
<dl>

### -param <i>Id</i> [in]

<dd>
<p>Specifies the module and symbol ID of the desired symbol.  For details on this structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541511">DEBUG_MODULE_AND_ID</a>.</p>
</dd>

### -param <i>Info</i> [out]

<dd>
<p>Receives the symbol entry information for the symbol.  For details on this structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541662">DEBUG_SYMBOL_ENTRY</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For details on the symbol entry information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

<p>For details on the symbol entry information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getsymbolentryinformation2">IdebugSymbolGroup2::GetSymbolEntryInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSymbolEntryInformation method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
