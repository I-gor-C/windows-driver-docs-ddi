---
UID: NS.ndiswwan._NDIS_WWAN_PREFERRED_PROVIDERS
title: NDIS_WWAN_PREFERRED_PROVIDERS
author: windows-driver-content
description: The NDIS_WWAN_PREFERRED_PROVIDERS structure represents a list of preferred providers including the number of providers in the list.
old-location: netvista\ndis_wwan_preferred_providers.htm
old-project: netvista
ms.assetid: cbbbf7d2-cf24-47af-89e9-c27d577165e4
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_WWAN_PREFERRED_PROVIDERS, NDIS_WWAN_PREFERRED_PROVIDERS, *PNDIS_WWAN_PREFERRED_PROVIDERS
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
req.alt-api: NDIS_WWAN_PREFERRED_PROVIDERS
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

# NDIS_WWAN_PREFERRED_PROVIDERS structure



## -description
<p>The NDIS_WWAN_PREFERRED_PROVIDERS structure represents a list of preferred providers including the
  number of providers in the list.</p>


## -syntax

````
typedef struct _NDIS_WWAN_PREFERRED_PROVIDERS {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_LIST_HEADER   PreferredListHeader;
} NDIS_WWAN_PREFERRED_PROVIDERS, *PNDIS_WWAN_PREFERRED_PROVIDERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_PREFERRED_PROVIDERS
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
<p>NDIS_WWAN_PREFERRED_PROVIDERS_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_PREFERRED_PROVIDERS)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field uStatus

<dd>
<p>Miniport driver must set this to WWAN_STATUS_SUCCESS for unsolicited events
     (NDIS_STATUS_INDICATION::RequestId = 0). WWAN_STATUS_SUCCESS is also set for successful execution of the
     NDIS_WWAN_SET_PREFERRED_PROVIDERS.
     </p>
<p>The following table shows other possible error status codes (other members need not be updated by
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
<p>WWAN_STATUS_READ_FAILURE</p>
</td>
<td>
<p>Reading information from device or SIM card, or both, failed. For example, the SIM card does not
        have preferred providers information provisioned.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BAD_SIM</p>
</td>
<td>
<p>Bad SIM detected.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SIM_NOT_INSERTED</p>
</td>
<td>
<p>SIM not inserted in the device.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>A 
        <i>set</i> request is not supported.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field PreferredListHeader

<dd>
<p>A formatted 
     <a href="..\wwan\ns-wwan--wwan-list-header.md">WWAN_LIST_HEADER</a> object that represents a
     list of preferred providers, including the number of providers in the list.
     </p>
<p>These point to the list of <a href="..\wwan\ns-wwan--wwan-provider2.md">WWAN_PROVIDER2</a> by using the WWAN_LIST_HEADER structure. 
     <b>WwanDataClass</b> flags describe the preference of the specific data access technology and can be set
     to any combination within its own cellular class.</p>
<p>Response to 
     <i>set</i> OID_WWAN_PREFERRED_PROVIDERS requests must contain zero elements in the 
     <b>PreferenceListHeader</b>.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_PREFERRED_PROVIDERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
