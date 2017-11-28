---
UID: NF.dbgeng.IDebugSymbols3.GetSourcePathElement
title: IDebugSymbols3::GetSourcePathElement
author: windows-driver-content
description: The GetSourcePathElement method returns an element from the source path.
old-location: debugger\getsourcepathelement.htm
old-project: debugger
ms.assetid: 69507aed-ff32-46f2-8efb-68c1a7288bfb
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetSourcePathElement, IDebugSymbols3::GetSourcePathElement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols.GetSourcePathElement,IDebugSymbols2.GetSourcePathElement,IDebugSymbols3.GetSourcePathElement
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetSourcePathElement method



## -description
<p>The <b>GetSourcePathElement</b>  method returns an element from the source path.</p>


## -syntax

````
HRESULT GetSourcePathElement(
  [in]            ULONG  Index,
  [out, optional] PSTR   Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG ElementSize
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the element in the source path that will be returned.  The source path is a string that contains elements separated by semicolons (;).  The index of the first element is zero.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the source path element.  Each source path element can be a directory or a source server.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the <i>Buffer</i> buffer.</p>
</dd>

### -param <i>ElementSize</i> [out, optional]

<dd>
<p>Receives the size, in characters, of the source path element.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The source path contains fewer than <i>Index</i> elements.</p>

<p> </p>

## -remarks
<p>The source path is used by the engine when searching for source files.</p>

<p>For more information about manipulating the source path, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560141">Using Source Files</a>.  For an overview of the source path and its syntax, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556906">Source Path</a>.</p>

<p>The source path is used by the engine when searching for source files.</p>

<p>For more information about manipulating the source path, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560141">Using Source Files</a>.  For an overview of the source path and its syntax, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556906">Source Path</a>.</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550856">IDebugSymbols</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550864">IDebugSymbols2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538102">AppendSourcePath</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548358">GetSourcePath</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols::GetSourcePathElement method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
