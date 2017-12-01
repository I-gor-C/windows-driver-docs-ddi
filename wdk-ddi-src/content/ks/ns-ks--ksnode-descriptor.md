---
UID: NS.ks._KSNODE_DESCRIPTOR
title: KSNODE_DESCRIPTOR
author: windows-driver-content
description: The KSNODE_DESCRIPTOR structure describes a topology node within a filter.
old-location: stream\ksnode_descriptor.htm
old-project: stream
ms.assetid: dfc5760f-fdd6-45f3-aeac-4406892e518a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSNODE_DESCRIPTOR,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSNODE_DESCRIPTOR
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

# KSNODE_DESCRIPTOR structure



## -description
<p>The KSNODE_DESCRIPTOR structure describes a topology node within a filter.</p>


## -syntax

````
typedef struct _KSNODE_DESCRIPTOR {
  const KSAUTOMATION_TABLE *AutomationTable;
  const GUID               *Type;
  const GUID               *Name;
} KSNODE_DESCRIPTOR, *PKSNODE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>AutomationTable</b>

<dd>
<p>A pointer to a <a href="stream.ksautomation_table">KSAUTOMATION_TABLE</a> structure for this topology node. The automation table contains the properties, methods, and events supported by this topology node.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>A pointer to a GUID defining the topology node.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>A pointer to a GUID that represents the name of this topology node. This is used to return information about a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565809">KSPROPERTY_TOPOLOGY_NAME</a> query.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
</td>
</tr>
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
<a href="..\ks\ns-ks--ksfilter-descriptor.md">KSFILTER_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSNODE_DESCRIPTOR structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
