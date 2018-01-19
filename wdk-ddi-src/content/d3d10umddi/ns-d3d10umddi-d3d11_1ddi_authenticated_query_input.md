---
UID : NS:d3d10umddi.D3D11_1DDI_AUTHENTICATED_QUERY_INPUT
title : D3D11_1DDI_AUTHENTICATED_QUERY_INPUT
author : windows-driver-content
description : Contains input data for the QueryAuthenticatedChannel(D3D11_1) function.
old-location : display\d3d11_1ddi_authenticated_query_input.htm
old-project : display
ms.assetid : f7a4fb53-aa01-4279-a59a-fd92b0ceeab7
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D11_1DDI_AUTHENTICATED_QUERY_INPUT, D3D11_1DDI_AUTHENTICATED_QUERY_INPUT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3D11_1DDI_AUTHENTICATED_QUERY_INPUT
req.alt-loc : D3d10umddi.h
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
req.typenames : D3D11_1DDI_AUTHENTICATED_QUERY_INPUT
---

# D3D11_1DDI_AUTHENTICATED_QUERY_INPUT structure
Contains input data for the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_queryauthenticatedchannel.md">QueryAuthenticatedChannel(D3D11_1)</a> function.

## Syntax
````
typedef struct D3D11_1DDI_AUTHENTICATED_QUERY_INPUT {
  GUID   QueryType;
  HANDLE hChannel;
  UINT   SequenceNumber;
} D3D11_1DDI_AUTHENTICATED_QUERY_INPUT;
````

## Members

        
            `hChannel`

            A handle to the authenticated channel. This handle was created through a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createauthenticatedchannel.md">CreateAuthenticatedChannel(D3D11_1)</a> function.
        
            `QueryType`

            A GUID that specifies the query. The following GUIDs are defined.
        
            `SequenceNumber`

            The query sequence number. At the start of the session, generate a cryptographically secure 32-bit random number to use as the starting sequence number. For each query, increment the sequence number by 1.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createauthenticatedchannel.md">CreateAuthenticatedChannel(D3D11_1)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_queryauthenticatedchannel.md">QueryAuthenticatedChannel(D3D11_1)</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_AUTHENTICATED_QUERY_INPUT structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>