---
UID: NS.windot11.DOT11_HRDSSS_PHY_ATTRIBUTES
title: DOT11_HRDSSS_PHY_ATTRIBUTES
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_hrdsss_phy_attributes.htm
ms.assetid: 435e74b4-1a29-4031-bf21-92eae71e99a1
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
req.alt-api: DOT11_HRDSSS_PHY_ATTRIBUTES
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
ms.keywords: DOT11_HRDSSS_PHY_ATTRIBUTES, DOT11_HRDSSS_PHY_ATTRIBUTES, *PDOT11_HRDSSS_PHY_ATTRIBUTES
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_HRDSSS_PHY_ATTRIBUTES structure



## -description

## -syntax

````
typedef struct DOT11_HRDSSS_PHY_ATTRIBUTES {
  BOOLEAN bShortPreambleOptionImplemented;
  BOOLEAN bPBCCOptionImplemented;
  BOOLEAN bChannelAgilityPresent;
  ULONG   uHRCCAModeSupported;
} DOT11_HRDSSS_PHY_ATTRIBUTES, *PDOT11_HRDSSS_PHY_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>bShortPreambleOptionImplemented</b>

<dd>
<p>A Boolean value that, if set to <b>TRUE</b>, specifies that the PHY supports the option to enable the
     short Physical Layer Convergence Procedure (PLCP) preamble and header. For more information about the
     short PLCP preamble and header, refer to Clause 18.2.2.2 of the IEEE 802.11b-1999 standard</p>
</dd>

### -field <b>bPBCCOptionImplemented</b>

<dd>
<p>A Boolean value that, if set to <b>TRUE</b>, specifies that the PHY supports enabled packet binary
     convolutional code (PBCC) modulation. For more information about PBCC modulation, refer to Clause
     18.4.6.6 of the IEEE 802.11b-1999 standard.</p>
</dd>

### -field <b>bChannelAgilityPresent</b>

<dd>
<p>A Boolean value that, if set to <b>TRUE</b>, specifies that the PHY supports channel agility. For more
     information about channel agility, refer to Clause 18 of the IEEE 802.11b-1999 standard and Clause 19 of
     the IEEE 802.11g-2003 standard.</p>
</dd>

### -field <b>uHRCCAModeSupported</b>

<dd>
<p>The type of clear channel assessment (CCA) mode supported by the current PHY type. For more
     information about CCA, refer to Clause 16.4.8.5 of the IEEE 802.11-2012 standard and Clause 18.4.8.4 of
     the IEEE 802.11b-1999 standard.
     </p>
<p>The CCA modes supported by the PHY are defined through the following bitmask:</p>
<p></p>
<dl>

### -field <a id="DOT11_CCA_MODE_ED_ONLY__0x00000001_"></a><a id="dot11_cca_mode_ed_only__0x00000001_"></a><a id="DOT11_CCA_MODE_ED_ONLY__0X00000001_"></a>DOT11_CCA_MODE_ED_ONLY (0x00000001)

<dd>
<p>CCA mode using the energy detect (ED) signal. For more information about the ED signal, refer to
       Clause 15.4.6.1 of the IEEE 802.11-2012 standard.</p>
</dd>

### -field <a id="DOT11_CCA_MODE_CS_ONLY__0x00000002_"></a><a id="dot11_cca_mode_cs_only__0x00000002_"></a><a id="DOT11_CCA_MODE_CS_ONLY__0X00000002_"></a>DOT11_CCA_MODE_CS_ONLY (0x00000002)

<dd>
<p>CCA mode using the carrier sense (CS) signal. For more information about the CS signal, refer to
       Clause 15.4.6.2 of the IEEE 802.11-2012 standard.</p>
</dd>

### -field <a id="DOT11_CCA_MODE_ED_and_CS__0x00000004_"></a><a id="dot11_cca_mode_ed_and_cs__0x00000004_"></a><a id="DOT11_CCA_MODE_ED_AND_CS__0X00000004_"></a>DOT11_CCA_MODE_ED_and_CS (0x00000004)

<dd>
<p>Both ED and CS modes.</p>
</dd>

### -field <a id="DOT11_HR_CCA_MODE_CS_WITH_TIMER__0x00000008_"></a><a id="dot11_hr_cca_mode_cs_with_timer__0x00000008_"></a><a id="DOT11_HR_CCA_MODE_CS_WITH_TIMER__0X00000008_"></a>DOT11_HR_CCA_MODE_CS_WITH_TIMER (0x00000008)

<dd>
<p>CCA mode using the CS signal with a timer. For more information about this CCA mode, refer to
       Clause 18.4.8.4 of the IEEE 802.11b-1999 standard.</p>
</dd>

### -field <a id="DOT11_HR_CCA_MODE_HRCS_AND_ED__0x00000010_"></a><a id="dot11_hr_cca_mode_hrcs_and_ed__0x00000010_"></a><a id="DOT11_HR_CCA_MODE_HRCS_AND_ED__0X00000010_"></a>DOT11_HR_CCA_MODE_HRCS_AND_ED (0x00000010)

<dd>
<p>Both ED and CS modes on high-rate (HR) PHYs. For more information about this CCA mode, refer to
       Clause 18.4.8.4 of the IEEE 802.11b-1999 standard.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The miniport driver defines the attributes of a PHY on the 802.11 station through the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff548728">DOT11_PHY_ATTRIBUTES</a> structure, and
    formats the 
    <b>HRDSSSAttributes</b> member as a DOT11_HRDSSS_PHY_ATTRIBUTES structure. The driver must only do this if
    the PHY defined by the DOT11_PHY_ATTRIBUTES structure is an HRDSSS PHY type.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548728">DOT11_PHY_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_HRDSSS_PHY_ATTRIBUTES structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
