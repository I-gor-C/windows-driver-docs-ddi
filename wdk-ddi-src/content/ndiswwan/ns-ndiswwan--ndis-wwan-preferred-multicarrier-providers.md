---
UID: NS.ndiswwan._NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
title: NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
author: windows-driver-content
description: The NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS structure represents a list of preferred multi-carrier providers and the number of providers in the list.
old-location: netvista\ndis_wwan_preferred_multicarrier_providers.htm
old-project: netvista
ms.assetid: 4856D1DF-8A31-4290-91C6-A4FC289BDC35
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS, NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS, *PNDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
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

# NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS structure



## -description
<p>The NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS structure represents a list of preferred multi-carrier providers and the number of providers in the list.</p>


## -syntax

````
typedef struct _NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_LIST_HEADER   PreferredListHeader;
} NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS, *PNDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS
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
<p>NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>Miniport drivers must set this member to WWAN_STATUS_SUCCESS for unsolicited events. WWAN_STATUS_SUCCESS is also specified for successful execution of OID_WWAN_PREFERRED_MULTICARRIER_PROVIDERS <i>set</i> requests.  The following table shows other possible error status codes (other members need not be updated by miniport driver):</p>
<table>
<tr>
<td>
<p><b>Value</b></p>
</td>
<td>
<p><b>Meaning</b></p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_READ_FAILURE</p>
</td>
<td>
<p>Reading information from the device failed</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>A <i>set</i> request is not supported</p>
</td>
</tr>
</table>
<p> </p>
<table></table>
<p> </p>
</dd>

### -field <b>PreferredListHeader</b>

<dd>
<p> A formatted WWAN_LIST_HEADER object that represents a list of preferred multi-carrier providers, including the number of providers in the list.</p>
<p>These point to the list of the WWAN_PROVIDER2 by using the WWAN_LIST_HEADER structure. <b>WwanDataClass</b> flags describe the preference of the specific data access technology and can be set to any combination within its own cellular class.
Response to  <a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a><i>set </i> requests must contain zero elements in the <b>PreferredListHeader</b>.</p>
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
<p>Supported starting with  Windows 8.</p>
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
<a href="..\wwan\ns-wwan--wwan-list-header.md">WWAN_LIST_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569830">OID_WWAN_PREFERRED_PROVIDERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_PREFERRED_MULTICARRIER_PROVIDERS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
