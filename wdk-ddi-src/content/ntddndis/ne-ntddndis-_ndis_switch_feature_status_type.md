---
UID: NE.ntddndis._NDIS_SWITCH_FEATURE_STATUS_TYPE
title: _NDIS_SWITCH_FEATURE_STATUS_TYPE
author: windows-driver-content
description: The NDIS_SWITCH_FEATURE_STATUS_TYPE enumeration specifies the type of status information for a custom policy property, or feature, of a Hyper-V extensible switch.
old-location: netvista\ndis_switch_feature_status_type.htm
old-project: NetVista
ms.assetid: a3255313-1d49-4286-a48a-6a1729ccf7fe
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _NDIS_SWITCH_FEATURE_STATUS_TYPE, *PNDIS_SWITCH_FEATURE_STATUS_TYPE, PNDIS_SWITCH_FEATURE_STATUS_TYPE, NDIS_SWITCH_FEATURE_STATUS_TYPE
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
req.alt-api: NDIS_SWITCH_FEATURE_STATUS_TYPE
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

# _NDIS_SWITCH_FEATURE_STATUS_TYPE enumeration



## -description

The <b>NDIS_SWITCH_FEATURE_STATUS_TYPE</b> enumeration specifies the type of status information for a custom policy property, or <i>feature</i>, of a Hyper-V extensible switch.

An extensible switch feature is defined and supported by an independent software vendor (ISV).



The <b>NDIS_SWITCH_FEATURE_STATUS_TYPE</b> enumeration specifies the type of status information for a custom policy property, or <i>feature</i>, of a Hyper-V extensible switch.

An extensible switch feature is defined and supported by an independent software vendor (ISV).



## -syntax

````
typedef enum _NDIS_SWITCH_FEATURE_STATUS_TYPE { 
  NdisSwitchFeatureStatusTypeUndefined,
  NdisSwitchFeatureStatusTypeCustom,
  NdisSwitchFeatureStatusTypeMaximum
} NDIS_SWITCH_FEATURE_STATUS_TYPE, *PNDIS_SWITCH_FEATURE_STATUS_TYPE;
````


## -enum-fields

### -field NdisSwitchFeatureStatusTypeUndefined

The feature status information is not defined.


### -field NdisSwitchFeatureStatusTypeCustom

The feature status information is for a custom extensible switch feature that is provided by an ISV.




### -field NdisSwitchFeatureStatusTypeMaximum

The maximum value for this enumeration. This value might change in future versions of the NDIS header files and binaries.




## -remarks
The <b>FeatureStatusType</b> member of the  <a href="netvista.ndis_switch_feature_status_parameters">NDIS_SWITCH_FEATURE_STATUS_PARAMETERS</a> structure is an <a href="netvista.ndis_switch_property_type">NDIS_SWITCH_PROPERTY_TYPE</a> enumeration data type.

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
<a href="netvista.ndis_switch_feature_status_parameters">NDIS_SWITCH_FEATURE_STATUS_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NDIS_SWITCH_FEATURE_STATUS_TYPE enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

