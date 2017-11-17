---
UID: NF.strmini.StreamClassDebugAssert
title: StreamClassDebugAssert
author: windows-driver-content
description: A minidriver can use the StreamClassDebugAssert routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger.
old-location: stream\streamclassdebugassert.htm
ms.assetid: df9b3231-4c43-4d4b-b128-e8d6a9f21b17
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StreamClassDebugAssert
req.alt-loc: Stream.lib,Stream.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Stream.lib
req.dll: 
req.irql: 
ms.keywords: StreamClassDebugAssert
req.iface: 
req.product: Windows 10 or later.
---

# StreamClassDebugAssert function



## -description
<p>A minidriver can use the <b>StreamClassDebugAssert</b> routine in a checked build environment to fail an assert, causing the stream class driver to output a debug message and break into the kernel debugger.</p>


## -syntax

````
VOID StreamClassDebugAssert(
  _In_ PCHAR File,
  _In_ ULONG Line,
  _In_ PCHAR AssertText,
  _In_ ULONG AssertValue
);
````


## -parameters
<dl>

### -param <i>File</i> [in]

<dd>
<p>Pointer to a <b>NULL</b>-terminated string containing the file name in which the assert occurred.</p>
</dd>

### -param <i>Line</i> [in]

<dd>
<p>Specifies the line number of the assert.</p>
</dd>

### -param <i>AssertText</i> [in]

<dd>
<p>Pointer to a <b>NULL</b>-terminated string containing text to be printed in the debug message.</p>
</dd>

### -param <i>AssertValue</i> [in]

<dd>
<p>Specifies a value to be printed in the debug message.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When running a checked version of the class driver, asserts are recognized, and result in a debug message and breakpoint. When running a free version of the class driver, asserts are ignored. For more information, see <a href="NULL">Stream Class Debugging</a>.</p>

<p>When running a checked version of the class driver, asserts are recognized, and result in a debug message and breakpoint. When running a free version of the class driver, asserts are ignored. For more information, see <a href="NULL">Stream Class Debugging</a>.</p>

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
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Stream.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543626">DbgBreakPoint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568235">StreamClassDebugPrint</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20StreamClassDebugAssert routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
