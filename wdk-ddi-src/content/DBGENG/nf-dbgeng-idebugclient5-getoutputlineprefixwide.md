---
UID: NF.dbgeng.IDebugClient5.GetOutputLinePrefixWide
title: IDebugClient5::GetOutputLinePrefixWide
author: windows-driver-content
description: Gets a Unicode character string prefix for output lines.
old-location: debugger\idebugclient5_getoutputlineprefixwide.htm
ms.assetid: 145A478E-826B-4E82-B358-6140D3A4063F
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient5.GetOutputLinePrefixWide
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
ms.keywords: IDebugClient5, GetOutputLinePrefixWide, IDebugClient5::GetOutputLinePrefixWide
req.iface: IDebugClient5
---

# IDebugClient5::GetOutputLinePrefixWide method



## -description
<p>Gets a Unicode character string prefix for output lines.</p>


## -syntax

````
HRESULT GetOutputLinePrefixWide(
  [out]           _writes_opt_(BufferSize) PWSTR Buffer,
  [in]            ULONG                          BufferSize,
  [out, optional] PULONG                         PrefixSize
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [out]

<dd>
<p>The pointer to the buffer of the prefix.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The length of the buffer.</p>
</dd>

### -param <i>PrefixSize</i> [out, optional]

<dd>
<p>A pointer to the length of the prefix.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient5::GetOutputLinePrefixWide method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
