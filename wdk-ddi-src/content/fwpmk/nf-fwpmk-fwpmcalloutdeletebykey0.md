---
UID: NF.fwpmk.FwpmCalloutDeleteByKey0
title: FwpmCalloutDeleteByKey0
author: windows-driver-content
description: The FwpmCalloutDeleteByKey0 function deletes a callout from the filter engine.Note  FwpmCalloutDeleteByKey0 is a specific version of FwpmCalloutDeleteByKey.
old-location: netvista\fwpmcalloutdeletebykey0.htm
old-project: netvista
ms.assetid: b4c3cb7e-9c4a-40a5-a11b-952562c4790b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FwpmCalloutDeleteByKey0
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
req.alt-api: FwpmCalloutDeleteByKey0
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

# FwpmCalloutDeleteByKey0 function



## -description
<p>The 
  <b>FwpmCalloutDeleteByKey0</b> function deletes a callout from the filter engine.</p>


## -syntax

````
NTSTATUS NTAPI FwpmCalloutDeleteByKey0(
  _In_       HANDLE engineHandle,
  _In_ const GUID   *key
);
````


## -parameters
<dl>

### -param engineHandle [in]

<dd>
<p>A handle for an open session to the filter engine. A callout driver calls the 
     <a href="..\fwpmk\nf-fwpmk-fwpmengineopen0.md">FwpmEngineOpen0</a> function to open a
     session to the filter engine.</p>
</dd>

### -param key [in]

<dd>
<p>A pointer to a GUID that uniquely identifies the callout that is being deleted from the filter
     engine. This must be a pointer to the same GUID that was specified when the callout driver called the 
     <a href="..\fwpmk\nf-fwpmk-fwpmcalloutadd0.md">FwpmCalloutAdd0</a> function to add the
     callout to the filter engine.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpmCalloutDeleteByKey0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout was successfully deleted from the filter engine.</p><dl>
<dt><b>STATUS_FWP_IN_USE</b></dt>
</dl><p>One or more filters in the filter engine specify the callout for the filter's action.</p><dl>
<dt><b>STATUS_FWP_CALLOUT_NOT_FOUND</b></dt>
</dl><p>There is not a callout in the filter engine that matches the GUID specified in the 
       <i>key</i> parameter.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpmCalloutDeleteByKey0</b> function to delete a callout from the filter engine, using the GUID key to
    identify the callout to be deleted.</p>

<p>Callout drivers do not typically delete their callouts from the filter engine. In most situations, this
    is handled by a user-mode <a href="fwp.windows_filtering_platform_start_page">Windows Filtering Platform</a> management application.</p>

<p>A callout can be deleted from the filter engine only if there are no filters in the filter engine that
    specify the callout for the filter's action.</p>

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
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpmk.h (include Fwpmk.h)</dt>
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
<a href="..\fwpmk\nf-fwpmk-fwpmcalloutadd0.md">FwpmCalloutAdd0</a>
</dt>
<dt>
<a href="..\fwpmk\nf-fwpmk-fwpmcalloutdeletebyid0.md">FwpmCalloutDeleteById0</a>
</dt>
<dt>
<a href="..\fwpmk\nf-fwpmk-fwpmengineopen0.md">FwpmEngineOpen0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpmCalloutDeleteByKey0 function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
