---
UID: NS.ks.PKSNODE_CREATE
title: PKSNODE_CREATE
author: windows-driver-content
description: The KSNODE_CREATE structure describes the set of information used to create the node handle.
old-location: stream\ksnode_create.htm
old-project: stream
ms.assetid: db08cc72-3797-46e3-8e4d-d8469dc126ab
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSNODE_CREATE, KSNODE_CREATE, *PKSNODE_CREATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSNODE_CREATE
req.alt-loc: ks.h
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
req.iface: 
---

# PKSNODE_CREATE structure



## -description
<p>The KSNODE_CREATE structure describes the set of information used to create the node handle.</p>


## -syntax

````
typedef struct {
  ULONG CreateFlags;
  ULONG Node;
} KSNODE_CREATE, *PKSNODE_CREATE;
````


## -struct-fields
<dl>

### -field <b>CreateFlags</b>

<dd>
<p>Set to zero.</p>
</dd>

### -field <b>Node</b>

<dd>
<p>Indicates what node a handle should be created for. This refers to the node identifiers returned when querying topology information. A node identifier of −1 may be used to refer to the collection of nodes as a whole, if the filter supports it.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\nf-ks-kscreatetopologynode.md">KsCreateTopologyNode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSNODE_CREATE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
