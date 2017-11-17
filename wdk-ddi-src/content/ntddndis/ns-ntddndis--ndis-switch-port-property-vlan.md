---
UID: NS.ntddndis._NDIS_SWITCH_PORT_PROPERTY_VLAN
title: NDIS_SWITCH_PORT_PROPERTY_VLAN
author: windows-driver-content
description: The NDIS_SWITCH_PORT_PROPERTY_VLAN structure specifies a virtual local area network (VLAN) policy property for a Hyper-V extensible switch port.
old-location: netvista\ndis_switch_port_property_vlan.htm
ms.assetid: 2A151351-AC57-4F7C-BA1A-201F6FB29C4F
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_PORT_PROPERTY_VLAN
req.alt-loc: Ntddndis.h
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
ms.keywords: NDIS_SWITCH_PORT_PROPERTY_VLAN, NDIS_SWITCH_PORT_PROPERTY_VLAN, *PNDIS_SWITCH_PORT_PROPERTY_VLAN
req.iface: 
---

# NDIS_SWITCH_PORT_PROPERTY_VLAN structure



## -description
<p>The <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure specifies a virtual local area network (VLAN) policy property for a Hyper-V extensible switch port.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_PORT_PROPERTY_VLAN {
  NDIS_OBJECT_HEADER         Header;
  ULONG                      Flags;
  NDIS_SWITCH_PORT_VLAN_MODE OperationMode;
  union {
    struct {
      UINT16 AccessVlanId;
      UINT16 NativeVlanId;
      UINT64 PruneVlanIdArray[64];
      UINT64 TrunkVlanIdArray[64];
    } VlanProperties;
    struct {
      NDIS_SWITCH_PORT_PVLAN_MODE PvlanMode;
      UINT16                      PrimaryVlanId;
      union {
        UINT16 SecondaryVlanId;
        UINT64 SecondaryVlanIdArray[64];
      };
    } PvlanProperties;
  };
  UINT64                     SupportedModes;
} NDIS_SWITCH_PORT_PROPERTY_VLAN, *PNDIS_SWITCH_PORT_PROPERTY_VLAN;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value:</p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_PORT_PROPERTY_VLAN_REVISION_1"></a><a id="ndis_switch_port_property_vlan_revision_1"></a>NDIS_SWITCH_PORT_PROPERTY_VLAN_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_PORT_PROPERTY_VLAN_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>OperationMode</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/hh598246">NDIS_SWITCH_PORT_VLAN_MODE</a> enumeration value that specifies the operation mode of the VLAN.</p>
</dd>

### -field <b>VlanProperties</b>

<dd>
<p>A structure that specifies the properties of a VLAN with an operation mode of <b>NdisSwitchPortVlanModeAccess</b> or <b>NdisSwitchPortVlanModeTrunk</b>. This structure contains the following members:
</p>
<dl>

### -field <b>AccessVlanId</b>

<dd>
<p>A UINT16 value that specifies the VLAN identifier for the extensible switch port that operates in VLAN access mode.</p>
<div class="alert"><b>Note</b>  This member is only valid if  the <b>OperationMode</b> member is set to <b>NdisSwitchPortVlanModeAccess</b>.</div>
<div> </div>
</dd>

### -field <b>NativeVlanId</b>

<dd>
<p>A UINT16 value that specifies the VLAN identifier for the extensible switch port that operates in VLAN trunk mode.</p>
</dd>

### -field <b>PruneVlanIdArray</b>

<dd>
<p>An array of UINT64 elements that specifies VLAN identifiers whose packets are blocked on an extensible switch port.</p>
<p>The array has 64 UINT64 elements that represent 4096 consecutive bits.
         Each bit that has a value of one specifies a VLAN identifier whose packets are blocked from being sent or received on an extensible switch port. For example,  if bit three is set to one, packet traffic from VLAN identifier three is blocked on a port. Similarly, if bit 64 is set to zero, packet traffic from VLAN identifier 64 is not blocked on a port.
</p>
<div class="alert"><b>Note</b>  VLANS with identifiers that map to a bit value of one are
        always blocked. This overrides the equivalent bit setting for the VLAN identifier in the <b>TrunkVlanIdArray</b> member.</div>
<div> </div>
</dd>

### -field <b>TrunkVlanIdArray</b>

<dd>
<p>An array of UINT64 elements that specifies VLAN identifiers whose packets are allowed on an extensible switch port.</p>
<p>The array has 64 UINT64 elements that represent 4096 consecutive bits.
         Each bit that has a value of one specifies a VLAN identifier whose packets are allowed to be sent or received on an extensible switch port. For example,  if bit two is set to one, packet traffic from VLAN identifier two is allowed on a port. Similarly, if bit 1954 is set to zero, packet traffic from VLAN identifier 1954 is not allowed on a port.
