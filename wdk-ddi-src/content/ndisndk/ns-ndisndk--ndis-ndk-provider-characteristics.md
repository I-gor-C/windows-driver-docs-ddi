---
UID: NS.ndisndk._NDIS_NDK_PROVIDER_CHARACTERISTICS
title: NDIS_NDK_PROVIDER_CHARACTERISTICS
author: windows-driver-content
description: The NDIS_NDK_PROVIDER_CHARACTERISTICS structure specifies NDK provider characteristics.
old-location: netvista\ndis_ndk_provider_characteristics.htm
old-project: netvista
ms.assetid: 40F07AC8-80F7-4DBC-BDC9-236530B011D4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_NDK_PROVIDER_CHARACTERISTICS, NDIS_NDK_PROVIDER_CHARACTERISTICS, *PNDIS_NDK_PROVIDER_CHARACTERISTICS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndisndk.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_NDK_PROVIDER_CHARACTERISTICS
req.alt-loc: ndisndk.h
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
req.iface: 
---

# NDIS_NDK_PROVIDER_CHARACTERISTICS structure



## -description
<p>The <b>NDIS_NDK_PROVIDER_CHARACTERISTICS</b> structure specifies NDK provider characteristics.</p>


## -syntax

````
typedef struct _NDIS_NDK_PROVIDER_CHARACTERISTICS {
  NDIS_OBJECT_HEADER        Header;
  ULONG                     Flags;
  OPEN_NDK_ADAPTER_HANDLER  OpenNDKAdapterHandler;
  CLOSE_NDK_ADAPTER_HANDLER CloseNDKAdapterHandler;
} NDIS_NDK_PROVIDER_CHARACTERISTICS, *PNDIS_NDK_PROVIDER_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>An 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure that describes this
     <b>NDIS_NDK_PROVIDER_CHARACTERISTICS</b> structure. NDIS sets the members of the <b>NDIS_OBJECT_HEADER</b> structure as follows:</p>
<ul>
<li>NDIS sets the <b>Type</b> member to <b>NDIS_OBJECT_TYPE_NDK_PROVIDER_CHARACTERISTICS</b>.</li>
<li>NDIS sets the <b>Revision</b> member to <b>NDIS_NDK_PROVIDER_CHARACTERISTICS_REVISION_1</b>.</li>
<li>NDIS sets the <b>Size</b> member to <b>NDIS_SIZEOF_NDK_PROVIDER_CHARACTERISTICS_REVISION_1</b>.</li>
</ul>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved, must be set to zero.</p>
</dd>

### -field <b>OpenNDKAdapterHandler</b>

<dd>
<p>The entry point for the <a href="..\ndisndk\nc-ndisndk-open-ndk-adapter-handler.md">OPEN_NDK_ADAPTER_HANDLER</a> function.</p>
</dd>

### -field <b>CloseNDKAdapterHandler</b>

<dd>
<p>The entry point for the <a href="..\ndisndk\nc-ndisndk-close-ndk-adapter-handler.md">CLOSE_NDK_ADAPTER_HANDLER</a> function.</p>
</dd>
</dl>

## -remarks
<p>To specify entry points for NDK services and other NDK provider characteristics, NDIS miniport drivers pass a pointer to an initialized <b>NDIS_NDK_PROVIDER_CHARACTERISTICS</b> structure to the <a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndisndk.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndisndk\nc-ndisndk-close-ndk-adapter-handler.md">CLOSE_NDK_ADAPTER_HANDLER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetoptionalhandlers.md">NdisSetOptionalHandlers</a>
</dt>
<dt>
<a href="..\ndisndk\nc-ndisndk-open-ndk-adapter-handler.md">OPEN_NDK_ADAPTER_HANDLER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_NDK_PROVIDER_CHARACTERISTICS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
