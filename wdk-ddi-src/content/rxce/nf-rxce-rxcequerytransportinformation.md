---
UID: NF.rxce.RxCeQueryTransportInformation
title: RxCeQueryTransportInformation
author: windows-driver-content
description: RxCeQueryTransportInformation queries transport information for a given transport.
old-location: ifsk\rxcequerytransportinformation.htm
old-project: ifsk
ms.assetid: 94744af6-0c62-4942-a8a8-3a45a0ab98da
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCeQueryTransportInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxce.h
req.include-header: Rxce.h, Rxcehdlr.h, Tdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCeQueryTransportInformation
req.alt-loc: rxce.h
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

# RxCeQueryTransportInformation function



## -description
<p><b>RxCeQueryTransportInformation</b> queries transport information for a given transport.</p>


## -syntax

````
NTSTATUS RxCeQueryTransportInformation(
   PRXCE_TRANSPORT             pTransport,
   PRXCE_TRANSPORT_INFORMATION pTransportInformation
);
````


## -parameters
<dl>

### -param <i>pTransport</i> 

<dd>
<p>A pointer to the transport.</p>
</dd>

### -param <i>pTransportInformation</i> 

<dd>
<p>A pointer to the caller-supplied buffer for returning information. </p>
</dd>
</dl>

## -returns
<p><b>RxCeQueryTransportInformation</b> returns STATUS_SUCCESS on success or the following error code on failure: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This value can be returned for any of the following conditions:</p><dl>
<dd>
<p>The <i>pTransport</i> parameter passed to this routine was invalid.</p>
</dd>
<dd>
<p>The <i>pTransportInformation</i> parameter did not point to allocated memory large enough to hold an <b>RXCE_TRANSPORT_INFORMATION</b> data structure. </p>
</dd>
</dl><p>The <i>pTransport</i> parameter passed to this routine was invalid.</p>

<p>The <i>pTransportInformation</i> parameter did not point to allocated memory large enough to hold an <b>RXCE_TRANSPORT_INFORMATION</b> data structure. </p>

<p> </p>

## -remarks
<p><b>RxCeQueryTransportInformation</b> returns information for a given transport. The <b>RXCE_TRANSPORT_INFORMATION</b> data structure contains two data elements that are filled in by <b>RxCeQueryTransportInformation</b>:</p><dl>
<dd>
<p>ConnectionCount</p>
</dd>
<dd>
<p>QualityOfService</p>
</dd>
</dl><p>ConnectionCount</p>

<p>QualityOfService</p>

<p><b>RxCeQueryTransportInformation</b> returns information for a given transport. The <b>RXCE_TRANSPORT_INFORMATION</b> data structure contains two data elements that are filled in by <b>RxCeQueryTransportInformation</b>:</p><dl>
<dd>
<p>ConnectionCount</p>
</dd>
<dd>
<p>QualityOfService</p>
</dd>
</dl><p>ConnectionCount</p>

<p>QualityOfService</p>

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
<dt>Rxce.h (include Rxce.h, Rxcehdlr.h, or Tdi.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553456">RxCeQueryAdapterStatus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553461">RxCeQueryInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeQueryTransportInformation function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
