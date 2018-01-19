---
UID : NS:ndis._NDIS_OFFLOAD_ENCAPSULATION
title : _NDIS_OFFLOAD_ENCAPSULATION
author : windows-driver-content
description : The NDIS_OFFLOAD_ENCAPSULATION structure specifies encapsulation settings when it is used with the OID_OFFLOAD_ENCAPSULATION OID.
old-location : netvista\ndis_offload_encapsulation.htm
old-project : netvista
ms.assetid : 19013ffa-6bb5-4a77-b85b-c32fb0bf0530
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_OFFLOAD_ENCAPSULATION, NDIS_OFFLOAD_ENCAPSULATION, *PNDIS_OFFLOAD_ENCAPSULATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.0 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_OFFLOAD_ENCAPSULATION
req.alt-loc : ndis.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : See Remarks section
req.typenames : NDIS_OFFLOAD_ENCAPSULATION, *PNDIS_OFFLOAD_ENCAPSULATION
---

# _NDIS_OFFLOAD_ENCAPSULATION structure
The NDIS_OFFLOAD_ENCAPSULATION structure specifies encapsulation settings when it is used with the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff569762">OID_OFFLOAD_ENCAPSULATION</a> OID.

## Syntax
````
typedef struct _NDIS_OFFLOAD_ENCAPSULATION {
  NDIS_OBJECT_HEADER Header;
  struct {
    ULONG Enabled;
    ULONG EncapsulationType;
    ULONG HeaderSize;
  } IPv4;
  struct {
    ULONG Enabled;
    ULONG EncapsulationType;
    ULONG HeaderSize;
  } IPv6;
} NDIS_OFFLOAD_ENCAPSULATION, *PNDIS_OFFLOAD_ENCAPSULATION;
````

## Members

        
            `Header`

            The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_OFFLOAD_ENCAPSULATION structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_OFFLOAD_ENCAPSULATION, the 
     <b>Revision</b> member to NDIS_OFFLOAD_ENCAPSULATION_ REVISION _1, and the 
     <b>Size</b> member to NDIS_SIZEOF_OFFLOAD_ENCAPSULATION_REVISION_1.
        
            `IPv4`

            A structure within NDIS_OFFLOAD_ENCAPSULATION that specifies IPv4 encapsulation and that contains
     the following members:
        
            `IPv6`

            A structure within NDIS_OFFLOAD_ENCAPSULATION that specifies IPv6 encapsulation and that contains
     the following members:

    ## Remarks
        The NDIS_OFFLOAD_ENCAPSULATION structure specifies the requested encapsulation settings that a
    miniport adapter should use for task offload services.

In a set of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569762">OID_OFFLOAD_ENCAPSULATION</a>, a
    protocol driver specifies an NDIS_OFFLOAD_ENCAPSULATION structure in the 
    <b>InformationBuffer</b> member of the 
    <a href="..\ndis\ns-ndis-_ndis_oid_request.md">NDIS_OID_REQUEST</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis-_ndis_oid_request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569762">OID_OFFLOAD_ENCAPSULATION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OFFLOAD_ENCAPSULATION structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>