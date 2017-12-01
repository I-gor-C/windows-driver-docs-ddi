---
UID: NF.dbgeng.IDebugControl2.SetCodeLevel
title: IDebugControl2::SetCodeLevel
author: windows-driver-content
description: The SetCodeLevel method sets the current code level and is mainly used when stepping through code.
old-location: debugger\setcodelevel.htm
old-project: debugger
ms.assetid: b2f318d2-9ee2-4b4b-86ff-4561f1bbe084
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, SetCodeLevel, IDebugControl2::SetCodeLevel
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
req.alt-api: IDebugControl.SetCodeLevel,IDebugControl2.SetCodeLevel,IDebugControl3.SetCodeLevel
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
req.iface: IDebugControl2
---

# IDebugControl2::SetCodeLevel method



## -description
<p>The <b>SetCodeLevel</b> method sets the current code level and is mainly used when stepping through code.</p>


## -syntax

````
HRESULT SetCodeLevel(
  [in] ULONG Level
);
````


## -parameters
<dl>

### -param <i>Level</i> [in]

<dd>
<p>Specifies the current code level.  <i>Level</i> can take one of the values in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_LEVEL_SOURCE</p>
</td>
<td>
<p><i>Source mode</i>.  When stepping through code on the target, the size of a single step will be a line of source code.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_LEVEL_ASSEMBLY</p>
</td>
<td>
<p><i>Assembly mode</i>.  When stepping through code on the target, the size of a single step will be a single processor instruction.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about the code level, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560141">Using Source Files</a>.</p>

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
<a href="debugger.getcodelevel">GetCodeLevel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::SetCodeLevel method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
