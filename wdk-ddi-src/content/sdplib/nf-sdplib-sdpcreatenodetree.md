---
UID: NF.sdplib.SdpCreateNodeTree
title: SdpCreateNodeTree function
author: windows-driver-content
description: The Bluetooth SdpCreateNodeTree function is used to allocate an empty root SDP_TREE_ROOT_NODE structure.
old-location: bltooth\sdpcreatenodetree.htm
old-project: bltooth
ms.assetid: c019f382-1ad3-4b08-a254-ae803e2b6bc6
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SdpCreateNodeTree
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sdplib.h
req.include-header: BthSdpddi.h
req.target-type: Desktop
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SdpCreateNodeTree
req.alt-loc: sdplib.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# SdpCreateNodeTree function



## -description
The Bluetooth 
  <b>SdpCreateNodeTree</b> function is used to allocate an empty root 
  <a href="bltooth.sdp_tree_root_node">SDP_TREE_ROOT_NODE</a> structure.


## -syntax

````
PSDP_TREE_ROOT_NODE SdpCreateNodeTree(
  _In_ ULONG tag
);
````


## -parameters

### -param tag [in]

A profile driver defined tag to associate with the node.

## -returns
If successful, this function returns a pointer to the newly allocated SDP_TREE_ROOT_NODE
     structure. If not successful, this function returns <b>NULL</b>.

## -remarks
Calling the 
    <b>SdpCreateNodeTree</b> function is the first step in building an SDP tree. After a Bluetooth profile
    driver allocates a root node by using this function, the node can be populated by using calls to other
    functions pointed to by the 
    <a href="bltooth.bthddi_sdp_node_interface">
    BTHDDI_SDP_NODE_INTERFACE</a> structure.

When an SDP tree is no longer needed, the Bluetooth profile driver should destroy it by calling the 
    <a href="bltooth.sdpfreetree">SdpFreeTree</a> function. 
    <b>SdpFreeTree</b> frees the root node and all child nodes that have been attached to it. Individual 
    <a href="bltooth.sdp_node">SDP_NODE</a> structures can be freed by calling the 
    <a href="kernel.exfreepool">ExFreePool</a> driver support routine as long as they
    are no longer part of a tree or other list.

Bluetooth profile drivers can obtain a pointer to this function through the BTHDDI_SDP_NODE_INTERFACE
    structure.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Versions: Supported in Windows Vista, and later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Sdplib.h (include BthSdpddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="bltooth.sdp_tree_root_node">SDP_TREE_ROOT_NODE</a>
</dt>
<dt>
<a href="bltooth.bthddi_sdp_node_interface">BTHDDI_SDP_NODE_INTERFACE</a>
</dt>
<dt>
<a href="bltooth.sdpfreetree">SdpFreeTree</a>
</dt>
<dt>
<a href="bltooth.sdp_node">SDP_NODE</a>
</dt>
<dt>
<a href="kernel.exfreepool">ExFreePool</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20SdpCreateNodeTree function%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
