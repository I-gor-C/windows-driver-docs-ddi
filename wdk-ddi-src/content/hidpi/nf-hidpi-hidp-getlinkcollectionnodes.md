---
UID: NF.hidpi.HidP_GetLinkCollectionNodes
title: HidP_GetLinkCollectionNodes
author: windows-driver-content
description: The HidP_GetLinkCollectionNodes routine returns a top-level collection's link collection array.
old-location: hid\hidp_getlinkcollectionnodes.htm
old-project: hid
ms.assetid: d829b203-8b7f-4504-a9ac-da1f91b3bbd6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_GetLinkCollectionNodes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hidpi.h
req.include-header: Hidpi.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HidP_GetLinkCollectionNodes
req.alt-loc: Hidparse.lib,Hidparse.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hidparse.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# HidP_GetLinkCollectionNodes function



## -description
<p>The <b>HidP_GetLinkCollectionNodes</b> routine returns a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> <a href="hid.link_collections#ddk_link_collection_array_kg#ddk_link_collection_array_kg">link collection array</a>.</p>


## -syntax

````
NTSTATUS __stdcall HidP_GetLinkCollectionNodes(
  _Out_   PHIDP_LINK_COLLECTION_NODE LinkCollectionNodes,
  _Inout_ PULONG                     LinkCollectionNodesLength,
  _In_    PHIDP_PREPARSED_DATA       PreparsedData
);
````


## -parameters
<dl>

### -param LinkCollectionNodes [out]

<dd>
<p>Pointer to a caller-allocated array of HIDP_LINK_COLLECTION_NODE structures in which <b>HidP_GetLinkCollectionNodes</b> returns a top-level collection's link collection array.</p>
</dd>

### -param LinkCollectionNodesLength [in, out]

<dd>
<p>Specifies, on input, the length, in array elements, of the <i>LinkCollectionNodes</i> buffer. On output, the routine sets <i>LinkCollectionNodesLength</i> to the number of entries in the array that it set.</p>
</dd>

### -param PreparsedData [in]

<dd>
<p>Pointer to the preparsed data of the top-level collection for which this routine returns a link collection array.</p>
</dd>
</dl>

## -returns
<p><b>HidP_GetLinkCollectionNodes</b> returns one of the following status codes:</p><dl>
<dt><b>HIDP_STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully returned the specified collection's link collection array.</p><dl>
<dt><b>HIDP_STATUS_BUFFER_TOO_SMALL </b></dt>
</dl><p>The <i>LinkCollectionNodes</i> buffer is too small to hold the entire link collection array.</p>

<p> </p>

## -remarks
<p>The required length of the <i>LinkCollectionNodes</i> buffer is specified by the <b>NumberLinkCollectionNodes</b> member of a collection's <a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a> structure.</p>

<p>If <b>HidP_GetLinkCollectionNodes</b> returns the status value HIDP_STATUS_BUFFER_TOO_SMALL, it also sets <i>LinkCollectionNodesLength</i> to the length, in array elements, required to hold the link collection nodes information.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/2d3efb38-4eba-43db-8cff-9fac30209952">HID Collections</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidpi.h (include Hidpi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hidparse.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543586">_HIDP_PREPARSED_DATA</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getcaps.md">HidP_GetCaps</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-link-collection-node.md">HIDP_LINK_COLLECTION_NODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_GetLinkCollectionNodes routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
