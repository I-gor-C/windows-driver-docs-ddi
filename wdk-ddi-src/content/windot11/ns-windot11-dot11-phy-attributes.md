---
UID: NS.windot11.DOT11_PHY_ATTRIBUTES
title: DOT11_PHY_ATTRIBUTES
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_phy_attributes.htm
old-project: netvista
ms.assetid: 9e81144e-e562-4f61-83de-7b7659106de8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_PHY_ATTRIBUTES,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_PHY_ATTRIBUTES
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

# DOT11_PHY_ATTRIBUTES structure



## -description

## -syntax

````
typedef struct DOT11_PHY_ATTRIBUTES {
  NDIS_OBJECT_HEADER                  Header;
  DOT11_PHY_TYPE                      PhyType;
  BOOLEAN                             bHardwarePhyState;
  BOOLEAN                             bSoftwarePhyState;
  BOOLEAN                             bCFPollable;
  ULONG                               uMPDUMaxLength;
  DOT11_TEMP_TYPE                     TempType;
  DOT11_DIVERSITY_SUPPORT             DiversitySupport;
  union {
    DOT11_HRDSSS_PHY_ATTRIBUTES HRDSSSAttributes;
    DOT11_OFDM_PHY_ATTRIBUTES   OFDMAttributes;
    DOT11_ERP_PHY_ATTRIBUTES    ERPAttributes;
  };
  ULONG                               uNumberSupportedPowerLevels;
  ULONG                               TxPowerLevels[8];
  ULONG                               uNumDataRateMappingEntries;
  DOT11_DATA_RATE_MAPPING_ENTRY       DataRateMappingEntries[DOT11_RATE_SET_MAX_LENGTH];
  DOT11_SUPPORTED_DATA_RATES_VALUE_V2 SupportedDataRatesValue;
} DOT11_PHY_ATTRIBUTES, *PDOT11_PHY_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the DOT11_PHY_ATTRIBUTES structure. This member is formatted as an 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the members of 
      <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field <a id="Type"></a><a id="type"></a><a id="TYPE"></a>Type

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field <a id="Revision"></a><a id="revision"></a><a id="REVISION"></a>Revision

<dd>
<p>This member must be set to DOT11_PHY_ATTRIBUTES_REVISION_1.</p>
</dd>

### -field <a id="Size"></a><a id="size"></a><a id="SIZE"></a>Size

<dd>
<p>This member must be set to 
        sizeof(DOT11_PHY_ATTRIBUTES).</p>
</dd>
</dl>
<p>For more information about these members, see 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field <b>PhyType</b>

<dd>
<p>The type of the PHY as specified by a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff548741">DOT11_PHY_TYPE</a> enumerator value.</p>
</dd>

### -field <b>bHardwarePhyState</b>

<dd>
<p>A Boolean value that specifies the hardware power state of the PHY. If <b>TRUE</b>, the hardware power
      state is enabled. If <b>FALSE</b>, the hardware power state is disabled.</p>
<p>For more information about the PHY's hardware power state, see 
      <a href="netvista.oid_dot11_hardware_phy_state">
      OID_DOT11_HARDWARE_PHY_STATE</a>.</p>
<div class="alert"><b>Note</b>  Whenever the PHY's hardware power state changes, the miniport driver must make an 
      <a href="netvista.ndis_status_dot11_phy_state_changed">
      NDIS_STATUS_DOT11_PHY_STATE_CHANGED</a> media-specific status indication.</div>
<div> </div>
</dd>

### -field <b>bSoftwarePhyState</b>

<dd>
<p>A Boolean value that specifies the software power state of the PHY. If <b>TRUE</b>, the software power
      state is enabled. If <b>FALSE</b>, the software power state is disabled.</p>
<p>For more information about the PHY's software power state, see 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff569392">OID_DOT11_NIC_POWER_STATE</a>.</p>
<div class="alert"><b>Note</b>  Whenever the PHY's software power state changes, the miniport driver must make an 
      <a href="netvista.ndis_status_dot11_phy_state_changed">
      NDIS_STATUS_DOT11_PHY_STATE_CHANGED</a> media-specific status indication.</div>
<div> </div>
</dd>

### -field <b>bCFPollable</b>

<dd>
<p>A Boolean value that, if set to <b>TRUE</b>, indicates that the 802.11 station supports CF-Poll frames. For
      more information about CF-Poll frames, refer to Clause 9.4 of the IEEE 802.11-2012 standard.</p>
<p>This member is not applicable to the Extensible Access Point (ExtAP) operation mode and is ignored
      when the NIC is in the ExtAP mode.</p>
</dd>

### -field <b>uMPDUMaxLength</b>

