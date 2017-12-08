---
UID: NS.windot11._DOT11_SUPPORTED_OFDM_FREQUENCY_LIST
title: DOT11_SUPPORTED_OFDM_FREQUENCY_LIST
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_supported_ofdm_frequency_list.htm
old-project: netvista
ms.assetid: 0c967358-821b-4f78-acbc-dacee24dcd57
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_SUPPORTED_OFDM_FREQUENCY_LIST, DOT11_SUPPORTED_OFDM_FREQUENCY_LIST, *PDOT11_SUPPORTED_OFDM_FREQUENCY_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_SUPPORTED_OFDM_FREQUENCY_LIST
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

# DOT11_SUPPORTED_OFDM_FREQUENCY_LIST structure



## -description

## -syntax

````
typedef struct _DOT11_SUPPORTED_OFDM_FREQUENCY_LIST {
  ULONG                          uNumOfEntries;
  ULONG                          uTotalNumOfEntries;
  DOT11_SUPPORTED_OFDM_FREQUENCY dot11SupportedOFDMFrequency[1];
} DOT11_SUPPORTED_OFDM_FREQUENCY_LIST, *PDOT11_SUPPORTED_OFDM_FREQUENCY_LIST;
````


## -struct-fields
<dl>

### -field uNumOfEntries

<dd>
<p>The number of entries in the 
     <b>dot11SupportedOFDMFrequency</b> array.</p>
</dd>

### -field uTotalNumOfEntries

<dd>
<p>The maximum number of entries that the 
     <b>dot11SupportedOFDMFrequency</b> array can contain.</p>
</dd>

### -field dot11SupportedOFDMFrequency

<dd>
<p>An array that specifies the list of supported channel center frequencies that the NIC can operate
     with. Each element in this list is formatted as a 
     <a href="..\windot11\ns-windot11--dot11-supported-ofdm-frequency.md">
     DOT11_SUPPORTED_OFDM_FREQUENCY</a> structure.</p>
</dd>
</dl>

## -remarks
<p>A miniport driver returns the DOT11_SUPPORTED_OFDM_FREQUENCY_LIST structure when queried by 
    <a href="netvista.oid_dot11_supported_ofdm_frequency_list">
    OID_DOT11_SUPPORTED_OFDM_FREQUENCY_LIST</a>.</p>

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
<a href="..\windot11\ns-windot11--dot11-supported-ofdm-frequency.md">
   DOT11_SUPPORTED_OFDM_FREQUENCY</a>
</dt>
<dt>
<a href="netvista.oid_dot11_supported_ofdm_frequency_list">
   OID_DOT11_SUPPORTED_OFDM_FREQUENCY_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_SUPPORTED_OFDM_FREQUENCY_LIST structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
