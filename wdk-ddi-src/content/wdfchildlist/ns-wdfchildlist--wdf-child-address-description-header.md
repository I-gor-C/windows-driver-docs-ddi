---
UID: NS.wdfchildlist._WDF_CHILD_ADDRESS_DESCRIPTION_HEADER
title: WDF_CHILD_ADDRESS_DESCRIPTION_HEADER
author: windows-driver-content
description: The WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure is a header structure that must be the first member of every address description structure.
old-location: wdf\wdf_child_address_description_header.htm
old-project: wdf
ms.assetid: 2ea8041c-be80-42ff-9693-f6331508f6b2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_CHILD_ADDRESS_DESCRIPTION_HEADER,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_CHILD_ADDRESS_DESCRIPTION_HEADER
req.alt-loc: wdfchildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</b> structure is a header structure that must be the first member of every <a href="wdf.dynamic_enumeration">address description</a> structure.</p>


## -syntax

````
typedef struct _WDF_CHILD_ADDRESS_DESCRIPTION_HEADER {
  ULONG AddressDescriptionSize;
} WDF_CHILD_ADDRESS_DESCRIPTION_HEADER, *PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER;
````


## -struct-fields
<dl>

### -field <b>AddressDescriptionSize</b>

<dd>
<p>The size, in bytes, of a driver-defined structure that contains device address information.</p>
</dd>
</dl>

## -remarks
<p>To initialize a <b>WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</b> structure, your driver should call <a href="..\wdfchildlist\nf-wdfchildlist-wdf-child-address-description-header-init.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT</a>.</p>

<p>The value that the driver specifies for the <b>AddressDescriptionSize</b> member must match the value it specifies for the <b>AddressDescriptionSize</b> member in its <a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-list-config.md">WDF_CHILD_LIST_CONFIG</a> structure.</p>

<p>Address description structures are driver-defined. The driver must store the structure's size in the <b>AddressDescriptionSize</b> member. The size value must include the size of this header structure. For example, a driver might define an address descriptor as follows:</p>

<p>To set the <b>AddressDescriptionSize</b> member for this address descriptor, the driver can use the following code:</p>

<p>For more information about address descriptions, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nf-wdfchildlist-wdf-child-address-description-header-init.md">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT</a>
</dt>
<dt>
<a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-identification-description-header.md">WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="..\wdfchildlist\ns-wdfchildlist--wdf-child-list-config.md">WDF_CHILD_LIST_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
