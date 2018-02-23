---
UID: NS:ndis._NDIS_OID_REQUEST
title: "_NDIS_OID_REQUEST"
author: windows-driver-content
description: To query or set OID information, NDIS submits NDIS_OID_REQUEST structures to filter drivers and miniport drivers.
old-location: netvista\ndis_oid_request.htm
old-project: netvista
ms.assetid: 3a5e151d-2a2d-4477-a736-8a5f3d3820a2
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ndis/NDIS_OID_REQUEST, _NDIS_OID_REQUEST, ndis_request_ref_c431d090-b403-40a7-90de-5f47ca6213f4.xml, *PNDIS_OID_REQUEST, NDIS_OID_REQUEST, PNDIS_OID_REQUEST structure pointer [Network Drivers Starting with Windows Vista], netvista.ndis_oid_request, ndis/PNDIS_OID_REQUEST, PNDIS_OID_REQUEST, NDIS_OID_REQUEST structure [Network Drivers Starting with Windows Vista]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ndis.h
apiname:
-	NDIS_OID_REQUEST
product: Windows
targetos: Windows
req.typenames: "*PNDIS_OID_REQUEST, NDIS_OID_REQUEST"
---

# _NDIS_OID_REQUEST structure
To query or set OID information, NDIS submits NDIS_OID_REQUEST structures to filter drivers and
  miniport drivers.

## Syntax
````
typedef struct _NDIS_OID_REQUEST {
  NDIS_OBJECT_HEADER  Header;
  NDIS_REQUEST_TYPE   RequestType;
  NDIS_PORT_NUMBER    PortNumber;
  UINT                Timeout;
  PVOID               RequestId;
  NDIS_HANDLE         RequestHandle;
  union _REQUEST_DATA {
    struct _QUERY {
      NDIS_OID Oid;
      PVOID    InformationBuffer;
      UINT     InformationBufferLength;
      UINT     BytesWritten;
      UINT     BytesNeeded;
    } QUERY_INFORMATION;
    struct _SET {
      NDIS_OID Oid;
      PVOID    InformationBuffer;
      UINT     InformationBufferLength;
      UINT     BytesRead;
      UINT     BytesNeeded;
    } SET_INFORMATION;
    struct _METHOD {
      NDIS_OID Oid;
      PVOID    InformationBuffer;
      ULONG    InputBufferLength;
      ULONG    OutputBufferLength;
      ULONG    MethodId;
      UINT     BytesWritten;
      UINT     BytesRead;
      UINT     BytesNeeded;
    } METHOD_INFORMATION;
  } DATA;
  UCHAR               NdisReserved[NDIS_OID_REQUEST_NDIS_RESERVED_SIZE * sizeof(PVOID)];
  UCHAR               MiniportReserved[2*sizeof(PVOID)];
  UCHAR               SourceReserved[2*sizeof(PVOID)];
  UCHAR               SupportedRevision;
  UCHAR               Reserved1;
  USHORT              Reserved2;
} NDIS_OID_REQUEST, *PNDIS_OID_REQUEST;
````

## Members


`_REQUEST_DATA`



`DATA`

A union that defines the request data. The information in the data varies according to the type of
     request as specified by the 
     <b>RequestType</b> member. The following member structures are specified:

`Flags`



`Header`

The 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure for the
     NDIS_OID_REQUEST structure. Set the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_OID_REQUEST, the 
     <b>Revision</b> member to NDIS_OID_REQUEST_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_OID_REQUEST_REVISION_1.

`MiniportReserved`

An area that is reserved for the miniport driver.

`NdisReserved`

An area that is reserved for NDIS.

`PortNumber`

The port to which the request is sent. If the port is unknown or default, this member is
     zero.

`RequestHandle`

A handle that identifies the source that issued the OID request. If a miniport driver must complete
      the request immediately and completes the request with a status of NDIS_STATUS_INDICATION_REQUIRED, the
      miniport driver uses this 
      <b>RequestHandle</b> value to set the 
      <b>DestinationHandle</b> member of the associated NDIS_STATUS_INDICATION
      structure. In this case, NDIS will send only the subsequent status indication to the source that issued
      the OID request.

For more information about status indications, see the following Remarks section.

`RequestId`

An identifier for the request. If a miniport driver must complete a request immediately and it
     completes the request with a status of NDIS_STATUS_INDICATION_REQUIRED, the miniport driver uses this 
     <b>RequestId</b> value to set the 
     <b>RequestId</b> member of the associated 
     <a href="..\ndis\ns-ndis-_ndis_status_indication.md">NDIS_STATUS_INDICATION</a> structure. 
     

