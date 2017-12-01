---
UID: NF.wdfchildlist.WDF_CHILD_RETRIEVE_INFO_INIT
title: WDF_CHILD_RETRIEVE_INFO_INIT
author: windows-driver-content
description: The WDF_CHILD_RETRIEVE_INFO_INIT function initializes a WDF_CHILD_RETRIEVE_INFO structure.
old-location: wdf\wdf_child_retrieve_info_init.htm
old-project: wdf
ms.assetid: e41a656c-c507-45ca-a232-6926ace3c9d9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_CHILD_RETRIEVE_INFO_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_RETRIEVE_INFO_INIT
req.alt-loc: Wdfchildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WDF_CHILD_RETRIEVE_INFO_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_CHILD_RETRIEVE_INFO_INIT</b> function initializes a <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-retrieve-info.md">WDF_CHILD_RETRIEVE_INFO</a> structure.</p>


## -syntax

````
VOID WDF_CHILD_RETRIEVE_INFO_INIT(
  _Out_ PWDF_CHILD_RETRIEVE_INFO                     Info,
  _In_  PWDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER IdentificationDescription
);
````


## -parameters
<dl>

### -param <i>Info</i> [out]

<dd>
<p>A pointer to a driver-supplied <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-retrieve-info.md">WDF_CHILD_RETRIEVE_INFO</a> structure.</p>
</dd>

### -param <i>IdentificationDescription</i> [in]

<dd>
<p>A pointer to a driver-supplied <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-identification-description-header.md">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>For a code example that uses <b>WDF_CHILD_RETRIEVE_INFO_INIT</b>, see <a href="..\wdfchildlist\nf-wdfchildlist-wdfchildlistretrievenextdevice.md">WdfChildListRetrieveNextDevice</a>.</p>

## -remarks


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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-identification-description-header.md">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-retrieve-info.md">WDF_CHILD_RETRIEVE_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_RETRIEVE_INFO_INIT function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
