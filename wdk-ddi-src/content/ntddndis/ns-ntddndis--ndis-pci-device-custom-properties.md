---
UID: NS.ntddndis._NDIS_PCI_DEVICE_CUSTOM_PROPERTIES
title: NDIS_PCI_DEVICE_CUSTOM_PROPERTIES
author: windows-driver-content
description: The NDIS_PCI_DEVICE_CUSTOM_PROPERTIES structure defines the type and speed of the PCI bus that a NIC is running on.
old-location: netvista\ndis_pci_device_custom_properties.htm
ms.assetid: fd61184f-0502-492d-9014-6afbfd70c189
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PCI_DEVICE_CUSTOM_PROPERTIES
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
ms.keywords: NDIS_PCI_DEVICE_CUSTOM_PROPERTIES, NDIS_PCI_DEVICE_CUSTOM_PROPERTIES, *PNDIS_PCI_DEVICE_CUSTOM_PROPERTIES
req.iface: 
---

# NDIS_PCI_DEVICE_CUSTOM_PROPERTIES structure



## -description
<p>The NDIS_PCI_DEVICE_CUSTOM_PROPERTIES structure defines the type and speed of the PCI bus that a NIC
  is running on.</p>


## -syntax

````
typedef struct _NDIS_PCI_DEVICE_CUSTOM_PROPERTIES {
  NDIS_OBJECT_HEADER Header;
  UINT32             DeviceType;
  UINT32             CurrentSpeedAndMode;
  UINT32             CurrentPayloadSize;
  UINT32             MaxPayloadSize;
  UINT32             MaxReadRequestSize;
  UINT32             CurrentLinkSpeed;
  UINT32             CurrentLinkWidth;
  UINT32             MaxLinkSpeed;
  UINT32             MaxLinkWidth;
#if ((NTDDI_VERSION >= NTDDI_WIN7) || NDIS_SUPPORT_NDIS620)
  UINT32             PciExpressVersion;
  UINT32             InterruptType;
  UINT32             MaxInterruptMessages;
#endif 
} NDIS_PCI_DEVICE_CUSTOM_PROPERTIES, *PNDIS_PCI_DEVICE_CUSTOM_PROPERTIES;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_PCI_DEVICE_CUSTOM_PROPERTIES structure. NDIS sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_OBJECT_TYPE_PCI_DEVICE_CUSTOM_PROPERTIES_REVISION_1, and the 
     <b>Size</b> member to 
     sizeof(NDIS_PCI_DEVICE_CUSTOM_PROPERTIES).</p>
</dd>

### -field <b>DeviceType</b>

<dd>
<p>The PCI device type. For example, conventional, PCI-X, PCI-E, and so on. See the definitions for
     DevProp_PciDevice_DeviceType_xxx in pciprop.h.</p>
</dd>

### -field <b>CurrentSpeedAndMode</b>

<dd>
<p>The speed and mode of conventional PCI or PCI-X devices. For conventional PCI devices, see the
     definitions for DevProp_PciDevice_CurrentSpeedAndMode_Pci_Conventional_xxx. For PCI-X devices, see the
     definitions for DevProp_PciDevice_CurrentSpeedAndMode_Pci_X_xxx. This property is valid only for
     conventional PCI and PCI-X devices.</p>
</dd>

### -field <b>CurrentPayloadSize</b>

<dd>
<p>The current payload size in the transaction layer for a PCI Express device. See definitions for
     DevProp_PciExpressDevice_PayloadOrRequestSize_xxx. This property is valid only for PCI Express
     devices.</p>
</dd>

### -field <b>MaxPayloadSize</b>

<dd>
<p>The maximum payload size in the transaction layer that is supported by a PCI Express device. See
     definitions for DevProp_PciExpressDevice_PayloadOrRequestSize_xxx. This property is valid only for PCI
     Express devices.</p>
</dd>

### -field <b>MaxReadRequestSize</b>

<dd>
<p>The maximum read request size for a PCI Express device. See definitions for
     DevProp_PciExpressDevice_PayloadOrRequestSize_xxx. This property is valid only for PCI Express
     devices..</p>
</dd>

### -field <b>CurrentLinkSpeed</b>

<dd>
<p>The current link speed for the device. This property is applicable to a PCI Express device. See
     the definitions for DevProp_PciExpressDevice_LinkSpeed_xxx. This property is valid only for PCI Express
     devices.</p>
</dd>

### -field <b>CurrentLinkWidth</b>

<dd>
<p>The current link width of the device. This property is applicable to a PCI express device. See the
     definitions for DevProp_PciExpressDevice_LinkWidth_xxx. This property is valid only for PCI Express
     devices.</p>
</dd>

### -field <b>MaxLinkSpeed</b>

<dd>
<p>The maximum link speed of an express link for a PCI Express device. See the definitions for
     DevProp_PciExpressDevice_LinkSpeed_xxx. This property is valid only for PCI Express devices..</p>
</dd>

### -field <b>MaxLinkWidth</b>

<dd>
<p>The maximum link width that is implemented by an express link for a PCI Express device. See the
     definitions for DevProp_PciExpressDevice_LinkWidth_xxx. This property is valid only for PCI Express
     devices.</p>
</dd>

### -field <b>PciExpressVersion</b>

<dd>
<p>The specification version to which an PCI Express device was built. See the definitions for
     DevProp_PciExpressDevice_Spec_Version_xxx. This property is valid only for PCI Express devices.</p>
</dd>

### -field <b>InterruptType</b>

<dd>
<p>The hardware support for interrupts on the PCI Express device. See the definitions for
     DevProp_PciDevice_InterruptType_xxx. This property is valid only for PCI Express devices.</p>
</dd>

### -field <b>MaxInterruptMessages</b>

<dd>
<p>The number of message interrupts that a PCI Express device supports in hardware. See the
     definition for DevProp_PciDevice_InterruptMessageMaximum. This property is valid only for PCI Express
     devices that support message interrupts.</p>
</dd>
</dl>

## -remarks
<p>Some high performance miniport adapters can adjust the hardware configuration and resource allocation
    based on the type and speed of the PCI bus that the NIC is running on. To provide miniport drivers with
    this information during initialization, NDIS queries the custom PCI properties of PCI adapters and
    provides the results in 
    <b>PciDeviceCustomProperties</b> member of the 
    <a href="https://msdn.microsoft.com/945d921b-3024-4c4f-a50d-e996c6183db7">
    NDIS_MINIPORT_INIT_PARAMETERS</a> structure. The type and speed of the PCI bus is also available
    through the 
    <a href="netvista.oid_gen_pci_device_custom_properties">
    OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES</a> OID request and the 
    <a href="netvista.guid_ndis_gen_pci_device_custom_properties">
    GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES</a> WMI GUID.</p>

## -requirements
<table>
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
<a href="netvista.guid_ndis_gen_pci_device_custom_properties">
   GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565972">NDIS_MINIPORT_INIT_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.oid_gen_pci_device_custom_properties">
   OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PCI_DEVICE_CUSTOM_PROPERTIES structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
