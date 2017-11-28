---
UID: NC.ks.PFNKSCONTEXT_DISPATCH
title: PFNKSCONTEXT_DISPATCH
author: windows-driver-content
description: A streaming minidriver's KStrContextDispatch routine is called to process IRP_MJ_POWER IRPs.
old-location: stream\kstrcontextdispatch.htm
old-project: stream
ms.assetid: be96eb59-6128-41bd-ad31-38f0d1a4e656
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KStrContextDispatch
req.alt-loc: ks.h
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
req.iface: 
---

# PFNKSCONTEXT_DISPATCH callback



## -description
<p>A streaming minidriver's <i>KStrContextDispatch</i> routine is called to process IRP_MJ_POWER IRPs.</p>


## -prototype

````
PFNKSCONTEXT_DISPATCH KStrContextDispatch;

NTSTATUS KStrContextDispatch(
  _In_ PVOID Context,
  _In_ PIRP  Irp
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Specifies the user-supplied memory context to be passed as the <i>PowerContext</i> argument to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566843">KsSetPowerDispatch</a> function.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Specifies the power IRP to be processed.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS.</p>

## -remarks
<p><i>KStrContextDispatch</i> must not complete the power IRP that is passed in the <i>Irp</i> parameter.</p>

<p>To manipulate the list entry only, <i>KStrContextDispatch</i> can call<b> KsSetPowerDispatch</b> while processing the power IRP. Manipulating other list entries can cause enumeration errors.</p>

<p><i>KStrContextDispatch</i> must not complete the power IRP that is passed in the <i>Irp</i> parameter.</p>

<p>To manipulate the list entry only, <i>KStrContextDispatch</i> can call<b> KsSetPowerDispatch</b> while processing the power IRP. Manipulating other list entries can cause enumeration errors.</p>

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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566843">KsSetPowerDispatch</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KStrContextDispatch routine%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
