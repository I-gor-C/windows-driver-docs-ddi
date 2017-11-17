---
UID: NF.dbgeng.IDebugOutputCallbacks2.Output2
title: IDebugOutputCallbacks2::Output2
author: windows-driver-content
description: Returns notifications for the IDebugOutputCallbacks2 interface.
old-location: debugger\idebugoutputcallbacks2_output2.htm
ms.assetid: 2FFF9B54-6E77-4D46-B6C0-5BADD208BFCC
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
req.alt-api: IDebugOutputCallbacks2.Output2
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
ms.keywords: IDebugOutputCallbacks2, Output2, IDebugOutputCallbacks2::Output2
req.iface: IDebugOutputCallbacks2
---

# IDebugOutputCallbacks2::Output2 method



## -description
<p>Returns notifications for the <a href="https://msdn.microsoft.com/D35D8960-AD9F-4493-B6CD-3E3049CC3BBD">IDebugOutputCallbacks2</a> interface.</p>


## -syntax

````
HRESULT Output2(
  [in]           ULONG   Which,
  [in]           ULONG   Flags,
  [in]           ULONG64 Arg,
  [in, optional] PCWSTR  Text
);
````


## -parameters
<dl>

### -param <i>Which</i> [in]

<dd>
<p> The kind of notification that is coming in. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="DEBUG_OUTCBI_EXPLICIT_FLUSH"></a><a id="debug_outcbi_explicit_flush"></a><dl>

### -param <b>DEBUG_OUTCBI_EXPLICIT_FLUSH</b>


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

### -param <b>DEBUG_OUTCBI_TEXT</b>


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

### -param <b>DEBUG_OUTCBI_DML</b>


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

### -param <b>DEBUG_OUTCBI_ANY_FORMAT</b>


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

### -param <i>Flags</i> [in]

<dd>
<p>Flags that are part of the notification payload.</p>
</dd>

### -param <i>Arg</i> [in]

<dd>
<p>Arguments that are part of the notification payload.</p>
</dd>

### -param <i>Text</i> [in, optional]

<dd>
<p>A pointer to text that is part of the notification payload.</p>
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
<a href="https://msdn.microsoft.com/D35D8960-AD9F-4493-B6CD-3E3049CC3BBD">IDebugOutputCallbacks2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugOutputCallbacks2::Output2 method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
