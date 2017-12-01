---
UID: NF.dbgeng.IDebugClient2.ExitDispatch
title: IDebugClient2::ExitDispatch
author: windows-driver-content
description: The ExitDispatch method causes the DispatchCallbacks method to return.
old-location: debugger\exitdispatch.htm
old-project: debugger
ms.assetid: c4db90d9-d6d3-4bab-ac3a-6b94b0818f53
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugClient2, ExitDispatch, IDebugClient2::ExitDispatch
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
req.alt-api: IDebugClient.ExitDispatch,IDebugClient2.ExitDispatch,IDebugClient3.ExitDispatch,IDebugClient4.ExitDispatch,IDebugClient5.ExitDispatch
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
req.iface: IDebugClient2
---

# IDebugClient2::ExitDispatch method



## -description
<p>The <b>ExitDispatch</b> method causes the <a href="debugger.dispatchcallbacks">DispatchCallbacks</a> method to return.</p>


## -syntax

````
HRESULT ExitDispatch(
  [in] PDEBUG_CLIENT Client
);
````


## -parameters
<dl>

### -param <i>Client</i> [in]

<dd>
<p>Specifies the client whose <a href="debugger.dispatchcallbacks">DispatchCallbacks</a> method should return.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>This method is reentrant and may be called from any thread.</p>

<p>This method can be used to interrupt a thread waiting in <a href="debugger.dispatchcallbacks">DispatchCallbacks</a>.</p>

<p>For more information about callbacks, see <a href="https://msdn.microsoft.com/9090a465-b6ab-4e99-8155-b0abdb729468">Callbacks</a>.</p>

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
<a href="debugger.dispatchcallbacks">DispatchCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::ExitDispatch method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
