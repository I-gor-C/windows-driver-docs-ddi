---
UID: NF.fwpsk.FwpsQueryConnectionRedirectState0
title: FwpsQueryConnectionRedirectState0
author: windows-driver-content
description: The FwpsQueryConnectionRedirectState0 function returns the connection redirect state.Note  FwpsQueryConnectionRedirectState0 is a specific version of FwpsQueryConnectionRedirectState.
old-location: netvista\fwpsqueryconnectionredirectstate0.htm
old-project: netvista
ms.assetid: 6db0a5ac-edab-4e84-b378-30ed0c23cd4b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FwpsQueryConnectionRedirectState0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsQueryConnectionRedirectState0
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

# FwpsQueryConnectionRedirectState0 function



## -description
<p>The <b>FwpsQueryConnectionRedirectState0</b> function returns the connection redirect state.<div class="alert"><b>Note</b>  <b>FwpsQueryConnectionRedirectState0</b> is a specific version of <b>FwpsQueryConnectionRedirectState</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -syntax

````
FWPS_CONNECTION_REDIRECT_STATE NTAPI FwpsQueryConnectionRedirectState0(
   _In_ HANDLE                    redirectRecords,
   _In_ HANDLE                    redirectHandle,
   _Outptr_result_maybenull_ void **redirectContext
);
````


## -parameters
<dl>

### -param redirectRecords 

<dd>
<p>The redirect records handle  indicated to ALE_CONNECT_REDIRECT callout by the classify metadata.</p>
</dd>

### -param redirectHandle 

<dd>
<p>A redirect handle that was previously created by a call to the 
     <a href="..\fwpsk\nf-fwpsk-fwpsredirecthandlecreate0.md">FwpsRedirectHandleCreate0</a> function.</p>
</dd>

### -param redirectContext 

<dd>
<p>An optional handle to the redirect context. If the pointer is specified, and if the connection
     redirect state 
     <a href="netvista.fwps_connection_redirect_state">FWPS_CONNECTION_REDIRECT_STATE</a> associated with the injection handle is FWPS_CONNECTION_REDIRECTED_BY_SELF
     or FWPS_CONNECTION_PREVIOUSLY_REDIRECTED_BY_SELF, the redirect context supplied when the connection was redirected
     will be returned.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsQueryConnectionRedirectState0</b> function returns one of the states that are specified in the <a href="netvista.fwps_connection_redirect_state">FWPS_CONNECTION_REDIRECT_STATE</a> enumeration.</p>

## -remarks
<p>A callout driver calls the <b>FwpsQueryConnectionRedirectState0</b> function to get the redirect state of a connection. </p>

<p>If the redirect status is FWPS_CONNECTION_NOT_REDIRECTED, the ALE_CONNECT_REDIRECT callout can proceed to proxy the connection.</p>

<p>

If the redirect status is FWPS_CONNECTION_REDIRECTED_BY_SELF, the ALE_CONNECT_REDIRECT callout should return FWP_ACTION_PERMIT/FWP_ACTION_CONTINUE.

</p>

<p>If the redirect status is FWPS_CONNECTION_REDIRECTED_BY_OTHER, the ALE_CONNECT_REDIRECT callout could proceed to proxy the connection if it does not trust the other inspector's result.

</p>

<p>If the redirect status is FWPS_CONNECTION_PREVIOUSLY_REDIRECTED_BY_SELF, the ALE_CONNECT_REDIRECT callout must not perform redirection even if other inspectors' results are not acceptable. In this case,  it must either permit or block the connection (at the ALE_AUTH_CONNECT layer).

</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
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
<a href="netvista.fwps_connection_redirect_state">FWPS_CONNECTION_REDIRECT_STATE</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsredirecthandlecreate0.md">FwpsRedirectHandleCreate0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsQueryConnectionRedirectState0 function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
