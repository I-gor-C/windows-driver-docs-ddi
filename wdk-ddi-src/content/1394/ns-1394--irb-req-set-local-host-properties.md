---
UID: NS.1394._IRB_REQ_SET_LOCAL_HOST_PROPERTIES
title: IRB_REQ_SET_LOCAL_HOST_PROPERTIES
author: windows-driver-content
description: This structure contains the fields required to carry out a SetLocalHostProperties request.
old-location: ieee\irb_req_set_local_host_properties.htm
old-project: IEEE
ms.assetid: 59C1BBEF-ECC8-4852-B2E2-75751B5B25B2
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_SET_LOCAL_HOST_PROPERTIES, IRB_REQ_SET_LOCAL_HOST_PROPERTIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_SET_LOCAL_HOST_PROPERTIES
req.alt-loc: 1394.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# IRB_REQ_SET_LOCAL_HOST_PROPERTIES structure



## -description
<p>This structure contains the fields required to carry out a SetLocalHostProperties request.</p>


## -syntax

````
typedef struct _IRB_REQ_SET_LOCAL_HOST_PROPERTIES {
  ULONG nLevel;
  PVOID Information;
} IRB_REQ_SET_LOCAL_HOST_PROPERTIES;
````


## -struct-fields
<dl>

### -field <b>nLevel</b>

<dd>
<p>Specifies what level of information is desired from this call. The following flags are provided.  </p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>SET_LOCAL_HOST_PROPERTIES_GAP_COUNT </p>
</td>
<td>
<p>Sets a lower bound on the value the bus uses for its gap count. See the <i>IEEE 1394-1995 Specification</i> for a description of the gap count. </p>
</td>
</tr>
<tr>
<td>
<p>SET_LOCAL_HOST_PROPERTIES_MODIFY_CROM</p>
</td>
<td>
<p>Used to add or remove unit directories. This request cannot be used to modify instance directories or root keys in the configuration ROM. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Information</b>

<dd>
<p>Points to an information block to be filled in. The information returned depends on the value in <b>u.SetLocalHostProperties.nLevel</b>. Each block has its own particular structure.</p>
<table>
<tr>
<th>Flag</th>
<th>Structure</th>
</tr>
<tr>
<td>
<p>SET_LOCAL_HOST_PROPERTIES_GAP_COUNT </p>
</td>
<td>
<p>SET_LOCAL_HOST_PROPS2</p>
</td>
</tr>
<tr>
<td>
<p>SET_LOCAL_HOST_PROPERTIES_MODIFY_CROM</p>
</td>
<td>
<p>SET_LOCAL_HOST_PROPS3</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>