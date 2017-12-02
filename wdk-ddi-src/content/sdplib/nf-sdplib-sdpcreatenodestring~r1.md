---
UID: NF.sdplib.SdpCreateNodeString~r1
title: SdpCreateNodeString
author: windows-driver-content
description: The Bluetooth SdpCreateNodeString function is used to allocate and initialize an SDP_NODE structure to a string type.
old-location: bltooth\sdpcreatenodestring.htm
old-project: bltooth
ms.assetid: 27611211-a782-4c62-8848-d9ca6e49b5f4
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SdpCreateNodeString
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
req.alt-api: SdpCreateNodeString
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
req.iface: 
req.product: Windows 10 or later.
---

# SdpCreateNodeString function



## -description
<p>The Bluetooth 
  <b>SdpCreateNodeString</b> function is used to allocate and initialize an 
  <a href="..\sdpnode\ns-sdpnode--sdp-node.md">SDP_NODE</a> structure to a string type.</p>


## -syntax

````
PSDP_NODE SdpCreateNodeString(
  _In_ PCHAR            string,
       __in_bound ULONG StringLength,
  _In_ ULONG            tag
);
````


## -parameters
<dl>

### -param string [in]

<dd>
<p>A pointer to the string value to initialize the SDP_NODE structure.</p>
</dd>

### -param StringLength 

<dd>
<p>An unsigned long integer value that holds the length of the string.</p>
</dd>

### -param tag [in]

<dd>
<p>A profile driver defined tag to associate with the node.</p>
</dd>
</dl>

## -returns
<p>If successful, this function returns a pointer to the newly allocated SDP_NODE structure. If not
     successful, this function returns <b>NULL</b>.</p>

## -remarks
<p>After the 
    <b>SdpCreateNodeString</b> function allocates an 
    <a href="..\sdpnode\ns-sdpnode--sdp-node.md">SDP_NODE</a> structure, it initializes the structure in
    the following ways.</p>

<p>It ensures that the SDP_NODE structure's data type and data size fields are set appropriately.</p>

<p>It ensures that the pointer members of the associated 
      <a href="..\sdpnode\ns-sdpnode--sdp-node-header.md">SDP_NODE_HEADER</a> structure are initialized
      to point to the node itself. This creates a valid list with only one element.</p>

<p>It ensures that the 
      <i>value</i> parameter passed to the function is copied to the appropriate element of the 
      <a href="..\sdpnode\ns-sdpnode--sdp-node-data.md">SDP_NODE_DATA</a> union that is associated with
      the SDP_NODE structure.</p>

<p>The data associated with the 
    <b>SdpCreateNodeString</b> function is copied into the node, and the original data can be freed at any
    time.</p>

<p>Bluetooth profile drivers can obtain a pointer to this function through the 
    <a href="..\bthsdpddi\ns-bthsdpddi--bthddi-sdp-node-interface.md">BTHDDI_SDP_NODE_INTERFACE</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sdplib.h (include BthSdpddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\sdpnode\ns-sdpnode--sdp-node.md">SDP_NODE</a>
</dt>
<dt>
<a href="..\sdpnode\ns-sdpnode--sdp-node-header.md">SDP_NODE_HEADER</a>
</dt>
<dt>
<a href="..\sdpnode\ns-sdpnode--sdp-node-data.md">SDP_NODE_DATA</a>
</dt>
<dt>
<a href="..\bthsdpddi\ns-bthsdpddi--bthddi-sdp-node-interface.md">BTHDDI_SDP_NODE_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20SdpCreateNodeString function%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
