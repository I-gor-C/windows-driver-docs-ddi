---
UID: NF.fwpsk.FwpsClassifyOptionSet0
title: FwpsClassifyOptionSet0 function
author: windows-driver-content
description: The FwpsClassifyOptionSet0 function is called by a callout filter's classifyFn function to specify additional information that affects the characteristics of permitted filtering operations.Note  FwpsClassifyOptionSet0 is a specific version of FwpsClassifyOptionSet. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwpsclassifyoptionset0.htm
old-project: NetVista
ms.assetid: 8653fac0-8b2f-4e77-9588-2854ae168c1a
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FwpsClassifyOptionSet0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsClassifyOptionSet0
req.alt-loc: Fwpkclnt.lib,Fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# FwpsClassifyOptionSet0 function



## -description
The 
  <b>FwpsClassifyOptionSet0</b> function is called by a callout filter's 
  <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> function to specify additional
  information that affects the characteristics of permitted filtering operations.



## -syntax

````
NTSTATUS NTAPI FwpsClassifyOptionSet0(
  _In_ const FWPS_INCOMING_METADATA_VALUES0 *inMetadataValues,
  _In_ const FWP_CLASSIFY_OPTION_TYPE       option,
  _In_ const FWP_VALUE0                     *newValue
);
````


## -parameters

### -param inMetadataValues [in]

A pointer to an 
     <a href="netvista.fwps_incoming_metadata_values0">FWPS_INCOMING_METADATA_VALUES0</a> structure. This structure contains the values for each of the
     metadata fields at the layer that is being filtered.


### -param option [in]

An 
     <a href="netvista.fwp_classify_option_type">FWP_CLASSIFY_OPTION_TYPE</a> enumeration
     constant that indicates whether the 
     <i>newValue</i> parameter refers to unicast, multicast, or loose source mapping states, or to data
     time-out values. For more information, see Remarks.


### -param newValue [in]

A pointer to an array of 
     <a href="netvista.fwp_value0">FWP_VALUE0</a> structures. Each structure in the
     array contains particular values for a particular FWP_OPTION_VALUE_XXX constant. For more information, see
     Remarks.


## -returns
The 
     <b>FwpsClassifyOptionSet0</b> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The function completed successfully.
<dl>
<dt><b>STATUS_FWP_INVALID_ENUMERATOR</b></dt>
</dl>The 
       <i>option</i> parameter does not match any of the values in the 
       <a href="netvista.fwp_classify_option_type">
       FWP_CLASSIFY_OPTION_TYPE</a> enumeration.
<dl>
<dt><b>STATUS_FWP_OUT_OF_BOUNDS</b></dt>
</dl>The option value specified by 
       <i>newValue</i> -&gt;
       <b>uint32</b> does not include one of the defined FWP_OPTION_VALUE_XXX constant values.
<dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl>The data type specified by 
       <i>newValue</i> -&gt;
       <b>Type</b> was not FWP_UINT32.
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>A general error occurred.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

 


## -remarks
This function should be called only by a callout filter's 
    <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> function.

The following are the allowed values of the 
    <i>option</i> parameter and members of the 
    <a href="netvista.fwp_value0">FWP_VALUE0</a> structure pointed to by the 
    <i>newValue</i> parameter.

FWP_CLASSIFY_OPTION_LOOSE_SOURCE_MAPPING

FWP_UINT32

FWP_OPTION_VALUE_ENABLE_LOOSE_SOURCE
       <dl>
<dd>Enable loose source mapping.</dd>
</dl>


FWP_OPTION_VALUE_DISABLE_LOOSE_SOURCE
       <dl>
<dd>Disable loose source mapping.</dd>
</dl>


FWP_CLASSIFY_OPTION_MULTICAST_STATE

FWP_OPTION_VALUE_ALLOW_MULTICAST_STATE
       <dl>
<dd>Allow link-local multicast state creation on outbound traffic.</dd>
</dl>


FWP_OPTION_VALUE_DENY_MULTICAST_STATE
       <dl>
<dd>Do not allow link-local multicast state creation on outbound traffic.</dd>
</dl>


FWP_OPTION_VALUE_ALLOW_NON_LINK_LOCAL_RESPONSE
       <dl>
<dd>Allow multicast state creation for outbound traffic (permitting non–link-local
        responses).</dd>
</dl>


FWP_CLASSIFY_OPTION_MCAST_BCAST_LIFETIME

FWP_UINT32 &gt; 0

Specifies the multicast/broadcast state lifetime, in seconds.

FWP_CLASSIFY_OPTION_UNICAST_LIFETIME

Specifies the unicast state lifetime, in seconds.

The first (highest weight) caller to set a particular option will be granted that option. For example,
    if callout A sets the multicast state option, callout B will not be able to do so, but callout B can set
    other options.


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
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a>
</dt>
<dt>
<a href="netvista.fwp_classify_option_type">FWP_CLASSIFY_OPTION_TYPE</a>
</dt>
<dt>
<a href="netvista.fwp_value0">FWP_VALUE0</a>
</dt>
<dt>
<a href="netvista.fwpm_classify_option0">FWPM_CLASSIFY_OPTION0</a>
</dt>
<dt>
<a href="netvista.fwpm_classify_options0">FWPM_CLASSIFY_OPTIONS0</a>
</dt>
<dt>
<a href="netvista.fwps_incoming_metadata_values0">
   FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20FwpsClassifyOptionSet0 function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