</p>
</dd>
</dl>
</dd>

### -field <b>PvlanProperties</b>

<dd>
<p>A structure that specifies the properties of a VLAN with an operation mode of <b>NdisSwitchPortVlanModePrivate</b>. This structure contains the following members:</p>
<dl>

### -field <b>PvlanMode</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/hh598244">NDIS_SWITCH_PORT_PVLAN_MODE</a> enumeration value that specifies the operation mode of the PVLAN.</p>
</dd>

### -field <b>PrimaryVlanId</b>

<dd>
<p>A UINT16 value that specifies the primary VLAN identifier for an extensible switch port.</p>
<div class="alert"><b>Note</b>  This member is only valid if   the <b>PvlanMode</b> member is set to <b>NdisSwitchPortPvlanModeCommunity</b>.</div>
<div> </div>
</dd>

### -field <b>SecondaryVlanId</b>

<dd>
<p>A UINT16 value that specifies the secondary VLAN identifier for an extensible switch port.</p>
<div class="alert"><b>Note</b>  This member is only valid if   the  <b>PvlanMode</b> member is set to <b>NdisSwitchPortPvlanModeIsolated</b> or <b>NdisSwitchPortPvlanModeCommunity</b>.</div>
<div> </div>
</dd>

### -field <b>SecondaryVlanIdArray</b>

<dd>
<p>An array of UINT64 elements that specify the secondary VLAN identifiers for an extensible switch port.</p>
<p>The array has 64 UINT64 elements, which represent 4096 consecutive bits.
         Each bit that has a value of one specifies a secondary VLAN identifier for the extensible switch port. For example,  if bit five is set to one, the secondary VLAN identifier is five. Similarly, if bit 128 is set to zero, 128 cannot be used as a secondary VLAN identifier.
</p>
<div class="alert"><b>Note</b>  This member is only valid if   the <b>PvlanMode</b> member is set to <b>NdisSwitchPortPvlanModePromiscuous</b>.</div>
<div> </div>
</dd>
</dl>
</dd>

### -field <b>SupportedModes</b>

<dd>
<p>A UINT64 value that contains a bitwise OR of the flags that specify the VLAN operation modes that are supported on the extensible switch port. The following bits specify the supported operation modes:</p>
<p></p>
<dl>

### -field <a id="Bit_0"></a><a id="bit_0"></a><a id="BIT_0"></a>Bit 0

<dd>
<p>Specifies a VLAN access operation mode in which packets from a single VLAN can be sent or received over the port. These packets could be forwarded from other ports on the extensible switch.

</p>
</dd>

### -field <a id="Bit_1"></a><a id="bit_1"></a><a id="BIT_1"></a>Bit 1

<dd>
<p>Specifies a VLAN truck operation mode where packets from multiple VLANs and non-VLAN packets can be sent or received over the port. These packets could be forwarded from other ports on the extensible switch.

</p>
</dd>

### -field <a id="Bit_2"></a><a id="bit_2"></a><a id="BIT_2"></a>Bit 2

<dd>
<p>Specifies an operation mode where packets from a single VLAN can be sent or received over the port. These packets cannot be forwarded from other ports on the extensible switch.

</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure is used in the following OID set requests: </p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598275">OID_SWITCH_PORT_PROPERTY_ADD</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598278">OID_SWITCH_PORT_PROPERTY_UPDATE</a>
</p>

<p>The <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure follows the <a href="https://msdn.microsoft.com/library/windows/hardware/hh598238">NDIS_SWITCH_PORT_PROPERTY_PARAMETERS</a> structure in the buffer that is associated with these OID set requests. The <b>InformationBuffer</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a> structure contains a pointer to this buffer.</p>

<p>Port properties, such as <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b>, are enforced by the extensible switch extension that is installed as a forwarding extension. This type of extension enforces its own rules for forwarding packets, OIDs, and status indications through the extensible switch driver stack.  There can be only one forwarding extension per each instance of an extensible switch.</p>

<p>For more information on forwarding extensions, see <a href="NULL">Forwarding Extensions</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
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
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566710">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598238">NDIS_SWITCH_PORT_PROPERTY_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598246">NDIS_SWITCH_PORT_VLAN_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598275">OID_SWITCH_PORT_PROPERTY_ADD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598278">OID_SWITCH_PORT_PROPERTY_UPDATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_PROPERTY_VLAN structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
