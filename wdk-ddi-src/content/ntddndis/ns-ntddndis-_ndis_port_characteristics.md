---
UID : NS:ntddndis._NDIS_PORT_CHARACTERISTICS
title : _NDIS_PORT_CHARACTERISTICS
author : windows-driver-content
description : The NDIS_PORT_CHARACTERISTICS structure specifies the characteristics of an NDIS port. For more information about NDIS ports, see NDIS Ports.
old-location : netvista\ndis_port_characteristics.htm
old-project : netvista
ms.assetid : fd602dd6-c216-413a-a4da-292739774937
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_PORT_CHARACTERISTICS, *PNDIS_PORT_CHARACTERISTICS, NDIS_PORT_CHARACTERISTICS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.0 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_PORT_CHARACTERISTICS
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
req.typenames : "*PNDIS_PORT_CHARACTERISTICS, NDIS_PORT_CHARACTERISTICS"
---

# _NDIS_PORT_CHARACTERISTICS structure
The <b>NDIS_PORT_CHARACTERISTICS</b> structure specifies the characteristics of an NDIS port. For more information about NDIS ports, see <a href="https://msdn.microsoft.com/e65f4af5-c527-4d6d-a38c-56da006b1ef7">NDIS Ports</a>.

## Syntax
````
typedef struct _NDIS_PORT_CHARACTERISTICS {
  NDIS_OBJECT_HEADER            Header;
  NDIS_PORT_NUMBER              PortNumber;
  ULONG                         Flags;
  NDIS_PORT_TYPE                Type;
  NDIS_MEDIA_CONNECT_STATE      MediaConnectState;
  ULONG64                       XmitLinkSpeed;
  ULONG64                       RcvLinkSpeed;
  NET_IF_DIRECTION_TYPE         Direction;
  NDIS_PORT_CONTROLL_STATE      SendControlState;
  NDIS_PORT_CONTROLL_STATE      RcvControlState;
  NDIS_PORT_AUTHORIZATION_STATE SendAuthorizationState;
  NDIS_PORT_AUTHORIZATION_STATE RcvAuthorizationState;
} NDIS_PORT_CHARACTERISTICS, *PNDIS_PORT_CHARACTERISTICS;
````

## Members

        
            `Direction`

            A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568742">NET_IF_DIRECTION_TYPE</a> NDIS network
     interface direction type.
        
            `Flags`

            A bitwise OR combination of the port characteristics flags, or zero if no flags are set. There is
     currently one flag.
     

If the NDIS_PORT_CHAR_USE_DEFAULT_AUTH_SETTINGS flag is set, NDIS ignores authentication state
     settings and uses the default authentication state instead. A miniport driver can use this flag to
     request that NDIS use the default authentication state settings for the ports that it allocates and
     activates. If the miniport driver controls the default port, when the miniport driver activates the
     default port, the driver can set NDIS_PORT_CHAR_USE_DEFAULT_AUTH_SETTINGS to activate the default port
     with the default authentication state settings.
        
            `Header`

            The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_PORT_CHARACTERISTICS</b> structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_PORT_CHARACTERISTICS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_PORT_CHARACTERISTICS_REVISION_1.
        
            `MediaConnectState`

            The media connection state of the port. This state is the same information that the 
     <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-gen-media-connect-status-ex">
     OID_GEN_MEDIA_CONNECT_STATUS_EX</a> OID returns.
        
            `PortNumber`

            The number of the NDIS port that is associated with this <b>NDIS_PORT_CHARACTERISTICS</b> structure. The 
     <b>PortNumber</b> value is an NDIS_PORT_NUMBER value, which has a ULONG data type and is valid from zero
     through 0xffffff, where zero is reserved for the default port.
        
            `RcvAuthorizationState`

            The authorization state of the port for receive operations. Ignore this member if the 
     <b>RcvControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     

<b>RcvAuthorizationState</b> must contain one of the following values:
        
            `RcvControlState`

            The control state of the port for receive operations. This member must contain one of the
     following values:
        
            `RcvLinkSpeed`

            The receive link speed of the port, in bits per second. A value of -1 in this member indicates
     that the receive link speed is unknown.
        
            `SendAuthorizationState`

            The authorization state of the port for send operations. Ignore this member if the 
     <b>SendControlState</b> member is set to 
     <b>NdisPortControlStateUncontrolled</b>.
     

<b>SendAuthorizationState</b> must contain one of the following values:
        
            `SendControlState`

            The control state of the port for send operations. This member must contain one of the following
     values:
        
            `Type`

            The type of NDIS port. For more information, see <a href="https://msdn.microsoft.com/a77ceb1b-d4b9-4a42-aa5b-685295722fa3">Types of NDIS Ports</a>. This type can be one of the following values:
        
            `XmitLinkSpeed`

            The transmit link speed of the port in bits per second. A value of -1 in this member indicates
     that the transmit link speed is unknown.

    ## Remarks
        The <b>NDIS_PORT_CHARACTERISTICS</b> structure specifies the characteristics of an NDIS port. This structure
    appears in a list of port characteristics that are provided in the 
    <a href="..\ntddndis\ns-ntddndis-_ndis_port_array.md">NDIS_PORT_ARRAY</a> structure that is used with
    the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569583">OID_GEN_ENUMERATE_PORTS</a> OID.

To allocate an NDIS port, a driver initializes an <b>NDIS_PORT_CHARACTERISTICS</b> structure and passes it to
    the 
    <a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a> function. When 
    <b>NdisMAllocatePort</b> successfully returns, NDIS sets the 
    <b>PortNumber</b> member of <b>NDIS_PORT_CHARACTERISTICS</b> to the port number that NDIS assigned to the
    port.

NDIS uses a linked list of ports in port activation Plug and Play (PnP) events. NDIS uses the 
    <a href="..\ntddndis\ns-ntddndis-_ndis_port.md">NDIS_PORT</a> structure to create a linked list of
    ports, and each <b>NDIS_PORT</b> structure contains an <b>NDIS_PORT_CHARACTERISTICS</b> structure.

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
<a href="..\ntddndis\ns-ntddndis-_ndis_port.md">NDIS_PORT</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_port_array.md">NDIS_PORT_ARRAY</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568742">NET_IF_DIRECTION_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569583">OID_GEN_ENUMERATE_PORTS</a>
</dt>
<dt>
<a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/oid-gen-media-connect-status-ex">OID_GEN_MEDIA_CONNECT_STATUS_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e65f4af5-c527-4d6d-a38c-56da006b1ef7">NDIS Ports</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a77ceb1b-d4b9-4a42-aa5b-685295722fa3">Types of NDIS Ports</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PORT_CHARACTERISTICS structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>