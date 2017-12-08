---
UID: NF.dbgeng.IDebugClient7.SetClientContext
title: IDebugClient7::SetClientContext
author: windows-driver-content
description: The SetClientContext method is reserved for internal use.
old-location: debugger\idebugclient7_setclientcontext.htm
old-project: debugger
ms.assetid: 235DA791-D4D1-486C-B136-3703E62E91E2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugClient7, SetClientContext, IDebugClient7::SetClientContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient7.SetClientContext
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
req.iface: IDebugClient7
---

# IDebugClient7::SetClientContext method



## -description
<p>The <b>SetClientContext</b> method is reserved for internal use.</p>


## -syntax

````
HRESULT SetClientContext(
  [in] _reads_bytes_(ContextSize) PVOID Context,
  [in] ULONG                            ContextSize
);
````


## -parameters
<dl>

### -param Context [in]

<dd>
<p>The <b>SetClientContext</b> method is reserved for internal use.</p>
</dd>

### -param ContextSize [in]

<dd>
<p>The <b>SetClientContext</b> method is reserved for internal use.</p>
</dd>
</dl>

## -returns
<p>The <b>SetClientContext</b> method is reserved for internal use.</p>

## -remarks


## -requirements
<table>
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
<a href="..\dbgeng\ns-dbgeng--debug-client-context.md">DEBUG_CLIENT_CONTEXT</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient7.md">IDebugClient7</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient7::SetClientContext method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
