---
UID: NF.dbgeng.IDebugSymbols3.SetScopeFromJitDebugInfo
title: IDebugSymbols3::SetScopeFromJitDebugInfo
author: windows-driver-content
description: Recovers just-in-time (JIT) debugging information and sets current debugger scope context based on that information.
old-location: debugger\idebugsymbols3_setscopefromjitdebuginfo.htm
old-project: debugger
ms.assetid: 75417373-AA1B-4297-863A-00EA97069573
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, SetScopeFromJitDebugInfo, IDebugSymbols3::SetScopeFromJitDebugInfo
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
req.alt-api: IDebugSymbols3.SetScopeFromJitDebugInfo
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::SetScopeFromJitDebugInfo method



## -description
<p>Recovers just-in-time (JIT) debugging information and sets current
    debugger scope context based on that information.</p>


## -syntax

````
HRESULT SetScopeFromJitDebugInfo(
  [in] ULONG   OutputControl,
  [in] ULONG64 InfoOffset
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>An output control.</p>
</dd>

### -param <i>InfoOffset</i> [in]

<dd>
<p>An offset for the debugging information. </p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

<p>The method gets JUT debugging information from   a specified address from the debugging target, and then sets the current
    debugger scope context from that information. </p>

<p>This method is equivalent to '.jdinfo' command.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::SetScopeFromJitDebugInfo method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
