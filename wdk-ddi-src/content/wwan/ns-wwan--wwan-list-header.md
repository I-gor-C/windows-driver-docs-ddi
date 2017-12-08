---
UID: NS.wwan._WWAN_LIST_HEADER
title: WWAN_LIST_HEADER
author: windows-driver-content
description: The WWAN_LIST_HEADER structure represents the header of a list of MB objects, including the number of objects in the list that follow the header in memory.
old-location: netvista\wwan_list_header.htm
old-project: netvista
ms.assetid: ef5c94e9-641c-41ea-baf1-343b876c92a4
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WWAN_LIST_HEADER, WWAN_LIST_HEADER, *PWWAN_LIST_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_LIST_HEADER
req.alt-loc: wwan.h
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
req.product: Windows 10 or later.
---

# WWAN_LIST_HEADER structure



## -description
<p>The WWAN_LIST_HEADER structure represents the header of a list of MB objects, including the number of
  objects in the list that follow the header in memory.</p>


## -syntax

````
typedef struct _WWAN_LIST_HEADER {
  WWAN_STRUCT_TYPE ElementType;
  ULONG            ElementCount;
} WWAN_LIST_HEADER, *PWWAN_LIST_HEADER;
````


## -struct-fields
<dl>

### -field ElementType

<dd>
<p>A value from the 
     <a href="..\wwan\ne-wwan--wwan-struct-type.md">WWAN_STRUCT_TYPE</a> enumeration that represents
     the type of objects in the list.</p>
</dd>

### -field ElementCount

<dd>
<p>The number of elements in the list. The MB Service uses this information to allocate and
     reallocate memory for the list.</p>
</dd>
</dl>

## -remarks
<p>You can assume that the list of elements is stored in memory immediately following the data structure
    that contains the list.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-preferred-providers.md">NDIS_WWAN_PREFERRED_PROVIDERS</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-provisioned-contexts.md">
   NDIS_WWAN_PROVISIONED_CONTEXTS</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-set-preferred-providers.md">
   NDIS_WWAN_SET_PREFERRED_PROVIDERS</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-sms-receive.md">NDIS_WWAN_SMS_RECEIVE</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-visible-providers.md">NDIS_WWAN_VISIBLE_PROVIDERS</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan--wwan-struct-type.md">WWAN_STRUCT_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_LIST_HEADER structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
