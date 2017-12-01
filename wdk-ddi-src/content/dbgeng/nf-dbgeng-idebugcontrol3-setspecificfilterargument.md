---
UID: NF.dbgeng.IDebugControl3.SetSpecificFilterArgument
title: IDebugControl3::SetSpecificFilterArgument
author: windows-driver-content
description: The SetSpecificFilterArgument method sets the value of filter argument for the specific filters that can have an argument.
old-location: debugger\setspecificfilterargument.htm
old-project: debugger
ms.assetid: 99731ad4-1023-4225-a133-3cb73e3ad07f
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl3, SetSpecificFilterArgument, IDebugControl3::SetSpecificFilterArgument
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
req.alt-api: IDebugControl.SetSpecificFilterArgument,IDebugControl2.SetSpecificFilterArgument,IDebugControl3.SetSpecificFilterArgument
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
req.iface: IDebugControl3
---

# IDebugControl3::SetSpecificFilterArgument method



## -description
<p>The <b>SetSpecificFilterArgument</b>  method sets the value of filter argument for the specific filters that can have an argument.</p>


## -syntax

````
HRESULT SetSpecificFilterArgument(
  [in] ULONG Index,
  [in] PCSTR Argument
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the specific filter whose argument will be set.  <i>Index</i> must be the index of a specific filter that has an argument.</p>
</dd>

### -param <i>Argument</i> [in]

<dd>
<p>Specifies the argument for the specific filter.  The interpretation of this argument depends on the specific filter.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p><i>Index</i> does not refer to a specific filter that has an argument.</p>

<p> </p>

## -remarks
<p>For a list of specific filters that have argument and the interpretation of those arguments, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543071">Event Filters</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugcontrol.md">IDebugControl</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol2.md">IDebugControl2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol3.md">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/fdb5059f-e7d9-4e14-aa3d-030e72c30732">sx, sxd, sxe, sxi, sxn (Set Exceptions)</a>
</dt>
<dt>
<a href="debugger.getspecificfilterargument">GetSpecificFilterArgument</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::SetSpecificFilterArgument method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
