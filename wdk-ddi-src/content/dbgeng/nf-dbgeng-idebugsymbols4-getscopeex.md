---
UID: NF.dbgeng.IDebugSymbols4.GetScopeEx
title: IDebugSymbols4::GetScopeEx
author: windows-driver-content
description: Gets the scope as an extended frame structure.
old-location: debugger\idebugsymbols4_getscopeex.htm
old-project: debugger
ms.assetid: B91EF786-51F7-406E-BCC2-C917E6881886
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols4, GetScopeEx, IDebugSymbols4::GetScopeEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols4.GetScopeEx
req.alt-loc: Dbgeng.h
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
req.iface: IDebugSymbols4
---

# IDebugSymbols4::GetScopeEx method



## -description
<p>Gets the scope as an extended frame structure. </p>


## -syntax

````
HRESULT GetScopeEx(
  [out, optional] PULONG64                                   InstructionOffset,
  [out, optional] PDEBUG_STACK_FRAME_EX                      ScopeFrame,
  [out]           _writes_bytes_opt_(ScopeContextSize) PVOID ScopeContext,
  [in]            ULONG                                      ScopeContextSize
);
````


## -parameters
<dl>

### -param <i>InstructionOffset</i> [out, optional]

<dd>
<p>The offset of the instruction for the scope. </p>
</dd>

### -param <i>ScopeFrame</i> [out, optional]

<dd>
<p>The scope frame returned as a <a href="..\dbgeng\ns-dbgeng--debug-stack-frame-ex.md">DEBUG_STACK_FRAME_EX</a> structure. </p>
</dd>

### -param <i>ScopeContext</i> [out]

<dd>
<p>A pointer to the scope context returned. </p>
</dd>

### -param <i>ScopeContextSize</i> [in]

<dd>
<p>The size of the scope context.</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks


## -requirements
<table>
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
<a href="..\dbgeng\ns-dbgeng--debug-stack-frame-ex.md">DEBUG_STACK_FRAME_EX</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols4.md">IDebugSymbols4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols4::GetScopeEx method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
