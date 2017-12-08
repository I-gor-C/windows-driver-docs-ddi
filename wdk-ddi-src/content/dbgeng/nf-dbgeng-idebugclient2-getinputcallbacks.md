---
UID: NF.dbgeng.IDebugClient2.GetInputCallbacks
title: IDebugClient2::GetInputCallbacks
author: windows-driver-content
description: The GetInputCallbacks method returns the input callbacks object registered with this client.
old-location: debugger\getinputcallbacks.htm
old-project: debugger
ms.assetid: 1788d9b6-5e5e-48b6-b746-fd078768892f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugClient2, GetInputCallbacks, IDebugClient2::GetInputCallbacks
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
req.alt-api: IDebugClient.GetInputCallbacks,IDebugClient2.GetInputCallbacks,IDebugClient3.GetInputCallbacks,IDebugClient4.GetInputCallbacks,IDebugClient5.GetInputCallbacks
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

# IDebugClient2::GetInputCallbacks method



## -description
<p>The <b>GetInputCallbacks</b> method returns the <a href="debugger.using_input_and_output#input_callbacks#input_callbacks">input callbacks</a> object registered with this client.</p>


## -syntax

````
HRESULT GetInputCallbacks(
  [out] PDEBUG_INPUT_CALLBACKS *Callbacks
);
````


## -parameters
<dl>

### -param Callbacks [out]

<dd>
<p>Receives an interface pointer for the <a href="..\dbgeng\nn-dbgeng-idebuginputcallbacks.md">IDebugInputCallbacks</a> object registered with the client.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Each client can have at most one <a href="..\dbgeng\nn-dbgeng-idebuginputcallbacks.md">IDebugInputCallbacks</a> object registered with it to receive requests for input.</p>

<p>If no <b>IDebugInputCallbacks</b> object is registered with the client, the value of <i>Callbacks</i> will be set to <b>NULL</b>.</p>

<p>The <b>IDebugInputCallbacks</b> interface extends the COM interface <b>IUnknown</b>.  Before returning the <b>IDebugInputCallbacks</b> object specified by <i>Callbacks</i>, the engine calls its <b>IUnknown::AddRef</b> method.  When this object is no longer needed, its <b>IUnknown::Release</b> method should be called. </p>

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
<a href="..\dbgeng\nn-dbgeng-idebuginputcallbacks.md">IDebugInputCallbacks</a>
</dt>
<dt>
<a href="debugger.setinputcallbacks">SetInputCallbacks</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::GetInputCallbacks method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
