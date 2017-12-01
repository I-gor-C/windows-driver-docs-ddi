---
UID: NS.ntddndis._NDIS_SWITCH_PORT_PROPERTY_PROFILE
title: NDIS_SWITCH_PORT_PROPERTY_PROFILE
author: windows-driver-content
description: The NDIS_SWITCH_PORT_PROPERTY_PROFILE structure specifies a policy property for a Hyper-V extensible switch port that the extensible switch extension saves in its own policy store instead of in the Hyper-V policy store.
old-location: netvista\ndis_switch_port_property_profile.htm
old-project: netvista
ms.assetid: DFB7239F-4A6B-4C98-884E-FAC1A0DE2024
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_SWITCH_PORT_PROPERTY_PROFILE, NDIS_SWITCH_PORT_PROPERTY_PROFILE, *PNDIS_SWITCH_PORT_PROPERTY_PROFILE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_PORT_PROPERTY_PROFILE
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
req.iface: 
---

# NDIS_SWITCH_PORT_PROPERTY_PROFILE structure



## -description
<p>The <b>NDIS_SWITCH_PORT_PROPERTY_PROFILE</b> structure specifies a policy property for a Hyper-V extensible switch port that the extensible switch extension saves in its own policy store instead of in the Hyper-V policy store. In this case, policy definitions are identified by property profiles within the driver's policy store.</p>


## -syntax

````
typedef struct _NDIS_SWITCH_PORT_PROPERTY_PROFILE {
  NDIS_OBJECT_HEADER                          Header;
  ULONG                                       Flags;
  NDIS_SWITCH_PORT_PROPERTY_PROFILE_NAME      ProfileName;
  GUID                                        ProfileId;
  NDIS_VENDOR_NAME                            VendorName;
  GUID                                        VendorId;
  UINT32                                      BindingType;
  GUID                                        NetCfgInstanceId;
  struct {
    UINT32 PciSegmentNumber  :16;
    UINT32 PciBusNumber  :8;
    UINT32 PciDeviceNumber  :5;
    UINT32 PciFunctionNumber  :3;
  } PciLocation;
  UINT32                                      CdnLabelId;
  NDIS_SWITCH_PORT_PROPERTY_PROFILE_CDN_LABEL CdnLabel;
} NDIS_SWITCH_PORT_PROPERTY_PROFILE, *PNDIS_SWITCH_PORT_PROPERTY_PROFILE;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_SWITCH_PORT_PROPERTY_PROFILE</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_PORT_PROPERTY_PROFILE</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value:</p>
<p></p>
<dl>

### -field <a id="NDIS_SWITCH_PORT_PROPERTY_PROFILE_REVISION_1"></a><a id="ndis_switch_port_property_profile_revision_1"></a>NDIS_SWITCH_PORT_PROPERTY_PROFILE_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_NDIS_SWITCH_PROPERTY_PROFILE_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A ULONG value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.</p>
</dd>

### -field <b>ProfileName</b>

<dd>
<p>An NDIS_SWITCH_PORT_PROPERTY_PROFILE_NAME value that specifies the user-friendly name of the profile property.</p>
</dd>

### -field <b>ProfileId</b>

<dd>
<p>A GUID value that uniquely identifies the profile property.</p>
</dd>

### -field <b>VendorName</b>

<dd>
<p>An NDIS_VENDOR_NAME value that specifies the user-friendly name of the vendor that defined the port profile.</p>
</dd>

### -field <b>VendorId</b>

<dd>
<p>A GUID value that identifies the vendor that defined the port profile.</p>
</dd>

### -field <b>BindingType</b>

<dd>
<p>A UINT32 value that contains a proprietary value that is defined by the independent software vendor (ISV).</p>
</dd>

### -field <b>NetCfgInstanceId</b>

<dd>
<p>A GUID value that specifies the <b>NetCfgInstanceId</b> registry value of the underlying network adapter connection for which the property is applied.

</p>
<p>The <b>NetCfgInstanceId</b> value is specified for the network adapter connection through an object identifier (OID) set request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh598263">OID_SWITCH_NIC_CREATE</a>.</p>
</dd>

### -field <b>PciLocation</b>

<dd>
<p>A structure that specifies the PCI location of the underlying physical network adapter that is specified by the <b>NetCfgInstanceId</b> member.</p>
<p>For more information, see the Remarks section.</p>
<dl>

### -field <b>PciSegmentNumber</b>

<dd>
<p>A value that specifies the group of PCI buses on which the physical network adapter is attached.
</p>
</dd>

### -field <b>PciBusNumber</b>

<dd>
<p>A value that specifies the current PCI bus number on which the physical network adapter is attached.
</p>
</dd>

### -field <b>PciDeviceNumber</b>

<dd>
<p>A value that specifies the device number for the physical network adapter on the PCI bus.
</p>
<div class="alert"><b>Note</b>  The PCI device number is also known as the <i>PCI slot number</i>.</div>
<div> </div>
</dd>

### -field <b>PciFunctionNumber</b>

<dd>
<p>A value that specifies the function number of a logical device on the physical network adapter.</p>
</dd>
</dl>
</dd>

### -field <b>CdnLabelId</b>

<dd>
<p>A UINT32 value that specifies a unique identifier for the data that is contained in the <b>CdnLabel</b> member.</p>
</dd>

### -field <b>CdnLabel</b>

<dd>
<p>An  NDIS_SWITCH_PORT_PROPERTY_PROFILE_CDN_LABEL value that specifies the PCI Express (PCIe) CDN label for the location of the physical network adapter. A CDN label provides consistent device locations across similar hardware locations.</p>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_SWITCH_PORT_PROPERTY_PROFILE</b> structure is used by the extension to reference a policy property within a private policy store instead of the Hyper-V policy store. This allows the independent software vendor (ISV) to populate and manage this private policy store through private channels and interfaces.  Vendors can distinguish their profiles from other vendors' profiles using the <i>VendorName</i> and <i>VendorId</i> fields. </p>

<p>The <b>NDIS_SWITCH_PORT_PROPERTY_PROFILE</b> structure is used in the following OID set requests: </p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598275">OID_SWITCH_PORT_PROPERTY_ADD</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598278">OID_SWITCH_PORT_PROPERTY_UPDATE</a>
</p>

<p>The <b>NDIS_SWITCH_PORT_PROPERTY_PROFILE</b> structure follows the <a href="..\ntddndis\ns-ntddndis--ndis-switch-port-property-parameters.md">NDIS_SWITCH_PORT_PROPERTY_PARAMETERS</a> structure in the buffer that is associated with these OID set requests. The <b>InformationBuffer</b> member of the <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> structure contains a pointer to this buffer.</p>

<p>The <b>PciLocation</b> and <b>CdnLabel</b> members are only relevant if the property profile specifies a policy for an underlying physical network adapter that is attached to the extensible switch external network adapter. For example, if the external network adapter is bound to an extensible switch team of adapters, these members could specify policies for a single adapter from that team. For more information about the extensible switch team, see <a href="NULL">Types of Physical Network Adapter Configurations</a>.</p>

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
<a href="netvista.if_counted_string">IF_COUNTED_STRING</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-port-property-parameters.md">NDIS_SWITCH_PORT_PROPERTY_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598263">OID_SWITCH_NIC_CREATE</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_PROPERTY_PROFILE structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
