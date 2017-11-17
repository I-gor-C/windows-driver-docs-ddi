---
UID: NS.bdatypes._BDANODE_DESCRIPTOR
title: BDANODE_DESCRIPTOR
author: windows-driver-content
description: The BDANODE_DESCRIPTOR structure describes a BDA node.
old-location: stream\bdanode_descriptor.htm
ms.assetid: 324eddca-f619-44e2-b32f-34cefd4c9cdc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: bdatypes.h
req.include-header: Bdatypes.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDANODE_DESCRIPTOR
req.alt-loc: bdatypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: BDANODE_DESCRIPTOR, BDANODE_DESCRIPTOR, *PBDANODE_DESCRIPTOR
req.iface: 
---

# BDANODE_DESCRIPTOR structure



## -description
<p>The BDANODE_DESCRIPTOR structure describes a BDA node. </p>


## -syntax

````
typedef struct _BDANODE_DESCRIPTOR {
  ULONG ulBdaNodeType;
  GUID  guidFunction;
  GUID  guidName;
} BDANODE_DESCRIPTOR, *PBDANODE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>ulBdaNodeType</b>

<dd>
<p>The node type as the BDA template topology identifies it. The BDA node-type identifier typically corresponds to the index of the element in the zero-based array of node types. This array of node types is an array of KSNODE_DESCRIPTOR structures. </p>
</dd>

### -field <b>guidFunction</b>

<dd>
<p>GUID that describes the node's function. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff556529">BDA Node Category GUIDs</a> for a list of these GUIDs.</p>
</dd>

### -field <b>guidName</b>

<dd>
<p>GUID that can be used to store a string containing the name of the node. Applications can search the registry for this GUID to obtain the node's name and then can display the name. </p>
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
<dt>Bdatypes.h (include Bdatypes.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556529">BDA Node Category GUIDs</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563473">KSNODE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BDANODE_DESCRIPTOR structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
