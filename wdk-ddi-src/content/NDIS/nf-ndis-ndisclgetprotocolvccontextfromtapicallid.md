---
UID: NF.ndis.NdisClGetProtocolVcContextFromTapiCallId
title: NdisClGetProtocolVcContextFromTapiCallId
author: windows-driver-content
description: NdisClGetProtocolVcContextFromTapiCallId retrieves the client context for a virtual connection (VC) identified by a TAPI Call ID string.
old-location: netvista\ndisclgetprotocolvccontextfromtapicallid.htm
ms.assetid: 5c716207-b093-499a-8fad-344b5ac51e25
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   
   NdisClGetProtocolVcContextFromTapiCallId (NDIS 5.1)) in Windows Vista. Supported for NDIS 5.1
   drivers (see 
   
   NdisClGetProtocolVcContextFromTapiCallId (NDIS 5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisClGetProtocolVcContextFromTapiCallId
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Protocol_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: DISPATCH_LEVEL
ms.keywords: NdisClGetProtocolVcContextFromTapiCallId
req.iface: 
---

# NdisClGetProtocolVcContextFromTapiCallId function



## -description
<p><b>NdisClGetProtocolVcContextFromTapiCallId</b> retrieves the client context for a virtual connection (VC)
  identified by a TAPI Call ID string.</p>


## -syntax

````
NDIS_STATUS NdisClGetProtocolVcContextFromTapiCallId(
  _In_  UNICODE_STRING TapiCallId,
  _Out_ PNDIS_HANDLE   ProtocolVcContext
);
````


## -parameters
<dl>

### -param <i>TapiCallId</i> [in]

<dd>
<p>Unicode string that identifies a particular VC. This string is the Unicode version of a string
     identifier that was previously returned by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561700">NdisCoGetTapiCallID</a> function.</p>
</dd>

### -param <i>ProtocolVcContext</i> [out]

<dd>
<p>Pointer to a caller-allocated NDIS_HANDLE that receives a handle to the client context for the VC.
     The client supplied this context to NDIS on return from its 
     <a href="https://msdn.microsoft.com/b086dd24-74f5-474a-8684-09bf92ac731b">ProtocolCoCreateVc</a> handler.</p>
</dd>
</dl>

## -returns
<p>Returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS successfully retrieved the handle to the client VC context for the VC identified by the
       TAPI Call ID string.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The attempt to retrieve the handle to the client VC context failed.</p>

<p> </p>

## -remarks
<p>Suppose a call manager calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> to create a VC for a TAPI
    call. NDIS in turn supplies the handle to the VC to a client. The client passes this VC handle in a call
    to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561700">NdisCoGetTapiCallId</a> function to
    retrieve a string identifier for the VC. The client can then present this identifier as a Unicode string
    to 
    <b>NdisClGetProtocolVcContextFromTapiCallId</b> to get back its context for the VC.</p>

<p>The client creates a context for each VC that it manages. The client uses 
    <b>NdisCoGetTapiCallId</b> to retrieve a string identifier for each VC. The client passes each string
    identifier to a TAPI application to identify each VC. Later, if a TAPI application passes one of these
    string identifiers down to the client in a VC-related operation, the client must pass this string
    identifier as a Unicode string in a call to 
    <b>NdisClGetProtocolVcContextFromTapiCallId</b> to get back the correct context for the VC.</p>

<p>See the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure for more
    information.</p>

<p>Suppose a call manager calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a> to create a VC for a TAPI
    call. NDIS in turn supplies the handle to the VC to a client. The client passes this VC handle in a call
    to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561700">NdisCoGetTapiCallId</a> function to
    retrieve a string identifier for the VC. The client can then present this identifier as a Unicode string
    to 
    <b>NdisClGetProtocolVcContextFromTapiCallId</b> to get back its context for the VC.</p>

<p>The client creates a context for each VC that it manages. The client uses 
    <b>NdisCoGetTapiCallId</b> to retrieve a string identifier for each VC. The client passes each string
    identifier to a TAPI application to identify each VC. Later, if a TAPI application passes one of these
    string identifiers down to the client in a VC-related operation, the client must pass this string
    identifier as a Unicode string in a call to 
    <b>NdisClGetProtocolVcContextFromTapiCallId</b> to get back the correct context for the VC.</p>

<p>See the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure for more
    information.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/e2ca9aff-f308-465c-a2ff-d41eb2f6947d">
   NdisClGetProtocolVcContextFromTapiCallId (NDIS 5.1)</a>) in Windows Vista. Supported for NDIS 5.1
   drivers (see 
   <b>
   NdisClGetProtocolVcContextFromTapiCallId (NDIS 5.1)</b>) in Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547996">Irql_Protocol_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561696">NdisCoCreateVc</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561700">NdisCoGetTapiCallId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisClGetProtocolVcContextFromTapiCallId function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