<dd>
<p>The maximum length, in bytes, of a media access control (MAC) protocol data unit (MPDU) frame that
      the PHY can transmit or receive. For more information, see 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff569387">OID_DOT11_MPDU_MAX_LENGTH</a>.</p>
<div class="alert"><b>Note</b>  Whenever the PHY's software power state changes, the miniport driver must make an
      NDIS_STATUS_DOT11_MPDU_MAX_LENGTH_CHANGED media-specific status indication.</div>
<div> </div>
</dd>

### -field <b>TempType</b>

<dd>
<p>The PHY's operating temperature range, defined through a 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff548806">DOT11_TEMP_TYPE</a> enumeration value.</p>
</dd>

### -field <b>DiversitySupport</b>

<dd>
<p>The PHY's type of antenna diversity, defined through a 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff547683">DOT11_DIVERSITY_SUPPORT</a> enumeration
      value.</p>
</dd>

### -field <b>HRDSSSAttributes</b>

<dd>
<p>The PHY-specific attributes of a high-rate direct-sequence spread spectrum (HRDSS) PHY type. The
       miniport driver must use this member only if the 
       <b>PhyType</b> member is set to dot11_phy_type_hrdsss.</p>
</dd>

### -field <b>OFDMAttributes</b>

<dd>
<p>The PHY-specific attributes of an orthogonal frequency division multiplexing (OFDM) PHY type. The
       miniport driver must use this member only if the 
       <b>PhyType</b> member is set to dot11_phy_type_ofdm.</p>
</dd>

### -field <b>ERPAttributes</b>

<dd>
<p>The PHY-specific attributes of an extended-rate PHY (ERP) type. The miniport driver must use this
       member only if the 
       <b>PhyType</b> member is set to dot11_phy_type_erp.</p>
</dd>

### -field <b>uNumberSupportedPowerLevels</b>

<dd>
<p>The number of power levels within the 
      <b>TxPowerLevels</b> array. 
      <b>uNumOfSupportedPowerLevels</b> must have a value from 1 through 8.</p>
</dd>

### -field <b>TxPowerLevels</b>

<dd>
<p>An array of the supported transmit power levels in units of milliwatts (mWs). Each power level must
      be a value from 0 through 1000.</p>
</dd>

### -field <b>uNumDataRateMappingEntries</b>

<dd>
<p>The number of data rates within the 
      <b>DataRateMappingEntries</b> array.</p>
</dd>

### -field <b>DataRateMappingEntries</b>

<dd>
<p>An array of the data rates supported by the PHY. Each entry is formatted as a 
      <a href="..\windot11\ns-windot11-dot11-data-rate-mapping-entry.md">
      DOT11_DATA_RATE_MAPPING_ENTRY</a> structure.</p>
</dd>

### -field <b>SupportedDataRatesValue</b>

<dd>
<p>An array of the following data rates supported by the PHY:</p>
<ul>
<li>
<p>The transmit data rates supported by the Physical Layer Convergence Procedure (PLCP) and Physical
        Media Dependent (PMD) sublayer of the PHY.</p>
</li>
<li>
<p>The receive data rates supported by the PLCP and PMD of the PHY.</p>
</li>
</ul>
<p>Each entry in the array is formatted as a DOT11_SUPPORTED_DATA_RATES_VALUE_V2 structure.</p>
</dd>
</dl>

## -remarks
<p>The 
    <a href="..\ndis\ns-ndis--ndis-miniport-adapter-native-802-11-attributes.md">
    NDIS_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES</a> structure contains a member (<b>pExtPhyAttributes</b>) that specifies the address of an array of DOT11_PHY_ATTRIBUTES structures. When
    the miniport driver calls 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>,
    the driver sets the 
    <i>MiniportAttributes</i> parameter to the address of driver-allocated block of memory which contains an
    NDIS_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES structure along with the array of DOT11_PHY_ATTRIBUTES
    structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547683">DOT11_DIVERSITY_SUPPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547686">DOT11_ERP_PHY_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548643">DOT11_HRDSSS_PHY_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548707">DOT11_OFDM_PHY_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548806">DOT11_TEMP_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547679">DOT11_DATA_RATE_MAPPING_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569370">OID_DOT11_HARDWARE_PHY_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569392">OID_DOT11_NIC_POWER_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548741">DOT11_PHY_TYPE</a>
</dt>
<dt>
<a href="..\windot11\ns-windot11--dot11-supported-data-rates-value-v2.md">
   DOT11_SUPPORTED_DATA_RATES_VALUE_V2</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-miniport-adapter-native-802-11-attributes.md">
   NDIS_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_PHY_ATTRIBUTES structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
