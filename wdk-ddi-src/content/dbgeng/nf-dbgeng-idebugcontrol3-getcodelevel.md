---
UID: NF.dbgeng.IDebugControl3.GetCodeLevel
title: IDebugControl3::GetCodeLevel
author: windows-driver-content
description: The GetCodeLevel method returns the current code level and is mainly used when stepping through code.
old-location: debugger\getcodelevel.htm
old-project: debugger
ms.assetid: 965565ee-ef4c-4a1d-a6f1-77b6d63c6ee8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl3, GetCodeLevel, IDebugControl3::GetCodeLevel
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
req.alt-api: IDebugControl.GetCodeLevel,IDebugControl2.GetCodeLevel,IDebugControl3.GetCodeLevel
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

# IDebugControl3::GetCodeLevel method



## -description
<p>The <b>GetCodeLevel</b> method returns the current code level and is mainly used when stepping through code.</p>


## -syntax

````
HRESULT GetCodeLevel(
  [out] PULONG Level
);
````


## -parameters
<dl>

### -param Level [out]

<dd>
<p>Receives the current code level.  <i>Level</i> can take one of the values in the following table.</p>
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
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
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
<a href="debugger.setcodelevel">SetCodeLevel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetCodeLevel method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
