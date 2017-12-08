---
UID: NE.ntddndis._NDIS_SWITCH_PROPERTY_TYPE
title: _NDIS_SWITCH_PROPERTY_TYPE
author: windows-driver-content
description: The NDIS_SWITCH_PROPERTY_TYPE enumeration specifies the type of policy property for a Hyper-V extensible switch.
old-location: netvista\ndis_switch_property_type.htm
old-project: netvista
ms.assetid: baa1b837-6f9b-41f4-acf8-e640f8e9f8da
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _NDIS_SWITCH_PROPERTY_TYPE, NDIS_SWITCH_PROPERTY_TYPE, *PNDIS_SWITCH_PROPERTY_TYPE
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
---

# _NDIS_SWITCH_PROPERTY_TYPE enumeration



## -description
The <b>NDIS_SWITCH_PROPERTY_TYPE</b> enumeration specifies the type of policy property for a Hyper-V extensible switch.


## -syntax

````
typedef enum _NDIS_SWITCH_PROPERTY_TYPE { 
  NdisSwitchPropertyTypeUndefined,
  NdisSwitchPropertyTypeCustom,
  NdisSwitchPropertyTypeMaximum
} NDIS_SWITCH_PROPERTY_TYPE, *PNDIS_SWITCH_PROPERTY_TYPE;
````


## -enum-fields

### -field NdisSwitchPropertyTypeUndefined

The switch property type is not defined.

### -field NdisSwitchPropertyTypeCustom

This value specifies a custom switch property that is defined  by an independent software vendor (ISV).

### -field NdisSwitchPropertyTypeMaximum

The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.



## -remarks
The <b>PropertyType</b> member of the following structures is an <b>NDIS_SWITCH_PROPERTY_TYPE</b> enumeration data type: 




<a href="netvista.ndis_switch_property_delete_parameters">NDIS_SWITCH_PROPERTY_DELETE_PARAMETERS</a>



<a href="netvista.ndis_switch_property_enum_parameters">NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS</a>



<a href="netvista.ndis_switch_property_parameters">NDIS_SWITCH_PROPERTY_PARAMETERS</a>


For more information about extensible switch  policies, see <a href="netvista.hyper_v_extensible_switch_policies">Hyper-V Extensible Switch Policies</a>.



## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported in NDIS 6.30 and later.
</td>
</tr>
<tr>
<th width="30%">
Header
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
<a href="netvista.ndis_switch_property_delete_parameters">NDIS_SWITCH_PROPERTY_DELETE_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.ndis_switch_property_enum_parameters">NDIS_SWITCH_PROPERTY_ENUM_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.ndis_switch_property_parameters">NDIS_SWITCH_PROPERTY_PARAMETERS</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PROPERTY_TYPE enumeration%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
