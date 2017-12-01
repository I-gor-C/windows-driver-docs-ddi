---
UID: NF.dbgeng.IDebugClient3.SetOtherOutputMask
title: IDebugClient3::SetOtherOutputMask
author: windows-driver-content
description: The SetOtherOutputMask method sets the output mask for another client.
old-location: debugger\setotheroutputmask.htm
old-project: debugger
ms.assetid: 09e698cb-09f0-40e0-90ac-0a03c4e5c17b
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient3, SetOtherOutputMask, IDebugClient3::SetOtherOutputMask
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
req.alt-api: IDebugClient.SetOtherOutputMask,IDebugClient2.SetOtherOutputMask,IDebugClient3.SetOtherOutputMask,IDebugClient4.SetOtherOutputMask,IDebugClient5.SetOtherOutputMask
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
req.iface: IDebugClient3
---

# IDebugClient3::SetOtherOutputMask method



## -description
<p>The <b>SetOtherOutputMask</b> method sets the output mask for another client.</p>


## -syntax

````
HRESULT SetOtherOutputMask(
  [in] PDEBUG_CLIENT Client,
  [in] ULONG         Mask
);
````


## -parameters
<dl>

### -param <i>Client</i> [in]

<dd>
<p>Specifies the client whose output mask will be set.</p>
</dd>

### -param <i>Mask</i> [in]

<dd>
<p>Specifies the new output mask for the client.  See <a href="debugger.debug_output_xxx">DEBUG_OUTPUT_XXX</a> for a description of the possible values for <i>Mask</i>.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For an overview of output in the debugger engine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugclient.md">IDebugClient</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient2.md">IDebugClient2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient3.md">IDebugClient3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient4.md">IDebugClient4</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
<dt>
<a href="debugger.getotheroutputmask">GetOtherOutputMask</a>
</dt>
<dt>
<a href="debugger.setoutputmask">SetOutputMask</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::SetOtherOutputMask method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
