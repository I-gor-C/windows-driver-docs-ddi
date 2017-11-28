---
UID: NF.rxprocs.RxIsThisACscAgentOpen
title: RxIsThisACscAgentOpen
author: windows-driver-content
description: RxIsThisACscAgentOpen determines if a file open was made by a user-mode client-side caching agent.
old-location: ifsk\rxisthisacscagentopen.htm
old-project: ifsk
ms.assetid: b3bd9b9f-e859-4d7f-9735-5995cb3ef6e8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxIsThisACscAgentOpen
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxprocs.h
req.include-header: Rxcontx.h, Rxprocs.h
req.target-type: Desktop
req.target-min-winverclnt: The RxIsThisACscAgentOpen routine is only available on Windows Server 2003 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxIsThisACscAgentOpen
req.alt-loc: rxprocs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RxIsThisACscAgentOpen function



## -description
<p><b>RxIsThisACscAgentOpen</b> determines if a file open was made by a user-mode client-side caching agent.</p>


## -syntax

````
BOOLEAN RxIsThisACscAgentOpen(
  _In_ PRX_CONTEXT RxContext
);
````


## -parameters
<dl>

### -param <i>RxContext</i> [in]

<dd>
<p>A pointer to the RX_CONTEXT structure.</p>
</dd>
</dl>

## -returns
<p><b>RxIsThisACscAgentOpen </b>returns <b>TRUE</b> on success or <b>FALSE</b> on failure. </p>

## -remarks
<p><b>RxIsThisACscAgentOpen</b> is not useful for third-party network mini-redirectors since they cannot integrate into the existing client-side caching infrastructure.</p>

<p>The <b>RxIsThisACscAgentOpen</b> routine is called internally by RDBSS when initializing a V_NET_ROOT structure. A network mini-redirector integrated with client-side caching might call <b>RxIsThisACscAgentOpen</b> as part of the <b>MRxCreateVNetRoot</b> callback routine provided by the network mini-redirector. </p>

<p><b>RxIsThisACscAgentOpen</b> is not useful for third-party network mini-redirectors since they cannot integrate into the existing client-side caching infrastructure.</p>

<p>The <b>RxIsThisACscAgentOpen</b> routine is called internally by RDBSS when initializing a V_NET_ROOT structure. A network mini-redirector integrated with client-side caching might call <b>RxIsThisACscAgentOpen</b> as part of the <b>MRxCreateVNetRoot</b> callback routine provided by the network mini-redirector. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The RxIsThisACscAgentOpen routine is only available on Windows Server 2003 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxprocs.h (include Rxcontx.h or Rxprocs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.the_v_net_root_structure">The V_NET_ROOT Structure</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554751">RX_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxIsThisACscAgentOpen function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
