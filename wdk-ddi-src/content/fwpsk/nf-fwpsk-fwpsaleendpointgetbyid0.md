---
UID: NF.fwpsk.FwpsAleEndpointGetById0
title: FwpsAleEndpointGetById0 function
author: windows-driver-content
description: The FwpsAleEndpointGetById0 function retrieves information about an application layer enforcement (ALE) endpoint.Note  FwpsAleEndpointGetById0 is a specific version of FwpsAleEndpointGetById.
old-location: netvista\fwpsaleendpointgetbyid0.htm
old-project: NetVista
ms.assetid: fa9a5078-d254-4b4a-bbfb-256491beff5f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FwpsAleEndpointGetById0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsAleEndpointGetById0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: PASSIVE_LEVEL
---

# FwpsAleEndpointGetById0 function



## -description
The 
  <b>FwpsAleEndpointGetById0</b> function retrieves information about an application layer enforcement (ALE)
  endpoint.



## -syntax

````
NTSTATUS NTAPI FwpsAleEndpointGetById0(
  _In_  HANDLE                        engineHandle,
  _In_  UINT64                        endpointId,
  _Out_ FWPS_ALE_ENDPOINT_PROPERTIES0 **properties
);
````


## -parameters

### -param engineHandle [in]

A handle for an open session with the filter engine. This handle is obtained when a session is
     opened by calling 
     <a href="netvista.fwpmengineopen0">FwpmEngineOpen0</a>.


### -param endpointId [in]

The unique endpoint identifier.


### -param properties [out]

A pointer to an 
     <a href="netvista.fwps_ale_endpoint_properties0">
     FWPS_ALE_ENDPOINT_PROPERTIES0</a> structure that contains the properties of the endpoint.


## -returns
The 
     <b>FwpsAleEndpointGetById0</b> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The function succeeded.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 7.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.fwpsaleendpointenum0">FwpsAleEndpointEnum0</a>
</dt>
<dt>
<a href="netvista.fwpsaleendpointgetsecurityinfo0">
   FwpsAleEndpointGetSecurityInfo0</a>
</dt>
<dt>
<a href="netvista.fwpsaleendpointsetsecurityinfo0">
   FwpsAleEndpointSetSecurityInfo0</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20FwpsAleEndpointGetById0 function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

