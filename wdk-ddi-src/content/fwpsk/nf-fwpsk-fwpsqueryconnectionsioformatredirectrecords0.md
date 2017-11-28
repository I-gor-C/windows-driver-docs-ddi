---
UID: NF.fwpsk.FwpsQueryConnectionSioFormatRedirectRecords0
title: FwpsQueryConnectionSioFormatRedirectRecords0
author: windows-driver-content
description: The FwpsQueryConnectionSioFormatRedirectRecords0 function returns the connection redirect records for a redirected connection.
old-location: netvista\fwpsqueryconnectionsioformatredirectrecords0.htm
old-project: netvista
ms.assetid: AE24409D-AA60-4694-8855-AB2B0F6B1635
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsQueryConnectionSioFormatRedirectRecords0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 7
req.target-min-winversvr: Windows Server 2008 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsQueryConnectionSioFormatRedirectRecords0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# FwpsQueryConnectionSioFormatRedirectRecords0 function



## -description
<p>The <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> function returns the connection redirect records for a redirected connection. For more information about redirection, see <a href="NULL">Using Bind or Connect Redirection</a>.<div class="alert"><b>Note</b>  <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> is a specific version of <b>FwpsQueryConnectionSioFormatRedirectRecords</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS FwpsQueryConnectionSioFormatRedirectRecords0(
  _In_      HANDLE  RedirectRecords,
  _Out_opt_ PVOID   OutputBuffer,
  _In_      SIZE_T  OutputBufferLength,
  _Out_opt_ PSIZE_T BytesTransferred
);
````


## -parameters
<dl>

### -param <i>RedirectRecords</i> [in]

<dd>
<p>The redirect records handle that the  ALE_CONNECT_REDIRECT callout function received in the  <i>inMetaValues</i> parameter of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> function. This handle can be found in the <b>redirectRecords</b>   member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure.</p>
<p>A WFP redirect record is a buffer of opaque data that WFP must set on an outbound proxy connection so that the redirected connection and the original connection are logically related.</p>
</dd>

### -param <i>OutputBuffer</i> [out, optional]

<dd>
<p>A pointer to an output buffer that receives the redirect records. The buffer must be pointer-aligned.</p>
</dd>

### -param <i>OutputBufferLength</i> [in]

<dd>
<p>The size, in bytes, of the output buffer.</p>
</dd>

### -param <i>BytesTransferred</i> [out, optional]

<dd>
<p>A pointer to a variable that receives the number of bytes that were transferred. If the return value is <b>STATUS_BUFFER_TOO_SMALL</b>, this parameter receives the required buffer size.</p>
</dd>
</dl>

## -returns
<p>Returns an NTSTATUS value such as one of the following.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The output buffer was too small to contain all of the bytes to be transferred. The data transfer failed, and the required buffer size can be found in the <i>BytesTransferred</i> parameter.</p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The <i>RedirectRecords</i> parameter was null.</p>

<p> </p>

## -remarks
<p>The <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> function applies only to local proxies.</p>

<p>For more information about redirection, see <a href="NULL">Using Bind or Connect Redirection</a>.</p>

<p>The <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> function is designed to be used by a WFP connection redirection callout driver that doesn't accept the redirected connection until it has verified that it is able to connect to the actual remote endpoint.  To do this, the callout driver pends the redirected connection request at the <b>FWPS_LAYER_ALE_CONNECT_REDIRECT_V4</b> or <b>FWPS_LAYER_ALE_CONNECT_REDIRECT_V6</b> layer and calls <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> to retrieve the connection redirect records, which the callout driver then sends to the proxy to be used in a call to   <a href="https://msdn.microsoft.com/library/windows/hardware/hh802474">SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS</a>.</p>

<p>The <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> function applies only to local proxies.</p>

<p>For more information about redirection, see <a href="NULL">Using Bind or Connect Redirection</a>.</p>

<p>The <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> function is designed to be used by a WFP connection redirection callout driver that doesn't accept the redirected connection until it has verified that it is able to connect to the actual remote endpoint.  To do this, the callout driver pends the redirected connection request at the <b>FWPS_LAYER_ALE_CONNECT_REDIRECT_V4</b> or <b>FWPS_LAYER_ALE_CONNECT_REDIRECT_V6</b> layer and calls <b>FwpsQueryConnectionSioFormatRedirectRecords0</b> to retrieve the connection redirect records, which the callout driver then sends to the proxy to be used in a call to   <a href="https://msdn.microsoft.com/library/windows/hardware/hh802474">SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 7</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008 R2</p>
</td>
</tr>
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
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">Using Bind or Connect Redirection</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="netvista.sio_query_wfp_connection_redirect_records">SIO_QUERY_WFP_CONNECTION_REDIRECT_RECORDS (WDK)</a>
</dt>
<dt>
<a href="winsock.sio_query_wfp_connection_redirect_records">SIO_QUERY_WFP_CONNECTION_REDIRECT_RECORDS (SDK)</a>
</dt>
<dt>
<a href="netvista.sio_set_wfp_connection_redirect_records">SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS (WDK)</a>
</dt>
<dt>
<a href="winsock.sio_set_wfp_connection_redirect_records">SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS (SDK)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsQueryConnectionSioFormatRedirectRecords0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
