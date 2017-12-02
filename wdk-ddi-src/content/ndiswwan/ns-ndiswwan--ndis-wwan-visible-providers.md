---
UID: NS.ndiswwan._NDIS_WWAN_VISIBLE_PROVIDERS
title: NDIS_WWAN_VISIBLE_PROVIDERS
author: windows-driver-content
description: The NDIS_WWAN_VISIBLE_PROVIDERS structure represents a list of visible providers and the number of providers in the list.
old-location: netvista\ndis_wwan_visible_providers.htm
old-project: netvista
ms.assetid: ed30def8-41c5-4fa9-8098-80f47ddaaa99
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_VISIBLE_PROVIDERS
req.alt-loc: ndiswwan.h
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

# NDIS_WWAN_VISIBLE_PROVIDERS structure



## -description
<p>The NDIS_WWAN_VISIBLE_PROVIDERS structure represents a list of visible providers and the number of
  providers in the list.</p>


## -syntax

````
typedef struct _NDIS_WWAN_VISIBLE_PROVIDERS {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_LIST_HEADER   VisibleListHeader;
} NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_VISIBLE_PROVIDERS
     structure. The MB Service sets the header with the values that are shown in the following table when it
     sends the data structure to the miniport driver for 
     <i>set</i> operations. Miniport drivers must set the header with the same values when they send the data
     structure to the MB service.
     </p>
<table>
<tr>
<th>Header submember</th>
<th>Value</th>
</tr>
<tr>
<td>
<p>Type</p>
</td>
<td>
<p>NDIS_OBJECT_TYPE_DEFAULT</p>
</td>
</tr>
<tr>
<td>
<p>Revision</p>
</td>
<td>
<p>NDIS_WWAN_VISIBLE_PROVIDERS_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_VISIBLE_PROVIDERS)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field uStatus

<dd>
<p>A miniport driver must set this to WWAN_STATUS_SUCCESS for successful execution of query to the
     OID_WWAN_VISIBLE_PROVIDER.
     </p>
<p>The following table shows the other possible error status codes (other members need not be updated by
     miniport driver).</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PIN_REQUIRED</p>
</td>
<td>
<p>Device requires PIN value input.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_FAILURE</p>
</td>
<td>
<p>Unable to get visible list.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SIM_NOT_INSERTED</p>
</td>
<td>
<p>A SIM card is not inserted in the device.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PROVIDERS_NOT_FOUND</p>
</td>
<td>
<p>No providers are found. Device seems to be in no network coverage.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BUSY</p>
</td>
<td>
<p>The device is busy and unable to scan. This can happen if the device does a destructive scan (for
        example, a scan may result in current registered state or PDP activation to be changed to deregister
        or PDP deactivation).</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_RADIO_POWER_OFF</p>
</td>
<td>
<p>Unable to scan. Radio is switched off.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SERVICE_NOT_ACTIVATED</p>
</td>
<td>
<p>Service activation has failed. Subscription has expired. Device does not allow scanning.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field VisibleListHeader

<dd>
<p>A formatted 
     <a href="..\wwan\ns-wwan--wwan-list-header.md">WWAN_LIST_HEADER</a> object that represents a
     list of visible providers and the number of providers in the list.
     </p>
<p>This member points to the list of <a href="..\wwan\ns-wwan--wwan-provider2.md">WWAN_PROVIDER2</a> structures that use the WWAN_LIST_HEADER structure. <b>WwanDataClass</b> flags describe the presence of the specific data access technology and can be set to any combination according to the availability of the data-classes</p>
</dd>
</dl>

## -remarks


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
<dt>Ndiswwan.h (include Ndiswwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-list-header.md">WWAN_LIST_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_VISIBLE_PROVIDERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