NDIS or overlying drivers can also use the 
     <b>RequestId</b> to cancel a request. When a miniport driver receives a
     cancellation request, the miniport driver cancels any pending requests with a matching 
     <b>RequestId</b>. If 
     <b>RequestId</b> is zero, the miniport driver can ignore this member. For more
     information about status indications, see the following Remarks section.

`RequestType`

The request type as one of the 
     <a href="..\ntddndis\ne-ntddndis-_ndis_request_type.md">NDIS_REQUEST_TYPE</a> enumeration
     values.

`Reserved1`

Reserved for future use.

`Reserved2`

Reserved for future use.

`SourceReserved`

An area that is reserved for the originating driver. Reserved for the allocator of the
     NDIS_OID_REQUEST structure. This is usually an NDIS protocol driver or an NDIS filter driver.

`SupportedRevision`

The revision of an NDIS structure that was supported by an NDIS 6.0 or later driver when it
     handled an OID request. A revisioned structure is any NDIS 6.0 structure that has an 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure inside it.
     When the driver succeeds in setting an OID, it must set 
     <b>SupportedRevision</b> to the revision number of the structure that it
     supported. For more information about NDIS version information, see 
     <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/specifying-ndis-version-information">Specifying NDIS Version
     Information</a>.

`SwitchId`



`Timeout`

A time-out, in seconds, for the request. NDIS can reset the driver or cancel the request if the
     time-out expires before the driver completes the request.

`VPortId`



## Remarks
A protocol driver or a filter driver should allocate nonpaged memory for the buffer at 
    <b>InformationBuffer</b> and for the NDIS_OID_REQUEST structure. Using data that
    is allocated from paged memory can cause fatal page faults because the underlying drivers run at IRQL =
    DISPATCH_LEVEL to carry out the requested operation.

NDIS_OID_REQUEST contains a DATA substructure for each type of operation that a protocol driver can
    request of an underlying driver. Before calling 
    <a href="..\ndis\nf-ndis-ndisoidrequest.md">NdisOidRequest</a>, the protocol driver fills
    in the relevant members of the substructure that represents the query or set operation it specified in
    the 
    <b>Oid</b> member. NDIS or the underlying driver fills in the remaining members
    before it returns control to the caller.

Some OID requests allow a miniport driver to provide an OID completion status with a status
    indication. In this case, the miniport driver returns NDIS_STATUS_INDICATION_REQUIRED for the completion
    status of the OID request. A miniport driver cannot return this status unless the particular OID allows
    it. To determine if this status is allowed, see the OID reference page.

If a status indication is associated with an OID request where the miniport driver returned
    NDIS_STATUS_INDICATION_REQUIRED, the driver making the status indication must set the 
    <b>DestinationHandle</b> and 
    <b>RequestId</b> members in the 
    <a href="..\ndis\ns-ndis-_ndis_status_indication.md">NDIS_STATUS_INDICATION</a> structure.

In this case, the driver sets the 
    <b>DestinationHandle</b> and 
    <b>RequestId</b> members to the values from the 
    <b>RequestHandle</b> and 
    <b>RequestId</b> members in the NDIS_OID_REQUEST structure, respectively.

For example, in wireless networking, the processing of an OID request can take a very long time to
    complete. In this case, the miniport driver can complete the OID request immediately and provide a status
    indication later to provide the final result for the OID request.

The 
    <b>NdisRequestGeneric</b><i>n</i>(1-4) types are available for miniport drivers that create their own internal
    requests. To implement such a request, a miniport driver assigns an internal variable to one of these
    generic types.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.0 and later. Supported in NDIS 6.0 and later. |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<a href="..\ntddndis\ne-ntddndis-_ndis_request_type.md">NDIS_REQUEST_TYPE</a>



<a href="..\ndis\ns-ndis-_ndis_status_indication.md">NDIS_STATUS_INDICATION</a>



<a href="..\ntddndis\ne-ntddndis-_ndis_request_type.md">NDIS_REQUEST_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff569641">OID_GEN_SUPPORTED_GUIDS</a>



<a href="..\ndis\ns-ndis-_ndis_status_indication.md">NDIS_STATUS_INDICATION</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_OID_REQUEST structure%20 RELEASE:%20(2/16/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>