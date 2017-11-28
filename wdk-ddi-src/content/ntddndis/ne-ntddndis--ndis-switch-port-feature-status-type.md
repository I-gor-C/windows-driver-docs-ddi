---
UID: NE.ntddndis._NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE
title: NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE
author: windows-driver-content
description: The NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE enumeration specifies the type of status information for a proprietary policy property, or feature, of a Hyper-V extensible switch port.
old-location: netvista\ndis_switch_port_feature_status_type.htm
old-project: netvista
ms.assetid: bdf19090-5688-4496-8f9a-3a1c422ede60
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: GET_CONFIGURATION_IOCTL_INPUT, GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE
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

# NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE enumeration



## -description
<p>
<p>The <b>NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE</b> enumeration specifies the type of status information for a proprietary policy property, or <i>feature</i>, of a Hyper-V extensible switch port.

An extensible switch port feature is defined and supported by an independent software vendor (ISV).</p>
</p>
<p>The <b>NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE</b> enumeration specifies the type of status information for a proprietary policy property, or <i>feature</i>, of a Hyper-V extensible switch port.

An extensible switch port feature is defined and supported by an independent software vendor (ISV).</p>


## -syntax

````
typedef enum _NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE { 
  NdisSwitchPortFeatureStatusTypeUndefined,
  NdisSwitchPortFeatureStatusTypeCustom,
  NdisSwitchPortFeatureStatusTypeMaximum
} NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE, *PNDIS_SWITCH_PORT_FEATURE_STATUS_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdisSwitchPortFeatureStatusTypeUndefined"></a><a id="ndisswitchportfeaturestatustypeundefined"></a><a id="NDISSWITCHPORTFEATURESTATUSTYPEUNDEFINED"></a><b>NdisSwitchPortFeatureStatusTypeUndefined</b>

<dd>
<p>The port feature status information is not defined.</p>
</dd>

### -field <a id="NdisSwitchPortFeatureStatusTypeCustom"></a><a id="ndisswitchportfeaturestatustypecustom"></a><a id="NDISSWITCHPORTFEATURESTATUSTYPECUSTOM"></a><b>NdisSwitchPortFeatureStatusTypeCustom</b>

<dd>
<p>The feature status information is for a custom extensible switch port feature that is provided by an ISV.

</p>
</dd>

### -field <a id="NdisSwitchPortFeatureStatusTypeMaximum"></a><a id="ndisswitchportfeaturestatustypemaximum"></a><a id="NDISSWITCHPORTFEATURESTATUSTYPEMAXIMUM"></a><b>NdisSwitchPortFeatureStatusTypeMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.

</p>
</dd>
</dl>

## -remarks
<p>The <b>FeatureStatusType</b> member of the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh598227">NDIS_SWITCH_PORT_FEATURE_STATUS_PARAMETERS</a> structure is an <b>NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE</b> enumeration data type.</p>

<p>For more information about extensible switch port policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.

</p>

<p>The <b>FeatureStatusType</b> member of the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh598227">NDIS_SWITCH_PORT_FEATURE_STATUS_PARAMETERS</a> structure is an <b>NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE</b> enumeration data type.</p>

<p>For more information about extensible switch port policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.

</p>

<p>The <b>FeatureStatusType</b> member of the  <a href="https://msdn.microsoft.com/library/windows/hardware/hh598227">NDIS_SWITCH_PORT_FEATURE_STATUS_PARAMETERS</a> structure is an <b>NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE</b> enumeration data type.</p>

<p>For more information about extensible switch port policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.

</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598227">NDIS_SWITCH_PORT_FEATURE_STATUS_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_FEATURE_STATUS_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
