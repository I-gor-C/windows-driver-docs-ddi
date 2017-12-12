---
UID: NF.fwpmk.FwpmCalloutDeleteByKey0
title: FwpmCalloutDeleteByKey0 function
author: windows-driver-content
description: The FwpmCalloutDeleteByKey0 function deletes a callout from the filter engine.Note  FwpmCalloutDeleteByKey0 is a specific version of FwpmCalloutDeleteByKey.
old-location: netvista\fwpmcalloutdeletebykey0.htm
old-project: netvista
ms.assetid: b4c3cb7e-9c4a-40a5-a11b-952562c4790b
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
---

# FwpmCalloutDeleteByKey0 function



## -description
The 
  <b>FwpmCalloutDeleteByKey0</b> function deletes a callout from the filter engine.



## -syntax

````
NTSTATUS NTAPI FwpmCalloutDeleteByKey0(
  _In_       HANDLE engineHandle,
  _In_ const GUID   *key
);
````


## -parameters

### -param engineHandle [in]

A handle for an open session to the filter engine. A callout driver calls the 
     <a href="netvista.fwpmengineopen0">FwpmEngineOpen0</a> function to open a
     session to the filter engine.


### -param key [in]

A pointer to a GUID that uniquely identifies the callout that is being deleted from the filter
     engine. This must be a pointer to the same GUID that was specified when the callout driver called the 
     <a href="netvista.fwpmcalloutadd0">FwpmCalloutAdd0</a> function to add the
     callout to the filter engine.


## -returns
The 
     <b>FwpmCalloutDeleteByKey0</b> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The callout was successfully deleted from the filter engine.
<dl>
<dt><b>STATUS_FWP_IN_USE</b></dt>
</dl>One or more filters in the filter engine specify the callout for the filter's action.
<dl>
<dt><b>STATUS_FWP_CALLOUT_NOT_FOUND</b></dt>
</dl>There is not a callout in the filter engine that matches the GUID specified in the 
       <i>key</i> parameter.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

 


## -remarks
A callout driver calls the 
    <b>FwpmCalloutDeleteByKey0</b> function to delete a callout from the filter engine, using the GUID key to
    identify the callout to be deleted.

Callout drivers do not typically delete their callouts from the filter engine. In most situations, this
    is handled by a user-mode <a href="fwp.windows_filtering_platform_start_page">Windows Filtering Platform</a> management application.

A callout can be deleted from the filter engine only if there are no filters in the filter engine that
    specify the callout for the filter's action.


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
<a href="netvista.fwpmcalloutadd0">FwpmCalloutAdd0</a>
</dt>
<dt>
<a href="netvista.fwpmcalloutdeletebyid0">FwpmCalloutDeleteById0</a>
</dt>
<dt>
<a href="netvista.fwpmengineopen0">FwpmEngineOpen0</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpmCalloutDeleteByKey0 function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

