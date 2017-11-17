---
UID: NF.engextcpp.ExtRemoteTyped.SetPrint
title: ExtRemoteTyped::SetPrint
author: windows-driver-content
description: The SetPrint method sets the typed data represented by the ExtRemoteTyped object by formatting an expression and then evaluating that expression.
old-location: debugger\extremotetyped_setprint.htm
ms.assetid: ae478779-8ec1-4a50-a37c-3017aca2c912
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteTyped.SetPrint
req.alt-loc: engextcpp.hpp
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
ms.keywords: ExtRemoteTyped, SetPrint, ExtRemoteTyped::SetPrint
req.iface: ExtRemoteTyped
---

# ExtRemoteTyped::SetPrint method



## -description
<p>The <b>SetPrint</b> method sets the typed data represented by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544162">ExtRemoteTyped</a> object by formatting an expression and then evaluating that expression.</p>


## -syntax

````
void SetPrint(
  [in] CPSTR Format,
             ...
);
````


## -parameters
<dl>

### -param <i>Format</i> [in]

<dd>
<p>The format string used to create the expression.  This is the same as the format string used by the C <b>printf</b> function.</p>
<div class="alert"><b>Note</b>   While other methods and functions in the debugger engine API provide additional, debugger-specific conversion characters, <b>SetPrint</b> only supports the conversion characters used by <b>printf</b>.</div>
<div> </div>
</dd>

### -param <i>...</i> 

<dd>
<p>The arguments for the format string, as in <b>printf</b>.  The arguments should match the conversion characters in <i>Format</i>.</p>
</dd>
</dl>

## -returns
<p>This method does not return a value.</p>

## -remarks


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
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544162">ExtRemoteTyped</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e75c17d2-fdf7-4dba-9892-74c764956924">ExtRemoteTyped::Set(bool)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a19d6aff-c4e4-4188-8f27-3689e91023b4">ExtRemoteTyped::Set(pcstr)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/acf789f7-781d-4078-90cc-79b0d2709696">ExtRemoteTyped::Set(pcstr ulong64)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fc3d8d9c-0b19-42b3-b4d7-90df4667739b">ExtRemoteTyped::Set(pcstr ulong64 bool)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20ExtRemoteTyped.SetPrint method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
