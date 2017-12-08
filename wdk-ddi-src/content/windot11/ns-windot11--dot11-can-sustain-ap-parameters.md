---
UID: NS.windot11._DOT11_CAN_SUSTAIN_AP_PARAMETERS
title: DOT11_CAN_SUSTAIN_AP_PARAMETERS
author: windows-driver-content
description: The DOT11_CAN_SUSTAIN_AP_PARAMETERS structure specifies the reason why the NIC can sustain an access point (AP).
old-location: netvista\dot11_can_sustain_ap_parameters.htm
old-project: netvista
ms.assetid: 8d7995f3-6cc1-4f3c-a016-b31dc69ddd7f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_CAN_SUSTAIN_AP_PARAMETERS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_CAN_SUSTAIN_AP_PARAMETERS
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

# DOT11_CAN_SUSTAIN_AP_PARAMETERS structure



## -description

## -syntax

````
typedef struct _DOT11_CAN_SUSTAIN_AP_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              ulReason;
} DOT11_CAN_SUSTAIN_AP_PARAMETERS, *PDOT11_CAN_SUSTAIN_AP_PARAMETERS;
````


## -struct-fields
<dl>

### -field Header

<dd>
<p>The type, revision, and size of the DOT11_CAN_SUSTAIN_AP_PARAMETERS structure. This member is
     formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.
     </p>
<p>The miniport driver must set the members of 
     <b>Header</b> to the following values:</p>
<p></p>
<dl>

### -field Type

<dd>
<p>This member must be set to NDIS_OBJECT_TYPE_DEFAULT.</p>
</dd>

### -field Revision

<dd>
<p>This member must be set to DOT11_CAN_SUSTAIN_AP_PARAMETERS_REVISION_1.</p>
</dd>

### -field Size

<dd>
<p>This member must be set to 
       <b>sizeof</b>(DOT11_CAN_SUSTAIN_AP_PARAMETERS).</p>
</dd>
</dl>
<p>For more information about these members, see 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>.</p>
</dd>

### -field ulReason

<dd>
<p>A ULONG value that specifies the reason why the NIC can sustain the AP. An IHV can supply the
     following range of values:
     </p>
<p></p>
<dl>

### -field DOT11_CAN_SUSTAIN_AP_REASON_IHV_END

<dd>
<p>The end value of possible IHV-specified reasons.</p>
</dd>

### -field DOT11_CAN_SUSTAIN_AP_REASON_IHV_START

<dd>
<p>The start value of possible IHV-specified reasons.</p>
</dd>
</dl>
<p>If the value of 
     <b>ulReason</b> is in the range of DOT11_CAN_SUSTAIN_AP_REASON_IHV_START and
     DOT11_STOP_AP_REASON_IHV_END, inclusive, the operating system takes no action.</p>
</dd>
</dl>

## -remarks
<p>The Native 802.11 miniport driver includes a DOT11_CAN_SUSTAIN_AP_PARAMETERS structure when the driver
    makes an 
    <a href="netvista.ndis_status_dot11_can_sustain_ap">
    NDIS_STATUS_DOT11_CAN_SUSTAIN_AP</a> status indication.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating
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
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.ndis_status_dot11_can_sustain_ap">
   NDIS_STATUS_DOT11_CAN_SUSTAIN_AP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_CAN_SUSTAIN_AP_PARAMETERS structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
