---
UID: NS.windot11.DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO
title: DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_bss_entry_phy_specific_info.htm
old-project: netvista
ms.assetid: 85bcd355-633b-4d3f-a387-1e3b2ac3a013
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO, DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO, *PDOT11_BSS_ENTRY_PHY_SPECIFIC_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Wlclient.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO
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

# DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO structure



## -description

## -syntax

````
typedef union DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO {
  ULONG  uChCenterFrequency;
  struct {
    ULONG uHopPattern;
    ULONG uHopSet;
    ULONG uDwellTime;
  } FHSS;
} DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO, *PDOT11_BSS_ENTRY_PHY_SPECIFIC_INFO;
````


## -struct-fields
<dl>

### -field <b>uChCenterFrequency</b>

<dd>
<p>The channel center frequency of the band on which the 802.11 Probe-Response or Beacon frame was
     received. The value of 
     <b>uChCenterFrequency</b> is in units of megahertz (MHz). 
     </p>
<div class="alert"><b>Note</b>  This member is only valid for PHY types that are not frequency-hopping spread
     spectrum (FHSS).</div>
<div> </div>
</dd>

### -field <b>FHSS</b>

<dd>
<p>The FHSS parameters, as specified by the following members:</p>
<dl>

### -field <b>uHopPattern</b>

<dd>
<p>The current hopping pattern used by the layer management entity (LME) of the PHY to determine the
      hopping sequence. For more information about how the hopping sequence is determined, refer to Clause
      14.9.2.20 of the IEEE 802.11-2012 standard.
      </p>
<div class="alert"><b>Note</b>  This member is only valid for FHSS PHY types.</div>
<div> </div>
</dd>

### -field <b>uHopSet</b>

<dd>
<p>The current set of patterns used by the LME of the PHY to determine the hopping sequence. For
      more information about the hopping pattern sets, refer to Clause 14.9.2.19 of the IEEE 802.11-2012
      standard.
      </p>
<div class="alert"><b>Note</b>  This member is only valid for FHSS PHY types.</div>
<div> </div>
</dd>

### -field <b>uDwellTime</b>

<dd>
<p>The maximum amount of time that the PHY can use when transmitting on a single channel. The value
      of 
      <b>uDwellTime</b> is in units of 802.11 time units (TU). One TU is 1024 microseconds.
      </p>
<div class="alert"><b>Note</b>  This member is only valid for FHSS PHY types.</div>
<div> </div>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO union is a member of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff547665">DOT11_BSS_ENTRY</a> structure.</p>

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
<dt>Windot11.h (include Wlclient.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547665">DOT11_BSS_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_BSS_ENTRY_PHY_SPECIFIC_INFO union%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
