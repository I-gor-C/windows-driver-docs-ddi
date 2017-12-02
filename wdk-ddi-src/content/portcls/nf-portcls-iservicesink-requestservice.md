---
UID: NF.portcls.IServiceSink.RequestService
title: IServiceSink::RequestService
author: windows-driver-content
description: The RequestService method is called to forward a service request to an IServiceSink object.
old-location: audio\iservicesink_requestservice.htm
old-project: audio
ms.assetid: c5035dee-3523-4b0d-9baa-e30720115499
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IServiceSink, RequestService, IServiceSink::RequestService
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IServiceSink.RequestService
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: IServiceSink
---

# IServiceSink::RequestService method



## -description
<p>The <code>RequestService</code> method is called to forward a service request to an <b>IServiceSink</b> object.</p>


## -syntax

````
VOID RequestService(
    None
);
````


## -parameters
<dl>

### -param None 

<dd></dd>
</dl>

## -returns
<p>None</p>

## -remarks


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
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>