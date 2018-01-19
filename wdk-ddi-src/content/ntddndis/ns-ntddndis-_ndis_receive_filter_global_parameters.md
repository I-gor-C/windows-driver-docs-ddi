---
UID : NS:ntddndis._NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
title : _NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
author : windows-driver-content
description : The NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS structure specifies the receive filtering features that are enabled or disabled on a network adapter.NDIS receive filters are used in the following NDIS interfaces:NDIS Packet Coalescing.
old-location : netvista\ndis_receive_filter_global_parameters.htm
old-project : netvista
ms.assetid : 4ec36054-ba61-4862-b185-7473a6806804
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS, *PNDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS, NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.20 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS
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
req.typenames : "*PNDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS, NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS"
---

# _NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS structure
The <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure specifies the receive filtering features that are
  enabled or disabled on a network adapter.

NDIS receive filters are used in the following NDIS interfaces:


<a href="https://msdn.microsoft.com/500FBF0F-54D9-4675-8E2D-447387DA8798">NDIS Packet Coalescing</a>. For more information about how to use receive filters in this interface, see <a href="https://msdn.microsoft.com/20EA71E0-B880-4891-A12E-76F4C9AB16E6">Managing Packet Coalescing Receive Filters</a>.


<a href="https://msdn.microsoft.com/E64DD4F0-D5F8-4FFF-931B-C04C5C42D000">Single Root I/O Virtualization (SR-IOV)</a>. For more information about how to use receive filters in this interface, see <a href="https://msdn.microsoft.com/F0137D59-1701-4DFC-BB30-27E477FC0706">Setting a Receive Filter on a Virtual Port</a>.


<a href="https://msdn.microsoft.com/c502c7d6-bdf1-4656-b5a5-339250910f08">Virtual Machine Queue (VMQ)</a>. For more information about how to use receive filters in this interface, see <a href="https://msdn.microsoft.com/bfee8a3c-d2be-4718-beb4-067b66756a41">Setting and Clearing VMQ Filters</a>.

## Syntax
````
typedef struct _NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  ULONG              EnabledFilterTypes;
  ULONG              EnabledQueueTypes;
} NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS, *PNDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS;
````

## Members

        
            `EnabledFilterTypes`

            A  bitwise OR of flags for types of enabled receive filters. The
     following filter type flag is valid.
        
            `EnabledQueueTypes`

            A  bitwise OR of flags for types of enabled receive queues. The
     following queue type flag is valid.
        
            `Flags`

            A bitwise OR of flags. This member is reserved for NDIS.
        
            `Header`

            The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT.

To indicate the version of the <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure, the driver sets the 
     <b>Revision</b> member to one of the following values:

    ## Remarks
        The <b>NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS</b> structure is used in the 
    <a href="netvista.oid_receive_filter_global_parameters">
    OID_RECEIVE_FILTER_GLOBAL_PARAMETERS</a> query OID to obtain the current global receive filter
    settings.

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
<a href="netvista.oid_receive_filter_global_parameters">
   OID_RECEIVE_FILTER_GLOBAL_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_RECEIVE_FILTER_GLOBAL_PARAMETERS structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>