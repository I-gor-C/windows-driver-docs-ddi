---
UID: NF.ks.KsDispatchSpecificProperty
title: KsDispatchSpecificProperty
author: windows-driver-content
description: The KsDispatchSpecificProperty function dispatches the property to a specific handler.
old-location: stream\ksdispatchspecificproperty.htm
old-project: stream
ms.assetid: 3ea9a473-606d-4021-89af-5f895020d054
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsDispatchSpecificProperty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsDispatchSpecificProperty
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsDispatchSpecificProperty function



## -description
<p>The <b>KsDispatchSpecificProperty</b> function dispatches the property to a specific handler. The function assumes that the caller has previously dispatched this IRP to a handler through the <b>KsPropertyHandler</b> function. </p>
<p>This function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
KSDDKAPI NTSTATUS NTAPI KsDispatchSpecificProperty(void);
````


## -parameters


## -returns
<p>The <b>KsDispatchSpecificProperty</b> function returns STATUS_SUCCESS if successful, or if unsuccessful it returns an error.</p>

<p>The <b>KsDispatchSpecificProperty</b> function returns STATUS_SUCCESS if successful, or if unsuccessful it returns an error.</p>

<p>The <b>KsDispatchSpecificProperty</b> function returns STATUS_SUCCESS if successful, or if unsuccessful it returns an error.</p>

## -remarks
<p>The <b>KsDispatchSpecificProperty</b> function is intended for additional processing of a property such as completing a pending operation.</p>

<p>The <b>KsDispatchSpecificProperty</b> function is intended for additional processing of a property such as completing a pending operation.</p>

<p>The <b>KsDispatchSpecificProperty</b> function is intended for additional processing of a property such as completing a pending operation.</p>

<p>The <b>KsDispatchSpecificProperty</b> function is intended for additional processing of a property such as completing a pending operation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564263">KsPropertyHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDispatchSpecificProperty function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
