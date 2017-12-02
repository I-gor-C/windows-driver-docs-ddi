---
UID: NS.windot11.DOT11_DATA_RATE_MAPPING_ENTRY
title: DOT11_DATA_RATE_MAPPING_ENTRY
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_data_rate_mapping_entry.htm
old-project: netvista
ms.assetid: d2772a9e-655a-4e3e-8b48-65d58b0a659d
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_DATA_RATE_MAPPING_ENTRY, DOT11_DATA_RATE_MAPPING_ENTRY, *PDOT11_DATA_RATE_MAPPING_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_DATA_RATE_MAPPING_ENTRY
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

# DOT11_DATA_RATE_MAPPING_ENTRY structure



## -description

## -syntax

````
typedef struct DOT11_DATA_RATE_MAPPING_ENTRY {
  UCHAR  ucDataRateIndex;
  UCHAR  ucDataRateFlag;
  USHORT usDataRateValue;
} DOT11_DATA_RATE_MAPPING_ENTRY, *PDOT11_DATA_RATE_MAPPING_ENTRY;
````


## -struct-fields
<dl>

### -field ucDataRateIndex

<dd>
<p>The index value for the data rate contained in the 
     <b>usDataRateValue</b> member. The value of the 
     <b>ucDataRateIndex</b> member must be unique for each entry in the 
     <b>DataRateMappingEntries</b> array.
     </p>
<p>This value is a bitmask as defined in the following table.</p>
<table>
<tr>
<th>Bits</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>0-6</p>
</td>
<td>
<p>The data rate index, containing a value from 2 through127.</p>
</td>
</tr>
<tr>
<td>
<p>7</p>
</td>
<td>
<p>This bit is not used and must be set to zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field ucDataRateFlag

<dd>
<p>The attributes of the data rate entry.
     </p>
<p>This value is a bitmask as defined in the following table.</p>
<table>
<tr>
<th>Bits</th>
<th>Name</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p><b>DOT11_DATA_RATE_NON_STANDARD</b></p>
</td>
<td>
<p>If set, the entry is not a standard data rate defined in IEEE 802.11 standards.</p>
</td>
</tr>
<tr>
<td>
<p>1-7</p>
</td>
<td></td>
<td>
<p>These bits are not used and must be set to zero.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field usDataRateValue

<dd>
<p>The data rate, defined in units of 500 kilobits per second (Kbps), with a value from 0x0002 to
     0xFFFF.</p>
</dd>
</dl>

## -remarks
<p>For the IEEE 802.11 standard data rates, the miniport driver must set the 
    <b>ucDataRateIndex</b> and 
    <b>usDataRateValue</b> members to the same value.</p>

<p>The following table shows the IEEE 802.11 standard data rates, in units of megabits per second (Mbps),
    and the related values for the 
    <b>ucDataRateIndex</b> and 
    <b>usDataRateValue</b> members.</p>

<p>1 Mbps</p>

<p>0x02</p>

<p>2 Mbps</p>

<p>0x04</p>

<p>3 Mbps</p>

<p>0x06</p>

<p>4.5 Mbps</p>

<p>0x09</p>

<p>5.5 Mbps</p>

<p>0x0B</p>

<p>6 Mbps</p>

<p>0x0C</p>

<p>9 Mbps</p>

<p>0x12</p>

<p>11 Mbps</p>

<p>0x16</p>

<p>12 Mbps</p>

<p>0x18</p>

<p>18 Mbps</p>

<p>0x24</p>

<p>22 Mbps</p>

<p>0x2C</p>

<p>24 Mbps</p>

<p>0x30</p>

<p>27 Mbps</p>

<p>0x36</p>

<p>33 Mbps</p>

<p>0x42</p>

<p>36 Mbps</p>

<p>0x48</p>

<p>48 Mbps</p>

<p>0x60</p>

<p>54 Mbps</p>

<p>0x6C</p>

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
<a href="..\windot11\ns-windot11-dot11-phy-attributes.md">DOT11_PHY_ATTRIBUTES</a>
</dt>
<dt>
<a href="netvista.oid_dot11_data_rate_mapping_table">
   OID_DOT11_DATA_RATE_MAPPING_TABLE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_DATA_RATE_MAPPING_ENTRY structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
