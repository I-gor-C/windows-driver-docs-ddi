---
UID: NF.sdplib.SdpCreateNodeBoolean
title: SdpCreateNodeBoolean
author: windows-driver-content
description: The Bluetooth SdpCreateNodeBoolean function is used to allocate and initialize an SDP_NODE structure to a Boolean type.
old-location: bltooth\sdpcreatenodeboolean.htm
old-project: bltooth
ms.assetid: d299074f-18db-4eff-b177-4d2d3535e299
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SdpCreateNodeBoolean
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
req.alt-api: SdpCreateNodeBoolean
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

# SdpCreateNodeBoolean function



## -description
<p>The Bluetooth 
  <b>SdpCreateNodeBoolean</b> function is used to allocate and initialize an 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff536848">SDP_NODE</a> structure to a Boolean type.</p>


## -syntax

````
PSDP_NODE SdpCreateNodeBoolean(
  _In_ SDP_BOOLEAN bVal,
  _In_ ULONG       tag
);
````


## -parameters
<dl>

### -param <i>bVal</i> [in]

<dd>
<p>The Boolean value that is used to initialize the SDP_NODE structure.</p>
</dd>

### -param <i>tag</i> [in]

<dd>
<p>A profile driver defined tag to associate with the node.</p>
</dd>
</dl>

## -returns
<p>If successful, this function returns a pointer to the newly allocated SDP_NODE structure. If not
     successful, this function returns <b>NULL</b>.</p>

## -remarks
<p>The data associated with the 
    <b>SdpCreateNodeBoolean</b> function is copied into the node, and the original data can be freed at any
    time.</p>

<p>Bluetooth profile drivers can obtain a pointer to this function through the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff536635">BTHDDI_SDP_NODE_INTERFACE</a>.</p>

<p>The data associated with the 
    <b>SdpCreateNodeBoolean</b> function is copied into the node, and the original data can be freed at any
    time.</p>

<p>Bluetooth profile drivers can obtain a pointer to this function through the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff536635">BTHDDI_SDP_NODE_INTERFACE</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536848">SDP_NODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536635">BTHDDI_SDP_NODE_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20SdpCreateNodeBoolean function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
