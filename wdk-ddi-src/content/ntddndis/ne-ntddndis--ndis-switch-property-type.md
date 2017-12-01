---
UID: NE.ntddndis._NDIS_SWITCH_PROPERTY_TYPE
title: NDIS_SWITCH_PROPERTY_TYPE
author: windows-driver-content
description: The NDIS_SWITCH_PROPERTY_TYPE enumeration specifies the type of policy property for a Hyper-V extensible switch.
old-location: netvista\ndis_switch_property_type.htm
old-project: netvista
ms.assetid: baa1b837-6f9b-41f4-acf8-e640f8e9f8da
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: NDIS_SWITCH_PROPERTY_TYPE
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

# NDIS_SWITCH_PROPERTY_TYPE enumeration



## -description
<p>The <b>NDIS_SWITCH_PROPERTY_TYPE</b> enumeration specifies the type of policy property for a Hyper-V extensible switch.</p>


## -syntax

````
typedef enum _NDIS_SWITCH_PROPERTY_TYPE { 
  NdisSwitchPropertyTypeUndefined,
  NdisSwitchPropertyTypeCustom,
  NdisSwitchPropertyTypeMaximum
} NDIS_SWITCH_PROPERTY_TYPE, *PNDIS_SWITCH_PROPERTY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdisSwitchPropertyTypeUndefined"></a><a id="ndisswitchpropertytypeundefined"></a><a id="NDISSWITCHPROPERTYTYPEUNDEFINED"></a><b>NdisSwitchPropertyTypeUndefined</b>

<dd>
<p>The switch property type is not defined.</p>
</dd>

### -field <a id="NdisSwitchPropertyTypeCustom"></a><a id="ndisswitchpropertytypecustom"></a><a id="NDISSWITCHPROPERTYTYPECUSTOM"></a><b>NdisSwitchPropertyTypeCustom</b>

<dd>
<p>This value specifies a custom switch property that is defined  by an independent software vendor (ISV).</p>
</dd>

### -field <a id="NdisSwitchPropertyTypeMaximum"></a><a id="ndisswitchpropertytypemaximum"></a><a id="NDISSWITCHPROPERTYTYPEMAXIMUM"></a><b>NdisSwitchPropertyTypeMaximum</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.

</p>
</dd>
</dl>

## -remarks
<p>The <b>PropertyType</b> member of the following structures is an <b>NDIS_SWITCH_PROPERTY_TYPE</b> enumeration data type: 

</p>

<p>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-property-delete-parameters.md">NDIS_SWITCH_PROPERTY_DELETE_PARAMETERS</a>
</p>

<p>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-property-enum-parameters.md">NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS</a>
</p>

<p>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-property-parameters.md">NDIS_SWITCH_PROPERTY_PARAMETERS</a>
</p>

<p>For more information about extensible switch  policies, see <a href="NULL">Hyper-V Extensible Switch Policies</a>.

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
<a href="..\ntddndis\ns-ntddndis--ndis-switch-property-delete-parameters.md">NDIS_SWITCH_PROPERTY_DELETE_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-property-enum-parameters.md">NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-switch-property-parameters.md">NDIS_SWITCH_PROPERTY_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PROPERTY_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
