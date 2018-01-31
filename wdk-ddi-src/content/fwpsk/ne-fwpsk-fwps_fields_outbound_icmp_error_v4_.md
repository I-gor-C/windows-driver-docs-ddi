---
UID : NE:fwpsk.FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4_
title : FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4_
author : windows-driver-content
description : The FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4 enumeration type specifies the data field identifiers for the FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4 and FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD run-time filtering layers.
old-location : netvista\fwps_fields_outbound_icmp_error_v4.htm
old-project : netvista
ms.assetid : be09f5d2-411b-4555-98de-4e6125add062
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_TUNNEL_TYPE, wfp_ref_5_const_3_data_fields_c7cdb743-fc6f-4504-b0fd-8e20f5cee4ff.xml, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_REMOTE_ADDRESS, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_TYPE, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_QUARANTINE_EPOCH, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_TYPE, FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4_, FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_TYPE, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_MAX, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_INTERFACE, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_CODE, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_INDEX, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_NEXTHOP_INTERFACE_PROFILE_ID, netvista.fwps_fields_outbound_icmp_error_v4, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_NEXTHOP_INTERFACE_PROFILE_ID, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_FLAGS, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_FLAGS, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_INTERFACE, FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4 enumeration [Network Drivers Starting with Windows Vista], fwpsk/FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_REMOTE_ADDRESS, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_MAX, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS_TYPE, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_TYPE, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_QUARANTINE_EPOCH, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_SUB_INTERFACE_INDEX, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_TUNNEL_TYPE, FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_SUB_INTERFACE_INDEX, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_INDEX, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_CODE, fwpsk/FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS_TYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : fwpsk.h
req.include-header : Fwpsk.h
req.target-type : Windows
req.target-min-winverclnt : Unless otherwise noted, supported starting with Windows Vista.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : "<= DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4
---

# FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4_ Enumeration
The FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4 and FWPS_LAYER_OUTBOUND_ICMP_ERROR_V4_DISCARD 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layers</a>.

## Syntax
````
typedef enum FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4_ { 
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_REMOTE_ADDRESS,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS_TYPE,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_INTERFACE,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_TYPE,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_CODE,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_INDEX,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_SUB_INTERFACE_INDEX,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_TYPE,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_TUNNEL_TYPE,
#if (NTDDI_VERSION >= NTDDI_WIN6SP1)
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_FLAGS,
#if (NTDDI_VERSION >= NTDDI_WIN7)
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_NEXTHOP_INTERFACE_PROFILE_ID,
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_QUARANTINE_EPOCH,
#endif 
#endif 
  FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_MAX
} FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4;
````

## Constants

<table>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_COMPARTMENT_ID</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_FLAGS</td>
<td>A bitwise OR of a combination of filtering condition flags. For information about the possible
     flags, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549942">Filtering Condition Flags</a>.
     
<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista SP1, and later versions of
     Windows.</div><div> </div></td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_CODE</td>
<td>The ICMP code field, as specified in RFC 792.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_ICMP_TYPE</td>
<td>The ICMP type field, as specified in RFC 792.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_INDEX</td>
<td>The index of the network interface, as enumerated by the network stack.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_QUARANTINE_EPOCH</td>
<td>The time that has passed since the last media state change occurred for the network interface.
     
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div><div> </div></td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_INTERFACE_TYPE</td>
<td>The type of the arrival network interface, as defined by the Internet Assigned Numbers Authority
     (IANA). For more information, see 
     <a href="http://go.microsoft.com/fwlink/p/?linkid=60066">IANAifType-MIB Definitions</a>.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS</td>
<td>The local IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_ADDRESS_TYPE</td>
<td>The local IP address type. The possible values are defined by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a> enumeration.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_LOCAL_INTERFACE</td>
<td>The locally unique identifier (<a href="..\igpupvdev\ns-igpupvdev-_luid.md">LUID</a>) for the network interface associated with the
     local IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_IP_REMOTE_ADDRESS</td>
<td>The remote IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_MAX</td>
<td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_NEXTHOP_INTERFACE_PROFILE_ID</td>
<td>The profile identifier (network category) of the next-hop interface. The possible network category
     values are: public (1), private (2), or domain (3).
     
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div><div> </div></td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_SUB_INTERFACE_INDEX</td>
<td>The index of the logical network interface, as enumerated by the network stack.</td>
</tr>

<tr>
<td>FWPS_FIELD_OUTBOUND_ICMP_ERROR_V4_TUNNEL_TYPE</td>
<td>The encapsulation method used by a tunnel if the 
     <b>IfType</b> member of the IP_ADAPTER_ADDRESSES structure is IF_TYPE_TUNNEL. The tunnel type is defined
     by IANA. For more information, see 
     <a href="http://go.microsoft.com/fwlink/p/?linkid=60066">IANAifType-MIB Definitions</a> and the
     Windows SDK.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |

## See Also

<a href="..\igpupvdev\ns-igpupvdev-_luid.md">LUID</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_FIELDS_OUTBOUND_ICMP_ERROR_V4 enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>