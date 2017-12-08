---
UID: NS.ntddndis._NDIS_OFFLOAD_PARAMETERS
title: NDIS_OFFLOAD_PARAMETERS
author: windows-driver-content
description: The NDIS_OFFLOAD_PARAMETERS structure specifies the current task offload configuration settings in response to an OID set request of OID_TCP_OFFLOAD_PARAMETERS.
old-location: netvista\ndis_offload_parameters.htm
old-project: netvista
ms.assetid: ceb6647a-a43e-4ab1-88d4-49927103ecba
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NDIS_OFFLOAD_PARAMETERS, NDIS_OFFLOAD_PARAMETERS, *PNDIS_OFFLOAD_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista,Supported in NDIS 6.0 and later.
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_OFFLOAD_PARAMETERS
req.alt-loc: ntddndis.h
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

# NDIS_OFFLOAD_PARAMETERS structure



## -description
<p>The <b>NDIS_OFFLOAD_PARAMETERS</b> structure specifies the current task offload configuration settings in
  response to an 
  OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569807">OID_TCP_OFFLOAD_PARAMETERS</a>.</p>


## -syntax

````
typedef struct _NDIS_OFFLOAD_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  UCHAR              IPv4Checksum;
  UCHAR              TCPIPv4Checksum;
  UCHAR              UDPIPv4Checksum;
  UCHAR              TCPIPv6Checksum;
  UCHAR              UDPIPv6Checksum;
  UCHAR              LsoV1;
  UCHAR              IPsecV1;
  UCHAR              LsoV2IPv4;
  UCHAR              LsoV2IPv6;
  UCHAR              TcpConnectionIPv4;
  UCHAR              TcpConnectionIPv6;
  ULONG              Flags;
#if (NDIS_SUPPORT_NDIS61)
  UCHAR              IPsecV2;
  UCHAR              IPsecV2IPv4;
#endif 
#if (NDIS_SUPPORT_NDIS630)
  struct {
    UCHAR RscIPv4;
    UCHAR RscIPv6;
  };
#endif 
#if (NDIS_SUPPORT_NDIS630)
  struct {
    UCHAR EncapsulatedPacketTaskOffload;
    UCHAR EncapsulationTypes;
  };
#endif 
} NDIS_OFFLOAD_PARAMETERS, *PNDIS_OFFLOAD_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_OFFLOAD_PARAMETERS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.
     </p>
<p>To indicate the version of the <b>NDIS_OFFLOAD_PARAMETERS</b> structure, set the 
     <b>Revision</b> member to one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_REVISION_3"></a><a id="ndis_offload_parameters_revision_3"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_REVISION_3


### -field 3

</dl>
</td>
<td width="60%">
<p>Supports the 
        <b>RscIPv4</b> , <b>RscIPv6</b>, <b>EncapsulatedPacketTaskOffload</b>, and   <b>EncapsulationTypes</b> members for NDIS 6.30.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_OFFLOAD_PARAMETERS_REVISION_3.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_REVISION_2"></a><a id="ndis_offload_parameters_revision_2"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_REVISION_2


### -field 2

</dl>
</td>
<td width="60%">
<p>Supports the 
        <b>IPsecV2</b>, 
        <b>IPsecV2IPv4</b>, 
        <b>Reserved1</b>, and 
        <b>Reserved2</b> members for NDIS 6.1.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_OFFLOAD_PARAMETERS_REVISION_2.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_REVISION_1"></a><a id="ndis_offload_parameters_revision_1"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_REVISION_1


### -field 1

</dl>
</td>
<td width="60%">
<p>Original version for NDIS 6.0.</p>
<p>Set the 
        <b>Size</b> member to NDIS_SIZEOF_OFFLOAD_PARAMETERS_REVISION_1.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field IPv4Checksum

<dd>
<p>The IPv4 checksum setting of the miniport adapter. For more information, see the following Remarks
     section.</p>
</dd>

### -field TCPIPv4Checksum

<dd>
<p>The IPv4 checksum setting of the miniport adapter for TCP packets. For more information, see the
     following Remarks section.</p>
</dd>

### -field UDPIPv4Checksum

<dd>
<p>The IPv4 checksum setting of the miniport adapter for UDP packets. For more information, see the
     following Remarks section.</p>
</dd>

### -field TCPIPv6Checksum

<dd>
<p>The IPv6 checksum setting of the miniport adapter for TCP packets. For more information, see the
     following Remarks section.</p>
</dd>

### -field UDPIPv6Checksum

<dd>
<p>The IPv6 checksum setting of the miniport adapter for UDP packets. For more information, see the
     following Remarks section.</p>
</dd>

### -field LsoV1

<dd>
<p>The large send offload version 1 (LSOV1) setting of the miniport adapter. This setting should be
     one of the following values:
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_LSOV1_DISABLED"></a><a id="ndis_offload_parameters_lsov1_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_LSOV1_DISABLED

