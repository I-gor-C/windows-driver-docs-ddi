---
UID: NF.fwpsk.FwpsOpenToken0
title: FwpsOpenToken0
author: windows-driver-content
description: The FwpsOpenToken0 function opens an access token.
old-location: netvista\fwpsopentoken0.htm
old-project: netvista
ms.assetid: B6C61023-F840-4517-83C1-BC9CBDFC27B0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FwpsOpenToken0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsOpenToken0
req.alt-loc: fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: 
---

# FwpsOpenToken0 function



## -description
<p>The <b>FwpsOpenToken0</b> function opens an access token.<div class="alert"><b>Note</b>  <b>FwpsOpenToken0</b> is a specific version of <b>FwpsOpenToken</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS NTAPI NTAPI FwpsOpenToken0(
  _In_  HANDLE engineHandle,
  _In_  LUID   modifiedId,
  _In_  DWORD  desiredAccess,
  _Out_ HANDLE *accessToken
);
````


## -parameters
<dl>

### -param <i>engineHandle</i> [in]

<dd>
<p>A handle for an open session to the filter engine. A callout driver calls the 
     <a href="..\fwpmk\nf-fwpmk-fwpmengineopen0.md">FwpmEngineOpen0</a> function to open a
     session to the filter engine.</p>
</dd>

### -param <i>modifiedId</i> [in]

<dd>
<p>Specifies an <a href="netvista.luid">LUID</a> that changes each time the token is modified. An application can use this value as a test of whether a security context has changed since it was last used.</p>
</dd>

### -param <i>desiredAccess</i> [in]

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> structure specifying the requested types of access to the access token. These requested access types are compared with the token's discretionary access-control list (<b>DACL</b>) to determine which accesses are granted or denied.</p>
</dd>

### -param <i>accessToken</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that receives a handle to the newly opened access token.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsOpenToken0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The access token was successfully opened.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with  Windows 7.</p>
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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fwpmk\nf-fwpmk-fwpmengineopen0.md">FwpmEngineOpen0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsOpenToken0 function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
