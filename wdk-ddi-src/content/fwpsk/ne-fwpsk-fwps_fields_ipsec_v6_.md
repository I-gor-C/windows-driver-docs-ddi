---
UID : NE:fwpsk.FWPS_FIELDS_IPSEC_V6_
title : FWPS_FIELDS_IPSEC_V6_
author : windows-driver-content
description : The FWPS_FIELDS_IPSEC_V6 enumeration type specifies the data field identifiers for the FWPS_LAYER_IPSEC_V6 run-time filtering layer.
old-location : netvista\fwps_fields_ipsec_v6.htm
old-project : netvista
ms.assetid : e3141736-6e85-43ad-b7f5-28845a57a75c
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : FWPS_FIELDS_IPSEC_V6 enumeration [Network Drivers Starting with Windows Vista], fwpsk/FWPS_FIELDS_IPSEC_V6, wfp_ref_5_const_3_data_fields_33605f4a-08a5-4d7e-bd5c-262711341b18.xml, FWPS_FIELD_IPSEC_V6_IP_REMOTE_ADDRESS, fwpsk/FWPS_FIELD_IPSEC_V6_IP_PROTOCOL, fwpsk/FWPS_FIELD_IPSEC_V6_IP_LOCAL_INTERFACE, fwpsk/FWPS_FIELD_IPSEC_V6_IP_REMOTE_PORT, FWPS_FIELD_IPSEC_V6_IP_LOCAL_INTERFACE, FWPS_FIELD_IPSEC_V6_IP_REMOTE_PORT, FWPS_FIELDS_IPSEC_V6, fwpsk/FWPS_FIELD_IPSEC_V6_IP_REMOTE_ADDRESS, FWPS_FIELD_IPSEC_V6_MAX, FWPS_FIELDS_IPSEC_V6_, FWPS_FIELD_IPSEC_V6_IP_PROTOCOL, FWPS_FIELD_IPSEC_V6_IP_LOCAL_ADDRESS, fwpsk/FWPS_FIELD_IPSEC_V6_IP_LOCAL_PORT, fwpsk/FWPS_FIELD_IPSEC_V6_MAX, FWPS_FIELD_IPSEC_V6_PROFILE_ID, fwpsk/FWPS_FIELD_IPSEC_V6_IP_LOCAL_ADDRESS, netvista.fwps_fields_ipsec_v6, FWPS_FIELD_IPSEC_V6_IP_LOCAL_PORT, fwpsk/FWPS_FIELD_IPSEC_V6_PROFILE_ID
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
req.irql : <= DISPATCH_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : FWPS_FIELDS_IPSEC_V6
---

# FWPS_FIELDS_IPSEC_V6_ Enumeration
The FWPS_FIELDS_IPSEC_V6 enumeration type specifies the data field identifiers for the
  FWPS_LAYER_IPSEC_V6 
  <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa366492">run-time filtering layer</a>.

## Syntax
````
typedef enum FWPS_FIELDS_IPSEC_V6_ { 
  FWPS_FIELD_IPSEC_V6_IP_PROTOCOL,
  FWPS_FIELD_IPSEC_V6_IP_LOCAL_ADDRESS,
  FWPS_FIELD_IPSEC_V6_IP_REMOTE_ADDRESS,
  FWPS_FIELD_IPSEC_V6_IP_LOCAL_PORT,
  FWPS_FIELD_IPSEC_V6_IP_REMOTE_PORT,
  FWPS_FIELD_IPSEC_V6_IP_LOCAL_INTERFACE,
#if (NTDDI_VERSION >= NTDDI_WIN7)
  FWPS_FIELD_IPSEC_V6_PROFILE_ID,
#endif 
  FWPS_FIELD_IPSEC_V6_MAX
} FWPS_FIELDS_IPSEC_V6;
````

## Constants

<table>

<tr>
<td>FWPS_FIELD_IPSEC_V6_IP_LOCAL_ADDRESS</td>
<td>The local IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_IP_LOCAL_INTERFACE</td>
<td>The locally unique identifier (<a href="..\igpupvdev\ns-igpupvdev-_luid.md">LUID</a>) for the network interface associated with the local IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_IP_LOCAL_PORT</td>
<td>The local transport protocol port number.</td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_IP_PROTOCOL</td>
<td>The IP protocol number, as specified in RFC 1700.</td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_IP_REMOTE_ADDRESS</td>
<td>The remote IP address.</td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_IP_REMOTE_PORT</td>
<td>The remote transport protocol port number.</td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_IPSEC_SECURITY_REALM_ID</td>
<td></td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_MAX</td>
<td>The maximum value for this enumeration. This value might change in future versions of the NDIS
     header files and binaries.</td>
</tr>

<tr>
<td>FWPS_FIELD_IPSEC_V6_PROFILE_ID</td>
<td>The profile identifier (network category) of the network interface. The possible network category
     values are: public (1), private (2), or domain (3).
     
<div class="alert"><b>Note</b>  Supported starting with Windows 7.</div><div> </div></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |