---
UID: NF.dbgeng.IDebugClient5.PushOutputLinePrefixWide
title: IDebugClient5::PushOutputLinePrefixWide
author: windows-driver-content
description: Saves a wide string output line prefix.
old-location: debugger\idebugclient5_pushoutputlineprefixwide.htm
old-project: debugger
ms.assetid: B3D4AE97-9CDB-425D-A04B-E164852FDF19
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient5, PushOutputLinePrefixWide, IDebugClient5::PushOutputLinePrefixWide
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
req.alt-api: IDebugClient5.PushOutputLinePrefixWide
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
req.iface: IDebugClient5
---

# IDebugClient5::PushOutputLinePrefixWide method



## -description
<p>    Saves a wide string output line prefix.</p>


## -syntax

````
HRESULT PushOutputLinePrefixWide(
  [in, optional] PCWSTR   NewPrefix,
  [out]          PULONG64 Handle
);
````


## -parameters
<dl>

### -param <i>NewPrefix</i> [in, optional]

<dd>
<p>A pointer to the new output line Unicode character prefix.</p>
</dd>

### -param <i>Handle</i> [out]

<dd>
<p>The handle of the previous output line prefix.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient5::PushOutputLinePrefixWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
