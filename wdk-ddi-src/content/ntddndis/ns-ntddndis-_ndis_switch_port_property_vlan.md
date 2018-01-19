---
UID : NS:ntddndis._NDIS_SWITCH_PORT_PROPERTY_VLAN
title : _NDIS_SWITCH_PORT_PROPERTY_VLAN
author : windows-driver-content
description : The NDIS_SWITCH_PORT_PROPERTY_VLAN structure specifies a virtual local area network (VLAN) policy property for a Hyper-V extensible switch port.
old-location : netvista\ndis_switch_port_property_vlan.htm
old-project : netvista
ms.assetid : 2A151351-AC57-4F7C-BA1A-201F6FB29C4F
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_SWITCH_PORT_PROPERTY_VLAN, NDIS_SWITCH_PORT_PROPERTY_VLAN, *PNDIS_SWITCH_PORT_PROPERTY_VLAN
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.30 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_SWITCH_PORT_PROPERTY_VLAN
req.alt-loc : Ntddndis.h
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
req.typenames : NDIS_SWITCH_PORT_PROPERTY_VLAN, *PNDIS_SWITCH_PORT_PROPERTY_VLAN
---

# _NDIS_SWITCH_PORT_PROPERTY_VLAN structure
The <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure specifies a virtual local area network (VLAN) policy property for a Hyper-V extensible switch port.

## Syntax
````
typedef struct _NDIS_SWITCH_PORT_PROPERTY_VLAN {
  NDIS_OBJECT_HEADER         Header;
  ULONG                      Flags;
  NDIS_SWITCH_PORT_VLAN_MODE OperationMode;
  union {
    struct {
      UINT16 AccessVlanId;
      UINT16 NativeVlanId;
      UINT64 PruneVlanIdArray[64];
      UINT64 TrunkVlanIdArray[64];
    } VlanProperties;
    struct {
      NDIS_SWITCH_PORT_PVLAN_MODE PvlanMode;
      UINT16                      PrimaryVlanId;
      union {
        UINT16 SecondaryVlanId;
        UINT64 SecondaryVlanIdArray[64];
      };
    } PvlanProperties;
  };
  UINT64                     SupportedModes;
} NDIS_SWITCH_PORT_PROPERTY_VLAN, *PNDIS_SWITCH_PORT_PROPERTY_VLAN;
````

## Members

        
            `Flags`

            A ULONG value that contains a bitwise OR of flags. This member is reserved for NDIS.
        
            `Header`

            The type, revision, and size of the <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure.

The <b>Type</b> member of <b>Header</b> must be set to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure, the <b>Revision</b> member of <b>Header</b> must be set to the following value:
        
            `OperationMode`

            An <a href="..\ntddndis\ne-ntddndis-_ndis_switch_port_vlan_mode.md">NDIS_SWITCH_PORT_VLAN_MODE</a> enumeration value that specifies the operation mode of the VLAN.

    ## Remarks
        The <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure is used in the following OID set requests: 


<a href="https://msdn.microsoft.com/library/windows/hardware/hh598275">OID_SWITCH_PORT_PROPERTY_ADD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh598278">OID_SWITCH_PORT_PROPERTY_UPDATE</a>


The <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b> structure follows the <a href="..\ntddndis\ns-ntddndis-_ndis_switch_port_property_parameters.md">NDIS_SWITCH_PORT_PROPERTY_PARAMETERS</a> structure in the buffer that is associated with these OID set requests. The <b>InformationBuffer</b> member of the <a href="..\ndis\ns-ndis-_ndis_oid_request.md">NDIS_OID_REQUEST</a> structure contains a pointer to this buffer.

Port properties, such as <b>NDIS_SWITCH_PORT_PROPERTY_VLAN</b>, are enforced by the extensible switch extension that is installed as a forwarding extension. This type of extension enforces its own rules for forwarding packets, OIDs, and status indications through the extensible switch driver stack.  There can be only one forwarding extension per each instance of an extensible switch.

For more information on forwarding extensions, see <a href="https://msdn.microsoft.com/7ABBB3F3-66F5-4651-8A5A-94940F3FD82D">Forwarding Extensions</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddndis.h (include Ndis.h) |

    ## See Also

        <dl>
<dt><b></b></dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis-_ndis_oid_request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_switch_port_property_parameters.md">NDIS_SWITCH_PORT_PROPERTY_PARAMETERS</a>
</dt>
<dt>
<a href="..\ntddndis\ne-ntddndis-_ndis_switch_port_vlan_mode.md">NDIS_SWITCH_PORT_VLAN_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598275">OID_SWITCH_PORT_PROPERTY_ADD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh598278">OID_SWITCH_PORT_PROPERTY_UPDATE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_SWITCH_PORT_PROPERTY_VLAN structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>