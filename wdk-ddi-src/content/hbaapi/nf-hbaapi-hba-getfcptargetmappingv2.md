---
UID: NF.hbaapi.HBA_GetFcpTargetMappingV2
title: HBA_GetFcpTargetMappingV2
author: windows-driver-content
description: The HBA_GetFcpTargetMappingV2 routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate on the indicated port.
old-location: storage\hba_getfcptargetmappingv2.htm
old-project: storage
ms.assetid: 970475d7-dd81-4189-bd2b-2a22c4f732dc
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_GetFcpTargetMappingV2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_GetFcpTargetMappingV2
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
req.iface: 
---

# HBA_GetFcpTargetMappingV2 function



## -description
<p>The <b>HBA_GetFcpTargetMappingV2</b> routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate on the indicated port.</p>


## -syntax

````
HBA_STATUS HBA_API HBA_GetFcpTargetMappingV2(
  _In_    HBA_HANDLE             HbaHandle,
  _In_    HBA_WWN                HbaPortWWN,
  _Inout_ HBA_FCPTARGETMAPPINGV2 *Mapping
);
````


## -parameters
<dl>

### -param <i>HbaHandle</i> [in]

<dd>
<p>Contains a value returned by the routine <a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a> that identifies the HBA to query for the target mappings. The HBA returns mappings for the targets that it can enumerate on the port specified by <i>HbaPortWWN</i>. </p>
</dd>

### -param <i>HbaPortWWN</i> [in]

<dd>
<p>Contains a 64-bit worldwide name (WWN) that uniquely identifies the fibre channel port on which the targets are enumerated. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -param <i>Mapping</i> [in, out]

<dd>
<p>Pointer to a structure of type <a href="..\hbaapi\ns-hbaapi-hba-fcptargetmappingv2.md">HBA_FCPTargetMappingV2</a> that contains an array of bindings between operating system and FCP identifiers for a set of target devices. These mappings are maintained by the HBA referenced by <i>HbaHandle</i>. On input, the <b>NumberOfEntries</b> member of HBA_FCPTargetMappingV2 should contain a number of mappings that fit in the output buffer. On output, the <b>NumberOfEntries</b> contains the number of mappings requested, or the full set of mappings, whichever is smaller. The value in <b>NumberOfEntries</b> contains the number of mappings returned even when an error occurred due to insufficient buffer space. </p>
</dd>
</dl>

## -returns
<p>The <b>HBA_GetFcpTargetMappingV2</b> routine returns a value of type <a href="storage.hba_status">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_GetFcpTargetMappingV2</b> returns one of the following qualifiers.</p><dl>
<dt><b>HBA_STATUS_OK</b></dt>
</dl><p>Returned if all mapping were successfully retrieved. </p><dl>
<dt><b>HBA_STATUS_ERROR_MORE_DATA</b></dt>
</dl><p>Returned if the buffer space is insufficient to hold all of the mapping information. </p><dl>
<dt><b>HBA_STATUS_ERROR_ILLEGAL_WWN</b></dt>
</dl><p>Returned if the HBA referenced by <i>HbaHandle</i> does not contain a port with a name of <i>HbaPortWWN. </i></p><dl>
<dt><b>HBA_STATUS_ERROR_NOT_SUPPORTED</b></dt>
</dl><p>Returned if the HBA referenced by <i>HbaHandle</i> does not support target mapping.</p><dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl><p>Returned if an unspecified error occurred that prevented the retrieval of the mapping information. </p>

<p> </p>

## -remarks
<p>The difference between the <b>HBA_GetFcpTargetMappingV2</b> routine and the <a href="..\hbaapi\nf-hbaapi-hba-getfcptargetmapping.md">HBA_GetFcpTargetMapping</a> routine is that the mappings returned by <b>HBA_GetFcpTargetMappingV2</b> include a logical unit ID descriptor (LUID) for each logical unit. If the vital product data for a logical unit provides more than one LUID, then the LUID that <b>HBA_GetFcpTargetMappingV2</b> returns depends on the types of LUIDs provided. For a complete explanation of how the LUID is chosen when more than one LUID is available, see the T11 committee's <i>Fibre Channel HBA API </i>specification.</p>

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
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hbaapi\ns-hbaapi-hba-fcptargetmappingv2.md">HBA_FCPTargetMappingV2</a>
</dt>
<dt>
<a href="..\hbaapi\nf-hbaapi-hba-getfcptargetmapping.md">HBA_GetFcpTargetMapping</a>
</dt>
<dt>
<a href="..\hbaapi\nf-hbaapi-hba-openadapter.md">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_GetFcpTargetMappingV2 routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
