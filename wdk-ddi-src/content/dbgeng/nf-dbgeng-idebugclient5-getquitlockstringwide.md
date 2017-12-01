---
UID: NF.dbgeng.IDebugClient5.GetQuitLockStringWide
title: IDebugClient5::GetQuitLockStringWide
author: windows-driver-content
description: Gets a Unicode character quit lock string.
old-location: debugger\idebugclient5_getquitlockstringwide.htm
old-project: debugger
ms.assetid: 0C69F19C-D048-47EB-9286-6F8C6E3398CC
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient5, GetQuitLockStringWide, IDebugClient5::GetQuitLockStringWide
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
req.alt-api: IDebugClient5.GetQuitLockStringWide
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

# IDebugClient5::GetQuitLockStringWide method



## -description
<p>Gets a Unicode character quit lock string.</p>


## -syntax

````
HRESULT GetQuitLockStringWide(
  [out]           writes_opt_(BufferSize) PWSTR Buffer,
  [in]            ULONG                         BufferSize,
  [out, optional] PULONG                        StringSize
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [out]

<dd>
<p>The buffer in which to write the Unicode character string.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size of the buffer.</p>
</dd>

### -param <i>StringSize</i> [out, optional]

<dd>
<p>A pointer to the string size.</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>    A quit lock string provides control to lock the session against
    undesired quits.  </p>

<p>The quit lock string
    cannot be retrieved from a secure session.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient5::GetQuitLockStringWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