</dl>
</td>
<td width="60%">
<p>LSOV1 is disabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_LSOV1_ENABLED"></a><a id="ndis_offload_parameters_lsov1_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_LSOV1_ENABLED

</dl>
</td>
<td width="60%">
<p>LSOV1 is enabled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field IPsecV1

<dd>
<p>The Internet protocol security (IPsec) offload setting of the miniport adapter. This setting
     should be one of the following values:
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV1_DISABLED"></a><a id="ndis_offload_parameters_ipsecv1_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV1_DISABLED

</dl>
</td>
<td width="60%">
<p>IPsec offload is disabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV1_AH_ENABLED"></a><a id="ndis_offload_parameters_ipsecv1_ah_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV1_AH_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload Authentication Header (AH) feature should be enabled for transmit and
       receive.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV1_ESP_ENABLED"></a><a id="ndis_offload_parameters_ipsecv1_esp_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV1_ESP_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload Encapsulating Security Payload (ESP) feature should be enabled for transmit
       and receive.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV1_AH_AND_ESP_ENABLED"></a><a id="ndis_offload_parameters_ipsecv1_ah_and_esp_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV1_AH_AND_ESP_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload AH and ESP features areenabled for transmit and receive.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field LsoV2IPv4

<dd>
<p>The IPv4 large send offload version 2 (LSOV2) setting of the miniport adapter. This setting should
     be one of the following values:
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_LSOV2_DISABLED"></a><a id="ndis_offload_parameters_lsov2_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_LSOV2_DISABLED

</dl>
</td>
<td width="60%">
<p>LSOV2 for IPv4 is disabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_LSOV2_ENABLED"></a><a id="ndis_offload_parameters_lsov2_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_LSOV2_ENABLED

</dl>
</td>
<td width="60%">
<p>LSOV2 for IPv4 is enabled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field LsoV2IPv6

<dd>
<p>The IPv6 LSOV2 setting of the miniport adapter. These settings are specified as one of the
     following values:
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_LSOV2_DISABLED"></a><a id="ndis_offload_parameters_lsov2_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_LSOV2_DISABLED

</dl>
</td>
<td width="60%">
<p>LSOV2 for IPv6 is disabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_LSOV2_ENABLED"></a><a id="ndis_offload_parameters_lsov2_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_LSOV2_ENABLED

</dl>
</td>
<td width="60%">
<p>LSOV2 for IPv6 is enabled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field TcpConnectionIPv4

<dd>
<p>The IPv4 connection offload setting of the miniport adapter. These settings are specified as one
     of the following values:
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field TcpConnectionIPv6

<dd>
<p>The IPv6 connection offload setting of the miniport adapter. These settings are specified as one
     of the following values:
     </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Flags

<dd>
<p>A set of flags that can be combined with a bitwise OR operation. Set this member to zero. There
     are currently no flags defined.</p>
</dd>

### -field IPsecV2

<dd>
<p>The Internet protocol security (IPsec) offload version 2 setting of a miniport adapter that supports
      IPv6 and IPv4. This member specifies the setting for both IPv6 and IPv4 support. This setting should be
      one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_DISABLED"></a><a id="ndis_offload_parameters_ipsecv2_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_DISABLED

</dl>
</td>
<td width="60%">
<p>IPsec offload version 2 is disabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_ENABLED"></a><a id="ndis_offload_parameters_ipsecv2_ah_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload version 2 Authentication Header (AH) feature should be enabled for transmit
        and receive.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_ESP_ENABLED"></a><a id="ndis_offload_parameters_ipsecv2_esp_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_ESP_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload version 2 Encapsulating Security Payload (ESP) feature should be enabled for
        transmit and receive.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_AND_ESP_ENABLED"></a><a id="ndis_offload_parameters_ipsecv2_ah_and_esp_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_AND_ESP_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload version 2A H and ESP features are enabled for transmit and receive.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field IPsecV2IPv4

<dd>
<p>The Internet protocol security (IPsec) offload version 2 setting of a miniport adapter that supports
      IPv4 and does not support IPv6. If the miniport driver supports IPv6, the 
      <b>IPsecV2</b> member specifies the IPv4 setting and this member is not used. This setting should be one
      of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The miniport driver should not change the current setting.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_DISABLED"></a><a id="ndis_offload_parameters_ipsecv2_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_DISABLED

</dl>
</td>
<td width="60%">
<p>IPsec offload version 2 is disabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_ENABLED"></a><a id="ndis_offload_parameters_ipsecv2_ah_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload version 2 Authentication Header (AH) feature should be enabled for transmit
        and receive.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_ESP_ENABLED"></a><a id="ndis_offload_parameters_ipsecv2_esp_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_ESP_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload version 2 Encapsulating Security Payload (ESP) feature should be enabled for
        transmit and receive.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_AND_ESP_ENABLED"></a><a id="ndis_offload_parameters_ipsecv2_ah_and_esp_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_IPSECV2_AH_AND_ESP_ENABLED

