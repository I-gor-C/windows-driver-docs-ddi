---
UID: NS.windot11._DOT11_SUPPORTED_ANTENNA_LIST
title: DOT11_SUPPORTED_ANTENNA_LIST
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_supported_antenna_list.htm
ms.assetid: 45c6b9a3-b834-4e57-b7f8-fab7be749269
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_SUPPORTED_ANTENNA_LIST
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
ms.keywords: DOT11_SUPPORTED_ANTENNA_LIST, DOT11_SUPPORTED_ANTENNA_LIST, *PDOT11_SUPPORTED_ANTENNA_LIST
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_SUPPORTED_ANTENNA_LIST structure



## -description

## -syntax

````
typedef struct _DOT11_SUPPORTED_ANTENNA_LIST {
  ULONG                   uNumOfEntries;
  ULONG                   uTotalNumOfEntries;
  DOT11_SUPPORTED_ANTENNA dot11SupportedAntenna[1];
} DOT11_SUPPORTED_ANTENNA_LIST, *PDOT11_SUPPORTED_ANTENNA_LIST;
````


## -struct-fields
<dl>

### -field <b>uNumOfEntries</b>

<dd>
<p>The number of entries in the 
     <b>dot11SupportedAntenna</b> array. A zero value for the 
     <b>uNumOfEntries</b> member indicates an empty list.</p>
</dd>

### -field <b>uTotalNumOfEntries</b>

<dd>
<p>The maximum number of entries that the 
     <b>dot11SupportedAntenna</b> array can contain.</p>
</dd>

### -field <b>dot11SupportedAntenna</b>

<dd>
<p>The list of supported antennas. Each element in this list is formatted as a 
     <a href="https://msdn.microsoft.com/55a9c9e0-24e2-436f-9132-77ae1bab7c2c">
     DOT11_SUPPORTED_ANTENNA</a> structure.</p>
</dd>
</dl>

## -remarks
<p>A miniport driver returns the DOT11_SUPPORTED_ANTENNA_LIST structure when queried by either 
    <a href="netvista.oid_dot11_supported_rx_antenna">
    OID_DOT11_SUPPORTED_RX_ANTENNA</a> or 
    <a href="netvista.oid_dot11_supported_tx_antenna">
    OID_DOT11_SUPPORTED_TX_ANTENNA</a>.</p>

<p>When these OIDs are queried, the miniport driver must verify that the 
    <b>InformationBuffer</b> member of the 
    <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function's
    <i>OidRequest</i> parameter is large enough to return the entire DOT11_SUPPORTED_ANTENNA_LIST structure,
    including all entries in the 
    <b>dot11SupportedAntenna</b> array. The value of the 
    <b>InformationBufferLength</b> member of the 
    <i>OidRequest</i> parameter determines what the miniport driver must do, as the following list shows:</p>

<p>If the value of the 
      <b>InformationBufferLength</b> member is less than the length, in bytes, of the entire
      DOT11_SUPPORTED_ANTENNA_LIST structure, the miniport driver must do the following:</p>

<p>Set the 
        <b>uNumOfEntries</b> member to zero.</p>

<p>Set the 
        <b>uTotalNumOfEntries</b> member to the number of entries in the 
        <b>dot11SupportedAntenna</b> array.</p>

<p>For the 
        <i>OidRequest</i> parameter, set the 
        <b>BytesWritten</b> member to zero and the 
        <b>BytesNeeded</b> member to the length, in bytes, of the entire DOT11_PHY_ID_LIST structure.</p>

<p>Fail the query request by returning NDIS_STATUS_BUFFER_OVERFLOW from its 
        <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function.</p>

<p>If the value of the 
      <b>InformationBufferLength</b> member is greater than or equal to the length, in bytes, of the entire
      DOT11_SUPPORTED_ANTENNA_LIST structure, the miniport driver must do the following to complete a
      successful query request:</p>

<p>For the DOT11_SUPPORTED_ANTENNA_LIST structure, set the 
        <b>uNumOfEntries</b> and 
        <b>uTotalNumOfEntries</b> members to the total number of entries in the 
        <b>dot11SupportedAntenna</b> array.</p>

<p>For the 
        <i>OidRequest</i> parameter, set the 
        <b>BytesNeeded</b> member to zero and the 
        <b>BytesWritten</b> member to the length, in bytes, of the entire DOT11_SUPPORTED_ANTENNA_LIST
        structure. The miniport driver must also copy the entire DOT11_SUPPORTED_ANTENNA_LIST structure to
        the 
        <b>InformationBuffer</b> member.</p>

<p>Return NDIS_STATUS_SUCCESS from its 
        <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548785">DOT11_SUPPORTED_ANTENNA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569428">OID_DOT11_SUPPORTED_RX_ANTENNA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569429">OID_DOT11_SUPPORTED_TX_ANTENNA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_SUPPORTED_ANTENNA_LIST structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
