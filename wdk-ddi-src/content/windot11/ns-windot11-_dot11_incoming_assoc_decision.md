---
UID : NS:windot11._DOT11_INCOMING_ASSOC_DECISION
title : _DOT11_INCOMING_ASSOC_DECISION
author : windows-driver-content
description : Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location : netvista\dot11_incoming_assoc_decision.htm
old-project : netvista
ms.assetid : aaddff8c-71da-475b-a395-ac40b3b787ae
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _DOT11_INCOMING_ASSOC_DECISION, *PDOT11_INCOMING_ASSOC_DECISION, DOT11_INCOMING_ASSOC_DECISION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : windot11.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 7 and later versions of the Windows operating   systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DOT11_INCOMING_ASSOC_DECISION
req.alt-loc : windot11.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PDOT11_INCOMING_ASSOC_DECISION, DOT11_INCOMING_ASSOC_DECISION"
req.product : Windows 10 or later.
---

# _DOT11_INCOMING_ASSOC_DECISION structure


## Syntax
````
typedef struct _DOT11_INCOMING_ASSOC_DECISION {
  NDIS_OBJECT_HEADER Header;
  DOT11_MAC_ADDRESS  PeerMacAddr;
  BOOLEAN            bAccept;
  USHORT             usReasonCode;
  ULONG              uAssocResponseIEsOffset;
  ULONG              uAssocResponseIEsLength;
} DOT11_INCOMING_ASSOC_DECISION, *PDOT11_INCOMING_ASSOC_DECISION;
````

## Members

        
            `bAccept`

            A Boolean value that indicates whether the miniport driver accepts the incoming association
     request. If <b>TRUE</b>, the driver instructs the NIC to accept the association request. Otherwise, the NIC
     should reject the request.
        
            `Header`

            The type, revision, and size of the DOT11_INCOMING_ASSOC_DECISION structure. This member is
     formatted as an 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure.
     

The miniport driver must set the members of 
     <b>Header</b> to the following values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `PeerMacAddr`

            The media access control (MAC) address of the peer station that the 802.11 station attempted to
     connect to.
        
            `uAssocResponseIEsLength`

            The length of the additional information elements (IEs), in bytes, which the NIC must add to the
     probe response frame that it sends to the peer station that seeks association. The default value is
     zero.
        
            `uAssocResponseIEsOffset`

            The offset of the additional information elements (IEs), in bytes, which the NIC must add to the
     association response frame that it sends to the peer station that seeks association. This offset is relative
     to the start of the buffer that contains the DOT11_INCOMING_ASSOC_DECISION structure. The default value
     is zero.
        
            `usReasonCode`

            A USHORT value that represents a reason code to include in the NIC's association response if 
     <b>bAccept</b> is <b>FALSE</b>.

    ## Remarks
        This structure is used with 
    <a href="netvista.oid_dot11_incoming_association_decision">
    OID_DOT11_INCOMING_ASSOCIATION_DECISION</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | windot11.h (include Ndis.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.oid_dot11_incoming_association_decision">
   OID_DOT11_INCOMING_ASSOCIATION_DECISION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_INCOMING_ASSOC_DECISION structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>