</dl>
</td>
<td width="60%">
<p>The IPsec offload version 2A H and ESP features are enabled for transmit and receive.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field RscIPv4

<dd>
<p>Indicates Receive Segment Coalescing state for IPv4.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The RSC state is unchanged.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_RSC_ENABLED"></a><a id="ndis_offload_parameters_rsc_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_RSC_ENABLED

</dl>
</td>
<td width="60%">
<p>The RSC state is enabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_RSC_DISABLED"></a><a id="ndis_offload_parameters_rsc_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_RSC_DISABLED

</dl>
</td>
<td width="60%">
<p>The RSC state is disabled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field RscIPv6

<dd>
<p>Indicates Receive Segment Coalescing state for IPv6.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_NO_CHANGE"></a><a id="ndis_offload_parameters_no_change"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_NO_CHANGE

</dl>
</td>
<td width="60%">
<p>The RSC state is unchanged.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_RSC_ENABLED"></a><a id="ndis_offload_parameters_rsc_enabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_RSC_ENABLED

</dl>
</td>
<td width="60%">
<p>The RSC state is enabled.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_PARAMETERS_RSC_DISABLED"></a><a id="ndis_offload_parameters_rsc_disabled"></a><dl>

### -field NDIS_OFFLOAD_PARAMETERS_RSC_DISABLED

</dl>
</td>
<td width="60%">
<p>The RSC state is disabled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field EncapsulatedPacketTaskOffload

<dd>
<p>A protocol driver sets <b>EncapsulatedPacketTaskOffload</b> as follows: </p>
<div class="alert"><b>Note</b>  For receive side offloads such as VMQ and RSS, there are other set OIDs that the protocol driver sends down to enable and configure the offload parameters (for example, queues, hash, and indirection table). The <b>EncapsulatedPacketTaskOffload</b> member is supplemental to those OIDs and instructs the NIC to also do these offloads for encapsulated packets.</div>
<div> </div>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_SET_NO_CHANGE"></a><a id="ndis_offload_set_no_change"></a><dl>

### -field NDIS_OFFLOAD_SET_NO_CHANGE


### -field 0

</dl>
</td>
<td width="60%">
<p>The NVGRE task offload state is unchanged.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_SET_ON"></a><a id="ndis_offload_set_on"></a><dl>

### -field NDIS_OFFLOAD_SET_ON


### -field 1

</dl>
</td>
<td width="60%">
<p>Enables NVGRE task offloads.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="NDIS_OFFLOAD_SET_OFF"></a><a id="ndis_offload_set_off"></a><dl>

### -field NDIS_OFFLOAD_SET_OFF


### -field 2

</dl>
</td>
<td width="60%">
<p>Disables NVGRE task offloads.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field EncapsulationTypes

<dd>
<p>This field is effective only when the <b>EncapsulatedPacketTaskOffload</b> is set to <b>NDIS_OFFLOAD_SET_ON</b>. If the <b>EncapsulatedPacketTaskOffload</b> member is not set to <b>NDIS_OFFLOAD_SET_ON</b>, this member is zero. A protocol driver must set <b>EncapsulationTypes</b> to the bitwise OR of the flags corresponding to encapsulation types that it requires. It can select flags from the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="NDIS_ENCAPSULATION_TYPE_GRE_MAC"></a><a id="ndis_encapsulation_type_gre_mac"></a><dl>

### -field NDIS_ENCAPSULATION_TYPE_GRE_MAC


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>Specifies GRE MAC  encapsulation (NVGRE).</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>In response to an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569807">OID_TCP_OFFLOAD_PARAMETERS</a> OID set
    request, a miniport driver uses the settings in the <b>NDIS_OFFLOAD_PARAMETERS</b> structure to set the current
    configuration of the miniport adapter.</p>

<p>NDIS retains the requested settings in the registry in the offload standardized keywords. When NDIS
    restarts the miniport adapter, the miniport driver reads the offload standardized keywords and uses them
    to set the default offload configuration of the NIC.</p>

<p>To access the checksum offload settings, use the following members of the <b>NDIS_OFFLOAD_PARAMETERS</b>
    structure:</p>

<p><b>IPv4Checksum</b></p>

<p><b>TCPIPv4Checksum</b></p>

<p><b>UDPIPv4Checksum</b></p>

<p><b>TCPIPv6Checksum</b></p>

<p><b>UDPIPv6Checksum</b></p>

<p>The preceding members can have one of the following values:</p>

<p></p>

<p>The miniport driver should not change the current setting.</p>

<p>The feature that the member specifies is disabled.</p>

<p>The feature that the member specifies is enabled for transmit and disabled for receive.</p>

<p>The feature that the member specifies is enabled for receive and disabled for transmit.</p>

<p>The feature that the member specifies is enabled for transmit and receive.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
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
<a href="netvista.oid_tcp_offload_hardware_capabilities">
   OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569807">OID_TCP_OFFLOAD_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OFFLOAD_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
