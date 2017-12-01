---
UID: NF.fwpsk.FwpsRedirectHandleCreate0
title: FwpsRedirectHandleCreate0
author: windows-driver-content
description: The FwpsRedirectHandleCreate0 function creates a handle that connection redirection functions can use to redirect connections to a local process.
old-location: netvista\fwpsredirecthandlecreate0.htm
old-project: netvista
ms.assetid: 841f3885-509a-457e-854d-e8ead657de54
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FwpsRedirectHandleCreate0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsRedirectHandleCreate0
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FwpsRedirectHandleCreate0 function



## -description
<p>The <b>FwpsRedirectHandleCreate0</b> function creates a handle that  connection redirection functions can use to redirect connections to a local process. For more information about redirection, see <a href="NULL">Using Bind or Connect Redirection</a>.<div class="alert"><b>Note</b>  <b>FwpsRedirectHandleCreate0</b> is a specific version of <b>FwpsRedirectHandleCreate</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS NTAPI FwpsRedirectHandleCreate0(
   _In_ const GUID        *providerGuid,
   _In_ _Reserved_ UINT32 flags,
   _Out_ HANDLE           *redirectHandle
);
````


## -parameters
<dl>

### -param <i>providerGuid</i> 

<dd>
<p>The provider GUID.</p>
</dd>

### -param <i>flags</i> 

<dd>
<p>Reserved.  Set to zero.</p>
</dd>

### -param <i>redirectHandle</i> 

<dd>
<p>A pointer to the variable that receives the handle.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsRedirectHandleCreate0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>A redirect handle was successfully returned. The variable that the 
       <i>redirectHandle</i> parameter points to contains the handle.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the <b>FwpsRedirectHandleCreate0</b> function to create a handle that can be used to redirect connections.</p>

<p>For more information about redirection, see <a href="NULL">Using Bind or Connect Redirection</a>.</p>

<p>Your callout driver should call <b>FwpsRedirectHandleCreate0</b> once and cache the handle so that it can reuse the handle.</p>

<p>Before an Application Layer Enforcement (ALE) connect redirection callout can redirect connections to a local process, it must  obtain a redirect handle with the <b>FwpsRedirectHandleCreate0</b> function and put the handle in the <a href="..\fwpsk\ns-fwpsk--fwps-connect-request0.md">FWPS_CONNECT_REQUEST0</a> structure. The callout modifies the structure in the <a href="netvista.classifyfn">classifyFn</a> for the ALE connect redirect layers.
</p>

<p>After a callout driver has finished using a redirect handle, it must call the <a href="..\fwpsk\nf-fwpsk-fwpsredirecthandledestroy0.md">FwpsRedirectHandleDestroy0</a> function to destroy the handle. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.classifyfn">classifyFn</a>
</dt>
<dt>
<a href="..\fwpsk\ns-fwpsk--fwps-connect-request0.md">FWPS_CONNECT_REQUEST0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsredirecthandledestroy0.md">FwpsRedirectHandleDestroy0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsRedirectHandleCreate0 function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
