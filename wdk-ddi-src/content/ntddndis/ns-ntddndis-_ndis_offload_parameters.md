---
UID : NS:ntddndis._NDIS_OFFLOAD_PARAMETERS
title : _NDIS_OFFLOAD_PARAMETERS
author : windows-driver-content
description : The NDIS_OFFLOAD_PARAMETERS structure specifies the current task offload configuration settings in response to an OID set request of OID_TCP_OFFLOAD_PARAMETERS.
old-location : netvista\ndis_offload_parameters.htm
old-project : netvista
ms.assetid : ceb6647a-a43e-4ab1-88d4-49927103ecba
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_OFFLOAD_PARAMETERS, *PNDIS_OFFLOAD_PARAMETERS, NDIS_OFFLOAD_PARAMETERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Windows Vista,Supported in NDIS 6.0 and later.
req.target-min-winversvr : Windows Server 2008
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_OFFLOAD_PARAMETERS
req.alt-loc : ntddndis.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PNDIS_OFFLOAD_PARAMETERS, NDIS_OFFLOAD_PARAMETERS"
---

# _NDIS_OFFLOAD_PARAMETERS structure
The <b>NDIS_OFFLOAD_PARAMETERS</b> structure specifies the current task offload configuration settings in
  response to an 
  OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569807">OID_TCP_OFFLOAD_PARAMETERS</a>.

## Syntax
````
typedef struct _NDIS_OFFLOAD_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  UCHAR              IPv4Checksum;
  UCHAR              TCPIPv4Checksum;
  UCHAR              UDPIPv4Checksum;
  UCHAR              TCPIPv6Checksum;
  UCHAR              UDPIPv6Checksum;
  UCHAR              LsoV1;
  UCHAR              IPsecV1;
  UCHAR              LsoV2IPv4;
  UCHAR              LsoV2IPv6;
  UCHAR              TcpConnectionIPv4;
  UCHAR              TcpConnectionIPv6;
  ULONG              Flags;
#if (NDIS_SUPPORT_NDIS61)
  UCHAR              IPsecV2;
  UCHAR              IPsecV2IPv4;
#endif 
#if (NDIS_SUPPORT_NDIS630)
  struct {
    UCHAR RscIPv4;
    UCHAR RscIPv6;
  };
#endif 
#if (NDIS_SUPPORT_NDIS630)
  struct {
    UCHAR EncapsulatedPacketTaskOffload;
    UCHAR EncapsulationTypes;
  };
#endif 
} NDIS_OFFLOAD_PARAMETERS, *PNDIS_OFFLOAD_PARAMETERS;
````

## Members

        
            `Flags`

            A set of flags that can be combined with a bitwise OR operation. Set this member to zero. There
     are currently no flags defined.
        
            `Header`

            The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_OFFLOAD_PARAMETERS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.
     

To indicate the version of the <b>NDIS_OFFLOAD_PARAMETERS</b> structure, set the 
     <b>Revision</b> member to one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `IPsecV1`

            The Internet protocol security (IPsec) offload setting of the miniport adapter. This setting
     should be one of the following values:
     

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `IPsecV2`

            The Internet protocol security (IPsec) offload version 2 setting of a miniport adapter that supports
      IPv6 and IPv4. This member specifies the setting for both IPv6 and IPv4 support. This setting should be
      one of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `IPsecV2IPv4`

            The Internet protocol security (IPsec) offload version 2 setting of a miniport adapter that supports
      IPv4 and does not support IPv6. If the miniport driver supports IPv6, the 
      <b>IPsecV2</b> member specifies the IPv4 setting and this member is not used. This setting should be one
      of the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `IPv4Checksum`

            The IPv4 checksum setting of the miniport adapter. For more information, see the following Remarks
     section.
        
            `LsoV1`

            The large send offload version 1 (LSOV1) setting of the miniport adapter. This setting should be
     one of the following values:
     

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `LsoV2IPv4`

            The IPv4 large send offload version 2 (LSOV2) setting of the miniport adapter. This setting should
     be one of the following values:
     

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `LsoV2IPv6`

            The IPv6 LSOV2 setting of the miniport adapter. These settings are specified as one of the
     following values:
     

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `TcpConnectionIPv4`

            The IPv4 connection offload setting of the miniport adapter. These settings are specified as one
     of the following values:
     

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `TcpConnectionIPv6`

            The IPv6 connection offload setting of the miniport adapter. These settings are specified as one
     of the following values:
     

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `TCPIPv4Checksum`

            The IPv4 checksum setting of the miniport adapter for TCP packets. For more information, see the
     following Remarks section.
        
            `TCPIPv6Checksum`

            The IPv6 checksum setting of the miniport adapter for TCP packets. For more information, see the
     following Remarks section.
        
            `UDPIPv4Checksum`

            The IPv4 checksum setting of the miniport adapter for UDP packets. For more information, see the
     following Remarks section.
        
            `UDPIPv6Checksum`

            The IPv6 checksum setting of the miniport adapter for UDP packets. For more information, see the
     following Remarks section.

    ## Remarks
        In response to an 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569807">OID_TCP_OFFLOAD_PARAMETERS</a> OID set
    request, a miniport driver uses the settings in the <b>NDIS_OFFLOAD_PARAMETERS</b> structure to set the current
    configuration of the miniport adapter.

NDIS retains the requested settings in the registry in the offload standardized keywords. When NDIS
    restarts the miniport adapter, the miniport driver reads the offload standardized keywords and uses them
    to set the default offload configuration of the NIC.

To access the checksum offload settings, use the following members of the <b>NDIS_OFFLOAD_PARAMETERS</b>
    structure:

<b>IPv4Checksum</b>

<b>TCPIPv4Checksum</b>

<b>UDPIPv4Checksum</b>

<b>TCPIPv6Checksum</b>

<b>UDPIPv6Checksum</b>

The preceding members can have one of the following values:



The miniport driver should not change the current setting.

The feature that the member specifies is disabled.

The feature that the member specifies is enabled for transmit and disabled for receive.

The feature that the member specifies is enabled for receive and disabled for transmit.

The feature that the member specifies is enabled for transmit and receive.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ndis.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.oid_tcp_offload_hardware_capabilities">
   OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569807">OID_TCP_OFFLOAD_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OFFLOAD_PARAMETERS structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>