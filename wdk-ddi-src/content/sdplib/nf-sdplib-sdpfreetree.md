---
UID: NF.sdplib.SdpFreeTree
title: SdpFreeTree function
author: windows-driver-content
description: The Bluetooth SdpFreeTree function is used to free the memory allocated for the tree-based representation of an SDP record.
old-location: bltooth\sdpfreetree.htm
old-project: bltooth
ms.assetid: 7d3f743e-2422-474d-aaad-4386e0dc100a
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SdpFreeTree
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
req.alt-api: SdpFreeTree
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

# SdpFreeTree function



## -description
The Bluetooth 
  <b>SdpFreeTree</b> function is used to free the memory allocated for the tree-based representation of an SDP
  record.



## -syntax

````
NTSTATUS SdpFreeTree(
  _In_ PSDP_TREE_ROOT_NODE Tree
);
````


## -parameters

### -param Tree [in]

The root node of the SDP tree-based representation to be freed.


## -returns
Possible return values include:


## -remarks
Callers should perform an 
    <b>SdpFreeTree</b> call when the tree-based representation of an SDP record is no longer needed. The 
    <a href="bltooth.sdpcreatenodetree">SdpCreateNodeTree</a> and 
    <a href="..\bthsdpddi\nc-bthsdpddi-pconvertstreamtotree.md">SdpConvertStreamToTree</a> functions
    allocate the memory for the tree representations of SDP records that they create. The 
    <b>SdpFreeTree</b> function releases the memory allocated to the 
    <a href="bltooth.sdp_tree_root_node">SDP_TREE_ROOT_NODE</a> structure that these
    functions create and all 
    <a href="bltooth.sdp_node">SDP_NODE</a> structures associated with the tree
    representation.

Bluetooth profile drivers can obtain a pointer to the 
    <b>SdpFreeTree</b> function through the 
    <a href="bltooth.bthddi_sdp_node_interface">
    BTHDDI_SDP_NODE_INTERFACE</a> structure.


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
<a href="bltooth.sdpcreatenodetree">SdpCreateNodeTree</a>
</dt>
<dt>
<a href="..\bthsdpddi\nc-bthsdpddi-pconvertstreamtotree.md">SdpConvertStreamToTree</a>
</dt>
<dt>
<a href="bltooth.sdp_tree_root_node">SDP_TREE_ROOT_NODE</a>
</dt>
<dt>
<a href="bltooth.sdp_node">SDP_NODE</a>
</dt>
<dt>
<a href="bltooth.bthddi_sdp_node_interface">BTHDDI_SDP_NODE_INTERFACE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20SdpFreeTree function%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

