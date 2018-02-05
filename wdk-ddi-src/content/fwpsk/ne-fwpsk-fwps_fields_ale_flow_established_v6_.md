---
UID : NE:fwpsk.FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6_
title : FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6_
author : windows-driver-content
description : The FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6 enumeration type specifies the data field identifiers for the FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6 and FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD run-time filtering layers.
old-location : netvista\fwps_fields_ale_flow_established_v6.htm
old-project : netvista
ms.assetid : e890f92f-9405-4c2d-87de-7b8c6e63cbd7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_USER_ID, FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_FLAGS, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_FLAGS, wfp_ref_5_const_3_data_fields_72375356-cd2e-4d0a-9d56-0721c57ff4c9.xml, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS_TYPE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_MAX, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_DESTINATION_ADDRESS_TYPE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_ADDRESS, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_PORT, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_MAX, FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6_, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_INTERFACE, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_ADDRESS, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_PORT, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_USER_ID, fwpsk/FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_MACHINE_ID, FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6 enumeration [Network Drivers Starting with Windows Vista], fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS_TYPE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_INTERFACE_TYPE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_USER_ID, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_INTERFACE_TYPE, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_MACHINE_ID, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_USER_ID, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_INTERFACE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_ORIGINAL_APP_ID, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_PROTOCOL, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_ORIGINAL_APP_ID, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_DESTINATION_ADDRESS_TYPE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_PORT, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_TUNNEL_TYPE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_PACKAGE_ID, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_DIRECTION, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_TUNNEL_TYPE, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_PORT, netvista.fwps_fields_ale_flow_established_v6, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_PROTOCOL, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_APP_ID, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS, FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_DIRECTION, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_PACKAGE_ID, fwpsk/FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_APP_ID
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
req.typenames : FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6
---

# FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6_ Enumeration
The FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6 and FWPS_LAYER_ALE_FLOW_ESTABLISHED_V6_DISCARD 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layers</a>.

## Syntax
````
typedef enum FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6_ { 
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_APP_ID,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_USER_ID,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS_TYPE,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_PORT,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_PROTOCOL,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_ADDRESS,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_PORT,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_USER_ID,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_MACHINE_ID,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_DESTINATION_ADDRESS_TYPE,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_INTERFACE,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_DIRECTION,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_INTERFACE_TYPE,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_TUNNEL_TYPE,
#if (NTDDI_VERSION >= NTDDI_WIN6SP1)
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_FLAGS,
#if (NTDDI_VERSION >= NTDDI_WIN8)
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_ORIGINAL_APP_ID,
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_PACKAGE_ID,
#endif 
#endif 
  FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_MAX
} FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6;
````

## Constants

<table>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_APP_ID</td>
<td>The full path of the application.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_ORIGINAL_APP_ID</td>
<td>The full path of the original application for proxy connections. If the application has not been proxied, this path is identical to the xxx_ALE_APP_ID.
<div class="alert"><b>Note</b>  Supported starting with Windows 8.</div><div> </div></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_PACKAGE_ID</td>
<td>The package identifier is a security identifier (SID) that identifies the associated AppContainer process. For more information about the SID structure, see the description for the SID structure in the Microsoft Windows SDK documentation.
<div class="alert"><b>Note</b>  Supported starting with Windows 8.</div><div> </div></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_MACHINE_ID</td>
<td>The identification of the remote machine.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_REMOTE_USER_ID</td>
<td>The identification of the remote user.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_SECURITY_ATTRIBUTE_FQBN_VALUE</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ALE_USER_ID</td>
<td>The identifier of the local user.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_BITMAP_IP_LOCAL_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_BITMAP_IP_LOCAL_PORT</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_BITMAP_IP_REMOTE_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_BITMAP_IP_REMOTE_PORT</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_COMPARTMENT_ID</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_DIRECTION</td>
<td>#### FWP_DIRECTION_INBOUND



#### FWP_DIRECTION_OUTBOUND



####  The possible values are:</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_FLAGS</td>
<td>A bitwise OR of a combination of filtering condition flags. For information about the possible
     flags, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff549942">Filtering Condition Flags</a>.
     
<div class="alert"><b>Note</b>  Supported in Windows Server 2008, Windows Vista SP1, and later versions of
     Windows.</div><div> </div></td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_INTERFACE_TYPE</td>
<td>The type of the network interface, as defined by the Internet Assigned Numbers Authority (IANA).
     For more information, see 
     <a href="http://go.microsoft.com/fwlink/p/?linkid=60066">IANAifType-MIB Definitions</a>.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_DESTINATION_ADDRESS_TYPE</td>
<td>The destination IP address type. The possible values are defined by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a> enumeration.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS</td>
<td>The local IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_ADDRESS_TYPE</td>
<td>The local IP address type. The possible values are defined by the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a> enumeration.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_INTERFACE</td>
<td>The locally unique identifier (<a href="..\igpupvdev\ns-igpupvdev-_luid.md">LUID</a>) for the network interface associated with the
     local IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_PORT</td>
<td>The local transport protocol port number.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_PROTOCOL</td>
<td>The IP protocol number, as specified in RFC 1700.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_ADDRESS</td>
<td>The remote IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_PORT</td>
<td>The remote transport protocol port number.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_MAX</td>
<td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
</tr>

<tr>
<td>FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_TUNNEL_TYPE</td>
<td>The encapsulation method used by a tunnel if the 
     <b>IfType</b> member of the IP_ADAPTER_ADDRESSES structure is IF_TYPE_TUNNEL. The tunnel type is defined
     by IANA. For more information, see 
     <a href="http://go.microsoft.com/fwlink/p/?linkid=60066">IANAifType-MIB Definitions</a> and the
     Windows SDK.</td>
</tr>
</table>

## Remarks

The following macros in 
    <i>Fwpsk.h</i> are defined with FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6 enumeration
    values:
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>
#define FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ICMP_TYPE \
        FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_LOCAL_PORT

#define FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_ICMP_CODE \
        FWPS_FIELD_ALE_FLOW_ESTABLISHED_V6_IP_REMOTE_PORT
</pre>
</td>
</tr>
</table></span></div>These macros are used to access the following IPV6 data fields:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Unless otherwise noted, supported starting with Windows Vista. Unless otherwise noted, supported starting with Windows Vista. |
| **Header** | fwpsk.h (include Fwpsk.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568757">NL_ADDRESS_TYPE</a>

<a href="..\igpupvdev\ns-igpupvdev-_luid.md">LUID</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_FIELDS_ALE_FLOW_ESTABLISHED_V6 enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>