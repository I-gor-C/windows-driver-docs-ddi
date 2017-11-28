---
UID: NF.fltkernel.FltClearCallbackDataDirty
title: FltClearCallbackDataDirty
author: windows-driver-content
description: The FltClearCallbackDataDirty routine clears the callback dirty flag in a callback data structure.
old-location: ifsk\fltclearcallbackdatadirty.htm
old-project: ifsk
ms.assetid: c53ec6e5-83f8-4262-b832-1a206e6652e6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltClearCallbackDataDirty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltClearCallbackDataDirty
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: 
req.iface: 
---

# FltClearCallbackDataDirty function



## -description
<p>The <b>FltClearCallbackDataDirty</b> routine clears the callback dirty flag in a callback data structure. </p>


## -syntax

````
VOID FltClearCallbackDataDirty(
  _Inout_ PFLT_CALLBACK_DATA Data
);
````


## -parameters
<dl>

### -param <i>Data</i> [in, out]

<dd>
<p>A pointer to a callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>To set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> structure's FLTFL_CALLBACK_DATA_DIRTY flag, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>. </p>

<p>To test a callback data structure's FLTFL_CALLBACK_DATA_DIRTY flag, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543311">FltIsCallbackDataDirty</a>. </p>

<p>To set an <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> structure's FLTFL_CALLBACK_DATA_DIRTY flag, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>. </p>

<p>To test a callback data structure's FLTFL_CALLBACK_DATA_DIRTY flag, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543311">FltIsCallbackDataDirty</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543311">FltIsCallbackDataDirty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltClearCallbackDataDirty routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
