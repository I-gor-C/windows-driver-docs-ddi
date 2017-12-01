---
UID: NS.ndiswwan._NDIS_WWAN_PCO_STATUS
title: NDIS_WWAN_PCO_STATUS
author: windows-driver-content
description: The NDIS_WWAN_PCO_STATUS structure represents the Protocol Configuration Option (PCO) status of the modem.
old-location: netvista\ndis_wwan_pco_status.htm
old-project: netvista
ms.assetid: C71187C5-74B6-450A-8461-BB9FDF60DB8D
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_WWAN_PCO_STATUS, NDIS_WWAN_PCO_STATUS, *PNDIS_WWAN_PCO_STATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndiswwan.h
req.include-header: Ndiswwan.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_WWAN_PCO_STATUS
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

# NDIS_WWAN_PCO_STATUS structure



## -description
<p>The <b>NDIS_WWAN_PCO_STATUS</b> structure represents the Protocol Configuration Option (PCO) status of the modem.</p>


## -syntax

````
typedef struct _NDIS_WWAN_PCO_STATUS {
  NDIS_OBJECT_HEADER Header;
  WWAN_STATUS        uStatus;
  WWAN_PCO_VALUE     PcoValue;
} NDIS_WWAN_PCO_STATUS, *PNDIS_WWAN_PCO_STATUS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header with type, revision, and size information about the <b>NDIS_WWAN_PCO_STATUS</b> structure.
     The MB Service sets the header with the values that are shown in the following table when it sends the
     data structure to the miniport driver for 
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
<p>NDIS_WWAN_PCO_STATUS_REVISION_1</p>
</td>
</tr>
<tr>
<td>
<p>Size</p>
</td>
<td>
<p>sizeof(NDIS_WWAN_PCO_STATUS)</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>uStatus</b>

<dd>
<p>The status of system capability. The following table shows the possible values for
     this member.
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WWAN_STATUS_SUCCESS</p>
</td>
<td>
<p>The PCO value operation succeeded.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_CONTEXT_NOT_ACTIVATED</p>
</td>
<td>
<p>TThe PCO value is not available because the PDP context is not activated.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NO_DEVICE_SUPPORT</p>
</td>
<td>
<p>The PCO operation is not supported by the modem.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_REGISTERED</p>
</td>
<td>
<p>The PCO value is not available because the modem is not registered.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_PACKET_SVC_DETACHED</p>
</td>
<td>
<p>The PCO value is not available because no packet service is attached.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_RADIO_POWER_OFF</p>
</td>
<td>
<p>The PCO value not available because the radio is in the OFF state.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_BUSY</p>
</td>
<td>
<p>PCO value is not available because the modem is busy.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_INITIALIZED</p>
</td>
<td>
<p>TThe PCO value is not available because the device is initializing. Retry after the ready-state has changed to <b>WwanReadyStateInitialized.</b></p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_NOT_ACTIVATED</p>
</td>
<td>
<p>The PCO value is not available because the service is not activated.</p>
</td>
</tr>
<tr>
<td>
<p>WWAN_STATUS_READ_FAILURE</p>
</td>
<td>
<p>The PCO value failed due to a read failure.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PcoValue</b>

<dd>
<p>A formatted <a href="..\wwan\ns-wwan--wwan-pco-value.md">WWAN_PCO_VALUE</a> structure, which contains the PCO information payload from the network as defined in the 3GPP TS24.008 spec.</p>
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
<p>Windows 10, version 1709</p>
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
<a href="..\wwan\ns-wwan--wwan-pco-value.md">WWAN_PCO_VALUE</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-wwan-pco">OID_WWAN_PCO</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-pco-status">NDIS_STATUS_WWAN_PCO_STATUS</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/windows-hardware/drivers/network/mb-protocol-configuration-operations--pco-">MB Protocol Configuration Operations (PCO)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_WWAN_PCO_STATUS structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
