---
UID: NF.ks.KsValidateConnectRequest
title: KsValidateConnectRequest
author: windows-driver-content
description: The KsValidateConnectRequest function validates a connection request and returns a pointer to the connection structure associated with the request.This function can only be called at PASSIVE_LEVEL.
old-location: stream\ksvalidateconnectrequest.htm
ms.assetid: 64343a8a-9629-469e-95a3-b9c140cdd324
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsValidateConnectRequest
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
ms.keywords: KsValidateConnectRequest
req.iface: 
---

# KsValidateConnectRequest function



## -description
<p>The <b>KsValidateConnectRequest</b> function validates a connection request and returns a pointer to the connection structure associated with the request.</p>
<p>This function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
NTSTATUS KsValidateConnectRequest(
  _In_        PIRP             Irp ,
  _In_        ULONG            DescriptorsCount ,
  _In_  const KSPIN_DESCRIPTOR *Descriptor ,
  _Out_       PKSPIN_CONNECT   *Connect 
);
````


## -parameters
<dl>

### -param <i>Irp </i> [in]

<dd>
<p>Pointer to an IRP specifying the connection request.</p>
</dd>

### -param <i>DescriptorsCount </i> [in]

<dd>
<p>Specifies the number of pin descriptors passed.</p>
</dd>

### -param <i>Descriptor </i> [in]

<dd>
<p>Specifies a pointer to the list of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563533">KSPIN_DESCRIPTOR</a> structures.</p>
</dd>

### -param <i>Connect </i> [out]

<dd>
<p>Specifies a location in which to place a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563531">KSPIN_CONNECT</a> pointer passed to the create request. If <b>KsValidateConnectRequest</b>  returns success, then Connect+1 will contain a pointer to the KSDATAFORMAT with which the pin was opened.</p>
</dd>
</dl>

## -returns
<p>The <b>KsValidateConnectRequest</b> function returns STATUS_SUCCESS if successful, or it returns an error.</p>

## -remarks
<p>The <b>KsValidateConnectRequest</b> function handles basic connection structure access exceptions and validates the communication requirements, medium, protocol, and basic data format. The validation performed on the data format passed is based on the data range list for the specified pin against which a pin instance is to be created. Validation is successful in three instances: if a range major format is a wildcard, the range major format matches and the range subformat is a wildcard, or the range major format, range subformat, and the range specifier all match.</p>

<p>The buffer is passed a copy of the original input buffer, if the originator was not in kernel mode, and is therefore safe to access.</p>

<p>The <b>KsValidateConnectRequest</b> function handles basic connection structure access exceptions and validates the communication requirements, medium, protocol, and basic data format. The validation performed on the data format passed is based on the data range list for the specified pin against which a pin instance is to be created. Validation is successful in three instances: if a range major format is a wildcard, the range major format matches and the range subformat is a wildcard, or the range major format, range subformat, and the range specifier all match.</p>

<p>The buffer is passed a copy of the original input buffer, if the originator was not in kernel mode, and is therefore safe to access.</p>

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