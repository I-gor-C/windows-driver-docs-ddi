---
UID: NF.dbgeng.IDebugControl2.SetLogMask
title: IDebugControl2::SetLogMask
author: windows-driver-content
description: The SetLogMask method sets the output mask for the currently open log file.
old-location: debugger\setlogmask.htm
old-project: debugger
ms.assetid: 86c4e5ec-e893-4b1e-b397-6c51351df46c
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugControl2, SetLogMask, IDebugControl2::SetLogMask
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
req.alt-api: IDebugControl.SetLogMask,IDebugControl2.SetLogMask,IDebugControl3.SetLogMask
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

# IDebugControl2::SetLogMask method



## -description
<p>The <b>SetLogMask</b> method sets the output mask for the currently open log file.</p>


## -syntax

````
HRESULT SetLogMask(
  [in] ULONG Mask
);
````


## -parameters
<dl>

### -param <i>Mask</i> [in]

<dd>
<p>Specifies the new output mask for the log file.  See <a href="debugger.debug_output_xxx">DEBUG_OUTPUT_XXX</a> for details about this value.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

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
<a href="debugger.getlogmask">GetLogMask</a>
</dt>
<dt>
<a href="debugger.openlogfile2">OpenLogFile2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::SetLogMask method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
