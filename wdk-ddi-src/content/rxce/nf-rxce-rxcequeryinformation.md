---
UID: NF.rxce.RxCeQueryInformation
title: RxCeQueryInformation
author: windows-driver-content
description: RxCeQueryInformation queries information about a connection in a caller-allocated buffer.
old-location: ifsk\rxcequeryinformation.htm
old-project: ifsk
ms.assetid: 58dd579c-3fb8-45c7-a7bc-ca0919166153
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxCeQueryInformation
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
req.alt-api: RxCeQueryInformation
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

# RxCeQueryInformation function



## -description
<p><b>RxCeQueryInformation</b> queries information about a connection in a caller-allocated buffer.</p>


## -syntax

````
NTSTATUS RxCeQueryInformation(
  _In_  PRXCE_VC                          pVc,
  _In_  RXCE_CONNECTION_INFORMATION_CLASS InformationClass,
  _Out_ PVOID                             pInformation,
  _In_  ULONG                             Length
);
````


## -parameters
<dl>

### -param <i>pVc</i> [in]

<dd>
<p>A pointer to the virtual circuit associated with this connection.</p>
</dd>

### -param <i>InformationClass</i> [in]

<dd>
<p>The desired information class for this query type. The value specified for <i>InformationClass</i> determines the type of information that is returned. This parameter is an enumeration defined in <i>rxcehdlr.h</i> and can be one of the following values:</p>
<p></p>
<dl>

### -param <a id="RxCeTransportProviderInformation"></a><a id="rxcetransportproviderinformation"></a><a id="RXCETRANSPORTPROVIDERINFORMATION"></a>RxCeTransportProviderInformation

<dd>
<p>Query the transport for provider information. An RXCE_TRANSPORT_PROVIDER_INFO structure is copied to the <i>pInformation</i> buffer on success. Note that RXCE_TRANSPORT_PROVIDER_INFO is a typedef for TDI_PROVIDER_INFO.</p>
</dd>

### -param <a id="RxCeConnectionInformation"></a><a id="rxceconnectioninformation"></a><a id="RXCECONNECTIONINFORMATION"></a>RxCeConnectionInformation

<dd>
<p>Query For information about the connection. An RXCE_CONNECTION_INFORMATION structure is copied to the <i>pInformation</i> buffer on success. Note that RXCE_CONNECTION_INFORMATION is a typedef for TDI_CONNECTION_INFORMATION.</p>
</dd>

### -param <a id="RxCeConnectionEndpointInformation"></a><a id="rxceconnectionendpointinformation"></a><a id="RXCECONNECTIONENDPOINTINFORMATION"></a>RxCeConnectionEndpointInformation

<dd>
<p>Query the transport For information about the connection endpoint. An RXCE_CONNECTION_INFO structure is copied to the <i>pInformation</i> buffer on success. Note that RXCE_CONNECTION_INFO is a typedef for TDI_CONNECTION_INFO.</p>
</dd>

### -param <a id="RxCeRemoteAddressInformation"></a><a id="rxceremoteaddressinformation"></a><a id="RXCEREMOTEADDRESSINFORMATION"></a>RxCeRemoteAddressInformation

<dd>
<p>Query the transport For information about the remote address. A  TDI_ADDRESS_INFO structure is copied to the <i>pInformation</i> buffer on success. </p>
</dd>
</dl>
</dd>

### -param <i>pInformation</i> [out]

<dd>
<p>The caller-supplied buffer for returning information. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length of  the buffer. </p>
</dd>
</dl>

## -returns
<p><b>RxCeQueryInformation</b> returns STATUS_SUCCESS on success or one of the following warning or error codes: </p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>This specified <i>length</i> of the output buffer pointed to by <i>pInformation</i> was not large enough to receive the information requested by the <i>InformationClass</i> query type.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The allocation of nonpaged pool memory needed by this routine failed. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This value can be returned for any of the following conditions:</p><dl>
<dd>
<p>The <i>pVC</i> parameter passed to this routine was invalid.</p>
</dd>
<dd>
<p>The connection, address, or transport defined for this virtual circuit was invalid. </p>
</dd>
<dd>
<p>The <i>InformationClass</i> for this query type was not one of the allowed values.</p>
</dd>
</dl><p>The <i>pVC</i> parameter passed to this routine was invalid.</p>

<p>The connection, address, or transport defined for this virtual circuit was invalid. </p>

<p>The <i>InformationClass</i> for this query type was not one of the allowed values.</p>

<p> </p>

## -remarks
<p><b>RxCeQueryInformation</b> returns information for a given virtual circuit. The  only values for <i>InformationClass</i> that can be specified when calling <b>RxCeQueryInformation</b> are the following:</p><dl>
<dd>
<p>RxCeTransportProviderInformation</p>
</dd>
<dd>
<p>RxCeConnectionInformation</p>
</dd>
<dd>
<p>RxCeConnectionEndpointInformation</p>
</dd>
<dd>
<p>RxCeRemoteAddressInformation</p>
</dd>
</dl><p>RxCeTransportProviderInformation</p>

<p>RxCeConnectionInformation</p>

<p>RxCeConnectionEndpointInformation</p>

<p>RxCeRemoteAddressInformation</p>

<p>For some values of <i>InformationClass</i>, <b>RxCeQueryInformation</b> calls <b>TdiBuildQueryInformation</b> and TDI to retrieve the requested information.</p>

<p><b>RxCeQueryInformation</b> returns information for a given virtual circuit. The  only values for <i>InformationClass</i> that can be specified when calling <b>RxCeQueryInformation</b> are the following:</p><dl>
<dd>
<p>RxCeTransportProviderInformation</p>
</dd>
<dd>
<p>RxCeConnectionInformation</p>
</dd>
<dd>
<p>RxCeConnectionEndpointInformation</p>
</dd>
<dd>
<p>RxCeRemoteAddressInformation</p>
</dd>
</dl><p>RxCeTransportProviderInformation</p>

<p>RxCeConnectionInformation</p>

<p>RxCeConnectionEndpointInformation</p>

<p>RxCeRemoteAddressInformation</p>

<p>For some values of <i>InformationClass</i>, <b>RxCeQueryInformation</b> calls <b>TdiBuildQueryInformation</b> and TDI to retrieve the requested information.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553474">RxCeQueryTransportInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeQueryInformation function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
