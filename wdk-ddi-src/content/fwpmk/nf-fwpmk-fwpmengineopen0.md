---
UID: NF.fwpmk.FwpmEngineOpen0
title: FwpmEngineOpen0 function
author: windows-driver-content
description: The FwpmEngineOpen0 function opens a session to the filter engine.Note  FwpmEngineOpen0 is a specific version of FwpmEngineOpen.
old-location: netvista\fwpmengineopen0.htm
old-project: netvista
ms.assetid: 4d805ffe-7cf9-4cbc-9077-e191ddc24ecd
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: FwpmEngineOpen0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpmk.h
req.include-header: Fwpmk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpmEngineOpen0
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
---

# FwpmEngineOpen0 function



## -description
The 
  <b>FwpmEngineOpen0</b> function opens a session to the filter engine.


## -syntax

````
NTSTATUS NTAPI FwpmEngineOpen0(
  _In_opt_ const wchar_t                   *serverName,
  _In_           UINT32                    authnService,
  _In_opt_       SEC_WINNT_AUTH_IDENTITY_W *authIdentity,
  _In_opt_ const FWPM_SESSION0             *session,
  _Out_          HANDLE                    *engineHandle
);
````


## -parameters

### -param serverName [in, optional]

A pointer to a NULL-terminated string that specifies the standard DNS name of the system on which
     the session to the filter engine is opened. Callout drivers must specify <b>NULL</b> for this parameter.

### -param authnService [in]

The authentication service to use. For a list of valid choices for this parameter, see
     Authentication-Service Constants in the RPC section in the Microsoft Windows SDK documentation. Callout
     drivers must specify either RPC_C_AUTHN_WINNT or RPC_C_AUTHN_DEFAULT for this parameter.

### -param authIdentity [in, optional]

A pointer to a <b>SEC_WINNT_AUTH_IDENTITY_W</b> structure that contains the authentication and
     authorization credentials for accessing the filter engine. This parameter is ignored when the 
     <b>FwpmEngineOpen0</b> function is called from a callout driver. Callout drivers should set this
     parameter to <b>NULL</b>.

### -param session [in, optional]

A pointer to an 
     <a href="netvista.fwpm_session0">FWPM_SESSION0</a> structure that defines
     session-specific parameters for the session being opened. This pointer is optional and can be
     <b>NULL</b>.

### -param engineHandle [out]

A pointer to a variable that receives a handle for the open session to the filter engine.

## -returns
The 
     <b>FwpmEngineOpen0</b> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>A session to the filter engine was successfully opened. The variable pointed to by the 
       <i>engineHandle</i> parameter contains a handle for the open session.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

 

## -remarks
A callout driver calls the 
    <b>FwpmEngineOpen0</b> function to open a session to the filter engine. A handle to an open session to the
    filter engine is a required parameter to most of the <a href="fwp.windows_filtering_platform_start_page">Windows Filtering Platform</a>
<a href="netvista.management_functions"> management functions</a>.

Callout drivers normally do not need to open a session to the filter engine because callout drivers
    typically do not call any of the <a href="fwp.windows_filtering_platform_start_page">Windows Filtering Platform</a> management functions.

For a callout driver to successfully open a session to the filter engine, the filter engine
    must be currently running at the time that the callout driver calls the 
    <b>FwpmEngineOpen0</b> function. A callout driver can call the 
    <a href="netvista.fwpmbfestateget0">FwpmBfeStateGet0</a> function to obtain the
    current state of the filter engine. Before calling <b>FwpmBfeStateGet0</b>, the callout driver must call the 
    <a href="netvista.fwpmbfestatesubscribechanges0">FwpmBfeStateSubscribeChanges0</a> function to register a callback function that will be called whenever
    there is a change in the state of the filter engine.

After a callout driver has finished accessing the filter engine, it calls the 
    <a href="netvista.fwpmengineclose0">FwpmEngineClose0</a> function to close the
    open session to the filter engine.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows Vista.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fwpmk.h (include Fwpmk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.fwpmbfestateget0">FwpmBfeStateGet0</a>
</dt>
<dt>
<a href="netvista.fwpmbfestatesubscribechanges0">
   FwpmBfeStateSubscribeChanges0</a>
</dt>
<dt>
<a href="netvista.fwpmcalloutadd0">FwpmCalloutAdd0</a>
</dt>
<dt>
<a href="netvista.fwpmcalloutdeletebyid0">FwpmCalloutDeleteById0</a>
</dt>
<dt>
<a href="netvista.fwpmcalloutdeletebykey0">FwpmCalloutDeleteByKey0</a>
</dt>
<dt>
<a href="netvista.fwpmengineclose0">FwpmEngineClose0</a>
</dt>
<dt>
<a href="netvista.other_windows_filtering_platform_functions">Other Windows Filtering
   Platform Functions</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpmEngineOpen0 function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
