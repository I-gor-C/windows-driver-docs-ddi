---
UID: NF.ks.KsValidateClockCreateRequest
title: KsValidateClockCreateRequest
author: windows-driver-content
description: The KsValidateClockCreateRequest function validates the clock creation request and returns the create structure associated with the request.This can only be called at PASSIVE_LEVEL.
old-location: stream\ksvalidateclockcreaterequest.htm
old-project: stream
ms.assetid: ec10c10e-4604-47fc-a2e7-4df9d90acf0b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsValidateClockCreateRequest
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
req.alt-api: KsValidateClockCreateRequest
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

# KsValidateClockCreateRequest function



## -description
<p>The <b>KsValidateClockCreateRequest</b> function validates the clock creation request and returns the create structure associated with the request.</p>
<p>This can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
NTSTATUS KsValidateClockCreateRequest(
  _In_  PIRP            lrp,
  _Out_ PKSCLOCK_CREATE *ClockCreate
);
````


## -parameters
<dl>

### -param <i>lrp</i> [in]

<dd>
<p>Specifies the IRP with the clock create request being handled.</p>
</dd>

### -param <i>ClockCreate</i> [out]

<dd>
<p>Specifies the clock create structure pointer passed to the create request.</p>
</dd>
</dl>

## -returns
<p>The <b>KsValidateClockCreateRequest</b> function returns STATUS_SUCCESS if successful, or an error if unsuccessful.</p>

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