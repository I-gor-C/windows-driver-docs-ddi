---
UID: NS.WINDOT11.DOT11_VWIFI_ATTRIBUTES
title: DOT11_VWIFI_ATTRIBUTES
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_vwifi_attributes.htm
old-project: netvista
ms.assetid: 46eee6ea-8259-4036-b1c4-f0eef6587879
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: DOT11_VWIFI_ATTRIBUTES, *PDOT11_VWIFI_ATTRIBUTES, DOT11_VWIFI_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating   system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_VWIFI_ATTRIBUTES
req.alt-loc: windot11.h
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
req.product: Windows 10 or later.
---

# DOT11_VWIFI_ATTRIBUTES structure



## -description

## -syntax

````
typedef struct DOT11_VWIFI_ATTRIBUTES {
  NDIS_OBJECT_HEADER      Header;
  ULONG                   uTotalNumOfEntries;
  DOT11_VWIFI_COMBINATION Combinations[1];
} DOT11_VWIFI_ATTRIBUTES, *PDOT11_VWIFI_ATTRIBUTES;
````


## -struct-fields

### -field Header

The type, revision, and size of the DOT11_VWIFI_ATTRIBUTES structure. This member is formatted as
     an 
     <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a> structure.
     

The miniport driver must set the members of 
     <b>Header</b> to the following values:




### -field Type

This member must be set to NDIS_OBJECT_TYPE_DEFAULT.


### -field Revision

This member must be set to DOT11_VWIFI_ATTRIBUTES_REVISION_1.


### -field Size

This member must be set to 
       sizeof(DOT11_VWIFI_ATTRIBUTES).

</dd>
</dl>
For more information about these members, see 
     <a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>.


### -field uTotalNumOfEntries

The maximum number of entries that the 
     <b>Combinations</b> array can contain.


### -field Combinations

The list of supported combinations of 802.11 MAC entities that an 802.11 miniport driver can
     simultaneously support when it is virtualized. Each entry in this list is specified through an array of 
     <a href="netvista.dot11_vwifi_combination">DOT11_VWIFI_COMBINATION</a>,  <a href="netvista.dot11_vwifi_combination_v2">
     DOT11_VWIFI_COMBINATION_V2</a>, or <a href="netvista.dot11_vwifi_combination_v3">DOT11_VWIFI_COMBINATION_V3</a> structures.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 7 and later versions of the Windows operating
   system.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.dot11_vwifi_combination">DOT11_VWIFI_COMBINATION</a>
</dt>
<dt>
<a href="netvista.dot11_vwifi_combination_v2">DOT11_VWIFI_COMBINATION_V2</a>
</dt>
<dt>
<a href="netvista.ndis_object_header">NDIS_OBJECT_HEADER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_VWIFI_ATTRIBUTES structure%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

