---
UID: NS.windot11._DOT11_VWIFI_COMBINATION_V2
title: DOT11_VWIFI_COMBINATION_V2
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_vwifi_combination_v2.htm
old-project: netvista
ms.assetid: b30b868d-3012-4bdc-80f4-ffae2ebaa4d6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_VWIFI_COMBINATION_V2,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_VWIFI_COMBINATION_V2
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
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_VWIFI_COMBINATION_V2 structure



## -description

## -syntax

````
typedef struct _DOT11_VWIFI_COMBINATION_V2 {
  NDIS_OBJECT_HEADER Header;
  ULONG              uNumInfrastructure;
  ULONG              uNumAdhoc;
  ULONG              uNumSoftAP;
  ULONG              uNumVirtualStation;
} DOT11_VWIFI_COMBINATION_V2, *PDOT11_VWIFI_COMBINATION_V2;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_VWIFI_COMBINATION_V2 structure. This member is formatted
     as an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a><b>Type</b>

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a><b>Revision</b>

<dd>
<p>This member must be set to DOT11_VWIFI_COMBINATION_REVISION_2.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a><b>Size</b>

<dd>
<p>This member must be set to 
       sizeof(DOT11_VWIFI_COMBINATION_V2).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uNumInfrastructure</b>

<dd>
<p>The number of 802.11 infrastructure stations supported. For more information, see the following
     Remarks section.</p>
</dd>

### -field <b>uNumAdhoc</b>

<dd>
<p>The number of Adhoc Stations supported. For more information, see the following Remarks
     section.</p>
</dd>

### -field <b>uNumSoftAP</b>

<dd>
<p>The number of Soft AP Stations supported. For more information, see the following Remarks
     section.</p>
</dd>

### -field <b>uNumVirtualStation</b>

<dd>
<p>The number of Virtual Stations supported. For more information, see the following Remarks
     section.</p>
</dd>
</dl>

## -remarks
<p>Starting with Windows 7, the 802.11 miniport driver must only report one or more of the following
    combinations of member values.</p>

<p><b>No 802.11 Virtual Station
     </b></p>

<p><b>uNumInfrastructure</b> = 1</p>

<p><b>uNumAdhoc</b> = 0</p>

<p><b>uNumSoftAP</b> = 1</p>

<p><b>uNumVirtualStation</b> = 0</p>

<p><b>One 802.11 Virtual Station
     </b></p>

<p><b>uNumInfrastructure</b> = 1</p>

<p><b>uNumAdhoc</b> = 0</p>

<p><b>uNumSoftAP</b> = 1</p>

<p><b>uNumVirtualStation</b> = 1</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_VWIFI_COMBINATION_V2 structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
