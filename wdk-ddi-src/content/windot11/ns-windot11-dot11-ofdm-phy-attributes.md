---
UID: NS.windot11.DOT11_OFDM_PHY_ATTRIBUTES
title: DOT11_OFDM_PHY_ATTRIBUTES
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_ofdm_phy_attributes.htm
old-project: netvista
ms.assetid: edc9bd9b-938f-43df-80fd-5a4d49f6f768
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_OFDM_PHY_ATTRIBUTES, DOT11_OFDM_PHY_ATTRIBUTES, *PDOT11_OFDM_PHY_ATTRIBUTES
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
req.alt-api: DOT11_OFDM_PHY_ATTRIBUTES
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

# DOT11_OFDM_PHY_ATTRIBUTES structure



## -description

## -syntax

````
typedef struct DOT11_OFDM_PHY_ATTRIBUTES {
  ULONG uFrequencyBandsSupported;
} DOT11_OFDM_PHY_ATTRIBUTES, *PDOT11_OFDM_PHY_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field uFrequencyBandsSupported

<dd>
<p>The frequency bands in which the PHY is capable of operating. Frequency bands are defined for:
     </p>
<ul>
<li>
<p>Unlicensed national information infrastructure (U-NII) bands.</p>
</li>
<li>
<p>Conference of European Post and Telecommunication (CEPT) bands.</p>
</li>
<li>
<p>Japan 5 GHz bands.</p>
</li>
</ul>
<p>The frequency bands supported by the PHY are defined through the following bitmask:</p>
<table>
<tr>
<th>Bit</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>Can operate in the lower (5.15-5.25 GHz) U-NII band.</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Can operate in the middle (5.25-5.35 GHz) U-NII band.</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Can operate in the upper (5.725-5.825 GHz) U-NII band.</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>Can operate in CEPT B (5.47-5.7253 GHz) band.</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>Can operate in the lower Japan (5.15-5 5.25 GHz) band.</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p>Can operate in the Japan 5.0 (5.03-8 5.091 GHz) band.</p>
</td>
</tr>
<tr>
<td>
<p>6</p>
</td>
<td>
<p>Can operate in the Japan 4.9 (4.9-5.0GHz) band.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>The miniport driver defines the attributes of a PHY on the 802.11 station through the 
    <a href="..\windot11\ns-windot11-dot11-phy-attributes.md">DOT11_PHY_ATTRIBUTES</a> structure, and
    formats the 
    <b>OFDMAttributes</b> member as a DOT11_OFDM_PHY_ATTRIBUTES structure. The miniport driver must only do this
    if the PHY defined by the DOT11_PHY_ATTRIBUTES structure is an OFDM PHY type.</p>

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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_OFDM_PHY_ATTRIBUTES structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
