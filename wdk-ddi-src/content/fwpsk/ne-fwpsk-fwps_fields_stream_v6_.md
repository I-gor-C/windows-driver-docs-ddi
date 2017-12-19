---
UID: NE.fwpsk.FWPS_FIELDS_STREAM_V6_
title: FWPS_FIELDS_STREAM_V6_
author: windows-driver-content
description: The FWPS_FIELDS_STREAM_V6 enumeration type specifies the data field identifiers for the FWPS_LAYER_STREAM_V6 and FWPS_LAYER_STREAM_V6_DISCARD run-time filtering layers.
old-location: netvista\fwps_fields_stream_v6.htm
old-project: NetVista
ms.assetid: a6fd200c-e573-4bca-aa0d-3e4717c7e81c
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FWPS_FIELDS_STREAM_V6_, FWPS_FIELDS_STREAM_V6
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Unless otherwise noted, supported starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_FIELDS_STREAM_V6
req.alt-loc: fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# FWPS_FIELDS_STREAM_V6_ enumeration



## -description
The FWPS_FIELDS_STREAM_V6 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_STREAM_V6 and FWPS_LAYER_STREAM_V6_DISCARD 
  <a href="netvista.run_time_filtering_layer_identifiers">run-time filtering layers</a>.



## -syntax

````
typedef enum FWPS_FIELDS_STREAM_V6_ { 
  FWPS_FIELD_STREAM_V6_IP_LOCAL_ADDRESS,
  FWPS_FIELD_STREAM_V6_IP_LOCAL_ADDRESS_TYPE,
  FWPS_FIELD_STREAM_V6_IP_REMOTE_ADDRESS,
  FWPS_FIELD_STREAM_V6_IP_LOCAL_PORT,
  FWPS_FIELD_STREAM_V6_IP_REMOTE_PORT,
  FWPS_FIELD_STREAM_V6_DIRECTION,
#if (NTDDI_VERSION >= NTDDI_WIN6SP1
  FWPS_FIELD_STREAM_V6_FLAGS,
#endif 
  FWPS_FIELD_STREAM_V6_MAX
} FWPS_FIELDS_STREAM_V6;
````


## -enum-fields

### -field FWPS_FIELD_STREAM_V6_IP_LOCAL_ADDRESS

The local IP address.


### -field FWPS_FIELD_STREAM_V6_IP_LOCAL_ADDRESS_TYPE

The local IP address type. The possible values are defined by the 
     <a href="netvista.nl_address_type">NL_ADDRESS_TYPE</a> enumeration.


### -field FWPS_FIELD_STREAM_V6_IP_REMOTE_ADDRESS

The remote IP address.


### -field FWPS_FIELD_STREAM_V6_IP_LOCAL_PORT

The local transport protocol port number.


### -field FWPS_FIELD_STREAM_V6_IP_REMOTE_PORT

The remote transport protocol port number.


### -field FWPS_FIELD_STREAM_V6_DIRECTION


### -field The direction of the data flow. The possible values are:
     

### -field FWP_DIRECTION_INBOUND
     

### -field FWP_DIRECTION_OUTBOUND


### -field FWPS_FIELD_STREAM_V6_FLAGS

A bitwise OR of a combination of filtering condition flags. For information about the possible
     flags, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549942">Filtering Condition Flags</a>.
     

<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista SP1, and later versions of
     Windows.</div>
<div> </div>

### -field FWPS_FIELD_STREAM_V6_MAX

The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Unless otherwise noted, supported starting with Windows Vista.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.nl_address_type">NL_ADDRESS_TYPE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20FWPS_FIELDS_STREAM_V6 enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

