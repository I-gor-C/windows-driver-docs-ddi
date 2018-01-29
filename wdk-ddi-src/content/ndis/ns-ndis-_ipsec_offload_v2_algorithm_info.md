---
UID : NS:ndis._IPSEC_OFFLOAD_V2_ALGORITHM_INFO
title : _IPSEC_OFFLOAD_V2_ALGORITHM_INFO
author : windows-driver-content
description : The IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure specifies an algorithm that is used for a security association (SA).
old-location : netvista\ipsec_offload_v2_algorithm_info.htm
old-project : netvista
ms.assetid : 787e5a98-ba77-42d4-8624-abcc02fccf53
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : "*PIPSEC_OFFLOAD_V2_ALGORITHM_INFO, PIPSEC_OFFLOAD_V2_ALGORITHM_INFO structure pointer [Network Drivers Starting with Windows Vista], _IPSEC_OFFLOAD_V2_ALGORITHM_INFO, PIPSEC_OFFLOAD_V2_ALGORITHM_INFO, netvista.ipsec_offload_v2_algorithm_info, ndis/PIPSEC_OFFLOAD_V2_ALGORITHM_INFO, ndis/IPSEC_OFFLOAD_V2_ALGORITHM_INFO, IPSEC_OFFLOAD_V2_ALGORITHM_INFO, IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure [Network Drivers Starting with Windows Vista], task_offload_IPsecv2_ref_72dc6155-8044-4b56-b7c7-0587bf82889d.xml"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Windows
req.target-min-winverclnt : Supported in NDIS 6.1 and later.
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
req.irql : See Remarks section
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : IPSEC_OFFLOAD_V2_ALGORITHM_INFO, *PIPSEC_OFFLOAD_V2_ALGORITHM_INFO
---

# _IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure
<p class="CCE_Message">[The IPsec Task Offload feature is deprecated and should not be used.]

The IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure specifies an algorithm that is used for a security
  association (SA).

## Syntax
````
typedef struct _IPSEC_OFFLOAD_V2_ALGORITHM_INFO {
  ULONG Identifier;
  ULONG KeyLength;
  ULONG KeyOffsetBytes;
  ULONG AdditionalInfo;
} IPSEC_OFFLOAD_V2_ALGORITHM_INFO, *PIPSEC_OFFLOAD_V2_ALGORITHM_INFO;
````

## Members


`AdditionalInfo`

Additional information that should be interpreted differently based on the algorithm. For AES-GCM,
     
     <b>AdditionalInfo</b> contains the ICV length.

`Identifier`

The encryption or authentication algorithm that is used for the SA. 
     

If the algorithm is an encryption algorithm, 
     <b>Identifier</b> can be any of the following values:



If the algorithm is an authentication algorithm, 
     <b>Identifier</b> can be one of the following values:

`KeyLength`

The length, in bytes, of the key for the algorithm. The key is contained in the array at the 
     <b>KeyData</b> member in the 
     <a href="..\ndis\ns-ndis-_ipsec_offload_v2_add_sa.md">IPSEC_OFFLOAD_V2_ADD_SA</a> structure.
     

<b>KeyLength</b> indicates the length of the cryptographic algorithm, starting at the offset that is
     specified in 
     <b>KeyOffsetBytes</b> .

If both algorithms (
     <b>AuthenticationAlgorithm</b> and 
     <b>EncryptionAlgorithm</b> ) are specified in IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION, the keys are
     concatenated. The respective keys start at the offset that is specified in 
     <b>KeyOffsetBytes</b> .

`KeyOffsetBytes`

The offset, in bytes, into in the array at the 
     <b>KeyData</b> member in the 
     <mshelp:link keywords="netvista.ipsec_offload_v2_add_sa" tabindex="0"><b>
     IPSEC_OFFLOAD_V2_ADD_SA</b></mshelp:link> structure.

## Remarks
The IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure specifies algorithm information in the 
    <b>EncryptionAlgorithm</b> and 
    <b>AuthenticationAlgorithm</b> members of the 
    <mshelp:link keywords="netvista.ipsec_offload_v2_security_association" tabindex="0"><b>
    IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION</b></mshelp:link> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |

## See Also

<mshelp:link keywords="netvista.ipsec_offload_v2_security_association" tabindex="0"><b>
   IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION</b></mshelp:link>

<a href="..\ndis\ns-ndis-_ipsec_offload_v2_add_sa.md">IPSEC_OFFLOAD_V2_ADD_SA</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20IPSEC_OFFLOAD_V2_ALGORITHM_INFO structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>