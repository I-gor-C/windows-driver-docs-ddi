---
UID: NF.fwpsk.FwpsRedirectHandleDestroy0
title: FwpsRedirectHandleDestroy0 function
author: windows-driver-content
description: The FwpsRedirectHandleDestroy0 function destroys a redirect handle that was previously created by calling the FwpsRedirectHandleCreate0 function.Note  FwpsRedirectHandleDestroy0 is a specific version of FwpsRedirectHandleDestroy.
old-location: netvista\fwpsredirecthandledestroy0.htm
old-project: netvista
ms.assetid: 0859c9bb-04f2-4bef-9da7-da72375d05f7
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: FwpsRedirectHandleDestroy0
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
req.alt-api: FwpsRedirectHandleDestroy0
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

# FwpsRedirectHandleDestroy0 function



## -description
The <b>FwpsRedirectHandleDestroy0</b> function destroys a redirect handle that was previously created by calling the <a href="netvista.fwpsredirecthandlecreate0">FwpsRedirectHandleCreate0</a> function.<div class="alert"><b>Note</b>  <b>FwpsRedirectHandleDestroy0</b> is a specific version of <b>FwpsRedirectHandleDestroy</b>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>



## -syntax

````
void NTAPI FwpsRedirectHandleDestroy0(
   _In_ HANDLE redirectHandle
);
````


## -parameters

### -param redirectHandle 

The redirect handle being destroyed.



## -returns
None.

## -remarks

    A callout driver calls the <b>FwpsRedirectHandleDestroy0</b> function to destroy a redirect handle that the callout driver previously created by calling the <a href="netvista.fwpsredirecthandlecreate0">FwpsRedirectHandleCreate0</a> function. 


   

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
Available starting with Windows 8.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
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
<a href="netvista.fwpsredirecthandlecreate0">FwpsRedirectHandleCreate0</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsRedirectHandleDestroy0 function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
