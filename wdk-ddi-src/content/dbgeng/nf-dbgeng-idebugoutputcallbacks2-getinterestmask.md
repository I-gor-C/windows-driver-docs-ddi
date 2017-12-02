---
UID: NF.dbgeng.IDebugOutputCallbacks2.GetInterestMask
title: IDebugOutputCallbacks2::GetInterestMask
author: windows-driver-content
description: Allows the callback object to describe which kinds of output notifications it wants to receive.
old-location: debugger\idebugoutputcallbacks2_getinterestmask.htm
old-project: debugger
ms.assetid: BA710D92-63F4-4B4B-868A-58074FC052E9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugOutputCallbacks2, GetInterestMask, IDebugOutputCallbacks2::GetInterestMask
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
req.alt-api: IDebugOutputCallbacks2.GetInterestMask
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
req.iface: IDebugOutputCallbacks2
---

# IDebugOutputCallbacks2::GetInterestMask method



## -description
<p>Allows the callback object to describe which kinds of output notifications it wants to receive. </p>


## -syntax

````
HRESULT GetInterestMask(
   PULONG Mask
);
````


## -parameters
<dl>

### -param Mask 

<dd>
<p>The type of output notification to receive. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="DEBUG_OUTCBI_EXPLICIT_FLUSH"></a><a id="debug_outcbi_explicit_flush"></a><dl>

### -param DEBUG_OUTCBI_EXPLICIT_FLUSH


### -param 0x00000001

</dl>
</td>
<td width="60%">
<p>Indicates that the callback wants notifications
of all explicit flushes.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DEBUG_OUTCBI_TEXT"></a><a id="debug_outcbi_text"></a><dl>

### -param DEBUG_OUTCBI_TEXT


### -param 0x00000002

</dl>
</td>
<td width="60%">
<p>Indicates that the callback wants
content in text form.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DEBUG_OUTCBI_DML"></a><a id="debug_outcbi_dml"></a><dl>

### -param DEBUG_OUTCBI_DML


### -param 0x00000004


</dl>
</td>
<td width="60%">
<p>Indicates that the callback wants
content in markup form.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DEBUG_OUTCBI_ANY_FORMAT"></a><a id="debug_outcbi_any_format"></a><dl>

### -param DEBUG_OUTCBI_ANY_FORMAT


### -param 0x00000006

</dl>
</td>
<td width="60%">
<p>Indicates that the callback wants
content in any format.</p>
</td>
</tr>
</table>
<p> </p>
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
<a href="..\dbgeng\nn-dbgeng-idebugoutputcallbacks2.md">IDebugOutputCallbacks2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugOutputCallbacks2::GetInterestMask method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
