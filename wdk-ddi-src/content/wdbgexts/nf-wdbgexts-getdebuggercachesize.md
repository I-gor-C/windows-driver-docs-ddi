---
UID: NF.wdbgexts.GetDebuggerCacheSize
title: GetDebuggerCacheSize
author: windows-driver-content
description: The GetDebuggerCacheSize function returns the size of the cache that is used by the debugger to hold data that was obtained from the target.
old-location: debugger\getdebuggercachesize.htm
old-project: debugger
ms.assetid: 0365ffe5-575b-44a9-8711-837d499be8bc
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GetDebuggerCacheSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetDebuggerCacheSize
req.alt-loc: wdbgexts.h
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
req.iface: 
req.product: Windows 10 or later.
---

# GetDebuggerCacheSize function



## -description
<p>The <b>GetDebuggerCacheSize</b> function returns the size of the cache that is used by the debugger to hold data that was obtained from the target.</p>


## -syntax

````
__inline BOOL GetDebuggerCacheSize(
  _Out_ PULONG64 CacheSize
);
````


## -parameters
<dl>

### -param <i>CacheSize</i> [out]

<dd>
<p>Receives the size of the debugger's cache.</p>
</dd>
</dl>

## -returns
<p>If the function succeeds, the return value is <b>TRUE</b>; otherwise, it is <b>FALSE</b>.</p>

## -remarks
<p>The size of the cache can be set and retrieved by using the <a href="https://msdn.microsoft.com/638cb2e6-b333-4311-967c-d86c2e93b4ec">.cache</a> command.</p>

<p>Each target process has its own cache.  The returned size is the size of the cache for the current target.</p>

<p>The size of the cache can be set and retrieved by using the <a href="https://msdn.microsoft.com/638cb2e6-b333-4311-967c-d86c2e93b4ec">.cache</a> command.</p>

<p>Each target process has its own cache.  The returned size is the size of the cache for the current target.</p>

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
<dt>Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562180">.cache (Set Cache Size)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20GetDebuggerCacheSize function%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
